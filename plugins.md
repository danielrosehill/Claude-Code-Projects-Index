<!-- GENERATED from categories/08-plugins.md — do not edit directly. Run `npm run build`. -->

<!-- GENERATED FROM data/marketplace.json — do not edit by hand. Run scripts/sync_marketplace.py or npm run build. -->

# Plugins

![Plugins](images/plugins.png)

All plugins registered in the [danielrosehill marketplace](https://github.com/danielrosehill/Claude-Code-Plugins). Install any of these with `/plugin install <name>@danielrosehill`.

## Systems Administration

### Desktop Manager
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Desktop-Manager-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Linux desktop management — auto-profiles the local machine on first run and persists it to user data, then runs system checks, package install/remove, config application, hardware troubleshooting, service/log inspection against that profile.

---

### Security Auditor
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Security-Auditor-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Register machines and run repeatable Claude-Code-driven security audits over SSH, with timestamped reports and per-machine profiles.

---

## Development & Debugging

### Debugging
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Debugging-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Debugging — capture logs, isolate issue, diagnose error, track bugs, with code/system/issue variants. Includes a KDE hotkey utility for capturing live system bugs.

---

### Dev Debugger
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/dev-debugger-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Bug-ticket workflow for development repos — capture bugs into planning/bugs/, dispatch specialist remediation agents (reproducer, diagnoser, patcher, fix-documenter), document fixes, and ship releases.

---

### Dev Tools
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Dev-Tools-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Dev-tools — scaffold repos, multi-agent QA review, templatize. Session-handover commands and agent moved to claude-hopper in 1.2.0.

---

### Kaizen
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Kaizen) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Kaizen for mature codebases: atomic improvements, one commit each, tracked pass by pass from a baseline. Init, intake, step, pass skills.

---

### Kaizen Please
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Kaizen-Please) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Kaizen for any project, not just code: small steps, a shared journal, reviews, the agent's Kaizen thoughts as PDF.

---

### Workspace Foundational
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Workspace-Foundational-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Foundational workspace — setup, context management, report parsing, inventory, template discovery, with 6 variants.

---

## Meta & Context

### Personal Context
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Personal-Context-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Builds and maintains a persistent, portable background context layer about the user — intake interview, ingestion of material they already have, gap analysis, scoped retrieval, maintenance and export. Plain markdown entries in a store the user owns, read through declared scopes and sensitivity levels; explicitly does not use model-managed memory. Ships the Portable Context Contract so issue-scoped workspaces can read it without re-asking who the person is.

---

### Plugin Vault
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Vault) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Meta-plugin for per-project activation of dormant plugins and MCP servers from a personal vault. Mitigates user-level eager skill description loading.

---

### User Memory
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-User-Memory-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Backend-agnostic persistent user memory for Claude Code. Ships a save/recall/commit contract with personal/work context routing; defaults to the `memory` upstream on an MCP gateway, or bring your own memory MCP via a workspace memory-config.md.

---

## Research & Investigation

### Ideation Planning
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Ideation-Planning-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Ideation and planning — capture, generate, evaluate, rank, simulate, and plan ideas, with ideation/single-idea-eval/multi-idea-ranking/feature-ideas/simulation/idea-capture variants and Typst PDF deliverables.

---

### Legal Investigative
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Legal-Investigative-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Legal and investigative — log evidence, analyze documents, redact, generate briefs, with legal-research/evidence/osint/document-analysis variants.

---

### Modular Research
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Modular-Research-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Modular research task: brief in, PDF + podcast out. Takes a (dictated) brief through a GitHub repo as research notebook, parallel-subagent research with a source log, a Typst PDF report and a two-host educational podcast (Gemini TTS), then Google Drive and email. Every output module is optional and runs alone; the repo can stay a one-off or keep growing in follow-up rounds.

---

### Research Space
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Research-Space-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Research — source log, summarize, deep-dive, export, with deep-research/technical/osint/georeaction/stack/ecosystem/competitor/purchasing/general-research-workspace/obsidian-vault variants. The obsidian-vault variant scaffolds the research loop as a working Obsidian vault (committed .obsidian/ config, frontmatter schema, wikilinks, templates, canvas). Includes a 30-agent tech research team for hardware/software stack evaluations (folded in from Claude-Tech-Research-Team).

---

### Social Feedback
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Social-Feedback-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Check what people are actually saying about a topic, product, or provider by searching curated social-discourse sources (Reddit, Hacker News, Stack Exchange, Trustpilot, YouTube, Lobsters).

---

## AI & Prompts

### AI Attribution
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-AI-Attribution-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

AI transparency — document human vs AI contributions, add attribution, audit provenance.

---

### AI Engineering
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-AI-Engineering-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Prompt engineering — craft, eval, catalog, version, search prompts, with library/factory variants.

---

## Media & Content

### AI Video Producer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-AI-Video-Producer-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Drive an AI-generated video project end-to-end: creative brief, model selection, character sheets, script, storyboard, generation pipelines (text-to-image-to-video, voice-to-lip-sync, text-to-video, upscale), clip assembly, and final export. Ships fal.ai/Replicate/MiniMax MCP servers and fal-js + WaveSpeed Python SDK runners.

---

### Audio Production
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Audio-Production-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Audio production — normalize, VAD, transcribe, diarize, podcast assembly, with engineering/podcast/transcript variants.

---

### Media Library
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Media-Library-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Media library — catalog, tag, search, sort, dedupe assets.

---

### PR & Media Work
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-PR-Media-Work-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

PR and media monitoring — scan coverage, summarize press, draft responses, comms strategy, with monitoring/response/strategy variants.

---

### Transcription Pipeline
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Transcription-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Audio transcription — denoise, VAD, transcribe (Gemini/AssemblyAI/Whisper), clean, structure, export, with cloud and local engine backends.

---

### Video Editing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Video-Editor-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Video editing, transcoding, video processing, and multimedia workflow automation. Two-tier workspace (index + project), per-user data store, and a growing set of ffmpeg/MLT/Kdenlive primitives.

---

## Writing & Documentation

### Content Writing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Content-Writing-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Content writing — draft, proofread, version, publish, style guides, with writing/blog/opinion/document variants.

---

### Knowledge Documentation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Knowledge-Documentation-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Knowledge documentation — index, cross-link, build taxonomy, version docs, with wiki/resource-library/process-docs/experiment-report variants.

---

### Technical Docs
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Technical-Docs-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Technical documentation — READMEs, reference docs, changelogs, environment docs, with api-reference/code-docs/environment-docs/dev-notebook variants.

---

## Personal & Planning

### Amazon
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Amazon-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Amazon.com marketplace research — verified price, stock, rating, seller and specs read from the listing rather than the search grid; Prime-aware delivery dates checked against the ZIP they were actually rendered for; filtered signed-in search with tested extractors, a marketplace profile and a durable brand allowlist.

---

### Budgeting
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Budgeting-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Personal budgeting — log transactions, categorize, forecast, track goals, monthly reports.

