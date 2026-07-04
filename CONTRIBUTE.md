# Contribute to the PlugLayer Antigravity Plugin

1. Star the repo.
2. Open an issue first for larger changes.
3. Fork the repo.
4. Create a branch from `dev` if it exists, otherwise `main`.
5. Make a focused change.
6. Validate `plugin.json`, `mcp_config.json`, `hooks.json`, skills, agents, and shell scripts locally.
   Keep every Python source file at or below 500 lines; split larger scripts by responsibility while preserving their CLI and output contracts.
   Bump `VERSION` whenever any file in this plugin changes, including docs, rules, skills, agents, hooks, installer scripts, MCP config, or metadata. Do not put the version in `plugin.json`; Antigravity's live schema rejects undeclared fields.
7. Push to your fork.
8. Open a PR into the public `dev` branch unless a maintainer tells you otherwise.
