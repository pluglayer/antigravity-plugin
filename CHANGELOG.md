# Changelog

## 1.0.11 - 2026-07-26

- Treat root and `www` as separate routes, require an explicit root redirect or attachment, and validate nested-path preservation.

## 1.0.10 - 2026-07-26

- Teach agents, rules, and deployment guidance to use `rename_project` for display-name-only project renames.

## 1.0.9 - 2026-07-26

- Prevent GoDaddy apex CNAME instructions and guide users to a PlugLayer `www` domain plus GoDaddy HTTPS 301 forwarding.

## 1.0.8 - 2026-07-19

- Add secure arbitrary env import through MCP and document JSON, dotenv/config content, and reusable Action flows without returning secret values.

## 1.0.6 - 2026-07-15

- Add a feedback skill, focused agent, global feedback rule, and safe automatic submission guidance backed by PlugLayer MCP.

## 1.0.2 - 2026-07-04

- Document the rule that every plugin-file change must bump `VERSION`.

## 1.0.1 - 2026-07-04

- Make desktop and CLI plugin-file installation explicit without requiring the `agy` CLI.
- Treat `agy-pluglayer` as an optional convenience launcher when `agy` exists.

## 1.0.0 - 2026-06-20

- Add the PlugLayer Google Antigravity plugin.
- Bundle five PlugLayer skills and four focused agents.
- Add PlugLayer MCP, deployment rules, and an optional command-safety hook.
- Add global IDE and CLI installation support.