---

### Career
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Career-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Career planning — log roles, compare offers, track applications, salary benchmark, with planning/job-search/salary variants.

---

### Personal Planning
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Personal-Planning-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Personal life planning — log entries, review progress, set goals, with diary/health/family/house-search/preparedness/personal-dev/inbox variants.

---

### Procurement Tools
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/procurement-tools-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Product research and procurement skills with a particular focus on technical specification conformance — does this part actually meet the requirement, and can you show your working. Marketplace-agnostic: spec definition from a vague want or a photograph, annotated search vocabulary, versioned spec-as-code, manufacturer datasheet retrieval, cross-region part-number equivalence, conformance evaluation matrices, bills of materials and RFQ packages. Plus the surrounding process: intake, research, compare, evaluate, recommend, market-check, spec-driven market landscape surveys, live price/delivery scanning through your own VPN egress, preference memory and hardware-rig profiling. Hands off to the marketplace-specific plugins (shopping, israel-shopping, amazon, aliexpress-israel-skills) once a question becomes about a particular shop.

---

### Shopping
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Shopping-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Region-specific consumer shopping primitives — find products, compare local vendors, check availability, and generate ranked purchase recommendations. Ships variant scaffolds per supported region and a provisioning skill for fresh shopping workspaces. Marketplace-specific research (Amazon US, AliExpress Israel) now lives in dedicated per-marketplace plugins; the marketplace-plugins skill is the roster.

---

### Therapy Tracking
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Therapy-Tracking-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Organising therapy reflections — pre/post-session notes, goal tracking, and turning voice-memo transcripts into structured problem summaries. Not therapy: organises notes only. Workspace data lives outside the plugin so the same install survives plugin updates.

---

## Home & Hardware

### Smart Home
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Smart-Home-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Smart home — Home Assistant, Snapcast multi-room audio, Plex media server ops, with HA/audio/media-server variants.

---

## Filesystem & Organisation

### Filesystem Organiser
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Filesystem-Organiser-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Filesystem organisation — scan, dedupe, cleanup, rename, sort for local directories and Google Drive, with local/gdrive variants. Includes organise-filesystem (modular modes) and super-organise (comprehensive single-pass) skills.

---

## MCP & Infrastructure

### Unofficial MCP Builder
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Unofficial-MCP-Builder-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Author and maintain unofficial MCP servers for third-party APIs that don't ship one. Generate a server from the vendor's API docs verified against the live API with your own key, detect upstream drift on a schedule, and smoke-test against real operations. Bound by a committed api-surface.yaml recording what the API actually does versus what its docs claim. Publishes to npm.

---

## Adb

### Adb Ops
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-ADB-Ops-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

ADB (Android Debug Bridge) operations — onboard a phone, map folders, import media, capture screenshots, and manage bloatware with a persistent log.

---

## Adguard

### Pseudospam Filter
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Pseudospam-Filter-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

A second spam filter for pseudospam (outreach produced at scale, dressed up as personal): parallel Haiku judges taught by your own Gmail example labels, a review-queue label instead of deletion, a reply queue for genuine mail, plus sender blocks, unsubscribe replies and tracking-pixel/DNS blocking.

---

## Agent To Agent

### Dead Drop
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Dead-Drop) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Asynchronous agent-to-agent messages between Claude Code sessions working in different repositories. Agent A writes a markdown message into repo B's a2a/ folder and pings B by SendMessage if it is running; B's SessionStart hook lists open messages, B acts on them, sets any reminders the message asks for in its own scheduler, and records what it did in the same file. For long tasks the sender keeps one living message current (revision: counter) and asks the reader to re-check it on an interval (watch: 30m). No server and no shared meeting place: the target repo's folder is the mailbox. Breakout (an idea that needs its own new repo) and same-repo handover are message kinds.

---

## Air Quality

### Air Quality Toolkit
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Air-Quality-Toolkit-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Look up current and historical air quality, calculate AQI from raw pollutant readings, and run modelling utilities. Defaults to WAQI with fallbacks to OpenAQ and AireLibre.

---

## Aliexpress

### Aliexpress Israel Skills
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Aliexpress-Israel-Skills) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

AliExpress shopping skills for Israel-based buyers — Choice-first search in ILS via a local browser, free-shipping filter, Israeli-reviews filter, single-listing landed-cost parse, and a running cart-value VAT-threshold nudge ($75 de-minimis).

---

## Analysis

### Report Analyst
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Report-Analyst-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Skeptical analyst toolkit for long reports — READ/SKIM/SKIP verdicts, structured extraction (arguments, findings, stats, case studies, key snippets), and an opinionated executive summary. Built-in Jaded Report Reader persona that refuses credit for filler.

---

## Avp

### Avp Music Video
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-AVP-Music-Video-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Audio → branded music video (avp): waveform, logo, karaoke. Install audio-visualizer-python, pull logo/colours/font from a repo into a brand kit, render an MP3 (e.g. from Suno) through JSON templates (waveform, spectrum bars, logo pulse, 9:16), burn in karaoke lyrics from LRC/SRT, and encode small with AV1 by default.

---

## Awesome List

### Resource List Builder
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Resource-List-Builder-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Build, maintain, and audit curated GitHub resource lists (Awesome-style indexes) with AI-driven categorisation, alphabetised tables, and dynamic shields.io badges.

---

## Backup

### Backup Planner
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Backup-Planner-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Plan, document, and implement a backup and data-protection strategy for the current project — from architecture discovery through script generation and restore drills.

---

## Bluetooth

### Linux Bt
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Linux-BT-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Bluetooth on Linux from the command line, because the desktop pairing dialogs are unreliable. Diagnose the adapter, scan, pair + trust + connect in one non-interactive bluetoothctl session, manage known devices (connect, disconnect, forget, battery) and reset the stack.

---

## Book

### Book Writing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Book-Writing-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Write a full-length reference or instructional book with teams of subagents — definition, planning, research, parallel chapter drafting, review, graphics and publication. Organised so no single agent is ever handed the whole book, because quality degrades long before a context window fills; consistency is carried by a style guide, per-chapter briefs and a continuity ledger instead of by shared context. Authorship only — print geometry hands off to kdp-publishing.

---

## Btrfs

### Snap It
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Snap-It-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage BTRFS snapshots via snapper and btrfs from Claude Code — create, list, diff, rollback, and prune subvolume snapshots. Includes /snap and /snap-before commands for one-shot and pre/post-paired snapshots around risky changes.

---

## Business

### Business Idea Eval
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Business-Idea-Eval-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Evaluate, refine, and develop business ideas through structured lenses — VC review, TAM, B2B/B2C fit, assumptions, objections, hardware feasibility, dev specs, timelines, social impact — plus an LLM council pattern (subagents or Karpathy clone), synthesis, and Typst PDF outputs for internal and public-facing docs.

---

## Buttondown

