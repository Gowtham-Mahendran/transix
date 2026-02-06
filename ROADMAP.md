# transix Roadmap

This roadmap outlines the planned evolution of **transix** from v0.2.0 to v1.0.0.
Each release focuses on a *small, coherent set of linear electrical transforms*.
The goal is correctness, clarity, and long-term stability — not feature rush.

## v0.1.0 — Symmetrical Components (Fortescue)

![status-done](https://img.shields.io/badge/status-done-brightgreen)

**Focus:** Unbalanced power systems

* abc → (0, +, −) sequences
* Explicit Fortescue matrix
* Scalar + vectorized support


## v0.2.0 — Signal Generation (Base)

![status-ongoing](https://img.shields.io/badge/status-ongoing-blue)

**Focus:** Test & reference signals

* `generate_sine()`
* Phase, frequency, amplitude, offset
* Scalar + vectorized time support
* Deterministic, math-documented

**Focus:** System-level signals

* `generate_abc()`
* Balanced / unbalanced sets
* Phase sequence (abc / acb)
* Zero-sequence injection
* Built on `generate_sine()`


## v0.3.0 — Clarke Transform

<!-- ![status-planned](https://img.shields.io/badge/status-planned-lightgrey) -->

**Focus:** Stationary reference frame

* abc → αβ0 (power-invariant)
* Explicit transform matrix
* Scalar + vectorized support
* Unit tests & math docs


## v0.4.0 — Clarke Inverse

**Focus:** Reversibility

* αβ0 → abc
* Round-trip validation
* Numerical tolerance definition


## v0.5.0 — Clarke Variants

**Focus:** Practical variants

* Power-variant Clarke
* Method selection via arguments


## v0.6.0 — Park Transform (Base)

**Focus:** Rotating reference frame

* αβ0 → dq0
* Angle convention clearly defined
* Power-invariant formulation


## v0.7.0 — Park Inverse

**Focus:** Completeness

* dq0 → αβ0
* dq ↔ αβ round-trip tests


## v0.8.0 — Park Variants

**Focus:** Practical usage

* Power-variant Park
* Zero-sequence-free (dq)
* Method selection via arguments


## v0.9.0 — Direct abc → dq0 (Base)

**Focus:** Convenience API

* abc → dq0 (chained reference)
* Same defaults as Clarke/Park
* Tests vs chained path


## v0.10.0 — abc → dq0 (Convention Control)

**Focus:** Angles & alignment

* `angle="sin"|"cos"`
* `direction="abc"|"acb"`
* `alignment="d_axis"|"q_axis"`


## v0.11.0 — abc → dq0 (Topology & IO)

**Focus:** Real systems

* 3-wire / 4-wire handling
* Zero-sequence control
* Input forms & output slicing


## v1.0.0 — Stable Electrical Core

**Focus:** Stability & polish

* API freeze
* Unified naming & signatures
* Coverage ≥ 95%
* Docs complete
* **Stable**


This ordering is **conceptually perfect**:
signals → transforms → composed APIs.
