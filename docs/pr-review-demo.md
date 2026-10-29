# Pull Request Review Workflow

This note documents a lightweight review checklist for the TAPD Bug Service.

## Review checklist

- Verify `GET /health` before testing an intake flow.
- Confirm bug-intake requests produce a draft without writing to TAPD.
- Confirm the explicit confirmation endpoint is required before creating a TAPD bug.
- Keep TAPD, GitLab, DingTalk, and model credentials in environment variables.
- Run the test suite before merging changes.

## Suggested progress fields

When reviewing an open pull request, record:

1. Summary of changed files and behavior.
2. Test or CI status.
3. Review comments and unresolved threads.
4. Remaining risks and next steps.
