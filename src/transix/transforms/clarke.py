from typing import Literal

import numpy as np


def abc_to_ab0(a,b,c,
    variant: Literal["power_variant", "power_invariant"] = "power_invariant"):
    r"""
    Compute clarke alpha, beta and zero components from abc quantities.

    Parameters
    ----------
    a, b, c : array_like
        Signal a, b, c. These can be three phase signals in complex form.

    variant : {"power_invariant","power_variant"}, optional
        Default is power_invariant

    Returns
    -------
    out : ndarray, shape (N,3)
        alpha-, beta-, and zero components of three phase quantities.

    Notes
    -----
    The Clarke's transformation [1] converts three phase abc quantities to
    alpha-beta-zero quantities.
    
    The **power invariant** type is computed by,

    .. math::

       \begin{bmatrix}
       \alpha \\
       \beta \\
       z
       \end{bmatrix}
       =
       \sqrt{\frac{2}{3}}
       \begin{bmatrix}
       1 & -1/2 & -1/2\\
       0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2}\\
       \sqrt{\frac{1}{2}} & \sqrt{\frac{1}{2}} & \sqrt{\frac{1}{2}}
       \end{bmatrix}
       \begin{bmatrix}
       a\\
       b\\
       c
       \end{bmatrix}

    The **power variant** type is computed by,

    .. math::

       \begin{bmatrix}
       \alpha \\
       \beta \\
       z
       \end{bmatrix}
       =
       \frac{2}{3}
       \begin{bmatrix}
       1 & -1/2 & -1/2\\
       0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2}\\
       \frac{1}{2} & \frac{1}{2} & \frac{1}{2}
       \end{bmatrix}
       \begin{bmatrix}
       a\\
       b\\
       c
       \end{bmatrix}
    
    Examples
    --------

    >>> import transix
    >>> a, b, c = transix.generate_abc(mag=230,f=50,t=0.1,fs=50000)
    [ 0.      2.0437  4.0873 ... -4.0873 -2.0437 -0.    ] 
    [-281.6913 -282.7076 -283.7128 ... -279.6254 -280.6639 -281.6913] 
    [281.6913 280.6639 279.6254 ... 283.7128 282.7076 281.6913]
    >>> alpha,beta,z = tx.abc_to_ab0(a,b,c)
    [ 0.      2.503   5.0059 ... -5.0059 -2.503   0.    ] 
    [-398.3717 -398.3638 -398.3403 ... -398.3403 -398.3638 -398.3717] 
    [ 0.      0.     -0.0001 ...  0.0001  0.      0.    ]

    References
    ----------
    .. [1] E. Clarke, Circuit Analysis of A-C Power Systems: Symmetrical 
        and Related Components. Wiley, 1943.

    """

    if variant == "power_invariant":
        alpha = np.sqrt(2/3) * ((1 * a) + ((-1/2) * b) + ((-1/2) * c))
        beta = np.sqrt(2/3) * ((0 * a) + ((np.sqrt(3)/2) * b) + (-(np.sqrt(3)/2) * c))
        zero = np.sqrt(2/3) * (np.sqrt(1/2) * (a + b + c))

    elif variant == "power_variant":
        alpha = (2/3) * ((1 * a) + ((-1/2) * b) + ((-1/2) * c))
        beta = (2/3) * ((0 * a) + ((np.sqrt(3)/2) * b) + (-(np.sqrt(3)/2) * c))
        zero = (2/3) * ((1/2) * (a + b + c))

    else:
        raise ValueError("variant must be 'power_invariant' or 'power_variant'")

    return alpha, beta, zero