### Buttondown Mgmt
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Buttondown-Mgmt-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage one or more Buttondown newsletters from Claude Code — multi-newsletter config, reusable email templates, drafts, sends, subscribers, and API ops grounded in a locally cached copy of the official Buttondown docs.

---

## Certification

### Spec Led Certification
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/spec-led-certification-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Choose a professional certification specification-first rather than market-first. create-workspace stands the search up as a private GitHub repo instantiated from the Spec-Led-Certification template, so it survives the machine and its git history shows when the scorecard was frozen relative to when the research ran. Three entry points for the three situations — start-search onboards and runs the full intake, rerun-search archives the previous run and reports what moved in the market, update-profile changes what is stored about you and marks the scorecard stale. Intake writes five dated profile files — subject, current position read from evidence, learning preferences, objectives and standing positions, money and time — a weighted scorecard is derived from those alone and frozen before any credential is looked up, then candidates are scored against it with a source tier and confidence tag on every number. Hard requirements exclude rather than score down. Emits a ranked comparison and a Typst PDF whose figures are computed from the CSVs at compile time. All state is written to the working directory, never to an agent memory store.

---

## Chatgpt

### Chatgpt Importer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-ChatGPT-Importer-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Import a ChatGPT conversation into local files via the browser. Captures the full thread from a chatgpt.com URL, a shared link, or an official export archive, then normalizes it to JSON and renders Markdown or a styled Typst PDF with user and assistant turns marked, artifacts (canvas docs, images, code) extracted, cited sources collected, and conversation metadata recorded. Includes a two-pass redaction skill and a conversation-to-context workflow that writes transcripts into a repo's context/ folder.

---

## Claude Code

### Rudder
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Rudder) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude-Rudder — collection of utilities to smoothen Claude Code UX. Context-gate workflow, log/blocker capture, plugin/MCP primitives, repo & docs spawning, and the canonical user-data storage convention. (Session-hopping skills moved to Claude-Hopper.)

---

### Session Hopper
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Hopper) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude-Hopper — skills for hopping between discrete terminal-bound Claude Code sessions on Linux. Spawn new instances (Konsole), hand off context (full / clipboard / with-tasks), resume from handovers, and pick up leftover work.

---

### Style Switcher
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Style-Switcher) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Persona-recipe library for swapping Claude into themed personalities (Daredevil, Jaded IT, Reluctant, Chatty, Philosophical, Operational, Dubious, Hyper Creative, Approval Needed, Visionary, Claude FM, Claude Bouncer). Each recipe ships a banner image and sound effect, and applies via either a managed block in ~/.claude/CLAUDE.md or a repo-sandbox mode that holds the user CLAUDE.md aside.

---

## Claude MD

### Context File Tester
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-MD-Tester) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Safely swap ~/.claude/CLAUDE.md for test/joke configs via symlink. Terminal-only restore that does not depend on the Claude harness, so a hostile test config can never trap you.

---

### User Context File
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/User-Claude-MD-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage the user-level ~/.claude/CLAUDE.md and its chunked ~/.claude/context/ directory — audit, chunk, list, and edit global Claude Code user context for token efficiency.

---

## Comparison

### Comparison Artifacts
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Comparison-Artifacts) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Software evaluation tables, scoring and quadrants: tick/cross or short-descriptor feature tables, weighted scoring from your stated priorities, and 2x2 quadrant charts, rendered to Markdown, Typst or SVG from one data file and written into the document you're drafting.

---

## Copyq

### Copyq Scripting
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-CopyQ-Scripting-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Foundational advanced clipboard scripting skills for CopyQ on Ubuntu Linux — CLI reference, custom commands, tab/item management, global shortcuts, and command bundle import/export.

---

## Cups

### Network Cups
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Network-CUPS-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Discover, diagnose, and print to networked CUPS printers from Claude Code. Wraps the lan-mcp-cups MCP server and adds LAN discovery (avahi/Bonjour, arp-scan) plus ufw firewall sanity checks.

---

## Data Analysis

### Data Analyst
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Data-Analyst-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

First-pass data analysis toolkit: correlations, PII flagging, anomalies, hypothesis tests, data dictionaries, and trend analysis on a dataset in a folder.

---

## Data Cleaning

### Data Wrangler
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Data-Wrangler-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Data cleaning, enrichment, restructuring, packaging, and documentation skills for tabular and JSON datasets (no visualisation). 31 skills covering ISO standardisation, PII detection/synthesis, data dictionaries, SQL/graph/vector/HF/GeoJSON/API targets, date & Unicode hygiene, header & numeric-precision standardisation, multilingual header localisation, incremental upstream sync, and Typst-rendered PDF documents of the data.

---

## Data Ingestion

### Browser Data Capture
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Browser-Data-Capture-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Streamline programmatic data ingestion against sites and apps that don't ship a documented API — capture network traffic (HAR, mitmproxy, or live tab via claude-in-chrome), map endpoints, infer schemas, and produce a draft OpenAPI spec you can build a stable client against. Ships skills for per-domain map documents, version-controlled storage in a private GitHub repo, and good-faith vulnerability disclosure if a finding turns up incidentally. White-hat use only.

---

## Data Visualisation

### Data Visualisation And Publishing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Data-Visualisation-And-Publishing-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Create static and interactive data visualisations for reports, repos, and data storytelling. Purpose-organised inventory of 60+ validated open-source tools as a head start — static figures (Matplotlib, Seaborn, ggplot2), web charts (Chart.js, ECharts, Plotly.js, ApexCharts, Highcharts), high-perf (uPlot, Perspective, Lightweight Charts), bespoke (D3, Observable Plot, Vega/Vega-Lite, visx, Victory), Python/R apps (Bokeh, Dash, Altair, Streamlit, Gradio, Shiny, D-Tale, Briefer, Preswald), storytelling (Vizzu, VChart, vue-data-ui, SandDance), graphs (G6, sigma.js, Cytoscape, Gephi, Graphviz, GoJS, 3d-force-graph, Constellation), maps (deck.gl, react-map-gl, Leaflet, MapLibre, OpenLayers, folium, react-globe.gl), mobile (fl_chart, F2), BI (Superset, Metabase, Grafana, Kibana, Redash, Chartbrew), diagrams-as-code (Mermaid, PlantUML), domain-specific (Iris, QuantInvestStrats, XCharts, BizCharts, Tablesaw).

---

## Datasets

### Data Annotation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Data-Annotation-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

End-to-end data annotation toolkit. Prep raw data, design annotation schemas, annotate interactively with Claude (small scale) or scaffold Gemini batch inference (large scale), and publish to Hugging Face.

---

## Decision Making

### Decision Evaluation Framework
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Decision-Evaluation-Framework-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Apply 20+ classical decision-making frameworks (cost-benefit, pre-mortem, MCDA, decision tree, reversibility, regret minimization, OODA, Eisenhower, SWOT, second-order, opportunity cost, 10/10/10, inversion, base rates, Kepner-Tregoe, six hats, Cynefin, red-team, stakeholder map, time-horizon) to any major decision — parallel multi-lens analysis, synthesis, and Typst PDF export.

