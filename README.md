![Claude Agent Blueprints](images/banner.png)

# Claude Code Projects Index

A curated collection of Claude Code projects, agent workspace blueprints, and related resources — organized by use case. Most patterns here adapt to other agentic AI CLIs and frameworks.

**[Browse online](https://claude.danielrosehill.com)** · **[Plugins Marketplace](https://github.com/danielrosehill/Claude-Code-Plugins)** · **[Documentation portal](https://docs.bydanielrosehill.com)** · **[What are Claude Spaces?](./claude-spaces.md)**

> 🧩 **My Claude Code Plugins Marketplace** — [danielrosehill/Claude-Code-Plugins](https://github.com/danielrosehill/Claude-Code-Plugins) — 28 focused **cluster plugins** covering workflows across sysadmin, research, media, writing, planning, and more. Each plugin ships the domain primitives (commands, skills, agents) globally and provisions per-project scaffolds on demand — so you install the plugin once and scaffold new workspaces from it as needed, rather than cloning a separate template repo per workflow.

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

#### The Agent Workspace Pattern

All workspaces in this index follow the same pattern: a Git repository isn't just for code — it can serve as a complete, self-contained workspace for *any* activity. Each workspace uses a defined folder structure, a `CLAUDE.md` for agent instructions, slash commands, MCP configurations, and subagent definitions to create a purpose-built environment.

This pattern has been applied to everything from sysadmin and remote server management to legal research, health documentation, and financial planning — domains that have nothing to do with software development.

**Primitives globally, scaffolds per-cluster.** The tooling has been consolidated into **28 cluster plugins** (see [Plugins](#plugins)) — each one ships the domain primitives globally (commands, skills, agents for that cluster) and provisions a project scaffold on demand. So rather than forking a separate template repo for each new workflow, you install the relevant cluster plugin once and ask Claude Code to provision a scaffold wherever you need one.

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

# Systems Administration

![Systems Administration](images/sysadmin.png)

Projects involving using Claude for local or remote systems administration as distinct from development-related projects.

> **See also:** The **[Claude Code Sysadmin Workspaces Index](https://github.com/danielrosehill/Claude-Code-Sysadmin-Workspaces-Index)** is a dedicated sub-index for all sysadmin workspace templates.

### Bash Alias Manager Claude
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Bash-Alias-Manager-Claude)

Workspace for managing bash aliases with YADM synchronization support.

---

### Claude Bug Catcher
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Bug-Catcher)

Hotkey-triggered utility that launches Claude Code with relevant logs for real-time Linux debugging.

---

### Claude Code Bash Aliases
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-Bash-Aliases)

Collection of bash aliases for common Claude Code operations on Linux.

---

### Claude Rescue
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Rescue)

Concept for deploying Claude Code into recovery shell environments for AI-assisted system repair.

---

### Claude System Recovery Mode
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-System-Recovery-Mode)

Custom GRUB boot entry integrating Claude CLI into Linux system recovery workflows.

---

## Linux - KDE Plasma

Projects specifically targeting KDE Plasma desktop integration and Linux desktop workflows with Claude Code.

### Claude Dolphin & Konsole Actions
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Dolphin-Konsole-Actions)

KDE Dolphin right-click context menu actions (service menus) for launching Claude Code in various Konsole window layouts, including single terminal, split panes, and multi-instance grids.

---

### Claude Bug Catcher
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Bug-Catcher)

Hotkey-triggered utility that launches Claude Code with relevant logs for real-time Linux debugging.

---

### Claude System Recovery Mode
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-System-Recovery-Mode)

Custom GRUB boot entry integrating Claude CLI into Linux system recovery workflows.

---

## Android


# Productivity & Planning

Workspaces for decision-making, personal planning, file management, and general-purpose productivity workflows.

