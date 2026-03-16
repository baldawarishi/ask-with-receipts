# Company Evaluation Research Framework

Detailed criteria, scoring guidance, and methodology references for the `/evaluate-company` skill.

## Methodology Foundations

This framework synthesizes approaches from:

- **HBR "Evaluating a Potential Employer in a Downturn" (Marlo Lyons, 2022)**: Four-part framework — research the company, know the industry, ask strategic questions, leverage your network. Dismissal of questions about hiring adjustments is itself a red flag. [Source: hbr.org/2022/08/how-to-evaluate-a-potential-employer-in-a-downturn]
- **MIT Sloan "Toxic Culture Is Driving the Great Resignation" (Sull, Sull, Zweig, 2022)**: Analyzed 1.4M Glassdoor reviews. Identified the "Toxic Five" culture attributes that predict attrition 10.4x more than compensation. Lateral career opportunities were 2.5x more important than compensation. [Source: sloanreview.mit.edu/article/toxic-culture-is-driving-the-great-resignation/]
- **Adam Grant's Career/Community/Cause model (Wharton, 2025)**: Three-factor evaluation — Career (will your strengths be utilized?), Community (are people invested in your growth?), Cause (does the mission align?). Key probe: "Can you tell me a story about something that happens here but would not elsewhere?" [Source: cnbc.com/2025/01/30/wharton-psychologist-adam-grant-my-favorite-advice-for-job-seekers.html]
- **Reforge "Reverse Interview" (Elena Verna, Crystal Widjaja)**: Back-channel the company just as they back-channel you. The consequence of a bad career decision is bigger for you than for them. Talk to people who have left. [Source: reforge.com/blog/reverse-interview]
- **OpenAI/Wharton "GPTs are GPTs" (Eloundou, Manning, Mishkin, Rock, 2023)**: Task-level AI exposure framework — ~80% of US workforce has at least 10% of tasks affected by LLMs, ~19% may see 50%+ affected. Higher-income jobs face greater exposure. [Source: arxiv.org/abs/2303.10130]
- **Glassdoor Economic Research on layoff impacts (2024-2025)**: Quantified effects — 0.13-star rating drop post-layoff, 2+ year recovery, "forever layoffs" pattern emerging (51% of WARN notices now <50 people). [Source: glassdoor.com/blog/layoffs-cast-a-long-shadow/]
- **Psychology Today / I/O Psychology (Lauren Florko, Ph.D., 2025)**: Unstructured interviews have validity of .20 vs .63 for structured — companies using unstructured processes are both biased and making worse hires. [Source: psychologytoday.com/us/blog/people-planet-profits/202509/how-to-spot-hidden-clues-when-job-hunting]
- **Academic validation of Glassdoor (Huang, Li & Markov, 2020-2023)**: Employee business outlook ratings predict future business performance. Divergence between employee outlook and management forecasts predicts declining ROA and higher CEO turnover. [Source: scholarworks.bgsu.edu]

## Financial Health Evaluation Criteria

### Public Companies
| Indicator | Healthy Signal | Warning Signal |
|-----------|---------------|----------------|
| Revenue growth | Consistent YoY growth | Declining or erratic revenue |
| Profit margin | Stable or improving margins | Shrinking margins, especially gross margin |
| Debt-to-equity | < 1.0 for most industries | > 2.0 or rapidly increasing |
| Operating cash flow | Consistently positive | Negative or declining |
| Current ratio | > 1.5 | < 1.0 (may struggle with obligations) |
| Employee growth vs revenue growth | Growing in proportion | Headcount growing much faster than revenue |

**Important:** Revenue growth can be a vanity metric if not coupled with strong gross margin. Dig into: churn %, lifetime value, recurring vs. non-recurring revenue %, customer concentration. A 20% fall in sales historically correlates with ~8% headcount reduction [CITATION NEEDED].

