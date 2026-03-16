---
name: evaluate-company
description: Evaluate a company for job-seeker fit. Researches business model, financials, culture, AI posture, layoff risk, ethics, and remote work to produce a structured assessment with an overall signal (attractive / neutral / concerning).
argument-hint: [company-name]
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Agent
---

# Company Fit Evaluator

Evaluate **$ARGUMENTS** as a potential employer. Produce a structured, source-backed assessment using the research framework below.

## Instructions

1. **Search broadly first.** Run parallel web searches across multiple dimensions (see Research Dimensions below). Use the source selection rules from `@agents.md` — prioritize official docs, SEC filings, Glassdoor, Reddit, HN, and reputable news. Avoid SEO-farm content and AI-generated review sites.

2. **Triangulate every claim.** Apply the Research Triangulation pattern from `@agents.md`:
   - Official narrative vs. independent validation vs. competitive context vs. financial reality vs. user/employee experience.
   - Flag mismatches between layers.

3. **Cite everything.** Use footnote-style citations [1][2][3] with numbered URLs at the bottom. No unsourced factual claims.

4. **Be honest about confidence.** Use confidence percentages. Mark assumptions with [SQUARE BRACKETS].

5. **Output the full report** using the template structure below.

## Research Dimensions

Search for information across ALL of these dimensions. Run searches in parallel where possible.

### 1. Business Overview
- What does the company do? Core product/service, business model, how it makes money.
- Target market, competitive positioning, key differentiators.

### 2. Company Maturity & Financials
- Size (headcount, revenue if available), founding year, stage.
- Private, venture-backed (and runway/last raise), or publicly traded.
- For public companies: revenue trend, profit margins, debt-to-equity, cash flow, liquidity ratios. Check EDGAR filings.
- For private companies: last funding round, investors, runway signals, Crunchbase data. Assess investor quality and founder trajectory.
- Revenue growth is a vanity metric without gross margin context — dig into churn %, recurring vs. non-recurring revenue, customer concentration.
- Key question: Is there a mismatch between narrative ("we're growing!") and financial signals?

### 3. Recent Developments
- Notable news from the last 6-12 months: strategic shifts, leadership changes, acquisitions, product launches, pivots.
- Earnings calls or investor letters (public companies).
- Press coverage sentiment — is it mostly positive, mixed, or critical?

### 4. Work Structure & Remote Policy
- Current remote/hybrid/in-office policy.
- Any signals of policy changes (RTO mandates, office lease news, executive statements).
- Glassdoor/Reddit/Blind mentions of actual vs. stated policy.

### 5. AI Disruption Risk
Assess how defensible the business is against AI capabilities using this framework:

| Risk Level | Description |
|------------|-------------|
| **Low** | Core value is in physical operations, regulated processes, or deep domain expertise that AI augments but can't replace |
| **Medium** | Some workflows are AI-automatable, but company has defensible data moats, network effects, or switching costs |
| **High** | Core offering could be substantially replicated or disrupted by AI (content generation, simple SaaS, commodity analytics) |

Consider: Does the company's moat come from data, relationships, regulatory capture, physical infrastructure, or brand — or from processes that LLMs/AI agents can now do?

### 6. Layoffs & Workforce Stability
- Any layoffs in the past 12-24 months? Scale and stated reasons. Check layoffs.fyi, WARN Act filings, SEC 8-K filings.
- Watch for "forever layoffs" pattern: rolling small cuts (<50 people) that avoid WARN Act thresholds but create sustained anxiety.
- Hiring velocity: is the company actively hiring, frozen, or shrinking?
- Glassdoor/Blind/Reddit sentiment on job security. Note: Glassdoor research shows layoffs cause a 0.13-star drop that takes 2+ years to recover. Repeated layoffs have double the sentiment impact.
- Severance details if reported.
- Proxy signals: frequent reorgs, senior leadership departures, Glassdoor rating trends, "efficiency" language replacing "growth" language.

### 7. AI Posture
Classify the company's relationship with AI:

| Posture | Description |
|---------|-------------|
| **AI-Ignorant** | No meaningful AI strategy or adoption |
| **AI-Washing** | Uses AI mainly in marketing/PR but no substantive integration |
| **AI-Pragmatic** | Adopts AI tools where they add clear value; measured approach |
| **AI-Strategic** | AI is core to product/business strategy; building or deeply integrating AI capabilities |