> **See also:** The [Budgeting](https://github.com/danielrosehill/Claude-Budgeting-Plugin), [Personal Planning](https://github.com/danielrosehill/Claude-Personal-Planning-Plugin), [Career](https://github.com/danielrosehill/Claude-Career-Plugin), [Purchasing](https://github.com/danielrosehill/Claude-Purchasing-Plugin), [Shopping](https://github.com/danielrosehill/Claude-Shopping-Plugin), and [Ideation & Planning](https://github.com/danielrosehill/Claude-Ideation-Planning-Plugin) cluster plugins in the [Plugins](#plugins) section cover these domains.


# Legal

Workspaces and templates for legal research, case management, and evidence handling workflows.

> **See also:** The [Legal & Investigative](https://github.com/danielrosehill/Claude-Legal-Investigative-Plugin) cluster plugin in the [Plugins](#plugins) section covers this domain — evidence logging, document analysis, redaction, and brief generation.


# Health & Wellbeing

Workspaces and templates for health documentation, medical visit management, therapy tracking, and health-related research.

> **See also:** The [Personal Planning](https://github.com/danielrosehill/Claude-Personal-Planning-Plugin) cluster plugin in the [Plugins](#plugins) section covers this domain — diary, health, therapy, preparedness, and personal development variants.


# Communications & Writing

Workspaces and templates for content creation, blog management, writing workflows, and communications strategy.

### Claude Website Update Sender
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Website-Update-Sender)

Automated workflow for sending polished update emails about website changes via Resend MCP.

---

### Declaude
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Declaude) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

Personalized text rewriting rules that consolidate into a slash command for refining AI-generated documentation.

---

# Financial Planning

Workspaces and templates for budgeting, purchasing decisions, and personal finance management.

> **See also:** The [Budgeting](https://github.com/danielrosehill/Claude-Budgeting-Plugin), [Purchasing](https://github.com/danielrosehill/Claude-Purchasing-Plugin), and [Shopping](https://github.com/danielrosehill/Claude-Shopping-Plugin) cluster plugins in the [Plugins](#plugins) section cover these domains.


# Career

Workspaces and templates for job searching, career planning, and professional development.

> **See also:** The [Career](https://github.com/danielrosehill/Claude-Career-Plugin) cluster plugin in the [Plugins](#plugins) section covers this domain — role logging, offer comparison, application tracking, and salary benchmarking.


# Business

Workspaces and templates for business planning, idea evaluation, and organizational continuity.

> **See also:** The [Ideation & Planning](https://github.com/danielrosehill/Claude-Ideation-Planning-Plugin) cluster plugin in the [Plugins](#plugins) section covers business idea evaluation, decision frameworks, and simulation workflows.


# Privacy & Anonymity

Workspaces and templates for document redaction, identity protection, and PII obfuscation.

> **See also:** The [Legal & Investigative](https://github.com/danielrosehill/Claude-Legal-Investigative-Plugin) cluster plugin in the [Plugins](#plugins) section includes redaction and document-obfuscation workflows. For broader system hardening see the [Security Checkup](https://github.com/danielrosehill/Claude-Security-Checkup-Plugin) plugin.


# Technology & Hardware

Workspaces for hardware planning, PC builds, and technology procurement.

> **See also:** The [Purchasing](https://github.com/danielrosehill/Claude-Purchasing-Plugin) (includes a tech-procurement variant), [Sysadmin & Homelab](https://github.com/danielrosehill/Claude-Sysadmin-Homelab-Plugin), and [HP5200 Printer](https://github.com/danielrosehill/Claude-HP5200-Skill-plugin) plugins in the [Plugins](#plugins) section cover these domains.


# Marketing

Workspaces for SEO, web analytics, PR monitoring, and media tracking.

> **See also:** The [PR & Media Work](https://github.com/danielrosehill/Claude-PR-Media-Work-Plugin) cluster plugin in the [Plugins](#plugins) section covers coverage scanning, press summarisation, response drafting, and comms strategy.


# Research

![Research](images/research.png)

Projects using Claude and agentic systems for deep research, report generation, and information synthesis.

> **See also:** The [Research Space](https://github.com/danielrosehill/Claude-Research-Space-Plugin) cluster plugin in the [Plugins](#plugins) section covers deep research, technical research, OSINT, geo-reaction, stack, ecosystem, and competitor research workflows.

### Claude Deep Research Model (Notes / Documentation)
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Deep-Research-Model) ![Agent Workspace](https://img.shields.io/badge/Agent-Workspace-purple?style=flat-square)

Framework for iterative deep research using Claude with voice pipeline and structured outputs.

---

### Claude Dork
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Dork) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

Agent that generates platform-specific search dorks across Google, Reddit, Twitter/X, and more.

---

# Argument and Perspective Exploration

![Argument and Perspective Exploration](images/argument.png)

Projects using AI for synthesized debate to explore various perspectives, including policy modeling and analysis.

### Claude Change My View
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Change-My-View) ![Template](https://img.shields.io/badge/Template-Ready-green?style=flat-square) ![Agent Workspace](https://img.shields.io/badge/Agent-Workspace-purple?style=flat-square) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Workspace for challenging personal beliefs through AI-generated counterarguments and rebuttals.

---


# Context and Personalization

![Context and Personalization](images/context.png)

Projects exploring using Claude and related tooling for personalized user engagement, including through RAG, interviewing methods, and context injection.

### Batch ClaudeMD Repo Creator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Batch-ClaudeMD-Repo-Creator)

Automation workspace for batch-adding CLAUDE.md files across multiple GitHub repositories.

---

### Claude Code Context Toolkit
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-Context-Toolkit) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Bridges human-friendly CONTEXT.md files with AI-optimized CLAUDE.md briefings via slash commands.

---

### Claude Code Repo Managers ClaudeMD
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-Repo-Managers-ClaudeMD) ![Light Touch](https://img.shields.io/badge/Light-Touch-lightgray?style=flat-square)

Pre-configured CLAUDE.md templates for managing different repository types.

---

### Claude Model Identifier
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Model-Identifier) ![Light Touch](https://img.shields.io/badge/Light-Touch-lightgray?style=flat-square)

Prompt template for verifying the correct Claude model variant at conversation start.

---

### CONTEXT.md
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/CONTEXT.md) ![Light Touch](https://img.shields.io/badge/Light-Touch-lightgray?style=flat-square)

Workflow methodology for separating human-authored context from structured AI agent briefings.

---

### Linux Desktop ClaudeMD Seeder
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Linux-Desktop-ClaudeMD-Seeder) ![Light Touch](https://img.shields.io/badge/Light-Touch-lightgray?style=flat-square)

Automatically generates contextual CLAUDE.md files across a Linux desktop filesystem.

---

### Private And Public Claude MD
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Private-And-Public-Claude-MD)

Tools for managing public and private CLAUDE.md files with security-focused git configuration.

---

### The User Voice Types
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/The-User-Voice-Types) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square) ![Light Touch](https://img.shields.io/badge/Light-Touch-lightgray?style=flat-square)

CLAUDE.md snippets and slash commands telling Claude to silently infer around transcription errors from voice typing and stray keystrokes from one-handed or distracted typing.

---

# Multi-Agent Tooling

![Multi-Agent Tooling](images/resources.png)

Components and tooling for multi-agent development and orchestration frameworks.

## Multi-Agent Systems

### Agent Junction
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Agent-Junction) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

MCP server enabling encrypted peer-to-peer communication between Claude Code instances on localhost or LAN.

---

### Claude Agent Picker Pattern
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Agent-Picker-Pattern) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Framework for assembling context-optimized multi-agent crews with minimal overlap.

---

### Claude Agent Workspace Generator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Agent-Workspace-Generator) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Launchpad for creating standardized workspace templates conforming to the Agent Workspace Model v1.1 spec, with slash commands to generate, validate, and publish new workspaces.

---

### Claude Task Manager
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Task-Manager) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Sequential task queuing system addressing context window exhaustion in agentic coding tools.

---

## Agent Libraries & Collections

### Claude Development Agents
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Development-Agents) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Curated toolkit of 74+ Claude Code configurations for development workflows and multi-agent coordination.

