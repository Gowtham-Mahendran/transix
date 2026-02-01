from __future__ import annotations

from typing import NamedTuple

import numpy as np


class SequenceABC(NamedTuple):
    zero: tuple  # (a0, b0, c0)
    pos: tuple  # (a1, b1, c1)
    neg: tuple  # (a2, b2, c2)


def abc_to_sym(a, b, c):
    r"""
    Compute symmetrical components (Fortescue transform) from abc quantities.

    Parameters
    ----------
    a, b, c : array_like of complex
        Signal a, b, c. These can be three phase signals in complex form.

    Returns
    -------
    out : SequenceABC
        Zero-, positive-, and negative-sequence phase quantities in the abc frame.

        ``out.zero`` : tuple of complex
            Zero-sequence phase quantities ``(a0, b0, c0)``, where ``a0 = b0 = c0``.

        ``out.pos`` : tuple of complex
            Positive-sequence phase quantities ``(a1, b1, c1)``.

        ``out.neg`` : tuple of complex
            Negative-sequence phase quantities ``(a2, b2, c2)``.

    Notes
    -----
    Uses the Fortescue symmetrical component transformation with 
    :math:`\alpha = e^{j2\pi/3}`.
    
    The sequence components are computed by,

    .. math::

       \begin{bmatrix}
       a_0\\
       a_1\\
       a_2
       \end{bmatrix}
       =
       \frac{1}{3}
       \begin{bmatrix}
       1 & 1 & 1\\
       1 & \alpha & \alpha^2\\
       1 & \alpha^2 & \alpha
       \end{bmatrix}
       \begin{bmatrix}
       a\\
       b\\
       c
       \end{bmatrix}
    
    Then the corresponding phase triples are formed.

    .. math::

        \begin{aligned}
        \text{zero} &= (a_0,\; a_0,\; a_0) \\
        \text{pos}  &= \left(a_1,\; \alpha^2 a_1,\; \alpha a_1\right) \\
        \text{neg}  &= \left(a_2,\; \alpha a_2,\; \alpha^2 a_2\right)
        \end{aligned}

    Examples
    --------
    The below example is taken from Wagner and Evans (1933) [2]. 

    >>> import transix as tx
    >>> Ea = 60+0j
    >>> Eb = 45-75j
    >>> Ec = -21+120j
    >>> seq = tx.abc_to_sym(Ea, Eb, Ec)
    >>> seq.zero
    (28+15j, 28+15j, 28+15j)
    >>> seq.pos
    (72.29+11.55j, -26.14-68.38j, -46.15+56.83j)
    >>> seq.neg
    (-40.29-26.55j, 43.14-21.62j, -2.85+48.17j)

    References
    ----------
    .. [1] Fortescue, C.L. Method of symmetrical co-ordinates applied to the solution
        of poly-phase networks (with discussion). Presented at the 34th Annual 
        Convention of the AIEE (American Institute of Electrical Engineers), Atlantic 
        City, NJ, USA, 28 June 1918; Volume 37, pp. 1027-1140.
    .. [2] Wagner, C.F.; Evans, R.D. Symmetrical Components as Applied to the Analysis 
        of Unbalanced Electrical Circuits; Mc-Graw-Hill: New York, NY, USA, 1933.

    """

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
