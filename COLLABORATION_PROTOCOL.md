# Grok + Claude Collaboration Protocol

**Goal**: Grok and Claude work together as a team (with user oversight) to find paid AI gigs, prepare bids, execute deliverables, and scale the Forge AI business.

**Shared Workspace**: This GitHub repo (https://github.com/braxketball-code/forge-ai-demos). Both AIs and the user treat it as the single source of truth.

## Communication Method (How We "Talk")
1. **Handoff Files**: When one AI finishes a chunk of work, it creates or updates a file in `/collaboration/` (e.g., `handoff-2026-06-15-grok-to-claude.md`).
   - Structure every handoff like this:
     ```
     ## Summary of What I Did
     - ...
     ## Key Decisions & Context
     - ...
     ## Deliverables Created
     - Links to files in repo
     ## What Needs to Be Done Next
     - Clear, prioritized list
     ## Questions for the Other AI
     - ...
     ## Suggested Prompt for the Other AI
     - Copy-paste ready text the user can use in the other chat.
     ```
2. **User as Messenger**: The user copies the handoff file content (or key sections) into the other AI's chat when starting a new session with that AI.
3. **Repo as Persistent Memory**: Both AIs must `git pull` and read relevant files at the start of every task. Update files (proposals, code, logs) instead of just chatting.
4. **Direct User Coordination**: For urgent things, user pastes outputs between windows. For complex work, use the structured handoffs.

## Session Startup for Grok (this environment)
- Always run `git pull` first if possible.
- Read: AGENTS.md, COLLABORATION_PROTOCOL.md, latest in /proposals, /demos, /collaboration, and any open task files.
- Check memory for prior decisions.
- Use tools (GitHub MCP, terminal, etc.) to act.

## Session Startup for Claude
- Instruct Claude: "Read the latest from https://github.com/braxketball-code/forge-ai-demos. Start by reading AGENTS.md, COLLABORATION_PROTOCOL.md, and the most recent file in /collaboration/. Current task: [paste or describe]."
- Claude can analyze, plan, write high-quality text, review code, etc.

## Example Workflow (Finding & Delivering Paid Work)
1. Grok searches for gigs (web_search, x_search) and evaluates using tools.
2. Grok creates handoff file with top opportunities + draft proposals.
3. User pastes handoff into Claude.
4. Claude refines the proposals, writes better copy, plans execution strategy.
5. User pastes Claude's output back to Grok (or Grok reads from repo if updated).
6. Grok uses tools to generate assets (Gamma deck, Canva visuals, customize GitHub code).
7. Grok creates next handoff or final delivery package.
8. User submits or delivers, collects payment.

## Tools & Strengths
- **Grok**: Execution-heavy - file editing, terminal commands, MCP integrations (GitHub, Canva, Gamma), subagents for parallel work, real-time actions.
- **Claude**: Reasoning-heavy - strategy, architecture, excellent writing, detailed planning, code reviews, creative ideas.
- Combine both for faster, higher-quality results than either alone.

## Logging & Improvement
- After each major task, append a short summary to `/collaboration/activity-log.md` (date, what was done, outcome, learnings).
- Both AIs should suggest improvements to this protocol.

## Current Active Tasks (Update as Needed)
- Submitting $1,500 Upwork real estate AI automation proposal.
- Setting up bank/payouts in Upwork.
- Finding more fixed-price AI gigs (real estate focus or general automation).
- Delivering custom AI agents (lead qual, tour booking, follow-ups) using existing repo samples.

**Rule**: Never work in isolation. Always leave a clear handoff so the other AI (or user) can continue without re-explaining context.