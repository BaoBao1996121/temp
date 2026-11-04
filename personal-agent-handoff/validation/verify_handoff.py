#!/usr/bin/env python3
"""Validate handoff files only; does not run REA or any Agent product tests."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional output JSON; writing inside the package changes its hash manifest.')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    checks: list[dict] = []
    def record(name: str, passed: bool, details: object) -> None:
        checks.append({'name': name, 'passed': passed, 'details': details})
    try:
        manifest = json.loads((root/'sources/MANIFEST.json').read_text(encoding='utf-8'))
        cases_doc = json.loads((root/'schemas/acceptance_cases.json').read_text(encoding='utf-8'))
        for source in manifest['sources']:
            path = root/source['path']
            record('source_bytes_'+source['id'], path.exists() and sha256(path)==source['sha256'], {'path':source['path'],'expected_sha256':source['sha256']})
            if path.suffix=='.zip':
                with zipfile.ZipFile(path) as archive:
                    invalid = archive.testzip()
                    record('legacy_archive_'+source['id'], invalid is None, {'members':len(archive.namelist()),'corrupt_member':invalid})
        report=(root/'sources/最简PersonalAgent完整调研与设计取舍.md').read_text(encoding='utf-8')
        full=(root/'FULL_HANDOFF.md').read_text(encoding='utf-8')
        record('source_report_in_standalone', report in full, 'Full source text included; original file also preserved separately.')
        record('host_digest_consistency', manifest['reported_host_sha256'] in report and manifest['reported_host_sha256'] in (root/'CLAUDE_HANDOFF.md').read_text(encoding='utf-8'), 'Reported target digest is distinct from the report file digest; target bytes were not supplied.')
        expected_missing={x['name'] for x in manifest['referenced_reports_not_supplied']}
        referenced=set(re.findall(r'\]\(([^)]+)\)', report))
        record('missing_reports_declared', expected_missing==referenced and len(expected_missing)==12, sorted(expected_missing))
        broken=[]; declared=[]; checked=0
        for doc in sorted(root.rglob('*.md')):
            # Archive contents are not executed or treated as active documents.
            for raw in re.findall(r'\]\(([^)]+)\)',doc.read_text(encoding='utf-8')):
                target=raw.strip().split(' "',1)[0]
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target) or target.startswith('#'):
                    continue
                target=unquote(target.split('#',1)[0])
                if not target:
                    continue
                checked+=1
                p=doc.parent/target
                if p.exists():
                    continue
                if doc.name in {'最简PersonalAgent完整调研与设计取舍.md','FULL_HANDOFF.md'} and target in expected_missing:
                    declared.append({'document':str(doc.relative_to(root)),'target':target})
                else:
                    broken.append({'document':str(doc.relative_to(root)),'target':target})
        record('document_links', not broken, {'checked':checked,'declared_unavailable_occurrences':len(declared),'unexpected_broken':broken})
        cases=cases_doc['cases']; ids=[x['id'] for x in cases]
        record('acceptance_ids_unique',len(ids)==len(set(ids))==36,{'count':len(ids),'ids':ids})
        record('acceptance_not_claimed_run',all(x['status']=='not_implemented_not_run' for x in cases),'All are future specifications, not passed tests.')
        required={'id','phase','name','evaluation_type','requirement_ids','status','setup','action','assertions','required_evidence'}
        record('acceptance_complete',all(required<=set(x) and x['assertions'] and x['required_evidence'] for x in cases),'Each case declares setup/action/assertions/evidence.')
        reqs={r for x in cases for r in x['requirement_ids']}
        record('requirements_covered',reqs=={f'U{i:02d}' for i in range(1,11)},sorted(reqs))
        record('no_reverse_engineering_claim_this_handoff',manifest['reverse_engineering_executed_this_handoff'] is False,manifest['framework_implementation_status'])
        main_text=(root/'CLAUDE_HANDOFF.md').read_text(encoding='utf-8')
        record('user_requirements_preserved',all(f'U{i:02d}' in main_text for i in range(1,11)) and '不强制总管' in main_text and '口语化' in main_text and '业务无关' in main_text,'Requirements present in the entry document.')
        hashes=[]; invalid_hashes=[]
        for line in (root/'MANIFEST.sha256').read_text(encoding='utf-8').splitlines():
            digest, rel=line.split('  ',1)
            path=root/rel
            hashes.append(rel)
            if not path.is_file() or sha256(path)!=digest:
                invalid_hashes.append(rel)
        record('package_manifest',not invalid_hashes,{'entries':len(hashes),'mismatched':invalid_hashes,'self_manifest_excluded':True})
    except Exception as error:
        record('validator_exception',False,repr(error))
    passed=all(item['passed'] for item in checks)
    result={
        'checked_at_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'handoff_document_integrity_only',
        'passed':passed,
        'checks_passed':sum(x['passed'] for x in checks),
        'checks_total':len(checks),
        'checks':checks,
        'rea_executed':False,
        'local_original_function_tests_rerun':False,
        'agent_product_tests_executed':False,
        'limitations':['Referenced detailed reports and original local evidence were not supplied.','Source hash validation concerns the uploaded report/archive bytes, not the absent HOST/EVAL targets.','This validation does not establish any runtime, model, or production behavior.']
    }
    output=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(output,encoding='utf-8')
    sys.stdout.write(output)
    return 0 if passed else 1

if __name__=='__main__':
    raise SystemExit(main())
