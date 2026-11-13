# Multi-Agent Tooling

![Multi-Agent Tooling](images/resources.png)

Components and tooling for multi-agent development and orchestration frameworks.

## Multi-Agent Systems

### Agent Briefing Gateway
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Agent-Briefing-Gateway) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Design model for an orchestration agent that buffers a human from a batch of working sub-agents — one consolidated brief per cycle, a budgeted override channel, and resumable approval gates.

---

### Agent Handover Demo
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Agent-Handover-Demo) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Pattern for handing tasks between code-generation agents working on different machines through shared handover docs, giving supervising humans an audit trail of what each agent did.

---

### Claude Agent Picker Pattern
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Agent-Picker-Pattern) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Pattern for assembling multi-agent crews where each agent's role and context overlap as little as possible.

---

### Claude Agent Workspace Generator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Agent-Workspace-Generator) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Launchpad for creating standardized workspace templates conforming to the Agent Workspace Model v1.1 spec, with slash commands to generate, validate, and publish new workspaces.

---

### Claude Air Traffic Control
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Air-Traffic-Control) ![Agent Workspace](https://img.shields.io/badge/Agent-Workspace-purple?style=flat-square)

Workspace model for one operator running agentic AI across many repositories all day, borrowed from air traffic control: a voice-first shift manager routes work across concurrent Claude Code sessions. Published as a 26-page typeset document.

---

### Claude Development Agents
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Development-Agents) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Curated toolkit of 74+ Claude Code configurations for development workflows and multi-agent coordination.

---

### Claude Fleet Traffic Shaper
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Fleet-Traffic-Shaper) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Specification for a local proxy that assigns priorities to concurrent Claude Code sessions and shapes their aggregate traffic, so rate limiting degrades background work instead of landing at random. Includes a prior-art survey of the multi-agent proxy and queueing landscape.

---

### Claude Net
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Net)

Agent-to-agent messaging and task delegation between two people's Claude Code sessions on different machines and accounts, through a tailnet relay. Documents a private implementation with generic diagrams and code samples.

---

### Claude Sub-Agent Network
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Sub-Agent-Network) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Collection of sub-agent system prompts and configs for development, operations and creative work.

---

### Cool Claude Code Stuff
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Cool-Claude-Code-Stuff)

Curated collection of Claude Code projects and resources organized by category.

---

### Research Pack
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Research-Pack)

Specification for packaging research findings so one agent can hand a predictable, bounded block of research to the next stage of a pipeline, such as a script-writing agent.

---

## Workspace Setup & Management

### Claude Skill Definer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Skill-Definer) ![Agent Workspace](https://img.shields.io/badge/Agent-Workspace-purple?style=flat-square)

Multimodal workspace for defining Claude Code skills from voice notes, videos, images and text, or written specs.

---

### Claude Vault Idea
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Vault-Idea)

Idea capture for a meta-plugin holding a personal vault of plugins and MCP servers, activated selectively per project to mitigate eager plugin description loading at user level.

---

### Claude Workspace Setup Helper
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Workspace-Setup-Helper) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

Interactive tool for discovering, selecting, and cloning Claude Workspace templates.

---

### Public Plugin Private Overlay
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Public-Plugin-Private-Overlay) ![Template](https://img.shields.io/badge/Template-Ready-green?style=flat-square)

Architecture for Claude Code plugins that do sustained work: a public plugin, a private workspace instantiated from a template repo, and a vault at `~/.claude-plugins/<name>/` for user data.

---

## Documentation & Notes

