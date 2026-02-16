# Ask With Receipts

Surprisingly effective research assistant configuration that enforces source-backed answers with citations.

## What This Is

A set of instruction files for AI research assistants (Claude Code, etc.). See [`agents.md`](agents.md) for the full rules.

## Files

- `CLAUDE.md` — Claude Code project configuration
- `agents.md` — Research agent instructions (source selection, citation rules, reasoning patterns)

## Usage

Clone into a workspace and let Claude Code pick up the instructions via `CLAUDE.md`:

```bash
git clone https://github.com/baldawarishi/ask-with-receipts.git
cd ask-with-receipts
```

Or copy `agents.md` into any project that uses AI research assistants.
