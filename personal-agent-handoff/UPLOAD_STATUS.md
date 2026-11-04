# Personal Agent — Claude handoff

The main handoff documents and verification scripts were uploaded directly and checked against their original Git blob hashes.

**Transfer status:** 16 of the original 18 files. Two historical ZIP archives under `legacy/` could not be transferred due to the binary-upload security check:
- `legacy/grok_bot_rea_analysis_20261103.zip`
- `legacy/rea_install_attempt_20261103.zip`

These archives are historical comparison material, not the primary research and implementation handoff. `MANIFEST.sha256` contains their expected checksums, so the original `verify_handoff.py` must not be reported as passing until those files are restored.

Start with `CLAUDE_START_PROMPT.md`, then `CLAUDE_HANDOFF.md`; `FULL_HANDOFF.md` is an alternative combined reading document. Keep the original private REA Host/EVAL research files outside this public repository.

Local Codex:

```bash
git clone https://github.com/BaoBao1996121/temp.git
cd temp/personal-agent-handoff
```
