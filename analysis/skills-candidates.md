# Skills Candidates Analysis

Analysis of repos in `categories/` evaluating which could be reimplemented as **Claude Code Skills** (single-purpose, model-invoked, SKILL.md-based capabilities) rather than full agent workspaces, plugins, templates, or MCP servers.

Classifications:
- **GOOD_SKILL_FIT** — narrow, stateless, procedural; maps cleanly to a single SKILL.md
- **PARTIAL** — core procedure could become a skill, but repo also carries workspace/template/state concerns
- **POOR_FIT** — persistent workspace, multi-agent orchestration, plugin, MCP server, template-to-fork, or data-heavy

---

## Summary: Strongest GOOD_SKILL_FIT Candidates

These are the cleanest conversions from repo/workspace to a lightweight SKILL.md:

1. **Declaude** — rewrite rules applied on demand; already slash-command shaped.
2. **Claude Redaction And Obfuscation** — stateless PII redaction transform.
3. **Claude Model Identifier** — tiny verification procedure, ideal SKILL.md.
4. **Claude MD Chunk** — one-shot CLAUDE.md condensation transform.
5. **Claude File Organiser Super Slash** — stateless filesystem reorganization procedure.
6. **Claude Document This** — procedure for writing up system-change docs.
7. **AI-Human Attribution Adder** — single README transformation.
8. **Claude App Optimiser** — codebase dead-code scan, invoke on demand.
9. **No Wheel Inventions** — checklist/heuristic procedure.
10. **Claude Dork** — generate platform-specific search dorks from query.
11. **Claude Spec Starter** — transforms unstructured description into spec.
12. **Claude Decision Evaluation Framework** — 7-framework analysis, stateless.
13. **Claude Business Idea Evaluator** — ICEC methodology scoring, stateless.
14. **Claude Code MCP Command Generator** — generates MCP config, narrow.
15. **Claude Repo Jumper** — handover procedure (already described as a skill).
16. **New Turn Claude Hook** — heuristic decision, lightweight.
17. **Claude Change My View** — counterargument generation procedure.
18. **ProofMode Unpacker** — evidence bundle processing utility.
19. **Claude Github Shortlister** — repo evaluation heuristic.
20. **Claude Report Parsing Space Template** — report triage/analysis procedure.

---

## 01 — Systems Administration

- **Bash Alias Manager Claude** — PARTIAL: core manage-aliases procedure could be a skill; YADM sync is stateful.
- **Claude Bug Catcher** — POOR_FIT: hotkey utility + logs capture plumbing.
- **Claude Code Bash Aliases** — POOR_FIT: alias collection, not a procedure.
- **Claude Code LAN Manager** — POOR_FIT: persistent multi-machine workspace with device state.
- **Claude Code Remote Machine Admin Space** — POOR_FIT: per-machine state/logs template.
- **Claude Code Security Auditor** — PARTIAL: audit checklist could be a skill; multi-machine state better as workspace.
- **Claude Conda Manager** — PARTIAL: "set up conda env" is skill-shaped (and already exists as such).
- **Claude Docker Manager** — PARTIAL: diagnostic procedures skill-shaped; broader template is not.
- **Claude Home Assistant Manager Template** — POOR_FIT: template with persistent config.
- **Claude Linux Desktop Manager** — POOR_FIT: already decomposed into many skills (linux-desktop-mgmt:*).
- **Claude Linux Server Manager** — POOR_FIT: server state template.
- **Claude OS Sync Agent** — PARTIAL: sync procedure is skill-shaped; carries config state.
- **Claude Proxmox Manager Template** — POOR_FIT: forkable template with host state.
- **Claude Rescue** — POOR_FIT: concept/deployment, not a procedure.
- **Claude Server Manager Template** — POOR_FIT: forkable template.
- **Claude Server Mgmt Template SBCs** — POOR_FIT: forkable template.
- **Claude Synology Manager** — POOR_FIT: persistent device context.
- **Claude System Recovery Mode** — POOR_FIT: GRUB boot integration.
- **Claude Dolphin & Konsole Actions** — POOR_FIT: desktop integration artifacts.
- **Claude ADB Workspace Template** — POOR_FIT: device-profile template.
- **Claude MVT Workspace** — PARTIAL: "run MVT scan & interpret" procedure could be a skill.

## 02 — Productivity

- **Claude Debugging Workspace** — PARTIAL: hypothesis-driven debug procedure could be a skill.
- **Claude Decision Evaluation Framework** — GOOD_SKILL_FIT: 7 stateless frameworks applied to a decision.
- **Claude Diary Planner Template** — POOR_FIT: persistent diary data (already a skill suite for planning, but repo is template).
- **Claude Google Drive Organiser** — PARTIAL: organize procedure skill-shaped; rclone config is state.
- **Claude Personal Development Workspace** — POOR_FIT: long-lived habit/goal state.
- **Claude Preparedness Planner** — PARTIAL: intake + plan generation could be a skill; persistent plans are not.