---

### Claude Sub-Agent Network
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Sub-Agent-Network) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Collection of system prompts and configurations for development, operational, and creative tasks.

---

### Cool Claude Code Stuff
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Cool-Claude-Code-Stuff)

Curated collection of Claude Code projects and resources organized by category.

---

## Workspace Setup & Management

### Claude Workspace Setup Helper
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Workspace-Setup-Helper) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

Interactive tool for discovering, selecting, and cloning Claude Workspace templates.

---

## Documentation & Notes

### Claude Code Linux Notes
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-Linux-Notes)

Personal documentation of workflows and tips for using Claude Code on Ubuntu with KDE Plasma.

---


# MCP

![MCP](images/mcp.png)

Projects related to Claude and MCP tooling and setup.

### Claude Code MCP Command Generator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-MCP-Command-Generator)

Generator for creating MCP server configuration commands for Claude Code.

---

### How-To-MCP
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/How-To-MCP)

Guide for instructing AI agents on how to provision and manage MCP server connections according to user-specific preferences, with a tiered decision matrix.

---

### Claude Code MCP List
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-MCP-List)

Curated index of MCP servers organized into 14+ categories for extending Claude Code.

---

### MCPM Claude Code Docs
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/MCPM-Claude-Code-Docs)

Documentation for integrating Claude Code with MCPM external MCP server manager.

