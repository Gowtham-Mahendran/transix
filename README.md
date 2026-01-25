# transix

[![PyPI](https://img.shields.io/pypi/v/transix.svg)](https://pypi.org/project/transix/)
[![Python](https://img.shields.io/pypi/pyversions/transix)](https://pypi.org/project/transix/)
[![CI](https://github.com/Gowtham-Mahendran/transix/actions/workflows/tests.yml/badge.svg)](https://github.com/Gowtham-Mahendran/transix/actions/workflows/tests.yml)
[![License](https://img.shields.io/pypi/l/transix.svg)](https://github.com/Gowtham-Mahendran/transix/blob/main/LICENSE)

**transix** is a lightweight toolkit for numerical transformations.

It provides clean, reusable, and well-tested building blocks for working with
numerical transforms, with an emphasis on clarity, correctness, and
vectorized usage.

## Installation

You can install this package using `pip install transix`

## Example: Numerical Transform

```python
import numpy as np
import transix

a = 1 + 0j
b = np.exp(-1j * 2*np.pi/3)
c = np.exp( 1j * 2*np.pi/3)

seq = transix.abc_to_seq(a, b, c)

a0, b0, c0 = seq.zero
a1, b1, c1 = seq.pos
a2, b2, c2 = seq.neg
```

The API works equally well with NumPy arrays (time-series or batch data).


## Testing

All transforms are validated using physics- and identity-based tests.

```bash
pytest
```

## Roadmap

Planned additions include:

* Clarke transforms
* Park transforms
* Inverse transforms
* Expanded documentation and examples

## Contributing

Issues and pull requests are welcome.

If you find a bug, have a question, or want to add a transformation,
please open an issue on GitHub.

---