### Private Companies (Limited Data)
| Signal | Where to Find It |
|--------|-----------------|
| Last funding round & date | Crunchbase, PitchBook, press releases |
| Investor quality | Look up investors' track records and portfolio outcomes |
| Reported revenue/ARR | Press coverage, founder interviews |
| Runway signals | Time since last raise vs burn rate clues |
| Customer logos & case studies | Company website, G2, case studies |
| Job posting velocity | LinkedIn, careers page history (Wayback Machine) |
| Founder quality | Trajectory over current position ("slope > y-intercept") |
| Early employee quality | Could they get roles elsewhere? Quality signals conviction |
| Growth quality | Organic vs. paid channels, payback periods, diversification |

### Key Financial Red Flags
- Multiple rounds of layoffs with "restructuring" framing
- Revenue declining while marketing spend increases
- Key executives selling stock (for public companies)
- Delayed financial reporting or auditor changes
- Rapid pivots in business model
- CEO track record of prior failures (check court records for lawsuits/liens/bankruptcy)

### Where to Find Financial Data
- **Public:** EDGAR (10-K, 10-Q, 8-K filings), earnings call transcripts, Yahoo Finance, Bloomberg
- **Private:** Crunchbase, local court records, LinkedIn employee count trends
- **Layoff-specific:** layoffs.fyi, WARN Act filings (WARNTracker.com), SEC 8-K filings (Federal Reserve research found these sometimes reveal layoffs before WARN notices)

## Layoff Risk Assessment

### Quantified Impact (Glassdoor Economic Research)
- Layoffs cause a **0.13-star drop** in overall rating (out of 5)
- Surviving employees show a **0.16-star drop** and are **19.4% more likely** to leave a 1-star lower review in 6 months post-layoff
- Ratings take **>2 years** to recover
- Post-layoff disengagement costs companies **$20.8 billion** in the first year
- "Anxiety" keywords appear **67% more** in year 1, **90% more** in year 2
- Repeated layoffs have **double the impact** on sentiment vs. first-round

### "Forever Layoffs" Pattern (2025-2026)
Small-scale firings (<50 people) now make up **51% of WARN Act notices** (up from 38% in 2015). Rolling layoffs "create cultures of anxiety, insecurity, and resentment." Biggest sentiment drops affect key talent, managers, and new hires.

### Leading Indicators
- **Hiring freeze or slowdown** — track via LinkedIn job posting trends
- **Senior leadership departures** — especially CFO, CTO, or multiple VPs
- **Frequent reorganizations** — more than 1 major reorg per year
- **Office consolidation** — closing satellite offices, subleasing space
- **Glassdoor rating decline** — sustained drop over 6+ months
- **Shift from "growth" to "efficiency" language** in earnings calls or company comms
- **Cutting perks** — often precedes headcount reduction
- **"Burnout" mentions** in reviews increased 32% YoY; affected employees are 58% more likely to apply elsewhere

### Where to Search
- layoffs.fyi for tech companies
- WARN Act notices (state-specific databases, WARNTracker.com)
- SEC filings (10-K, 10-Q for headcount disclosures; 8-K for event-driven layoff signals)
- Glassdoor reviews mentioning job security
- Reddit r/[companyname], Blind

## AI Disruption Risk Framework

### Assessment Questions
1. **What is the core unit of value?** If it's information synthesis, content creation, or pattern matching — higher risk. If it's physical operations, regulatory compliance, or deep relationship management — lower risk.
2. **What are the moats?** Data moats, network effects, regulatory capture, and physical infrastructure are more durable. Brand and process efficiency are less durable against AI.
3. **Is the company a tool-maker or tool-user?** Companies building AI tools may benefit. Companies whose products compete with AI capabilities face higher risk.
4. **What do the company's customers pay for?** Expertise and judgment (more defensible) vs. execution of known processes (less defensible)?
5. **How complex is the switching cost?** High integration depth = more defensible.
6. **What % of the workforce is in high-exposure tasks?** Per OpenAI/Wharton research, tasks involving programming and writing have highest LLM exposure. Science and critical thinking skills have negative correlation with exposure.

