# transix

[![PyPI](https://img.shields.io/pypi/v/transix.svg)](https://pypi.org/project/transix/)
[![Python](https://img.shields.io/pypi/pyversions/transix)](https://pypi.org/project/transix/)
[![CI](https://github.com/Gowtham-Mahendran/transix/actions/workflows/tests.yml/badge.svg)](https://github.com/Gowtham-Mahendran/transix/actions/workflows/tests.yml)
[![License](https://img.shields.io/pypi/l/transix.svg)](https://github.com/Gowtham-Mahendran/transix/blob/main/LICENSE)
[![Docs](https://img.shields.io/badge/docs-online-blue)](https://Gowtham-Mahendran.github.io/transix/)

**transix** is a lightweight Python library for linear, deterministic, matrix-based representation transforms, commonly used in electrical and control engineering.

## Available Transforms

- Fortescue (Symmetrical Components)
- Clarke (αβ)
- Signal generation utilities

## Features

- Supports complex and real-valued inputs
- Clean object-oriented output
- Fully tested with `pytest`
- Lightweight and minimal dependency

## Installation

transix can be installed from PyPI:

```bash
pip install transix
```

## Example: 

### Fortescue Transform

```python
import transix as tx
Ea = 60+0j
Eb = 45-75j
Ec = -21+120j
seq = tx.abc_to_sym(Ea, Eb, Ec)

a0, b0, c0 = seq.zero
a1, b1, c1 = seq.pos
a2, b2, c2 = seq.neg
```

### Clarke Transform

```python
import transix as tx
alpha, beta, zero = tx.abc_to_ab0(a, b, c)
```

## Testing

All transforms and utilities are tested and verifiable using `pytest`

## Roadmap

See [`ROADMAP.md`](https://github.com/Gowtham-Mahendran/transix/blob/main/ROADMAP.md) for planned additions and future work.

## Contributing

Issues and pull requests are welcome.

If you find a bug, have a question, or want to add a transformation,
please open an issue on GitHub.

---