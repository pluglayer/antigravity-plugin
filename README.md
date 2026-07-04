# PlugLayer for Google Antigravity

This public plugin gives Google Antigravity the same end-user PlugLayer workflows available in the Codex, Claude Code, and Cursor plugins.

## Included

- PlugLayer MCP access through `uvx pluglayer-mcp`
- skills for repo inspection, deployment, failed-deploy repair, domains, and GitHub CI/CD
- focused deploy, repair, domain, and CI/CD agents
- persistent PlugLayer deployment rules
- an optional, disabled-by-default command-safety hook

## One-line install

```bash
curl -fsSL https://raw.githubusercontent.com/pluglayer/antigravity-plugin/main/install.sh | bash
```

The installer:

- saves the PlugLayer token in `~/.pluglayer/credentials.env`
- installs the IDE plugin into `~/.gemini/config/plugins/pluglayer-antigravity-plugin`
- installs the CLI plugin into `~/.gemini/antigravity-cli/plugins/pluglayer-antigravity-plugin`
- does not require the `agy` CLI; when `agy` is installed, it also creates the convenience launcher `agy-pluglayer`
- supports version-aware reinstall and token-only updates

Get a token from [portal.pluglayer.com/tokens](https://portal.pluglayer.com/tokens).

## Manual install

For Antigravity 2.0 / IDE:

```bash
mkdir -p ~/.gemini/config/plugins
cp -R . ~/.gemini/config/plugins/pluglayer-antigravity-plugin
```

For Antigravity CLI without using `agy plugin install`:

```bash
mkdir -p ~/.gemini/antigravity-cli/plugins
cp -R . ~/.gemini/antigravity-cli/plugins/pluglayer-antigravity-plugin
```

Restart Antigravity after installation. In the CLI, verify with:

```bash
agy plugin list
```

If `agy` is not installed, the IDE plugin is still available after restarting Antigravity.

## Plugin structure

```text
pluglayer-antigravity-plugin/
├── plugin.json
├── mcp_config.json
├── hooks.json
├── agents/
├── rules/
├── scripts/
└── skills/
```

The manifest follows the live Antigravity schema and intentionally keeps release versioning in `VERSION`, because the current schema rejects undeclared manifest fields. Although the guide shows an optional `$schema` hint, Google's linked live schema does not currently permit that property.

## Agents

- `pluglayer-deploy`
- `pluglayer-fix-deploy`
- `pluglayer-domain-setup`
- `pluglayer-setup-cicd`

## Good first prompts

- "Inspect this repo and tell me the safest PlugLayer deploy path."
- "Use the PlugLayer deploy agent and ship this app."
- "Use the PlugLayer fix-deploy agent and repair this failed rollout."
- "Set up GitHub Actions for the existing PlugLayer app."
- "Attach this custom domain and translate the DNS records for my provider."

## Optional hook

`hooks.json` includes `pluglayer-command-safety`, disabled by default. If enabled, it forces explicit review of broad Docker or filesystem cleanup commands. It never silently approves commands.

## References

- [Antigravity plugins](https://antigravity.google/docs/plugins)
- [Antigravity CLI plugins and skills](https://antigravity.google/docs/cli-plugins)
- [Antigravity MCP](https://antigravity.google/docs/mcp)