### Industry Risk Heuristics
| Lower Risk | Medium Risk | Higher Risk |
|------------|-------------|-------------|
| Healthcare (regulated) | Enterprise SaaS (depends on moat) | Content/media production |
| Defense/aerospace | Financial services | Commodity analytics |
| Physical infrastructure | E-commerce/marketplace | Translation/localization |
| Biotech/pharma | EdTech | Basic customer support |
| Energy/utilities | HR/recruiting tech | SEO/digital marketing |

### Macro Context (McKinsey/BCG/WEF 2025)
- 88% of organizations use AI in at least one function, but only 31% are scaling enterprise-wide
- Only 25% of leaders report achieving significant value from AI (BCG)
- 32% expect AI to decrease workforce size in coming year (McKinsey)
- 60% generate no material value from AI despite investment (BCG)
- Companies not investing in AI may face competitive vulnerability; companies investing heavily but not achieving value may face cost-cutting that hits headcount

## AI Posture Classification Guide

### AI-Ignorant
- No AI mentions in product, blog, or job postings
- Leadership makes no public statements about AI
- Industry peers are adopting AI but company is silent

### AI-Washing
- Marketing materials mention AI prominently but product hasn't changed
- "AI-powered" labels on existing features without meaningful capability improvement
- No AI/ML engineering roles in job postings
- PR announcements about AI "partnerships" without product integration

### AI-Pragmatic
- Uses AI tools internally for productivity (Copilot, etc.)
- Some AI-enhanced product features with genuine utility
- Moderate AI/ML hiring
- Measured, realistic language about AI from leadership

### AI-Strategic
- AI is central to the product roadmap or business model
- Significant AI/ML team and investment
- Published research, patents, or open-source AI contributions
- Clear competitive advantage derived from AI capabilities
- Leadership articulates specific AI strategy (not just buzzwords)

## Culture Assessment

### The "Toxic Five" (MIT Sloan)

From Sull, Sull, & Zweig's research analyzing 1.4M Glassdoor reviews, these five attributes predict toxic culture and are 10.4x more predictive of attrition than compensation:

1. **Disrespectful** — Lack of consideration, courtesy, and dignity for others
2. **Non-inclusive** — Inequity based on gender, race, disability, LGBTQ+ identity, age
3. **Unethical** — Dishonesty, regulatory violations, lack of integrity
4. **Cutthroat** — Backstabbing, toxic competition, sabotage among colleagues
5. **Abusive** — Bullying, harassment, hostility from management

### Adam Grant's Career/Community/Cause (Wharton)
- **Career** — Will your strengths be utilized? Will you grow?
- **Community** — Are people invested in your growth, success, and well-being?
- **Cause** — Does the mission align with your values?

Culture matters more than role fit because "everybody's job changes over time" — culture determines whether you can adapt within the org.

### What to Look For in Reviews
- Read the 2-3 star reviews (most balanced signal)
- Look for patterns across multiple reviews, not individual complaints
- Weight recent reviews more heavily
- Check if management responds to reviews (engagement signal)
- Compare ratings across categories (culture, management, comp, work-life)
- Employee outlook ratings diverging from management narrative is a strong predictive signal (academic research)

### Interview Process as a Culture Signal (Psychology Today/I/O Psychology)
- **Red flags:** >2 interview rounds (poor process), unstructured interviews (validity .20 vs .63) [CITATION NEEDED: numbers conflate Sackett et al. 2022 and Schmidt & Hunter 1998 composite], illegal questions, vague role definition, 48-hour scheduling demands, pressure to accept quickly
- **Yellow flags:** "family" or "passion" language (blurred boundaries), missing salary in pay-transparency jurisdictions
- **Green flags:** Standardized questions with evaluation criteria, 2+ interviewers, candidate question time, clear duties and reporting structure, consistent messaging across recruiter/manager/posting

## Ethics Assessment Categories