---

### Smithery Claude Code MCP Jumpstarter
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Smithery-Claude-Code-MCP-Jumpstarter)

Curated collection of 35+ MCP servers with interactive installer across 15+ categories.

---

<!-- GENERATED FROM data/marketplace.json — do not edit by hand. Run scripts/sync_marketplace.py or npm run build. -->

# Plugins

![Plugins](images/plugins.png)

All plugins registered in the [danielrosehill marketplace](https://github.com/danielrosehill/Claude-Code-Plugins). Install any of these with `/plugin install <name>@danielrosehill`.

## Systems Administration

### Desktop Manager
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Desktop-Manager-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: Linux desktop management workflow — check system, install packages, apply config, troubleshoot hardware, review logs, update system.

---

### Security Checkup
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Security-Checkup-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: security and compliance workflow — vulnerability scanning, system hardening, config audits.

---

### Sysadmin Homelab
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Sysadmin-Homelab-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: sysadmin and homelab workflow — diagnose, status, update config, backup, with linux/docker/conda/proxmox/nas/adb/sbc/remote-admin/lan variants.

---

## Development & Debugging

### Debugging
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Debugging-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: debugging workflow — capture logs, isolate issue, diagnose error, track bugs, with code/system/issue variants.

---

### Dev Tools
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Dev-Tools-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: dev tools workflow — scaffold repos, QA code review, templatize, session continuity. Retrofit-* and janitor-* skills moved to the repo-mgmt plugin in 2.0.0.

---

### Workspace Foundational
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: foundational workspace workflow — setup, context management, report parsing, inventory, template discovery, with 6 variants.

---

## Meta & Context

### Claude User Memory
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-User-Memory-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Backend-agnostic persistent user memory for Claude Code. Ships a save/recall/commit contract with personal/work context routing; bring your own memory MCP (Pinecone, Mem0, or other) via a workspace memory-config.md.

---

### Meta Tools
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Meta-Tools-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: meta-tooling workflow — context management, MCP integration, feedback filing, primitive selection for Claude Code itself.

---

## Research & Investigation

### Ideation Planning
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Ideation-Planning-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: ideation and planning workflow — capture, evaluate, rank, simulate, with ideation/single-eval/multi-ranking/feature/decision/simulation/capture variants.

---

### Legal Investigative
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Legal-Investigative-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: legal and investigative workflow — log evidence, analyze documents, redact, generate briefs, with legal-research/evidence/osint/document-analysis variants.

---

### Research Space
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Research-Space-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: research workflow — source log, summarize, deep-dive, export, with deep-research/technical/osint/georeaction/stack/ecosystem/competitor variants.

---

## AI & Prompts

### AI Attribution
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-AI-Attribution-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: AI transparency workflow — document human vs AI contributions, add attribution, audit provenance.

---

### AI Engineering
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-AI-Engineering-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: prompt engineering workflow — craft, eval, catalog, version, search prompts, with library/factory variants.

---

## Media & Content

### AI Video Producer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/AI-Video-Producer) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Drive an AI-generated video project end-to-end: creative brief, model selection, character sheets, script, storyboard, generation pipelines (text-to-image-to-video, voice-to-lip-sync, text-to-video, upscale), clip assembly, and final export.

---

### Audio Production
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Audio-Production-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: audio production workflow — normalize, VAD, transcribe, diarize, podcast assembly, with engineering/podcast/transcript variants.

---

### Claude Transcription
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Transcription-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: audio transcription workflow — denoise, VAD, transcribe (Gemini/AssemblyAI/Whisper), clean, structure, export, with cloud and local engine backends.

---

### Media Library
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Media-Library-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: media library workflow — catalog, tag, search, sort, dedupe assets.

---

### PR & Media Work
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-PR-Media-Work-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: PR and media monitoring workflow — scan coverage, summarize press, draft responses, comms strategy, with monitoring/response/strategy variants.

---

### Video Production
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Video-Production-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: video production workflow — transcode, organise, dedupe, ComfyUI generation, cover art, with editing/generative/cover-art variants.

---

## Writing & Documentation

### Content Writing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Content-Writing-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: content writing workflow — draft, proofread, version, publish, style guides, with writing/blog/opinion/document variants.

---

### Knowledge Documentation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Knowledge-Documentation-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: knowledge documentation workflow — index, cross-link, build taxonomy, version docs, with wiki/resource-library/process-docs/experiment-report variants.

---

### Technical Docs
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Technical-Docs-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: technical documentation workflow — READMEs, reference docs, changelogs, environment docs, with api-reference/code-docs/environment-docs/dev-notebook variants.

---

## Personal & Planning

### Budgeting
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Budgeting-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: personal budgeting workflow — log transactions, categorize, forecast, track goals, monthly reports.

---

### Career
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Career-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: career planning workflow — log roles, compare offers, track applications, salary benchmark, with planning/job-search/salary variants.

---

### Daniel Rosehill
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Daniel-Rosehill-Claude-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Personal-use skills and slash commands for Daniel Rosehill — released publicly for convenience.

---

### Personal Planning
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Personal-Planning-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: personal life planning workflow — log entries, review progress, set goals, with diary/health/family/house-search/preparedness/therapy/personal-dev/inbox variants.

---

### Purchasing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Purchasing-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: purchasing workflow — intake, compare products, evaluate options, recommend, with general/tech-procurement/recommendations variants.

---

### Shopping
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Shopping-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: consumer shopping workflow — find product, compare vendors, check availability. Region-specific commands (e.g. Israel) now live in dedicated plugins like israel-skills.

---

## Home & Hardware

### HP5200 Printer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-HP5200-Skill-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: HP DeskJet 5200 printer and scanner operations — ink levels, color/B&W printing, scanning, auto-discovery.

---

### Smart Home
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Smart-Home-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: smart home workflow — Home Assistant, Snapcast multi-room audio, Plex media server ops, with HA/audio/media-server variants.

---

## Filesystem & Organisation

### Filesystem Organiser
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Filesystem-Organiser-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: filesystem organisation workflow — scan, dedupe, cleanup, rename, sort for local directories and Google Drive, with local/gdrive variants.

---

## Adb

### Adb Ops
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/adb-ops-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

ADB (Android Debug Bridge) operations — onboard a phone, map folders, import media, capture screenshots, and manage bloatware with a persistent log.

---

## Awesome List

### Resource List Builder
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Resource-List-Builder-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: build, maintain, and audit curated GitHub resource lists (Awesome-style indexes) with AI-driven categorisation, alphabetised tables, and dynamic shields.io badges.

---

## Backup

### Backup Planner
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Backup-Planner) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Plan, document, and implement a backup and data-protection strategy for the current project — from architecture discovery through script generation and restore drills.

