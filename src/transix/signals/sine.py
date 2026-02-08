import numpy as np


def time_array(t,fs):

    dt = 1.0 / fs
    n = int(t * fs) + 1

    return np.arange(n) * dt


def generate_sine(mag, f, t, fs, phase_shift=0.0):
    r"""
    Generate a sine wave

    Parameters
    ----------
    mag : float
        RMS magnitude of the signal (peak = √2 · mag).

    f : float
        Frequency of the sine wave in Hertz.

    t : float
        Total time of the signal in seconds.

    fs : float
        Sampling frequency in Hertz.

    phase_shift : float
        Phase shift in degrees. Default is 0°.   

    Returns
    -------
    out : ndarray
        Sine wave samples over time.

    See Also
    --------
    :func:`transix.generate_abc`

    Examples
    --------
    A sine wave of magnitude 1, frequency 1Hz is generated for
    a period of 1 second with a sampling frequency of 50Hz.

    >>> import transix as tx
    >>> tx.generate_sine(mag = 1, f=1, t=1, fs=50)
    [ 0.00000000e+00  1.77247959e-01  3.51700611e-01  5.20606735e-01
      6.81302580e-01  8.31253876e-01  9.68095801e-01  1.08967028e+00
      1.19406000e+00  1.27961869e+00  1.34499702e+00  1.38916395e+00
      1.41142293e+00  1.41142293e+00  1.38916395e+00  1.34499702e+00
      1.27961869e+00  1.19406000e+00  1.08967028e+00  9.68095801e-01
      8.31253876e-01  6.81302580e-01  5.20606735e-01  3.51700611e-01
      1.77247959e-01  1.73191211e-16 -1.77247959e-01 -3.51700611e-01
     -5.20606735e-01 -6.81302580e-01 -8.31253876e-01 -9.68095801e-01
     -1.08967028e+00 -1.19406000e+00 -1.27961869e+00 -1.34499702e+00
     -1.38916395e+00 -1.41142293e+00 -1.41142293e+00 -1.38916395e+00
     -1.34499702e+00 -1.27961869e+00 -1.19406000e+00 -1.08967028e+00
     -9.68095801e-01 -8.31253876e-01 -6.81302580e-01 -5.20606735e-01
     -3.51700611e-01 -1.77247959e-01 -3.46382422e-16]
 
    """

    w = float(2*np.pi*f)
    time = time_array(t,fs)
    phi = np.deg2rad(phase_shift)

    return np.sqrt(2) * mag * np.sin(w*time + phi)




def generate_abc(mag, f, t, fs, phase_shift=0.0):
    r"""
    Generate a three phase wave

    Parameters
    ----------
    mag : float
        RMS magnitude of the signal (peak = √2 · mag).

    f : float
        Frequency of the sine wave in Hertz.

    t : float
        Total time of the signal in seconds.

    fs : float
        Sampling frequency in Hertz.

    phase_shift : float
        Phase shift in degrees. Default is 0°.   

    Returns
    -------
    out : ndarray, shape (N,3)
        Three phase balanced sine wave over time.

    See Also
    --------
    :func:`transix.generate_sine`

    Examples
    --------
    A sine wave of magnitude 1, frequency 50Hz is generated for
    a period of 0.02 second with a sampling frequency of 1kHz.

    >>> import transix as tx
    >>> tx.generate_abc(mag = 1, f=50, t=0.02, fs=1000)
    (array([ 
         0.00000000e+00,  4.37016024e-01,  8.31253876e-01,  1.14412281e+00,
         1.34499702e+00,  1.41421356e+00,  1.34499702e+00,  1.14412281e+00,
         8.31253876e-01,  4.37016024e-01,  1.73191211e-16, -4.37016024e-01,
        -8.31253876e-01, -1.14412281e+00, -1.34499702e+00, -1.41421356e+00,
        -1.34499702e+00, -1.14412281e+00, -8.31253876e-01, -4.37016024e-01,
        -3.46382422e-16]), 
    array([
       -1.22474487, -1.3833096 , -1.40646635, -1.29194838, -1.05096549,
       -0.70710678, -0.29403153,  0.14782557,  0.57521248,  0.94629358,
        1.22474487,  1.3833096 ,  1.40646635,  1.29194838,  1.05096549,
        0.70710678,  0.29403153, -0.14782557, -0.57521248, -0.94629358,
       -1.22474487]), 
    array([ 
        1.22474487,  0.94629358,  0.57521248,  0.14782557, -0.29403153,
       -0.70710678, -1.05096549, -1.29194838, -1.40646635, -1.3833096 ,
       -1.22474487, -0.94629358, -0.57521248, -0.14782557,  0.29403153,
        0.70710678,  1.05096549,  1.29194838,  1.40646635,  1.3833096 ,
        1.22474487]))
 
    """

    w = float(2*np.pi*f)
    time = time_array(t,fs)
    phi = np.deg2rad(phase_shift)

    a = np.sqrt(2) * mag * np.sin(w*time + phi)
    b = np.sqrt(2) * mag * np.sin(w*time + np.deg2rad(-120) + phi)
    c = np.sqrt(2) * mag * np.sin(w*time + np.deg2rad(-240) + phi)
    
    return a,b,c