---

## Diagrams

### Nano Tech Diagrams
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Nano-Tech-Diagrams-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Generate, transform, and clean up tech diagrams and whiteboard photos via the Nano Banana 2 model (Fal AI). Wraps the nano-tech-diagrams MCP server with a curated prompt library across 5 diagram families and 28+ visual styles.

---

## Discovery

### Marketplace Guide
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Marketplace-Guide-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Start here: browse these plugins by theme, find one for a task, see what's new. Reads the live manifest.

---

## Docs

### Repo To Content
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Repo-To-Content-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Convert GitHub repos into polished content (PDF, white paper, internal doc, public-docs publication) via Typst, with optional AI banner generation and multi-target publishing.

---

## Donetick

### Donetick
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Donetick-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Companion plugin for the donetick-mcp server. Bundles the MCP and adds skills for chore management against a self-hosted Donetick instance — daily brief, list/create/complete chores, label management.

---

## Education

### Teach This Repo
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Teach-This-Repo-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Uses a real code repository in reverse for developer education: assesses the learner's profile, builds a teaching plan grounded in the repo, writes lessons and file-by-file analyses with code samples drawn from the source, supports interactive Q&A, and typesets any of it as a PDF via Typst.

---

## Email

### Html Email Designer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-HTML-Email-Designer-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Design and build responsive HTML email templates using Foundation for Emails, Maizzle, or MJML. Framework-agnostic authoring with email-client compatibility baked in.

---

### Rtl Email
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-RTL-Email) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Send email in right-to-left scripts (Hebrew, Arabic, Farsi, Urdu) that actually renders RTL. Plain-text email carries no direction metadata, so RTL bodies render LTR in many clients and multi-part numbers like account references reorder. Ships dir=rtl HTML templates, separate personal and business send skills inheriting saved signature profiles, and one-time signature setup. Works with Google Workspace MCP or Resend.

---

## Exchange

### Agent Exchange
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Agent-Exchange) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Two-way file exchange between you and Claude: from-human/ and from-agent/ folders, a CLAUDE.md block so Claude uses them unprompted, and a small explorer app (with launcher) locked to that folder, with new-file badges and read receipts.

---

## Fine Tuning

### Custom Model Planning
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Custom-Model-Planning-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Plan small custom models and fine-tunes: check the Hub, research options, write the spec in a planning repo.

---

## Forecasting

### Geopol Sim
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Geopol-Sim-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Thin orchestrator for geopolitical forecasting simulations. Scaffolds, runs, bundles, and grades simulations from multiple decoupled upstream templates (lean LLM-council and snowglobe-style actor-simulation variants).

---

## Forensics

### Digital Evidence
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Digital-Evidence-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

General-purpose digital-evidence processing: capture, hash, OpenTimestamps, ExifTool/MediaInfo metadata, BagIt packaging, immutable sync. Layers with legal-investigative for full chain-of-custody workflows.

---

## Freight

### Freight Vol Calculator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Freight-Vol-Calculator) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Freight volume arithmetic from a product's external dimensions — retrieves and cross-checks dimensions from a supplier listing, then pallet quantity across 11 pallet standards, container loads palletised or floor-loaded for 20 ft / 40 ft / HC / reefer / 13.6 m trailer with stated buffers and payload limits, master-carton permutations ranked by units per container, and freight cost per unit from rates you supply. Reproduces published trade figures; holds no rate data and makes no network call.

---

## Gimp

### Gimp
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-GIMP-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Bare-bones GIMP CLI wrapper for Linux: detect install (native/Flatpak/Snap/AppImage), persist a per-user profile, run Script-Fu batch ops, export images, install/list GIMP-side plugins.

---

## Github

### Gist Writer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Gist-Writer-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Publish content to GitHub gists with clear AI authorship — Claude-authored solution gists and collaborative debug write-ups, both with model+date attribution, environment context, and a PII pre-flight scrub for public publishes. Visibility is a per-call parameter with a configurable default.

---

### Github Explorer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Github-Explorer-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Semantic GitHub repo discovery for reusable components. Search, rank, overview, evaluate, and recommend open-source repos — Claude parses gh API results, weighing stars, activity, maintenance, license, and stack fit.

---

### Start Here
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Start-Here) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Find, navigate and download Daniel Rosehill's GitHub repositories: search all 1,000+ public repos, find the curated topic index for a subject, and clone one repo or a filtered set. Reads the Start-Here index JSON instead of crawling GitHub.

---

## Gpg

### Gpg Ops
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-GPG-Ops-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

GPG operations: generate keypairs, export public keys, encrypt, decrypt, sign, and verify files or text using the local GnuPG keyring.

---

## Greeninvoice

### Greeninvoice Ops
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Green-Invoice-Ops-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Operational commands and a skill for working with the Green Invoice MCP server — invoices, clients, expenses, and monthly summaries.

---

## Habits

### Habits
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Agent-Habits) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Habits (rules, always-on or triggered) and SOPs (procedures) as one markdown file each, in a private folder, with one small CLAUDE.md block. Library of example habits to adopt. Replaces sop-library.

---

## Hardware

### Hardware Id Annotation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Hardware-ID-Annotation-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Identify and annotate hardware components from photos — circuit boards, motherboards, ICs — with overlays, datasheet cross-checks, and structured BOMs.

---

### Hardware Spec Assembly
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Hardware-Spec-Assembly-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Define hardware project BOMs with ESP32-first focus — onboarding captures location/vendors/on-hand gear, then skills for spec creation, live web research of parts (AliExpress/Adafruit/etc.), budgeting, sourcing, compatibility checks, wiring specs, PCB design starting points, assembly instructions, 3D-printable suggestions, and AI-generated mockups via fal.ai nano-banana.

---

## Home Assistant

### Home Assistant Mgmt
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Home-Assistant-Mgmt-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage a Home Assistant instance via SSH and the HA REST API — guided first-run onboarding, automation/entity authoring, service calls, TTS testing, and log review. Per-host config is stored outside the plugin so the same install works across multiple Home Assistant environments.

---

## Hooks

### New Task Split
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/New-Task-Split) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Auto-/clear on a new task: local ONNX classifier moves unrelated prompts to a fresh session. claudehook trial launcher, install, toggle, update-model, remove.

---

## Image

### Background Removal
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Background-Removal-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Remove image backgrounds via rembg — single-pass, two-pass cleanup, batch mode, and KDE Dolphin right-click integration.

---

### Image Annotation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Image-Annotation-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Capture screenshots and apply annotations (arrows, callouts, boxes, highlights, blur/redaction) on Linux via Pillow + ImageMagick, with batch WebP conversion and PDF bundling. Originals are never modified.

---