Look for: engineering blog posts, product announcements mentioning AI, job postings for AI/ML roles, executive statements, patent filings.

### 8. Ethics & Controversies
- Leadership integrity issues, executive scandals, board problems.
- Worker treatment: wage theft, discrimination lawsuits, union conflicts, NLRB complaints.
- Environmental or societal impact concerns.
- Data privacy incidents or regulatory actions.
- Controversial business practices (dark patterns, predatory pricing, etc.).

### 9. Culture & Growth Opportunity
- Glassdoor overall rating and trends (improving or declining over 2+ years). Employee outlook ratings diverging from management narrative predicts declining ROA (academic research).
- MIT Sloan "Toxic Five" signals: disrespectful, non-inclusive, unethical, cutthroat, or abusive behavior patterns in reviews. These are 10.4x more predictive of attrition than compensation.
- Read 2-3 star reviews for the most balanced signal. Look for patterns, not individual complaints.
- Adam Grant's Career/Community/Cause lens: Does the company develop careers, invest in community, and have a meaningful cause?
- Employee development: Does the company invest in learning, internal mobility, mentorship? Lateral career opportunities are 2.5x more important than compensation for retention (MIT Sloan).
- Interview process quality: Unstructured interviews (validity .20) signal a company that is both biased and making worse hires vs. structured (.63). [CITATION NEEDED: these numbers conflate multiple meta-analyses; see research-framework.md]
- Management quality signals from review sites.
- Diversity & inclusion: published reports, reputation, lawsuits.

### 10. Competitive Context
- Who are the main competitors?
- How does this company compare on market position, growth, and employee satisfaction?
- Is the competitive landscape consolidating, fragmenting, or being disrupted?

## Output Template

Structure the final output as follows:

```
# Company Evaluation: [Company Name]

**Date:** [today's date]
**Confidence in overall assessment:** [X%]

## TL;DR
[2-3 sentence summary with the overall signal]

## 1. Business Overview
[What they do, how they make money, market position]

## 2. Company Maturity & Financial Health
[Size, stage, financial indicators]
**Financial Health Signal:** Strong / Adequate / Concerning / Insufficient Data

## 3. Recent Developments
[Key news and strategic moves from the last 6-12 months]

## 4. Work Structure
[Remote policy and any change signals]
**Remote-Friendliness:** Fully Remote / Hybrid-Flexible / Hybrid-Strict / In-Office / Unclear

## 5. AI Disruption Risk
[Analysis of business defensibility]
**Risk Level:** Low / Medium / High

## 6. Workforce Stability
[Layoff history, hiring trends, sentiment]
**Stability Signal:** Stable / Mixed Signals / Concerning

## 7. AI Posture
[How the company relates to AI]
**Classification:** AI-Ignorant / AI-Washing / AI-Pragmatic / AI-Strategic

## 8. Ethics & Controversies
[Any issues found, or clean record]
**Ethics Signal:** Clean / Minor Issues / Concerning / Serious Issues

## 9. Culture & Growth
[Review site trends, toxic culture signals, development investment]
**Culture Signal:** Strong / Adequate / Mixed / Concerning

## 10. Competitive Context
[Market position relative to peers]

---

## Overall Job-Seeker Signal

**[ATTRACTIVE / NEUTRAL / CONCERNING]**

[Final 3-5 sentence synthesis explaining the rating. Call out the strongest positives and most significant risks. Note any critical unknowns that the job seeker should investigate further during interviews.]

## Key Questions to Ask in Interviews
[3-5 targeted questions based on gaps or concerns identified in the research. Always include Adam Grant's probe: "Can you tell me a story about something that happens here but would not elsewhere?"]

## Back-Channel Strategy
[Suggest specific types of people to talk to outside the interview process — especially people who have LEFT the company (Reforge). The company back-channels you through references; do the same.]

## Sources
[Numbered list of all cited URLs]
```

## Important Notes

- If you cannot find sufficient information for a dimension, say so explicitly rather than speculating. Rate data confidence for each section.
- Distinguish between "no evidence of problems" and "evidence of no problems" — these are very different.
- For private companies, financial data will be limited. Focus on funding history, investor quality, and growth signals instead.
- Weight recent information more heavily than older data.
- When sources conflict, present both sides and note the conflict.

See [research-framework.md](research-framework.md) for detailed evaluation criteria, scoring guidance, and source references.
