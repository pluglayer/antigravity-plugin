# PlugLayer deployment rules

Apply these rules when the user wants to deploy, update, troubleshoot, or attach a domain through PlugLayer.

1. Inspect the repository and analyze frontend, backend, workers, queues, databases, storage, and external services before choosing a deployment path.
2. Treat standard databases as PlugLayer Data Layer resources. Reuse a suitable existing database when possible; otherwise provision from a Data Layer template.
3. Treat app name and PlugLayer slug as separate values. Do not change an existing slug during a normal restart or redeploy.
4. Before deploying into an existing project, inspect its apps. Prefer updating a matching app over creating a duplicate.
5. Default deploy and redeploy sizing to at least 1 CPU, 1 GB RAM, and 5 GB storage unless the user explicitly requests less.
6. Default redeploy strategy to `recreate`. Offer `rolling` when the user explicitly prioritizes lower downtime and has enough temporary compute headroom.
7. Prefer a tested local build for repo-backed apps. Export local-only builds as architecture-agnostic OCI archives and use PlugLayer's upload flow.
8. Keep temporary artifacts under `.pluglayer/`. Only remove images and archives recorded in the current PlugLayer task manifest.
9. If compute is missing, estimate the requirement, provide the PlugLayer compute link, and re-check availability before deploying.
10. For custom domains, detect and confirm the DNS provider before showing records. Use a table with Type, Name / Host, Content / Value / Target, and Description.
11. Poll asynchronous PlugLayer tasks until completion and report the backend's real failure detail.
12. Recognize transient recreate-rollout noise: an old revision may briefly show `Failed` while the new pod is `Pending`. Retry once before changing ports, probes, or app code.
13. After a successful repo-backed deploy, offer GitHub Actions using `pluglayer/actions` to build, upload, and redeploy the same app id.
14. Keep this plugin end-user scoped. Do not expose or invent admin-only cluster operations.