### Image Production
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Image-Production-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Image production — editing, format conversion, batch ops, and filesystem organisation by resolution, aspect ratio, orientation, format, EXIF time, camera, plus dedupe and metadata scrubbing.

---

## Inventory

### Declutter Genie
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Declutter-Genie-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Inventory analysis and decluttering assistant — import a household inventory in any format, then identify discards, duplicates, resale targets, donation targets (geo-aware), insurance-worthy items, and generate throw-out / giveaway lists as CSV or PDF.

---

## Israel

### Ikea Israel
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-IKEA-Israel-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Stock counts, aisle/bin and prices across IKEA Israel's 5 branches.

---

### Israel Agent Skills
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Israel-Agent-Skills-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code agent skills for Israel-specific workflows: emergency readiness utilities, medicine and drug registry lookups, Kol Zchut rights lookups, municipal and transport information, and regional lookups. For Hebrew correspondence and typography see the hebrew-correspondence plugin.

---

### Israel Opening Hours
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Israel-Opening-Hours-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Check opening hours for Israeli businesses, including hours stated relative to Shabbat and yom tov. Combines Google Business and easy.co.il for stated hours with Hebcal candle-lighting/havdalah times, resolving phrasing like 'reopens an hour after Shabbat' into concrete clock times. Bundles 56 Israeli locations with verified per-city candle-lighting customs.

---

### Israel Shopping
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Israel-Shopping-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Israeli shopping workflows — tech retailers (Ivory, KSP, Bug, TMS), Zap price comparison, Hebrew term resolution, ILS conversion, RRP checks, PN cross-reference, brand identification, and AliExpress IL-context search (ILS/Hebrew, IL reviews, free-shipping, combo exclusion, local-vs-import compare).

---

### Maccabi Online Skills
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Maccabi-Online-Skills) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Maccabi Online (Israel health fund) portal: meds, appointments, doctor messages, results, hitchaivut, refunds. Unofficial; needs your signed-in Chrome.

---

### Netek Disconnect
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/netek-disconnect-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Cancel Israeli service subscriptions (ניתוק) through netek.co.il — mobile, internet, landline, TV, international calling, water bars, newspapers and credit cards across 55 providers. Resolves the provider and exact Hebrew service string, validates the Israeli ID checksum and address, shows the exact request before sending, and submits only on explicit confirmation. Falls back to filling the form in Chrome when the API changes. Uses Netek's own private, undocumented backend — not a published API.

---

## Jewish

### Jewish Texts Reference
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Jewish-Texts-Reference-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Look up Jewish texts and references via the Sefaria MCP server — Tanakh, Talmud, Mishnah, Halakha, Kabbalah, commentary, dictionaries, and topics. Includes nikkud add/strip skills (Dicta nakdan + removenikud APIs, offline regex, unikud fallback).

---

### Jewish Utilities
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Jewish-Utilities-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Misc Jewish utility skills: shabbat candle-lighting/havdalah, zmanim (GR"A + MG"A), parsha-of-the-week, Hebrew/Gregorian date conversion (sunset-aware), upcoming holidays (IL/diaspora), and daf yomi. Wraps zmanim-mcp-server and hebcal MCP. Onboarding captures location for halachic-time skills. Companion to jewish-texts-reference.

---

## Kde

### Kde Agent Workspace
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-KDE-Agent-Workspace-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Give Claude its own KDE Plasma desktop to test apps in. Creates a "Claude" or "AI Agents" virtual desktop, launches real GUI or terminal apps there and drives them via AT-SPI with KWin window capture — without taking over the user's screen — and binds the agent desktop to its own monitor (per-output desktops on Plasma 6.7+). Or test in a headless sandbox KWin on a private bus, off your screen entirely.

---

### Kde Plasma
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-KDE-Plasma-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

KDE Plasma (Wayland) runtime utilities — KWin scripting, plasmoid management, panel layout backup, virtual desktops & activities, KGlobalAccel shortcuts, theme/look-and-feel switching, KDE Connect, Klipper, Baloo, kwriteconfig safe-edit, plasma-restart helpers, qdbus introspection, kscreen save/apply, KWallet ops. Complements generic Linux desktop-management plugins.

---

### Kde Plasmoid Dev
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-KDE-Plasmoid-Dev-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Skill for developing KDE Plasma plasmoids (QML/Plasma 6 desktop and panel widgets) — scaffold, debug, package, install, and migrate Plasma 5 → 6.

---

## Kdp

### Kdp Publishing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/KDP-Publishing-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Amazon KDP paperback production with Typst — choose a standard trim, typeset the interior with gutter-aware margins and an even page count, build the full-wrap cover last from the interior's measured extent, pre-flight for silent glyph substitution and stale spines, and assemble the upload folder. Production only; it does not write the book.

---

## Label Printer

### Label Printer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/label-printer-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Print labels from Claude Code on Brother QL and P-touch label printers on Linux. Discovers printers over mDNS, USB and CUPS and keeps a machine-local registry so later prints can name one; renders text and QR labels to the pixel canvas of the loaded DK or TZe media; previews without touching the printer, because brother_ql converts and transmits in a single step with no dry run. Ships a media catalogue of DK and TZe product codes, reusable label templates in the user's data directory, and a Linux driver-install skill covering brother_ql, ptouch-print, mDNS and CUPS. Zebra and DYMO are discovered and registered but not yet printable. Also bundles the original streamable-HTTP MCP server for P-touch setups built around a USB print bridge.

---

## Learning

### Test Project Ideator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Test-Project-Ideator-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Generates specifications for practice/dummy development projects tailored to the user's learning objectives, technology stack, and proficiency level in each language or tool.

---

## Licensing

### License Populator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-License-Populator-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Recommend, generate, and populate software/content licenses. Reads from a user-managed template store and advises on optimal license choice given desired freedoms and constraints.

---

## Linux

### Easy Effects Manager
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Easy-Effects-Manager) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage Easy Effects on Linux: maintain a preset library, install/export presets, bind autoload to specific mics, test input levels, and set up clean voice-dictation chains. Works with Flatpak or native installs.

---

### Hotkey Builder
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Ubuntu-Hotkey-Builder) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Free-key finder + shortcut builder for Ubuntu: probe keys, audit bindings, bind text macros. Checks and installs ydotool/input-remapper, records lsusb IDs, finds non-conflicting keys across KDE, GNOME, input-remapper, keyd and hwdb, and binds by the route that works on X11 or Wayland, then verifies.

---

### Keyboard Scanner
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Keyboard-Scanner) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Profile Linux keyboards, scan keycodes, and surface underused keys for remapping. Walks intake → keycode dump (xmodmap/XKB/evdev/libinput, X11 + Wayland) → tailored remap suggestions referencing keyd, kmonad, xremap, xmodmap, xbindkeys, input-remapper, autokey.

---

### Linux Debugging
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Linux-Debugging-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Linux desktop debugging toolkit — targeted journal/boot/log inspection skills plus proactive logging instrumentation (persistent journald, kdump, sysstat, OOM protection) so AI agents can analyze hard crashes, freezes, and runtime issues. Targets Ubuntu + Wayland; forkable for other distros.

