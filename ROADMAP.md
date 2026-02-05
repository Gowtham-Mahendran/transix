# transix Roadmap

This roadmap outlines the planned evolution of **transix** from v0.2.0 to v1.0.0.
Each release focuses on a *small, coherent set of linear electrical transforms*.
The goal is correctness, clarity, and long-term stability — not feature rush.

## v0.1.0 — Symmetrical Components (Fortescue) 

![status-done](https://img.shields.io/badge/status-done-brightgreen)

**Focus:** Unbalanced power systems

- abc → (0, +, −) sequences
- Explicit Fortescue matrix
- Scalar + vectorized support

## v0.2.0 — Clarke Transform

![status-ongoing](https://img.shields.io/badge/status-ongoing-blue)

**Focus:** Stationary reference frame

- abc → αβ0 (Clarke, power-invariant)
- Explicit transform matrix
- Scalar + vectorized support
- Unit tests & math docs


## v0.3.0 — Clarke Inverse

<!-- ![status-planned](https://img.shields.io/badge/status-planned-lightgrey) -->

**Focus:** Reversibility

- αβ0 → abc
- Round-trip validation
- Numerical tolerance definition


## v0.4.0 — Clarke Variants
**Focus:** Practical variants

- Power-variant Clarke
- Method selection via arguments


## v0.5.0 — Park Transform (Base)
**Focus:** Rotating reference frame

- αβ0 → dq0
- Angle convention clearly defined
- Power-invariant formulation


## v0.6.0 — Park Inverse
**Focus:** Completeness

- dq0 → αβ0
- dq ↔ αβ round-trip tests


## v0.7.0 — Park Variants
**Focus:** Practical usage

- Power-variant Park
- Zero-sequence-free (dq) form
- Method selection via arguments


## v0.8.0 — Direct Phase abc → dq0 (Base)
**Focus:** Convenience API

- abc → dq0 (abc→αβ0→dq0 chained)
- Same defaults as underlying Clarke/Park
- Tests vs chained reference


## v0.9.0 — abc → dq0 (Angle + alignment options)
**Focus:** Convention control

- `angle="sin"|"cos"` (or `phase_ref=...`)
- `direction="abc"|"acb"` (rotation sign)
- `alignment="d_axis"|"q_axis"` (where theta=0 points)
- Clear docs with one diagram + examples


## v0.10.0 — abc → dq0 (Topology options)
**Focus:** 3-wire vs 4-wire handling

- `wire="3"|"4"` (include/exclude zero-sequence path)
- `zero_seq="keep"|"drop"` (explicit behavior)
- Validation: zero-seq invariants


## v0.11.0 — abc → dq0 (Input form + normalization)
**Focus:** User inputs

- `frame="phase"|"line"` (Vph vs Vll inputs; if supported)
- `normalize="power_invariant"|"power_variant"`
- Robust shape handling (N,3), (3,N), scalar triplets


## v0.12.0 — abc → dq0 (Output options)
**Focus:** Ergonomics

- `return_type="tuple"|"namedtuple"|"ndarray"`
- `out="d"|"q"|"dq"|"dq0"` slicing without extra compute


## v1.0.0 — Stable Electrical Core
**Focus:** Stability & polish

- API freeze
- Unified naming & signatures
- Input normalization (scalar / array / pandas)
- Coverage ≥ 95%
- Documentation completeness
- Marked **Stable**