---

## Claude MD

### User Claude MD
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/User-Claude-MD-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage the user-level ~/.claude/CLAUDE.md and its chunked ~/.claude/context/ directory — audit, chunk, list, and edit global Claude Code user context for token efficiency.

---

## Data Analysis

### Claude Data Analyst
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Data-Analyst-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

First-pass data analysis toolkit: correlations, PII flagging, anomalies, hypothesis tests, data dictionaries, and trend analysis on a dataset in a folder.

---

## Data Cleaning

### Claude Data Wrangler
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Data-Wrangler-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Data cleaning, enrichment, restructuring, packaging, and documentation skills for tabular and JSON datasets (no visualisation). 31 skills covering ISO standardisation, PII detection/synthesis, data dictionaries, SQL/graph/vector/HF/GeoJSON/API targets, date & Unicode hygiene, header & numeric-precision standardisation, multilingual header localisation, incremental upstream sync, and Typst-rendered PDF documents of the data.

---

## Data Visualisation

### Data Visualisation And Publishing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Data-Visualisation-And-Publishing-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Create static and interactive data visualisations for reports, repos, and data storytelling. Purpose-organised inventory of 60+ validated open-source tools as a head start — static figures (Matplotlib, Seaborn, ggplot2), web charts (Chart.js, ECharts, Plotly.js, ApexCharts, Highcharts), high-perf (uPlot, Perspective, Lightweight Charts), bespoke (D3, Observable Plot, Vega/Vega-Lite, visx, Victory), Python/R apps (Bokeh, Dash, Altair, Streamlit, Gradio, Shiny, D-Tale, Briefer, Preswald), storytelling (Vizzu, VChart, vue-data-ui, SandDance), graphs (G6, sigma.js, Cytoscape, Gephi, Graphviz, GoJS, 3d-force-graph, Constellation), maps (deck.gl, react-map-gl, Leaflet, MapLibre, OpenLayers, folium, react-globe.gl), mobile (fl_chart, F2), BI (Superset, Metabase, Grafana, Kibana, Redash, Chartbrew), diagrams-as-code (Mermaid, PlantUML), domain-specific (Iris, QuantInvestStrats, XCharts, BizCharts, Tablesaw).

