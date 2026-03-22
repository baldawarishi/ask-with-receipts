---
name: fact-check
description: Fact-check a paragraph, article, or set of claims. Extracts individual claims, searches for supporting or contradicting evidence, and produces a verdict for each with sources.
argument-hint: [text or file path containing claims to verify]
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Agent
---

# Fact-Checker

Fact-check **$ARGUMENTS**. If the argument is a file path, read it first. If it's inline text, use it directly.

## Instructions

1. **Extract claims.** Parse the input into individual, verifiable factual claims. Skip opinions, framing, and subjective statements. Number each claim.

2. **Search for each claim.** For every extracted claim, search for primary sources that either support or contradict it. Follow the source selection rules from `@agents.md`:
   - Prioritize primary sources cited in the original text
   - Cross-reference with official statistics, academic papers, and authoritative reporting
   - Do NOT count re-reporting of the same original source as independent verification

3. **Verdict per claim.** For each claim, assign one of:
   - **Accurate** — supported by reliable sources
   - **Inaccurate** — contradicted by reliable sources (state what's actually true)
   - **Misleading** — technically true but missing critical context
   - **Unverifiable** — cannot find reliable sources to confirm or deny
   - **Partially accurate** — some elements correct, others wrong (specify which)

4. **Cite everything.** Use footnote-style citations [1][2][3] with numbered URLs at bottom. Each verdict must have at least one source.

5. **Flag the most consequential errors.** Not all inaccuracies matter equally. Call out which errors, if any, would materially change the reader's understanding or decisions.

## Output Template

```
# Fact-Check: [Brief description of input]

**Date:** [today's date]
**Claims checked:** [N]
**Summary:** [1-2 sentences — overall accuracy assessment]

## Results

| # | Claim | Verdict | Notes |
|---|-------|---------|-------|
| 1 | [claim text] | Accurate | [brief note + citation] |
| 2 | [claim text] | Inaccurate | [what's actually true + citation] |
| ... | ... | ... | ... |

## Most Consequential Issues

[If any inaccuracies or misleading claims were found, explain which ones matter most and why. If everything checks out, say so.]

## Detailed Analysis

[For each non-Accurate claim, provide a longer explanation with full source comparison.]

## Sources

[Numbered list of all cited URLs]
```

## Important Notes

- Extract quotes from the original text to ground each claim precisely.
- When sources conflict with each other, present both sides and note the conflict.
- Do not assume a claim is accurate just because it sounds plausible. Search first.
- Distinguish between "I found no sources contradicting this" (unverifiable) and "sources confirm this" (accurate).
- If the input is very long, focus on the most important/consequential claims first and note which claims were not checked.
