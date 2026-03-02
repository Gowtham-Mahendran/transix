from typing import Literal

import numpy as np


def abc_to_ab0(a,b,c,
    variant: Literal["power_variant", "power_invariant"] = "power_invariant"):
    r"""
    Compute Clarke alpha, beta and zero components from abc quantities.

    Parameters
    ----------
    a, b, c : array_like
        Signal a, b, c. These can be three phase signals in complex form.

    variant : {"power_invariant","power_variant"}, optional
        Default is power_invariant

    Returns
    -------
    alpha, beta, zero : ndarray
        Alpha-, beta-, and zero components of three phase quantities.

    See Also
    --------
    :func:`transix.ab0_to_abc`

    Notes
    -----
    Clarke's transformation [1] converts three phase abc quantities to
    alpha-beta-zero quantities.
    
    The **power invariant** type is computed by,

    .. math::

       \begin{bmatrix}
       \alpha \\
       \beta \\
       zero
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
       zero
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

    >>> import transix as tx
    >>> a, b, c = tx.generate_abc(rms=230,f=50,t=0.1,fs=50000)
    [ 0.      2.0437  4.0873 ... -4.0873 -2.0437 -0.    ] 
    [-281.6913 -282.7076 -283.7128 ... -279.6254 -280.6639 -281.6913] 
    [281.6913 280.6639 279.6254 ... 283.7128 282.7076 281.6913]
    >>> alpha,beta,zero = tx.abc_to_ab0(a,b,c)
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



def ab0_to_abc(alpha,beta,zero,
    variant: Literal["power_variant", "power_invariant"] = "power_invariant"):
    r"""
    Compute three phase abc quantities from Clarke's alpha, beta and zero components.

    Parameters
    ----------
    alpha, beta, zero : array_like
        alpha-, beta-, and zero components of clarke's three phase quantities.

    variant : {"power_invariant","power_variant"}, optional
        Default is power_invariant

    Returns
    -------
    a, b, c : ndarray
        Three phase abc quantities.

    See Also
    --------
    :func:`transix.abc_to_ab0`

    Notes
    -----
    The inverse Clarke's transformation [1] converts alpha-beta-zero quantities 
    to three phase abc quantities.
    
    The **power invariant** transformation type is orthonormal. So, the 
    inverse is given by taking transpose of original matrix.

    .. math::

       \begin{bmatrix}
        a\\
        b\\
        c
        \end{bmatrix}
        =
        \sqrt{\frac{2}{3}}
        \begin{bmatrix}
        1 & 0 & \frac{1}{\sqrt{2}}\\
        -\frac{1}{2} & \frac{\sqrt{3}}{2} & \frac{1}{\sqrt{2}}\\
        -\frac{1}{2} & -\frac{\sqrt{3}}{2} & \frac{1}{\sqrt{2}}
        \end{bmatrix}
        \begin{bmatrix}
        \alpha\\
        \beta\\
        zero
        \end{bmatrix}

    The **power variant** type is not orthonormal. The inverse is 
    given by,

    .. math::

       \begin{bmatrix}
        a\\
        b\\
        c
        \end{bmatrix}
        =
        \begin{bmatrix}
        1 & 0 & 1\\
        -\frac{1}{2} & \frac{\sqrt{3}}{2} & 1\\
        -\frac{1}{2} & -\frac{\sqrt{3}}{2} & 1
        \end{bmatrix}
        \begin{bmatrix}
        \alpha\\
        \beta\\
        zero
        \end{bmatrix}
    
    Examples
    --------

    >>> import transix as tx
    >>> a, b, c = tx.generate_abc(rms=230,f=50,t=0.1,fs=50000)
    [ 0.      2.0437  4.0873 ... -4.0873 -2.0437 -0.    ] 
    [-281.6913 -282.7076 -283.7128 ... -279.6254 -280.6639 -281.6913] 
    [281.6913 280.6639 279.6254 ... 283.7128 282.7076 281.6913]
    >>> alpha,beta,zero = tx.abc_to_ab0(a,b,c)
    [ 0.      2.503   5.0059 ... -5.0059 -2.503   0.    ] 
    [-398.3717 -398.3638 -398.3403 ... -398.3403 -398.3638 -398.3717] 
    [ 0.      0.     -0.0001 ...  0.0001  0.      0.    ]
    >>> a1,b1,c1 = tx.ab0_to_abc(alpha,beta,zero)
    >>> np.allclose(a, a1) and np.allclose(b, b1) and np.allclose(c, c1)
    True

    References
    ----------
    .. [1] E. Clarke, Circuit Analysis of A-C Power Systems: Symmetrical 
        and Related Components. Wiley, 1943.

    """

    if variant == "power_invariant":
        a = np.sqrt(2/3) * ((1 * alpha) + (0 * beta) + (np.sqrt(1/2) * zero))
        b = np.sqrt(2/3) * ((-(1/2) * alpha) + ((np.sqrt(3)/2) * beta) + (
            np.sqrt(1/2) * zero))
        c = np.sqrt(2/3) * ((-(1/2) * alpha) + (-(np.sqrt(3)/2) * beta) + (
            np.sqrt(1/2) * zero))

    elif variant == "power_variant":
        a = (1 * alpha) + (0 * beta) + (1 * zero)
        b = (-(1/2) * alpha) + ((np.sqrt(3)/2) * beta) + (1 * zero)
        c = (-(1/2) * alpha) + (-(np.sqrt(3)/2) * beta) + (1 * zero)

    else:
        raise ValueError("variant must be 'power_invariant' or 'power_variant'")

    return a, b, c