| Category | What to Search For |
|----------|-------------------|
| Leadership integrity | Executive scandals, fraud, SEC violations, lawsuits |
| Worker treatment | NLRB complaints, wage theft suits, discrimination cases, OSHA violations |
| Environmental | EPA violations, sustainability controversies, greenwashing |
| Privacy & data | Data breaches, FTC actions, GDPR fines, dark patterns |
| Social impact | Predatory business practices, community harm, controversial clients |
| Corporate governance | Board independence, shareholder lawsuits, executive compensation controversies |

## Interview Questions Generator

Based on research gaps, suggest questions from these categories:

### Financial Stability
- "How is the team/department funded, and what does the budget trajectory look like?"
- "What's the company's path to profitability?" (if pre-profit)
- "How did the company navigate the last downturn?"
- "How is the company adjusting hiring strategy to current market changes?" (HBR — dismissal of this question is itself a red flag)
- "When is the next funding round needed?" (startups)

### Culture & Management
- "Can you tell me a story about something that happens here but would not elsewhere?" (Adam Grant)
- "How does the team handle disagreements or conflicting priorities?"
- "What does career progression look like for someone in this role over 2-3 years?"
- "Can you tell me about someone who was promoted recently and why?"

### AI & Technology Strategy
- "How is the team thinking about AI's impact on this role/product?"
- "What AI tools does the engineering team use today?"
- "How do you see the product evolving with AI capabilities in the next 2 years?"

### Stability & Growth
- "Have there been any organizational changes in the last year?"
- "What's the team's retention been like?"
- "What are the biggest risks the company faces right now?"
- "Can you share employee growth data across the last four years?" (HBR)

### Back-Channel Strategy (Reforge)
- Talk to people who have **left** the company, not just current employees
- The company back-channels you through references — do the same to them
- Multiple perspectives reduce bias; single sources are unreliable

## Source References

1. [HBR: Evaluating Employers in a Downturn](https://hbr.org/2022/08/how-to-evaluate-a-potential-employer-in-a-downturn)
2. [Reforge: The Reverse Interview](https://www.reforge.com/blog/reverse-interview)
3. [Fishman AF: Reverse Interviewing](https://www.fishmanafnewsletter.com/p/how-to-reverse-interview)
4. [Product Teacher: Vetting Your Employer](https://www.productteacher.com/articles/vetting-your-employer-after-receiving-a-pm-job-offer)
5. [Product Lessons: Evaluating Startup Offers](https://www.productlessons.xyz/article/how-to-evaluate-startup-job-offer)
6. [GitHub: Reverse Interview Questions](https://github.com/viraptor/reverse-interview)
7. [MIT Sloan: Toxic Culture and the Great Resignation](https://sloanreview.mit.edu/article/toxic-culture-is-driving-the-great-resignation/)
8. [Psychology Today: Hidden Clues When Job Hunting](https://www.psychologytoday.com/us/blog/people-planet-profits/202509/how-to-spot-hidden-clues-when-job-hunting)
9. [CNBC/Adam Grant: Advice for Job Seekers](https://www.cnbc.com/2025/01/30/wharton-psychologist-adam-grant-my-favorite-advice-for-job-seekers.html)
10. [Glassdoor: Layoffs Cast a Long Shadow](https://www.glassdoor.com/blog/layoffs-cast-a-long-shadow/)
11. [CNBC/Glassdoor: Forever Layoffs in 2026](https://www.cnbc.com/2025/11/12/glassdoor-report-in-2026-forever-layoffs-for-some-pay-bumps-for-others.html)
12. [BGSU: Glassdoor Construct Validity Study](https://scholarworks.bgsu.edu/cgi/viewcontent.cgi?article=1099&context=pad)
13. [OpenAI/Wharton: GPTs are GPTs](https://arxiv.org/abs/2303.10130)
14. [McKinsey: State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
15. [BCG: Closing the AI Impact Gap](https://www.bcg.com/publications/2025/closing-the-ai-impact-gap)
16. [Federal Reserve: Tracking Layoffs with SEC Filings](https://www.federalreserve.gov/econres/feds/files/2024020pap.pdf)
17. [Science/AAAS: Employment Due Diligence](https://www.science.org/content/article/tooling-employment-due-diligence)
