# AGENTS.md - Collaboration Rules for Forge AI Project

This project uses multiple AIs (Grok and Claude) to accelerate building and selling custom AI agents, especially for real estate, to make money via freelance gigs and client work.

## Core Principles
- **Shared Source of Truth**: Always start every session by reading the latest from this GitHub repo (https://github.com/braxketball-code/forge-ai-demos). Pull the latest changes.
- **Collaboration over Isolation**: Use the collaboration protocol (see COLLABORATION_PROTOCOL.md) to hand off tasks, share context, research, code, and deliverables.
- **Focus on Value**: Prioritize tasks that lead to paid work (fixed-price, completion-based gigs on Upwork, Fiverr, direct clients). Use our pre-built assets (GitHub samples, Gamma decks, Canva visuals) to deliver fast.
- **User in the Loop for Critical Actions**: Get explicit user approval before submitting proposals, spending money, linking accounts, or final deliveries. User pastes outputs between AIs when needed.
- **Leverage Strengths**:
  - Grok: Tool use, execution (GitHub MCP, Canva, Gamma, terminal, code editing, subagents), file management, real-time actions in this environment.
  - Claude: Deep reasoning, planning, high-quality writing, architecture, code review, creative strategy.
- **Persistent Memory**: Update relevant files (e.g., collaboration logs, proposals, code) so the other AI can pick up exactly where left off. Use memory tools where available.

## Project Context (Always Load)
- Business: Forge AI - Custom AI agents for real estate (lead qualification, tour booking, follow-ups, content gen, automations).
- Pricing: Starter $497, Pro $997, Premium $1,997+ fixed-price setups.
- Assets: GitHub repo with real-estate Python samples, Gamma pitch decks, Canva flyers/proposals.
- Current Focus (as of 2026-06-15): Submitting to Upwork $1,500 real estate AI automation job. Preparing bank/payout setup. Finding and completing more paid work.
- Goal: Land and deliver fixed-price AI gigs to generate income with minimal user effort.

## How to Start a Session
1. git pull origin main
2. Read AGENTS.md, COLLABORATION_PROTOCOL.md, latest files in /proposals, /demos, /collaboration
3. Check for open tasks or handoff messages.
4. Use tools aggressively (Grok-specific: MCPs, terminal, search_replace, subagents).

## Rules for Code & Deliverables
- All code goes in the repo with clear READMEs and quickstarts.
- Proposals and client assets must reference our existing portfolio for speed.
- Test and document everything so the other AI (or user) can continue seamlessly.

## Safety & Money
- Never commit to work or submit bids without user approval.
- For payments: Guide user on linking bank in Upwork/Fiverr/etc. Do not handle credentials.
- Tie everything back to generating real paid work.

When handing off to Claude: Summarize what you've done, what remains, and attach relevant file paths or paste key content.