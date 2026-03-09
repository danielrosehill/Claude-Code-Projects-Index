# Agent Workspaces (The "Claude Space" Pattern)

In my own words:

Many of the repositories in this index are what I originally called a "Claude Space" — now more commonly known as an **agent workspace**. These are pre-configured repository environments designed for structured agentic AI workflows.

## What Is An Agent Workspace?

Repositories are usually associated with "code" — or development projects.

However they provide a very robust and adaptable mechanism for version control and for gathering resources in one space — and, through careful outlining, can support workflows.

I use Claude for conventional development projects. But I'm more excited about their utility in managing organised AI environments.

Claude Code lends itself ideally to this pattern by aggregating all the constituent elements of agentic AI in one modularised area:

- A system prompt (CLAUDE.md)
- Context (can be user-aggregated)
- Output storage (the most neglected part of the AI workflow!)
- Prompt versioning and storage

Add slash commands, subagents, and the other bells and whistles that Anthropic is rolling into the platform and you have a powerful template for working on just about any major task with persistent memory and context!

## Agent Workspaces For OS Management

My first use for agentic CLIs (Gemini, Qwen et al) has been systems admin. Thanks to their collective effort, running Linux no longer feels like a chore and my local network is well organised.

I have experimented with two methods of using Claude as a helper of sorts for environments: whether those are local, on-the-LAN, or remote: Claude on each server or one Claude locally that knows your SSH commands. The latter is greatly enhanced by the use of SSH MCP.

At the time of writing, I'm not sure there's a meaningful difference in terms of performance — although there are meaningful differences from a security standpoint.

What I *have* found useful, however, is defining repositories to manage systems — one repository per machine. These can be used to aggregate all the nitty gritty context data that makes or breaks the utility of agentic CLIs working on diverse environments: things like hardware listings, folder maps. These were the first agent workspaces I created.

## Agent Workspaces For Other Projects

Agent workspaces can be used in any other instance in which you have a predefined bank of context data and want Claude to work in a deep research type capacity on one major project.

I like to modularise tightly — which is why I also tend to create many repositories on Github! Each major project gets its own template and workspace.

These follow a standard pattern for AI workspaces that I have been using for more than a year now. But each is adapted to the nuances and specificities of that project.

Both types of workspaces are indexed in the README.md.
