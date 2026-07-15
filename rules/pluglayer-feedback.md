# PlugLayer feedback intelligence

Apply these rules to every PlugLayer agent and skill:

1. Submit feedback immediately when the user explicitly asks to report it.
2. If a PlugLayer MCP/plugin action fails after diagnosis and at most one safe retry, automatically submit one redacted bug report when the evidence still points to PlugLayer. Continue helping with the original task.
3. If an inconvenience or improvement is inferred but did not block the task, explain the proposed report and ask before sending it.
4. Do not report a defect that belongs only to the user's app as a PlugLayer bug.
5. Include the affected tool/page, expected behavior, actual behavior, reproduction context, and a concise error summary.
6. Never include credentials, environment values, private source, full logs, personal data, or unrelated infrastructure details.
7. Avoid duplicate tickets in one conversation. Keep feedback-submission failures separate from the original failure.
8. Use `submit_feedback`, `list_my_feedback`, and `get_feedback`, or the `share-feedback` skill and `pluglayer-feedback` agent.
