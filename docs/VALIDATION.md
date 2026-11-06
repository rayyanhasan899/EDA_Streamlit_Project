# Validation and limitations

## Observed locally — 6 November 2026

Dependency installation completed in an isolated Python 3.14.7 environment and `pip check` reported no broken requirements. Streamlit 1.67.0 was installed.

An attempted `AppTest` initial-render smoke test was blocked while loading pandas native DLLs by Windows Application Control. It did not pass. No security setting was weakened or bypassed.

CSV upload/plot interaction and the full application remain unverified in this environment. Documentation-only changes do not claim new functionality or a deployment. Original unpinned dependencies remain unchanged; establishing a tested dependency set is a future improvement.
