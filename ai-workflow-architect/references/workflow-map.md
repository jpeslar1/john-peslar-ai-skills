# Workflow Map Template

Use this when producing a full workflow spec.

## Discovery Questions

1. What starts the workflow?
2. Who does it today?
3. What tools are involved?
4. What input data is required?
5. What decisions are made?
6. What is the final output?
7. What makes output good or bad?
8. What happens when something fails?
9. What must a human approve?
10. How often does this run?

## Automation Classification

| Classification | Use When | Example |
|---|---|---|
| Automate | Repetitive, rule-based, low-risk | Rename files, classify leads, draft summaries |
| Assist | Judgment-heavy but draftable | Draft email, research account, prepare proposal |
| Approve | Customer-facing or consequential | Send email, update CRM stage, publish content |
| Avoid | Ambiguous, rare, or dangerous | Delete records, change billing, send legal notice |

## Implementation Spec

```markdown
# Workflow Name

## Trigger

## Inputs

## Output

## Tools

## Knowledge Sources

## Agent Instructions

## Human Review Gates

## Error Handling

## Logs and Metrics

## Rollout Plan
```

## Quality Metrics

- Time saved per run
- Error rate
- Human edit rate
- Customer-visible defect rate
- Number of escalations
- Cycle time from trigger to output
