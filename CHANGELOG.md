# Changelog

## 1.1.43

- Add app governance trees, private prompts and reviewed marketplace instructions.
- Support `@pluglayer prompt:human-readable-id` and revision-safe updates.

## 1.1.42 — 2026-10-16 (unreleased)

- Direct install starts native sign-in only when a terminal can be opened. Headless runs keep the manual connector step.

## 1.1.41 — 2026-10-15 (unreleased)

- Route PlugLayer questions to the matching tool. Use setup only for install, update, or reconnect, and do not browse the site for data the tools return.
- Direct install opens native PlugLayer sign-in when the agent CLI provides `mcp login`, instead of leaving connector authentication as a separate click.

## 1.1.40 — 2026-10-15 (unreleased)

- Verify setup and native component discovery; keep focused agents available without changing unrelated conversations.
- Document masked connection values, compact template discovery and launch-session cleanup.
- Align version/changelog gates and include marketplace readiness guidance.

## 1.1.39

- Fix public plugin loading, registration and OAuth recovery (2026-10-14, `1478bac`).

## 1.1.38

- Update PlugLayer Antigravity plugin to version 1.1.38, refining installation scripts and user guidance. Remove unnecessary OAuth prompts and enhance clarity in post-installation instructions. Update installation documentation to reflect changes and ensure users are informed about connecting through the native plugin UI. Improve overall user experience during the installation process. (2026-10-14, `6f06608`).

## 1.1.37

- Update installation scripts and documentation for PlugLayer Antigravity plugin to version 1.1.37. Refine OAuth connection prompts in Bash and PowerShell installers for improved user experience. Ensure proper handling of terminal interactions during installation and enhance clarity in installation instructions. (2026-10-12, `415ac82`).

## 1.1.36

- Add installation scripts for PlugLayer Antigravity plugin in Bash and PowerShell. Update installation instructions and README for clarity on setup and capabilities. Bump plugin version to 1.1.36 and enhance plugin description to reflect new features. (2026-10-12, `c1fff2b`).

## 1.1.35

- No distinct version declaration exists in this package’s checked-in history; this number is not asserted to have shipped.

## 1.1.34

- Bump public plugin release to 1.1.34 (2026-10-11, `345bcac`).

## 1.1.33

- Update VERSION to 1.1.33 for the antigravity plugin (2026-10-11, `8f26212`).

## 1.1.32

- No distinct version declaration exists in this package’s checked-in history; this number is not asserted to have shipped.

## 1.1.31

- No distinct version declaration exists in this package’s checked-in history; this number is not asserted to have shipped.

## 1.1.30

- No distinct version declaration exists in this package’s checked-in history; this number is not asserted to have shipped.

## 1.1.29

- No distinct version declaration exists in this package’s checked-in history; this number is not asserted to have shipped.

## 1.1.28

- No distinct version declaration exists in this package’s checked-in history; this number is not asserted to have shipped.

## Earlier recorded history

## 1.0.21

- Proactively submit safe PlugLayer feedback for product-caused poor experiences, challenges, friction, confusing guidance, and bugs.

## 1.0.20

- Isolate the public Windows installer from all private Admin, Security Operations, and GTM product details.

## 1.0.19

- Keep submitted feedback unchanged; create new follow-up tickets referencing the previous ticket, including recurrence after resolution.

## 1.0.18

- Plan dedicated compute per app, reuse project capacity first, prevent undersized machine bundles, and add confirmation-gated Extra Compute Requests.

## 1.0.17

- Bundle consent-gated plugin update guidance and always launch the latest compatible PlugLayer MCP package. Antigravity's strict manifest still permits only `name` and `description`, so it cannot declare an icon field.

## 1.0.16

- Add app security checks, IP allowlist and rate-limit skills, and focused security routing.

## 1.0.14 - 2026-08-29

- Support non-interactive quick setup from the portal's short-lived installer exchange.

## 1.0.13 - 2026-08-15

- Add project display-name/description updates through `update_project_metadata`, including explicit description clearing and routing-identity safeguards.

## 1.0.12 - 2026-08-15

- Let users inspect feedback status and update an owned ticket's title/description, while keeping status and resolution admin-managed.
- Check recent feedback and consolidate matching reports instead of creating repetitive tickets.

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
