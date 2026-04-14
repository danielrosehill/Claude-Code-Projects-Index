![Claude Agent Blueprints](images/banner.png)

# Claude Code Projects Index

A curated collection of Claude Code projects, agent workspace blueprints, and related resources — organized by use case. Most patterns here adapt to other agentic AI CLIs and frameworks.

**[Browse online](https://claude.danielrosehill.com)** · **[Plugins Marketplace](https://github.com/danielrosehill/Claude-Code-Plugins)** · **[Documentation portal](https://docs.bydanielrosehill.com)** · **[Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model)** · **[What are Claude Spaces?](./claude-spaces.md)**

> 🧩 **My Claude Code Plugins Marketplace** — [danielrosehill/Claude-Code-Plugins](https://github.com/danielrosehill/Claude-Code-Plugins) — centralized marketplace bundling the plugins referenced throughout this index (including the [New-Repo-From-Template plugin](#templates--scaffolds) for scaffolding workspaces).

---

## Contents

**Workspaces by Domain**
- [Systems Administration](#systems-administration)
- [Productivity & Planning](#productivity--planning) · [Legal](#legal) · [Health & Wellbeing](#health--wellbeing) · [Communications & Writing](#communications--writing) · [Financial Planning](#financial-planning) · [Career](#career) · [Business](#business) · [Privacy & Anonymity](#privacy--anonymity) · [Technology & Hardware](#technology--hardware) · [Marketing](#marketing)
- [Research](#research)
- [Argument and Perspective Exploration](#argument-and-perspective-exploration)

**Configuration & Tooling**
- [Context and Personalization](#context-and-personalization)
- [Multi-Agent Tooling](#multi-agent-tooling)
- [MCP (Model Context Protocol)](#mcp-model-context-protocol)

**Extensions & Scaffolds**
- [Plugins](#plugins)
- [Templates / Scaffolds](#templates--scaffolds) — *recommended way to spin up a new workspace*
- [Slash Commands](#slash-commands)

**Other**
- [Miscellaneous](#miscellaneous)

---

## About This Index

I've been using Claude Code daily for about six months — for development, but also audio editing, legal research, SEO analysis, health documentation, systems administration, and a long tail of non-code use cases. This index is the result: a collection of **agent workspaces** (repositories structured as self-contained environments for a specific activity) alongside supporting tooling — plugins, context files, MCP servers, and slash commands.

If there's a common thread, it's treating Claude Code less as a coding assistant and more as a general-purpose agent workspace that happens to run in a terminal.

| Type | What it is | Badge |
|------|------------|-------|
| **Agent Workspace** | Pre-configured repo using Claude as a conversational UI for a domain-specific workflow | ![Agent Workspace](https://img.shields.io/badge/Agent-Workspace-purple?style=flat-square) |
| **Template** | Forkable starting point you can customize | ![Template](https://img.shields.io/badge/Template-Ready-green?style=flat-square) |
| **Non-Code** | Applications beyond software development | ![Non-Code](https://img.shields.io/badge/Non--Code-teal?style=flat-square) |

![Agent Workspace Definition](images/claude-space.png)

<details>
<summary><strong>More context: the Agent Workspace Model, growth chart, praise</strong></summary>

#### The Agent Workspace Model

All workspaces in this index follow the pattern defined in the **[Claude Agent Workspace Model](https://github.com/danielrosehill/Claude-Agent-Workspace-Model)** repository. The core idea: a Git repository isn't just for code — it can serve as a complete, self-contained workspace for *any* activity. Each workspace uses a defined folder structure, a `CLAUDE.md` for agent instructions, slash commands, MCP configurations, and subagent definitions to create a purpose-built environment.

This pattern has been applied to everything from sysadmin and remote server management to legal research, health documentation, and financial planning — domains that have nothing to do with software development.

**Want to follow this approach?** Point Claude Code at the [model repository](https://github.com/danielrosehill/Claude-Agent-Workspace-Model) to give it context on the pattern, then ask it to scaffold a new workspace for your use case. Or — simpler — use the [New-Repo-From-Template plugin](#templates--scaffolds), which packages the curated templates into a one-command scaffold.

#### Repository Growth

![Repository Count Over Time](charts/repo-count-chart.png)

#### Praise

> *"This is either the work of a prolific genius, or a very clever bot (or both), although it hardly matters because the quality is so good - an index of 75+ Claude Code repositories published by the author... CMS, system design, deep research, IoT, agentic workflows, server management, personal health... If you spot the lie, let me know, otherwise please check these out."*
>
> — [awesome-claude-code](https://github.com/wong2/awesome-claude-code)

For the record: I'm a real human ([danielrosehill.com](https://danielrosehill.com)). The repos and workspaces in this index are generated with Claude Code but human-designed and refined.

#### Additional reading

- 📝 **[Notes on Templates & Workspaces](./notes.md)**
- 📖 **[What are Agent Workspaces?](./claude-spaces.md)**

</details>

---
