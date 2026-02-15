# transix Roadmap

This roadmap outlines the planned evolution of **transix** from v0.2.0 to v1.0.0.
Each release focuses on a *small, coherent set of linear electrical transforms*.
The goal is correctness, clarity, and long-term stability — not feature rush.

## v0.1.0 — Symmetrical Components (Fortescue)

![status-done](https://img.shields.io/badge/status-done-brightgreen)

* abc → (0, +, −) sequences
* `abc_to_sym()`
* Explicit Fortescue matrix
* Scalar + vectorized support

## v0.2.0 — Signal Generation (Base)

![status-done](https://img.shields.io/badge/status-done-brightgreen)

* `generate_sine()` and `generate_abc()`
* Phase, frequency, amplitude, offset
* Deterministic, math-documented

## v0.3.0 — Clarke Transform

![status-done](https://img.shields.io/badge/status-done-brightgreen)

* `abc_to_ab0()`
* Variants included
* Unit tests & math docs

## v0.4.0 — Clarke Inverse

![status-ongoing](https://img.shields.io/badge/status-ongoing-blue)

* `ab0_to_abc()`
* Unit tests & math docs
* Round-trip validation

## v0.5.0 — Park abc → dq0

![status-planned](https://img.shields.io/badge/status-planned-lightgrey)

* `abc_to_dq0`
* Same defaults as Clarke
* `alignment="d_axis"|"q_axis"`
* `angle="sin"|"cos"`
* Unit tests & math docs

## v0.6.0 — Inverse Park dq0 → abc

* `dq0_to_abc`
* Unit tests & math docs

## v0.7.0 — clarke to Park

* `ab0_to_dq0()`
* variants included
* Power-invariant formulation
* Unit tests & math docs

## v0.8.0 — Park to clarke

* `dq0_to_ab0()`
* Unit tests & math docs

<!-- 

v1.1 — Power from Clarke frame

Clarke power calculation (αβ → P, Q)

Instantaneous p–q formulation

Clear assumptions (3-phase, stationary frame)



v1.2 — Power from Park frame

Park power calculation (dq → P, Q)

Power-invariant formulation

Control-oriented examples



v1.3 — Generic P–Q from V & I

P, Q from (V, I)

Frame-agnostic API

abc / αβ / dq support

RMS + instantaneous options



v1.4 — Dual Synchronous Reference Frame

DSRF implementation

Positive/negative dq separation

Angle handling & sign conventions

Unbalanced signal validation



v1.5 — DDSRF

Decoupled double SRF

Cross-coupling removal

Control-ready outputs

Research-grade validation -->