## 02a — Legal

- **Claude Case File** — POOR_FIT: persistent case evidence store.
- **Claude Code Lawyer** — POOR_FIT: case management template.
- **Claude Evidence Assistant** — POOR_FIT: evidence workspace with crypto verification state.
- **Claude Legal Aid Clinic** — POOR_FIT: template.
- **ProofMode Unpacker** — GOOD_SKILL_FIT: stateless bundle unpacking/verification utility.

## 02b — Health

- **Claude ADHD Research Workspace** — POOR_FIT: long-lived research repo.
- **Claude Health Helper** — POOR_FIT: persistent health records.
- **Claude Therapy Tracker** — POOR_FIT: longitudinal tracking.

## 02c — Communications

- **Claude Blog Manager** — POOR_FIT: CMS-integrated content store.
- **Claude Code Writing Squad** — POOR_FIT: multi-agent orchestration.
- **Claude Communications Strategist Template** — POOR_FIT: 12-agent workspace.
- **Claude Visual Communications Space** — POOR_FIT: MCP-backed workspace.
- **Claude Website Update Sender** — PARTIAL: "generate + send update email" procedure; depends on Resend MCP.
- **Claude Writing Space Template** — POOR_FIT: versioned writing workspace.
- **Declaude** — GOOD_SKILL_FIT: rewrite rules collapse to a slash command / SKILL.md.

## 02d — Financial

- **Claude Budget Workspace Template** — POOR_FIT: persistent financial history.
- **Claude Purchasing Assistant** — PARTIAL: evaluate-product procedure is skill-shaped; pricing lookups stateful.

## 02e — Career

- **Claude Job Search Strategist** — POOR_FIT: persistent job-search state.
- **Claude Salary Research Agent** — PARTIAL: "benchmark salary" procedure could be a skill.

## 02f — Business

- **Claude Business Continuity Planner** — POOR_FIT: long-lived ISO 22301 plan.
- **Claude Business Idea Evaluator** — GOOD_SKILL_FIT: ICEC scoring procedure, stateless.
- **Claude Competitor Research Agent** — PARTIAL: scan/report procedures could be skills.

## 02g — Privacy

- **Claude Redaction And Obfuscation** — GOOD_SKILL_FIT: stateless PII redaction transform.

## 02h — Technology

- **Claude Ivory PC Builder** — POOR_FIT: depends on external pricing data + history.
- **Claude Rig Planner** — POOR_FIT: hardware profile workspace.

## 02i — Marketing

- **Claude Media Monitor** — POOR_FIT: ongoing collection with metadata store.
- **Claude News Fetcher** — POOR_FIT: batch pipeline workspace.
- **Claude Web Analytics Space** — POOR_FIT: data-holding workspace.

## 03 — Research

- **Claude Deep Research Model** — POOR_FIT: methodology doc.
- **Claude Deep Research Template** — POOR_FIT: forkable multi-agent template.
- **Claude Dork** — GOOD_SKILL_FIT: "generate search dorks for topic X" is textbook skill.
- **Claude Georeaction Researcher** — PARTIAL: research procedure is skill-shaped; persistent output less so.
- **Claude Github Shortlister** — GOOD_SKILL_FIT: evaluate/shortlist repos from a list.
- **Claude OSINT Investigator** — POOR_FIT: investigation workspace with evidence.
- **Claude Report Parsing Space Template** — GOOD_SKILL_FIT: stateless report-triage transform.
- **Claude Stack Research Workspace** — POOR_FIT: multi-agent evaluation workspace.

## 04 — Argument / Perspective

- **Claude AI Conference** — POOR_FIT: 30+ persona orchestration.
- **Claude Change My View** — GOOD_SKILL_FIT: belief-in, counterargument-out.
- **Claude Think Tank** — POOR_FIT: multi-agent policy framework.

## 05 — Context / Personalization

- **Batch ClaudeMD Repo Creator** — PARTIAL: batch procedure scriptable; multi-repo automation.
- **Claude Agent Workspace Model** — POOR_FIT: canonical template reference.
- **Claude Code Context Toolkit** — POOR_FIT: already a slash-command bundle over CONTEXT.md methodology.
- **Claude Code Repo Managers ClaudeMD** — POOR_FIT: template collection.
- **Claude Model Identifier** — GOOD_SKILL_FIT: tiny verification check.
- **Claude Space Self-Ideator** — PARTIAL: ideation procedure could be a skill.
- **Claude Spec Starter** — GOOD_SKILL_FIT: unstructured-text → spec transform.
- **ClaudeMD Turnstile** — POOR_FIT: architectural pattern for repos.
- **CONTEXT.md** — POOR_FIT: methodology.
- **Home Folder Claude MD** — POOR_FIT: versioned config file.
- **Linux Desktop ClaudeMD Seeder** — PARTIAL: "seed CLAUDE.md across filesystem" procedure.
- **Private And Public Claude MD** — POOR_FIT: git config tooling.
- **Split Context Setup** — PARTIAL: scaffolding slash command, already close to a skill.