---

## Docs

### Repo To Docs
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Repo-To-Docs-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Convert GitHub repos into polished documents (PDF, blog post, white paper, internal doc) via Typst, with optional AI banner generation and multi-target publishing.

---

## Education

### Teach This Repo
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/teach-this-repo-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Uses a real code repository in reverse for developer education: assesses the learner's profile, builds a teaching plan grounded in the repo, writes lessons with code samples drawn from the source, and supports an interactive Q&A mode.

---

## Email

### Html Email Designer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/html-email-designer-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Design and build responsive HTML email templates using Foundation for Emails, Maizzle, or MJML. Framework-agnostic authoring with email-client compatibility baked in.

---

## Github

### Github Explorer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Github-Explorer-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Semantic GitHub repo discovery for reusable components. Search, rank, overview, evaluate, and recommend open-source repos — Claude parses gh API results, weighing stars, activity, maintenance, license, and stack fit.

---

### Repo Mgmt
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Repo-Mgmt) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Repository management toolkit: organise and dedupe local repos, retrofit codebases with AI agent primitives, janitor-style cleanup, convert to Claude plugins, and spin off breakaway or parallel-private repos. Includes a preferences layer that remembers where different repo types live on disk.

---

## Greeninvoice

### Greeninvoice Ops
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Green-Invoice-Ops-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Operational commands and a skill for working with the Green Invoice MCP server — invoices, clients, expenses, and monthly summaries.

---

## Image

### Image Production
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Image-Production-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code plugin: image production — editing, format conversion, batch ops, and filesystem organisation by resolution, aspect ratio, orientation, format, EXIF time, camera, plus dedupe and metadata scrubbing.

---

## Israel

