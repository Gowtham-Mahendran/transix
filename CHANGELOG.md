
## 0.3.0
- Added clarke transformation function `abc_to_ab0()`

## 0.2.0
- Added signal generation utilities `generate_sine()` and `generate_abc()`
- Added python support and automated CI testing for 3.11 in addition to 3.12, 3.13 and 3.14
- Introduced tag-based releases with automated publishing to TestPyPI and PyPI
- Implemented GitHub Actions–based documentation build and deployment
- Improved test coverage and validation for signal utilities
- Strengthened branch protection and release workflows
- General cleanup and stability improvements

## 0.1.0
- First minor release
- Stable Fortescue transform API
- Renamed `abc_to_seq()` to `abc_to_sym()` (widely accepted terminology)
- Added documentation with usage examples
- Vectorized support for scalars and arrays
- Improved packaging and project metadata

## v0.4.0 (2026-02-21)

### Feat

- **matplotlib-formatter**: axis formatter to view time in mm:ss with support upto millisecond ticks
- **function**: Incorporated transix time function for signals

### Fix

- **fmt_mmss**: fixed negative axis ticks to show correct values
- **fmt_mmss**: removed value-error raise for negative time values
- **time**: argument in transix time function now takes duration instead of t

### Refactor

- **time-function**: changed time function name to be aligned with future timing function tx.time()

## v0.3.0 (2026-02-15)

## v0.3.0rc2 (2026-02-15)

## v0.3.0rc1 (2026-02-14)

## v0.2.0 (2026-02-08)

## v0.2.0rc2 (2026-02-08)

## v0.1.0 (2026-02-04)

## v0.0.1 (2026-01-24)