## 06 — Multi-Agent Tooling

- **Agent Junction** — POOR_FIT: MCP server.
- **Claude Agent Picker Pattern** — PARTIAL: assembly heuristic could be a skill.
- **Claude Agent Workspace Generator** — POOR_FIT: scaffolding template generator.
- **Claude Repo Jumper** — GOOD_SKILL_FIT: repo-handover procedure (description literally says "skill").
- **Claude Task Manager** — POOR_FIT: stateful queueing system.
- **Claude Tech Research Team** — POOR_FIT: multi-agent workspace.
- **Ecosystem Mapper** — PARTIAL: discover+visualize procedure skill-shaped.
- **Panel Of Claude** — POOR_FIT: multi-agent simulator.
- **Claude Development Agents** — POOR_FIT: 74+ configs collection.
- **Claude Sub-Agent Network** — POOR_FIT: agent config collection.
- **Cool Claude Code Stuff** — POOR_FIT: resource list.
- **Claude Workspace Setup Helper** — PARTIAL: discovery+clone procedure.
- **Claude Code Linux Notes** — POOR_FIT: personal notes.

## 07 — MCP

- **Claude Code MCP Command Generator** — GOOD_SKILL_FIT: generate MCP CLI command from inputs.
- **How-To-MCP** — PARTIAL: decision matrix could be a skill (close to existing `mcp:install-mcp`).
- **Claude Code MCP List** — POOR_FIT: curated index.
- **Claude MCP Guidelines** — POOR_FIT: guideline snippet (context, not procedure).
- **MCPM Claude Code Docs** — POOR_FIT: docs.
- **Smithery Claude Code MCP Jumpstarter** — POOR_FIT: installer collection.

## 08 — Plugins

All entries are plugins by definition — POOR_FIT as skills, though individual features inside could become skills.

- **Claude Code Marketplace Hub** — POOR_FIT.
- **Claude Code Plugin** — POOR_FIT.
- **Claude Code Plugins Marketplace** — POOR_FIT.
- **Claude Janitor** — PARTIAL: "remove Claude artifacts" cleanup is a skill-shaped procedure.
- **Make Agent Friendly** — PARTIAL: "restructure repo for agents" procedure.
- **Repo Retrofitter** — POOR_FIT: orchestrated multi-mode plugin (though its scan step is skill-shaped).
- **QA Team Plugin** — POOR_FIT: multi-agent.
- **User Manual Plugin** — PARTIAL: "generate user manual for codebase" procedure.

## 09 — Slash Commands

These are already the closest cousins to skills.

- **AI-Human Attribution Adder** — GOOD_SKILL_FIT.
- **Claude App Optimiser** — GOOD_SKILL_FIT.
- **Claude Code Linux Desktop Slash Commands** — POOR_FIT: collection (individual commands would each map to skills; many already do).
- **Claude Document This** — GOOD_SKILL_FIT.
- **Claude File Organiser Super Slash** — GOOD_SKILL_FIT.
- **Claude MD Chunk** — GOOD_SKILL_FIT.
- **Claude Slash Commands** — POOR_FIT: collection (each command individually could be a skill).
- **No Wheel Inventions** — GOOD_SKILL_FIT.

## 10 — Misc

- **Claude Agent Blueprints** — POOR_FIT: index of templates.
- **Claude Code Context Feature Requests** — POOR_FIT: feature request doc.
- **Claude Interview** — POOR_FIT: transcript.
- **Claude Is Awesome** — PARTIAL: "create curated resource list" is skill-shaped.
- **Claude Local AI Agent Research** — POOR_FIT: research notes.
- **Claude Resource List Builder** — PARTIAL: list builder procedure.
- **New Turn Claude Hook** — GOOD_SKILL_FIT: decision heuristic.
- **Non-Code Claude Code** — POOR_FIT: showcase/index.

---

## Aggregate Counts

- GOOD_SKILL_FIT: ~20
- PARTIAL: ~25
- POOR_FIT: ~60

The dominant pattern in the index is agent workspaces (persistent, domain-specific, data-holding), which correctly do not map to skills. The GOOD_SKILL_FIT bucket is concentrated in the slash-commands category (category 09) and in stateless "transform/evaluate" procedures scattered across research, context, and business categories.