---

### Linux Packaging
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Linux-Packaging-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Linux packaging and release workflows — Debian/.deb builds, npm publishing, GitHub release creation, agent deploy scripts, and local debugging

---

### Linux System Optimisation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Linux-System-Optimisation-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Performance and space optimisation for Linux desktops — hardware-aware CPU/GPU/disk/memory benchmarks with governor / I/O scheduler / sysctl tuning, plus disk-usage analysis (BTRFS-aware), duplicate-file detection, package audit, and dev-clutter pruning (venvs, node_modules, caches).

---

### Os Sync Agent
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-OS-Sync-Agent) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Hardware-aware desktop-to-laptop environment sync for Ubuntu/Debian. Snapshots packages (apt/snap/flatpak/pip/conda/ollama) and dotfiles from a base machine and a remote machine over SSH, then produces an incremental install/remove/sync plan rather than a perfect clone. Ships /sync-os command and sync-environments skill.

---

## Llm Council

### Llm Council Creator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-LLM-Council-Creator-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Scaffold new LLM Council projects from existing templates (Template, Grounded, Decide) or build bespoke council repos for specific purposes.

---

## Music Assistant

### Media Assistant Ops
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Media-Assistant-Ops-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Interface with a Music Assistant server via its local API — onboard a deployment, control players, snapshot speaker rosters, save/update per-player DSP presets, and apply a curated podcast EQ preset.

---

## Nfc

### Nfc Ops
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-NFC-Ops-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

NFC tag operations using libnfc — read, write, inspect, password-protect, and bulk-write from CSV with manual tag-by-tag feed.

---

## Nlp

### Text Corpus Analysis
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Text-Corpus-Analysis-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Skills for analyzing large text corpora — topic modeling (BERTopic with temporal evolution), NER, categorization into fixed taxonomies, bottom-up category derivation, multi-level taxonomy design, word frequency, synonym clustering for voice-note/STT corpora, parametric stats, and metadata↔content correlation. Three execution lanes (classical NLP, local LLM via Ollama, cloud LLM via OpenRouter) with explicit cost-awareness: mandatory pre-run estimates for >1k-doc LLM passes, two-pass cheap→premium pattern, embeddings+clustering preferred over pairwise LLM comparison.

---

## Obd

### Obd Diagnostics
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-OBD-Diagnostics-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Read OBD-II data from an ELM327-class adapter, normalise it to JSON, and use it to diagnose faults and plan vehicle maintenance. WIP.

---

## Obs

### Obs Mgmt
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-OBS-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage OBS Studio on Linux from Claude Code: detect install type (native/Flatpak/Snap/AppImage), enable and validate obs-websocket, ship a bundled obs-mcp MCP server for programmatic OBS control, back up configs to a user-defined folder, and install third-party OBS plugins.

---

## Openrouter

### AI Model Research
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-AI-Model-Research-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Research, discover, compare, and evaluate AI models on OpenRouter — backed by the bundled Model-Scout MCP server for live catalog data with caching. Subsumes the standalone open-router-model-research plugin and the Model-Scout-MCP server. 11 skills cover lookup, capability filtering (tools, vision, audio), recommendation, head-to-head comparison, deep evaluation, workload cost projection, and finding cheaper alternatives.

---

## Opnsense

### Opnsense Mgmt
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Opnsense-Mgmt-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage an OPNsense router/firewall via SSH and the OPNsense API — guided first-run onboarding, firewall rule inspection, network debugging, and host/log diagnostics. Per-host config is stored outside the plugin so the same install works across multiple environments.

---

## Optical

### Batch Optical Archivist
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Batch-Optical-Archivist-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Plan and burn batch M-Disc / BD-R / DVD archives from a source directory on Ubuntu, with copy multipliers for offsite duplicates. Wraps growisofs, xorriso, and dvd+rw-mediainfo; optional K3B handoff for manual fallback.

---

## Other

### Aliexpress Shopper
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Aliexpress-Shopper) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Browser-driven AliExpress shopping assistant for Claude in Chrome. Bundles userscripts (Find Similar, Hide Combo Deals) and skills/commands that drive aliexpress.com directly in the user's browser session — search, read current listing, compare open tabs, apply filters, hide bundles, and find similar items. Scope is global aliexpress.com (any locale/currency) and visual/interactive shopping, not headless scraping or programmatic API flows.

---

### Anonymisation Assistant
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Anonymisation-Assistant-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Anonymise sensitive documents (whistleblower disclosures, harassment diaries, incident reports) by replacing identifying details while preserving narrative integrity.

---

### Audio Voice Id
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/audio-voice-id-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Speaker diarization, voice enrollment, and identification for audio files — builds a local voiceprint library with optional cloud replication.

---

### Brainstorm Solutions
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/brainstorm-solutions-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

When you hit a wall, spin up a research workspace to brainstorm solutions — captures the blocker, what you tried, and kicks off deep research

---

### Conda Manager
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/conda-manager-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Conda environments — list, validate, compare, back up, audit and clean up environments with AI assistance.

---

### Diary Planner
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/diary-planner-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

A workflow planning and time management template with agent definitions and slash commands for managing daily, weekly, and monthly schedules while maintaining connections between immediate tasks and longer-term objectives.

---

### Docker Manager
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/docker-manager-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Slash commands and subagents for managing Docker containers, Compose stacks, volumes, networks, and multi-environment deployments.

---

### Eml Toolkit
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Eml-Toolkit) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Process .eml email exports — reconstruct a thread from loose .eml files, render the chain to a single PDF with correct right-to-left handling for Hebrew and Arabic, extract attachments, export Markdown, redact before sharing, and build numbered evidence bundles.

---

### Eval Runner
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Eval-Runner-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Scaffolding, running, documenting, and publishing AI evaluations. Ships skills and commands for setting up eval workspaces, creating custom evals (or adapting existing frameworks/benchmarks), running them, and publishing evals or datasets. Bundles a curated ground-truth list of open-source eval tools and benchmarks as a reference data source.

---

### Filesystem Organisation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/filesystem-org-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

File system organisation — folder structure optimisation and file management automation.

---

### Github Research
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/github-research-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Research existing GitHub repositories before building — search, rank, and evaluate candidate tools via gh CLI with careful attention to stars, recency, and maintenance quality

---

### Grainger
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Grainger-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Grainger.com (US industrial MRO) product research — typeahead and category discovery from a script, price and spec verification from the signed-in browser. Encodes the mapped /ta/v3, /tap/v2 and __PRELOADED_STATE__ surfaces, the facet grammar that filters a category, per-branch stock counts across ~325 branches, and the three distinct ways Grainger refuses a request while returning HTTP 200.

---

### Hebrew Correspondence
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Hebrew-Correspondence-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