### Israel Agent Skills
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Israel-Agent-Skills-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code agent skills for Israel and Hebrew-specific workflows: Hebrew translation, Hebrew typography, emergency readiness utilities, and regional lookups.

---

### Israel Shopping
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Israel-Shopping-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Israeli shopping workflows — tech retailers (Ivory, KSP, Bug, TMS), Zap price comparison, Hebrew term resolution, ILS conversion, RRP checks, PN cross-reference, brand identification, and AliExpress IL-context search (ILS/Hebrew, IL reviews, free-shipping, combo exclusion, local-vs-import compare).

---

## Learning

### Test Project Ideator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/test-project-ideator-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Generates specifications for practice/dummy development projects tailored to the user's learning objectives, technology stack, and proficiency level in each language or tool.

---

## Llm Council

### Llm Council Creator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/LLM-Council-Creator) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Scaffold new LLM Council projects from existing templates (Template, Grounded, Decide) or build bespoke council repos for specific purposes.

---

## Music Assistant

### Media Assistant Ops
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/media-assistant-ops-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Interface with a Music Assistant server via its local API — onboard a deployment, control players, snapshot speaker rosters, save/update per-player DSP presets, and apply a curated podcast EQ preset.

---

## Nlp

### Text Corpus Analysis
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Text-Corpus-Analysis) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Skills for analyzing large text corpora — topic modeling (BERTopic with temporal evolution), NER, categorization into fixed taxonomies, bottom-up category derivation, multi-level taxonomy design, word frequency, synonym clustering for voice-note/STT corpora, parametric stats, and metadata↔content correlation. Three execution lanes (classical NLP, local LLM via Ollama, cloud LLM via OpenRouter) with explicit cost-awareness: mandatory pre-run estimates for >1k-doc LLM passes, two-pass cheap→premium pattern, embeddings+clustering preferred over pairwise LLM comparison.

---

## Resume

### Resume Typesetter
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Resume-Typesetter) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage a resume as JSON Resume schema data and render it with custom Typst templates. Onboard, iterate, fork variants, and version.

---

## Scraping

### Local Web Capture
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Local-Web-Capture) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Capture geo-restricted web content (articles, prices) via the user's own localhost so requests exit via the user's IP. Headless-first escalation ladder (Scrapling static -> stealth -> Playwright -> real Chrome via bb-browser). Project-local save (in-repo captures/) with global fallback. Batch capture with human + agent summaries, Typst PDF compilation, and arbitrary-language capture+translate (default Hebrew -> English).

---

## Task Management

### Task Queuer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Task-Queuer-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Repo-based task queueing system with categorisation and prioritisation. Scaffolds a planning/ folder, logs tasks (single, batch list, or voice-transcribed), buckets them by category, and hands prioritised work off to the repo's orchestration agent.

---

# Templates / Scaffolds

Scaffolds used to be distributed as ~100 standalone template repos and a `New-Repo-From-Template` plugin. That pattern was retired in the April 2026 reshape.

**Scaffolds now live inside the [cluster plugins](#plugins).** Each of the 28 cluster plugins bundles the workspace primitives for its domain (commands, skills, agents, MCP configs) and exposes a provisioning skill that writes a fresh per-project scaffold on demand — so instead of cloning a template repo, you install the relevant plugin once and ask Claude Code to scaffold a new workspace for whatever project you're starting.

See the [Plugins](#plugins) section above for the full cluster list.

---

# Slash Commands

![Slash Commands](images/slashes.png)

Individual slash commands, sometimes integrated into other plugins or sometimes just for use at the user level.

> **See also:** The **[Claude Slash Commands](https://github.com/danielrosehill/Claude-Slash-Commands)** repo serves as both a 350+ command library and the dedicated index for all slash command repos.

### AI-Human Attribution Adder
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/AI-Human-Attribution-Adder) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

Adds AI/human attribution sections to README files for transparent tool usage documentation.

---

### Claude App Optimiser
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-App-Optimiser) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Slash command deploying a sub-agent for codebase optimization and dead code removal.

---

### Claude Calls The Shots
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Calls-The-Shots) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

