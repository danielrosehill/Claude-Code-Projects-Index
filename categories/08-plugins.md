<!-- GENERATED FROM data/marketplace.json — do not edit by hand. Run scripts/sync_marketplace.py or npm run build. -->

# Plugins

![Plugins](images/plugins.png)

All plugins registered in the [danielrosehill marketplace](https://github.com/danielrosehill/Claude-Code-Plugins). Install any of these with `/plugin install <name>@danielrosehill`.

## Systems Administration

### Bash Alias Manager
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/bash-alias-manager-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin for managing bash aliases — add, edit, delete, prune, ideate, and back up ~/.bash_aliases using a guided workflow.

---

### Bug Catcher
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/bug-catcher-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Slash commands for rapid Linux system bug capture and diagnosis — check fresh logs the moment an issue occurs.

---

### Security Checkup
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/security-checkup-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin for security audits, vulnerability scanning, firewall configuration, and system security hardening workflows.

---

## Development & Scaffolding

### Claude Code Feedback
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-Feedback-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Self-healing helper for filing well-formed bug reports, feature requests, model-behavior reports, and documentation issues against anthropics/claude-code. Fetches the live GitHub issue-form templates on every run so submissions always match Anthropic's current required fields.

---

### Claude Janitor
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Janitor) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Repository cleanup toolkit with automated operations for removing clutter, organizing structure, and polishing documentation.

---

### Claude Templatizer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Templatizer) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Turn a set of existing Claude Code workspace repos into a reusable GitHub template repo by extracting their commonalities.

---

### Make Agent Friendly
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Make-Agent-Friendly) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Prepares human-developed codebases for agentic development with structured refactoring, CLAUDE.md creation, and agent-friendly infrastructure.

---

### New Repo From Template
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/New-Repo-From-Template-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Create new GitHub repos from a built-in curated template library AND the user's own templates (GitHub public/private or local directories). Match-by-intent and recommendation skills search both pools; configure-template-sources skill discovers and caches user templates.

---

### QA Team
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-QA-Team) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

A multi-agent QA system for comprehensive code review and quality validation with specialized agents for general QA, cleanup, documentation, API review, performance optimization, and deployment review.

---

### Repo Retrofitter
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Repo-Retrofitter) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Bulk-retrofit repositories with AI agent scaffolding (CLAUDE.md, slash commands, subagents, MCP recommendations). Supports scan, interactive, and fully autonomous modes.

---

### Session Transfer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Session-Transfer) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Transfer a Claude Code session to a fresh instance — full context transfer via a structured HANDOVER.md (with a dedicated writer subagent), or quick-jump skills for spawning a sibling Konsole/Claude window at the current directory.

---

### Claude Code What Thing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-What-Thing) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Decision support for choosing the right Claude Code primitive — skill, subagent, slash command, plugin, MCP server, hook, or output style — based on what you're trying to build. Grounded in the official Anthropic docs, personalised by stored user context.

---

## Context & CLAUDE.md

### Claude User Memory
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-User-Memory-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Persistent cross-session memory about the user, backed by Mem0. Two isolated contexts (personal and work) with three skills for recall, save, and end-of-session commit.

---

### ClaudeMD Chunker
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/claudemd-chunker-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Slash command that prunes bloated CLAUDE.md files to their essentials and offloads supplementary context into an agent-context/ folder.

---

### New Turn Hook
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/new-turn-hook-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Evaluates whether the current conversation context is still useful or whether the user should start a fresh conversation to avoid context bloat and degraded performance.

---

### Workspace Setup
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/workspace-setup-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Interactive assistant for discovering and cloning Claude Code workspace templates. Asks about your objectives, recommends relevant workspaces from a curated catalog, and clones them to a directory of your choice.

---

## MCP & Infrastructure

### MCP Command Generator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/mcp-command-generator-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Natural language MCP server installation assistant for Claude Code. Generates and optionally executes valid 'claude mcp add' commands from plain English descriptions, backed by a curated server catalog and syntax reference.

---

## Writing & Documentation

### AI Attribution
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/ai-attribution-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Adds a transparent human-AI attribution section to a project README, documenting which parts of the work were human-authored and which were AI-assisted or AI-generated.

---

## Home & Hardware

### Hp5200 Printer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-HP5200-Skill-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

HP DeskJet 5200 printer and scanner operations — ink levels, color/B&W printing, scanning, auto-discovery. A simple demo of local AI agent hardware integration.

---

## Miscellaneous

### Fix Documentation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Document-This) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin for automated technical documentation generation and code documentation workflows.

---

### Tech Docs
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/documentation-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin for documentation generation, technical writing, README creation, and documentation management workflows.

---
