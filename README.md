# AI Agent Playbook

A practical playbook of AI agent patterns, checklists, and workflows.

## Agent design principles

Good AI agents should be:

- Goal-oriented
- Tool-aware
- Verifiable
- Human-supervised when risk is high
- Honest about uncertainty
- Designed around real user workflows

## Pattern 1: Research Agent

Use case: market research, company research, role research, competitor scans.

Checklist:

- Define the question clearly
- Search multiple sources
- Prefer primary/official sources
- Separate facts from interpretation
- Include confidence and source quality
- End with recommended next action

## Pattern 2: Evaluation Agent

Use case: AI response evaluation, localization QA, content quality checks.

Checklist:

- Define rubric
- Compare output against rubric
- Identify factual, language, tone, and safety issues
- Give concise correction
- Track repeated error patterns

## Pattern 3: Workflow Automation Agent

Use case: repetitive work across email, spreadsheets, GitHub, documents, or dashboards.

Checklist:

- Identify repeated manual steps
- Define required inputs and outputs
- Add verification before final action
- Log decisions
- Keep human approval for risky actions

## Pattern 4: Recruiter Assistant Agent

Use case: job search support.

Checklist:

- Match role requirements to profile
- Avoid overclaiming skills
- Draft concise applications
- Prioritize verified career pages and recruiter contacts
- Track applied companies to avoid duplicates

## Risk controls

- Do not automate irreversible actions without confirmation
- Do not expose secrets or API tokens
- Validate external facts before making claims
- Keep audit trails for important decisions

## Why this matters

AI agents are useful when they reduce repetitive work while keeping quality, verification, and human judgment in the loop.
