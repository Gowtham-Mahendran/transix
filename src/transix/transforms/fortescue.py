from __future__ import annotations

from typing import NamedTuple

import numpy as np


class SequenceABC(NamedTuple):
    zero: tuple  # (a0, b0, c0)
    pos: tuple  # (a1, b1, c1)
    neg: tuple  # (a2, b2, c2)


def abc_to_seq(a, b, c):
    a = np.asarray(a, dtype=complex)
    b = np.asarray(b, dtype=complex)
    c = np.asarray(c, dtype=complex)

    alpha = np.exp(1j * 2 * np.pi / 3)

    a0 = (a + b + c) / 3
    a1 = (a + alpha * b + (alpha * alpha) * c) / 3
    a2 = (a + (alpha * alpha) * b + alpha * c) / 3

    zero = (a0, a0, a0)
    pos = (a1, (alpha * alpha) * a1, alpha * a1)
    neg = (a2, alpha * a2, (alpha * alpha) * a2)

    # The order of the sequence is set to zero, positive and negative.
    # This also match with python-indexing.

    return SequenceABC(zero=zero, pos=pos, neg=neg)