One home for correspondence in Hebrew — send RTL email that renders correctly in every client, typeset formal letters to PDF with David Libre via Typst, turn incoming .eml threads into readable PDFs, and verify a render before it goes out.

---

### Learning
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/learning-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Learning resources, skill development, educational content creation and knowledge management.

---

### Mqtt Observability
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/mqtt-observability-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Observe and interact with an MQTT broker — monitor all payloads, watch a specific topic, and publish messages. Stores broker credentials once and reuses them.

---

### Stack Search
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Stack-Search-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Spawn a new stack search workspace from the Claude-Stack-Research-Workspace template — clone, name, create GitHub repo, and kick off the structured intake interview

---

### Tech Research
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/tech-research-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Technology research — competitive analysis, technical documentation retrieval and research workflows.

---

### User Manual
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/user-manual-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Personal user manuals and private documentation for codebases, with PDF output.

---

## Pdf

### Digital Printing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Digital-Printing-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Skills and an orchestrator agent for preparing PDFs for digital printing — resize, grayscale, font embedding, transparency flattening, image downsampling, color normalization, watermarks, footer burn-ins, cover pages, bleed-safety check, job folders, formal print orders, and email/Drive share.

---

### Document To Markdown
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/document-to-markdown-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Convert PDFs to clean Markdown, chunk into logical sections (chapters, indexes, appendices), and extract embedded tables to CSV. Local-first via marker/docling/pymupdf4llm + camelot/tabula, with TOON manifests.

---

## Pipewire

### Pipewire Audio
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Pipewire-Skills-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Claude Code skills for taming Pipewire/Wireplumber audio on Linux — manage default devices, persistent device-priority rules, per-app routing, mic level checks, and EasyEffects bindings.

---

## Planning

### Document Nudge
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Document-Nudge) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Nudges Claude to document decisions, todos, sprints, and handovers into a structured planning/ tree by default — without being asked each turn. Ships a home-level CLAUDE.md snippet plus /nudge-install and /nudge-scaffold slash commands.

---

### Planning Docs
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Planning-Docs-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Keep a repo's decision log and plans lean: record numbered decisions, and compact old decisions and plans into in-place summaries so agents read the live state, not the history.

---

## Plugin Authoring

### Site Skill Builder
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Site-Skill-Builder-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Site skills built by watching a site in your own signed-in Chrome — observe pages and endpoints, propose a skill roster for approval, then author skills that survive UI changes and probe for drift. Semantic handles only, never pixel coordinates. Every observation is classified publishable, private, or never-recorded, with a stop rule for incidental security findings.

---

## Plugins

### Favorite Plugins Installers
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Favorite-Plugins-Installers-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Curated batches of third-party Claude Code plugins, grouped by type/theme, installable in one command.

---

## Privacy

### Pii Scanner
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-PII-Scanner-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Scan files, directories, or git repositories for personally identifiable information — credentials (gitleaks), generic PII (Microsoft Presidio), and matches against a user-maintained personal PII inventory (names, addresses, family, IDs) stored locally.

---

## Productivity

### Schedule Manager
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Schedule-Manager-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Personal schedule, task, and meeting management. Routes mixed brain-dumps into Google Calendar (events) and Todoist (tasks); manages agenda/minutes Google Docs linked to events; produces wrapup logs and morning briefs. 22 skills covering Calendar/Todoist CRUD, firehose routing, task<->event migration, priority/date hygiene, and agenda/minutes lifecycle.

---

## Profiles

### Daniel Rosehill
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Daniel-Rosehill-Claude-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Jump to Daniel Rosehill's public work from Claude Code — profiles (LinkedIn, X, GitHub, YouTube, npm, Kaggle, DeviantArt, Pexels), blog, Hugging Face, public repos by recency/stars/A–Z, bio, resume download, and contact/newsletter pages. Also refreshes this marketplace's local cache. A directory of one person's published output, not personal configuration.

---

## Proxmox

### Proxmox Mgmt
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Proxmox-Mgmt-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage a Proxmox VE host via SSH and the Proxmox API — guided first-run onboarding, VM/CT lifecycle, storage and ZFS inspection, log review, and update workflows. Per-host config is stored outside the plugin so the same install works across multiple Proxmox environments.

---

## Recovery

### System Recovery Mode
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-System-Recovery-Mode) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

AI-assisted Linux system recovery — slash commands and agents (diagnose, logs, network, disk, services, packages) for diagnosing and fixing a broken system. Pairs with an optional GRUB/systemd installer that boots a minimal recovery TTY straight into Claude CLI.

---

## Resume

### Resume Typesetter
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Resume-Typesetter-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage a resume as JSON Resume schema data and render it with custom Typst templates. Onboard, iterate, fork variants, and version.

---

## Scraping

### Local Web Capture
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Local-Web-Capture-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Capture geo-restricted web content (articles, prices) via the user's own localhost so requests exit via the user's IP. Headless-first escalation ladder (Scrapling static -> stealth -> Playwright -> real Chrome via bb-browser). Project-local save (in-repo captures/) with global fallback. Batch capture with human + agent summaries, Typst PDF compilation, and arbitrary-language capture+translate (default Hebrew -> English).

---

## Session

### Session Restore
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Session-Restore) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Terminal crashed? Reopen the lost Claude Code sessions: finds the ones that died together and resumes each in its repo, in one Konsole window of split panes (or tabs, or windows). Also restores the last N or picked sessions.

---

## Skills

