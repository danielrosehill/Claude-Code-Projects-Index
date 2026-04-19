# Claude Code: Format Selection Rubric

A decision guide for choosing the right packaging format when building a Claude Code capability. Covers **Plugins**, **Slash Commands**, **Skills**, **Subagents**, and **Agent Workspaces** ("Spaces").

---

## Quick Comparison

| Format | Invocation | State | Scope | Best For |
|---|---|---|---|---|
| **Plugin** | Installed bundle; ships commands/agents/hooks/MCPs | Config-level | Distribution unit | Packaging a cohesive toolset for others to install |
| **Slash Command** | User types `/name` | Stateless | Single prompt template | Repeatable prompts the user wants to trigger explicitly |
| **Skill** | Model-invoked when relevant | Stateless / light | Single well-scoped capability | Procedures the model should reach for automatically |
| **Subagent** | Delegated by main agent | Isolated context | Parallelizable or context-heavy task | Research, search, review — work you want off the main thread |
| **Agent Workspace** ("Space") | Open repo in Claude Code | Persistent (files in repo) | Whole domain of ongoing work | Long-lived personal/professional domains with accumulating data |

---

## 1. Plugins

**What they are:** A distribution format. A plugin bundles any combination of slash commands, subagents, hooks, skills, and MCP server configs into one installable unit.

**Use when:**
- You want to **share** a capability with others (or across your own machines)
- The capability is **multi-part** (e.g. a command + its supporting agent + a hook)
- You need versioning and a clean install/uninstall story

**Don't use when:**
- It's a one-off personal workflow — a slash command or skill is lighter
- It's really just data/context — that's a workspace

**Signal phrases:** "I want others to install this", "this should ship as a bundle", "needs a marketplace entry".

---

## 2. Slash Commands

**What they are:** Named prompt templates the user invokes explicitly via `/command`.

**Use when:**
- The user wants **explicit control** over when it runs
- It's a **repeatable prompt** they'd otherwise retype
- Arguments are simple (a path, an ID, free text)
- The workflow is short and predictable

**Don't use when:**
- The model should decide when to apply it → **skill**
- It needs isolated context or parallelism → **subagent**
- It's a whole domain of work → **workspace**

**Signal phrases:** "I keep typing this same thing", "I want a shortcut for…", "run X on demand".

---

## 3. Skills

**What they are:** Model-invoked capabilities. A `SKILL.md` with frontmatter (name, description) plus optional scripts/resources. Claude picks them up automatically when the description matches the task.

**Use when:**
- The capability is **narrow and well-scoped** (one clear job)
- You want it invoked **automatically** based on context, not on user command
- It's a **procedure, checklist, or transformation** (redact a document, unpack a file, generate a spec)
- It's largely **stateless** — no persistent user data required
- The "how to do this" is the valuable part, not "remember my history"

**Don't use when:**
- The user always wants explicit control → slash command
- It requires persistent history/data across sessions → workspace
- It needs a totally isolated context window → subagent
- It's really a full app with its own runtime → MCP server or plugin

**Signal phrases:** "when the user asks to X, do Y", "automatically handle…", "procedure for…".

---

## 4. Subagents

**What they are:** Delegated agents with their own isolated context window, invoked by the main agent via the Agent tool.

**Use when:**
- The task would **pollute the main context** (large file reads, broad search, log trawling)
- Work can run in **parallel** with other work
- You want a **specialist** (reviewer, planner, explorer) with its own system prompt
- The result can be **summarized back** in a short report

**Don't use when:**
- The main agent already has everything it needs — delegation is pure overhead
- You need the user to interact turn-by-turn with the specialist → that's a separate session

**Signal phrases:** "go research X and come back", "in parallel, also…", "explore the codebase for…".

---

## 5. Agent Workspaces ("Spaces")

**What they are:** A repository structured as an AI work environment — CLAUDE.md, context files, data directories, domain-specific commands/agents — where Claude Code acts as a conversational UI over accumulated personal or professional data.

**Use when:**
- There's **persistent state** that grows over time (diary entries, health logs, case files, budget history, research notes)
- The domain has **multiple related workflows** that share context
- The user wants **continuity** across sessions — "remember what we discussed last week"
- The repo itself is the user's **system of record** for that domain
- Multiple agents/commands collaborate around the same data

**Don't use when:**
- It's a one-shot transformation → skill or slash command
- There's no persistent data — you're just wrapping a prompt → slash command
- It's meant to be installed by others → plugin

**Signal phrases:** "I want to track X over time", "keep a history of…", "my Y workspace", "living document".

---

## Decision Flowchart

```
Is there persistent, accumulating user data central to the capability?
├── YES → Agent Workspace (Space)
└── NO
    │
    Does the model need to reach for this automatically based on context?
    ├── YES → Skill
    └── NO
        │
        Does the task need isolated context or parallel execution?
        ├── YES → Subagent
        └── NO
            │
            Is this a prompt the user wants to trigger explicitly?
            ├── YES → Slash Command
            └── NO → Reconsider; may be an MCP server or library
```

Then ask: **Am I distributing this to others, or bundling multiple pieces together?**
→ If yes, wrap the above in a **Plugin**.

---

## Combinations & Overlaps

These formats compose — the right answer is often **more than one**:

- **Workspace + Slash Commands**: a diary space with `/daily-plan`, `/review-week` commands
- **Plugin = Slash Commands + Subagents + Hooks**: the diary workspace shipped as an installable plugin
- **Skill that delegates to a Subagent**: a skill whose procedure is "spawn an Explore subagent with this prompt"
- **Workspace + Skills**: a legal case workspace where skills handle redaction, citation formatting, evidence indexing

---

## Anti-Patterns

- **Skill masquerading as workspace**: stuffing user history into a skill's resource files. Skills aren't meant to accumulate state — use a workspace.
- **Workspace for a one-shot**: creating a whole repo for what's really a transform. Use a skill or slash command.
- **Plugin for one prompt**: wrapping a single slash command as a plugin adds install friction with no benefit. Ship the command directly.
- **Subagent for everything**: delegation has overhead. Only subagent when context isolation or parallelism actually pays for itself.
- **Slash command where skill fits**: if Claude should *know* to run it, a skill is more ergonomic than asking the user to remember the command name.

---

## Applying This to the Index

Most entries in this index are **Agent Workspaces** — correctly, because they hold accumulating personal data (diaries, legal cases, health, budgets, rigs). The candidates for **conversion to Skills** (see `skills-candidates.md`) are the stateless transforms hiding inside `categories/09-slash-commands.md` and a handful of "evaluate/score/transform" utilities scattered elsewhere.

The pattern to watch for:
- **"Run X on a document" → Skill**
- **"Track X over time" → Workspace**
- **"Ship X to others" → Plugin wrapper around whichever of the above**
