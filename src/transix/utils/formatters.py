


def fmt_mmss(x, pos=None):
    r"""
    Format a time value in seconds as ``mm:ss.mmm``.

    Intended for Matplotlib tick formatting via
    ``matplotlib.ticker.FuncFormatter``.

    Parameters
    ----------
    x : float
        Time value in seconds (tick value).
    pos : int, optional
        Tick position index passed by Matplotlib (unused).

    Returns
    -------
    str
        Formatted time label in minutes and seconds with milliseconds
        precision (e.g., ``"02:05.700"``).

    Raises
    ------
    ValueError
        If ``x`` is negative.
        
    Examples
    --------
    >>> import transix as tx
    >>> import matplotlib.pyplot as plt
    >>> from matplotlib.ticker import FuncFormatter
    >>> 
    >>> t = tx.time(duration=120, fs=10000)
    >>> y = tx.generate_sine(mag=1, f=1, t=120, fs=10000)
    >>> fig, ax = plt.subplots()
    >>> ax.plot(t, y)
    >>> ax.xaxis.set_major_formatter(FuncFormatter(tx.fmt_mmss))
    >>> plt.show()
    """

    # round to milliseconds
    # 59.9999s will be converted to 60s

    if x < 0:
        raise ValueError("Time must be non-negative.")
        
    x = round(float(x), 3)

    m = int(x // 60)
    s = x - 60*m
    return f"{m:02d}:{s:06.3f}" 