### Skill Or Not
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/To-Skill-Or-Not-To-Skill) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Ask 'should this become a skill?' before every task: a five-step checklist (repeatable, automatable, already ours, already someone else's, else create and validate it) plus an installer that puts the heuristic in your user-level CLAUDE.md / AGENTS.md.

---

## Sop

### Sop Writer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-SOP-Writer-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Project-scoped authoring tools for Standard Operating Procedures and decision flowcharts. Scaffold from templates, embed Mermaid/D2 diagrams, compile to printable PDFs via Typst, and assemble multi-document binders with TOC and page numbers.

---

## Spec

### Spec Starter
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/spec-starter-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Spec-driven development workflow for Claude Code: turn unstructured project briefs (especially voice transcripts) into a versioned spec, modular context, and a CLAUDE.md scaffolded into your current repo.

---

## Stack

### Stack Evaluator
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/stack-evaluator-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Component-level review of a project's technology stack, not its code — records the stack to docs/stack/ with the run date, checks each component for end-of-life and currency, finds architectural gaps (caching, backups, queues, rate limiting, observability), flags redundancy and over-engineering against the real workload, then emits a sequenced revision proposal and an execution brief. Re-runnable per repo with persistent decisions and finding history.

---

## Staging

### Loose Tasks
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Loose-Tasks-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Loose skills that will be migrated into other plugins later. Recommended not to enable/use this!

---

## Support

### Contact Support
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/contact-support-plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Contact a vendor's support desk from a registry of verified, dated contact routes rather than recalled ones — ticket URLs and which support plans can reach them, abuse and fraud addresses taken from mailto hrefs rather than page text, per-tier response windows, priority vocabulary, escalation ladders with SLA claim deadlines, pre-contact checks, and the plausible routes that turn out to be dead. Records the user's account identity and where credentials live (a pointer, never the secret), drafts the request with the identifiers the desk will demand, sends it through whichever channel is actually reachable, logs the ticket and chases it when the window elapses. Ships verified for Twilio only; extend with support-add-service. Work in progress — concept stage.

---

## Synology

### Synology Mgmt
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Synology-Mgmt-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Manage a Synology NAS via SSH — guided first-run onboarding, share/volume inspection, storage health, and file operations. Per-host config is stored outside the plugin so the same install works across multiple NAS environments.

---

## Synthetic Data

### Synthetic Data
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Synthetic-Data-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Generate synthetic datasets from schemas, real data, or LLM-driven personas. Tabular fit-and-sample (SDV: GaussianCopula, CTGAN, TVAE), Faker/Mimesis schema generation, deterministic PII swap, LLM-driven real-to-synth conversion for unstructured records, and SDMetrics-based quality/privacy evaluation (plus embedding-based leakage checks for text).

---

## Task Management

### Task Queuer
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Task-Queuer-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Repo-based task queueing system with categorisation and prioritisation. Scaffolds a planning/ folder, logs tasks (single, batch list, or voice-transcribed), buckets them by category, and hands prioritised work off to the repo's orchestration agent.

---

## Taxonomy

### Taxonomy Creation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Taxonomy-Creation-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Generate taxonomy and lookup tables (countries, currencies, languages, US states, timezones, custom domain taxonomies) and load them into Postgres, SQLite, MySQL, or export to CSV/JSON/SQL seed files. For data engineers, CMS builders, and eval pipeline authors.

---

## Text

### Novelty Text Editor
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Novelty-Text-Editor-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Rewrite text in deliberately ridiculous styles — Shakespearean, medieval, archaic, chaos-case, over-salesy, platitude-stuffed, pseudobot, plus length transforms (elongate / truncate). Nine no-config skills for stylistic mischief.

---

## Timemark

### Timemark
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Timemark-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Timemark stamp-camera photo import that recovers the field data the app withholds. No Timemark export carries both the full-resolution image and the values, so imports are gated on having the originals and the Photosheet XLSX, then joined on capture timestamp. Outputs are XMP burned into the files or a self-contained archive of images, JSON sidecars and an index.

---

## Tmp

### Network Tmp
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Network-Tmp-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Overflow /tmp to a capped, self-wiping NFS share on a home server. For laptops whose /tmp is a small tmpfs (RAM) or whose disk is tight: an ext4 image exported over NFS, mounted on demand with a local-disk fallback, expired hourly after 24 h. Skills to set it up, route large temporary files there, and report and clean it.

---

## Toon

### Get Toony
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Get-Toony-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Convert JSON, CSV, YAML, and other structured data into TOON (Token-Oriented Object Notation) — a compact, lossless re-encoding that uses ~40% fewer tokens than JSON when fed to LLMs. Wraps @toon-format/toon and tracks the wider ecosystem (Python, Java, .NET, PHP, Rust ports).

---

## Travel

### Travel Packing
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Travel-Packing-Assistant-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Make optimal use of a baggage allowance on an international itinerary — research each carrier's real checked, cabin and personal-item allowance per segment with a source and a confidence level for every figure, compute the binding limit that governs the journey, inventory what is carried by weight, reconcile scale readings against the inventory, solve the allocation to bags and packing cubes, price every way out of being over, and rank an emergency leave-behind list by cost per kilogram saved. Renders a one-page airport counter card and a per-bag packing list as PDF via Typst and as Markdown. One trip workspace per itinerary.

---

## Tts

### Text To Speech Toolkit
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Text-To-Speech-Toolkit-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Skills for preprocessing text for TTS engines — SSML conversion, ElevenLabs markup (grounded in live ElevenLabs prompting docs), TTS safety review, and manual prosody addition. Non-destructive by default: edits land in an edited/ folder alongside an unchanged original/ copy.

---

## Typst

### Programmatic Doc Generation
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Programmatic-Doc-Generation-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Build programmatic document generation pipelines — Typst templates for local batch rendering, plus integration scaffolding for n8n and cloud rendering services (Carbone, PDFMonkey, APITemplate, DocRaptor, Docmosis, Adobe Doc Gen).

---

## Ubuntu

### Ubuntu Admin
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Ubuntu-Admin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Administer Ubuntu machines, desktop or server, locally or over SSH: health and diagnosis, packages (apt/snap/flatpak), systemd services and logs, Docker, storage and backups, networking, hardware and GPU drivers, displays, fonts, codecs, shell and dev environments. Supersedes linux-desktop-mgmt, linux-server-mgmt and sysadmin-homelab.

---

### Ubuntu Security
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Ubuntu-Security) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Host security for Ubuntu desktops and servers: ufw firewall (setup, status, scoped allows, removal, diagnosing blocks), ClamAV/rkhunter/Lynis/AIDE scanning and schedules, security audits and updates, SSH keys and sshd config, fail2ban, YubiKey and fingerprint login, TLS certificate checks. Supersedes linux-av-manager and security-checkup.

---

## Userscript

### Userscript Development
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Userscript-Development-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Develop, test, and publish Tampermonkey userscripts — scaffolding, in-browser validation via Claude in Chrome, README generation, and version bumping.

---

## Vendor

### Vendor Liaison
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Vendor-Liaison) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Report bugs, request features, disclose security to vendors: per-vendor channel data with routing rules, a private overlay for your preferred channels and personal contacts, duplicate checks before filing. Vendors: Claude Code, 1Password, Whisperian.

---

## Visuals

### Visual Communications
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Visual-Communications-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Plan and prompt-engineer AI-generated visuals (images, diagrams, video) for whitepapers, blog posts, and long-form content. Six skills cover project onboarding, visual ideation, prompt generation, project listing, fal-ai execution, and a resolution/style reference.

---

## Voice

### Passive Aggressive Pa
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-PA) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Passive-aggressive PA system. Claude barks status updates over a speaker; if ignored, escalates across the house via Home Assistant or MQTT. Includes pre-recorded voice packs, RGB signal bulb, full-screen flash overlay, and a quiet-mode skill that translates natural-language pause/schedule requests.

---

## Zigbee

### Zigbee Home Maintenance
[![View Repo](https://img.shields.io/badge/View%20Repo-blue?style=flat-square&logo=github)](https://github.com/danielrosehill/Claude-Zigbee-Home-Maintenance-Plugin) ![Plugin](https://img.shields.io/badge/Plugin-purple?style=flat-square)

Maintain a home Zigbee network — onboard MQTT broker, coordinator (SMLight / Sonoff / ConBee / etc.), and Home Assistant; manage credentials, network exports, and routine maintenance.

---