Flips Claude Code into autonomous, action-first mode — ships a per-session `/calls-the-shots` slash command plus an optional always-on snippet injected into `~/.claude/CLAUDE.md`.

---

### Claude Code Linux Desktop Slash Commands
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-Linux-Desktop-Slash-Commands) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

System administration slash commands for Linux desktop environments.

---

### Claude File Organiser Super Slash
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-File-Organiser-Super-Slash) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

Slash command that transforms disorganized filesystems into well-structured directories.

---

### Claude MD Chunk
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-MD-Chunk) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

Slash command that condenses bloated CLAUDE.md files to essentials and organizes supplementary context into a structured `agent-context/` folder.

---

### Claude Slash Commands
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Slash-Commands) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square)

General-purpose slash command library for various Claude Code workflows.

---

### No Wheel Inventions
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/No-Wheel-Inventions) ![Slash Commands](https://img.shields.io/badge/Slash-Commands-cyan?style=flat-square) ![Agent Config](https://img.shields.io/badge/Agent-Config-orange?style=flat-square)

Slash commands encouraging use of existing libraries instead of building custom solutions.

---

# Miscellaneous

![Misc](images/misc.png)

Other projects including meta-resources, feedback, and utilities that span multiple categories.

### AI Ideation Runs
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/AI-Ideation-Runs)

Public archive of structured AI ideation sessions run via Claude Code — each `/run` takes a topic and saves a dated batch of ideas with name, summary, category, feasibility/impact ratings, considerations, and next steps.

---

### AI Memory Planning 0426
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/AI-Memory-Planning-0426)

Planning notes and architecture diagrams exploring three complementary methods for building a personal AI memory system over a vector store — passive distillation from chat, agentic interviews, and manual curation.

---

### Claude Agent Blueprints
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Agent-Blueprints)

Curated collection of 75+ agent workspace templates organized by use case, demonstrating the Agent Workspace Model across code and non-code domains.

---

### Claude Code Bugs And FRs
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-Bugs-And-FRs)

Staging area for Claude Code bug reports and feature requests before filing upstream at anthropics/claude-code.

---

### Claude Code Marketplace Hub
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/claude-code-marketplace)

Decentralized directory aggregating multiple community-maintained Claude Code plugin marketplaces.

---

### Claude Code Plugin (Meta)
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/claude-code-plugin)

Meta-plugin for managing Claude Code configuration, slash commands, and agent development.

---

### Claude Code Plugins Marketplace
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-Plugins)

Centralized marketplace for discovering and installing Claude Code plugins — source of truth for the [Plugins section](./plugins.md).

---

### Claude Code Context Feature Requests
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Code-Context-Feature-Requests)

Feature requests for improving Claude Code's context handling capabilities.

---

### Claude Interview
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Interview-062325)

Transcript from an Anthropic user research interview on AI tools and adoption.

---

### Claude Is Awesome
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Is-Awesome) ![Template](https://img.shields.io/badge/Template-Ready-green?style=flat-square) ![Light Touch](https://img.shields.io/badge/Light-Touch-lightgray?style=flat-square)

Template for creating curated resource lists with automated formatting and badge generation.

---

### Claude Local AI Agent Research
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Local-AI-Agent-Research)

Research into agentic AI tools optimized for system administration rather than code generation.

---

### Claude User Manual
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-User-Manual)

Plugin for generating personalized user manuals and private documentation for codebases.

---

### Local Claude Plugin Install Research
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Local-Claude-Plugin-Install-Research)

Research and notes on installing Claude Code plugins locally rather than through the marketplace.

---

### New Turn Claude Hook
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/New-Turn-Claude-Hook)

Tool that determines whether to continue an AI conversation or start fresh for optimal context.

---

### Non-Code Claude Code
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Non-Code-Claude-Code)

Showcase of creative Claude Code applications beyond traditional software development.

---

### Skill Creation Research
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Skill-Creation-Research)

Research and notes on designing and authoring Claude Code skills.

---
