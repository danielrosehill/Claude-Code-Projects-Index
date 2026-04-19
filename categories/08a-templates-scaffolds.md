# Templates / Scaffolds

Scaffolds used to be distributed as ~100 standalone template repos and a `New-Repo-From-Template` plugin. That pattern was retired in the April 2026 reshape.

**Scaffolds now live inside the [cluster plugins](#plugins).** Each of the 28 cluster plugins bundles the workspace primitives for its domain (commands, skills, agents, MCP configs) and exposes a provisioning skill that writes a fresh per-project scaffold on demand — so instead of cloning a template repo, you install the relevant plugin once and ask Claude Code to scaffold a new workspace for whatever project you're starting.

See the [Plugins](#plugins) section above for the full cluster list.

---
