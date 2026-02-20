


def fmt_mmss(x, pos=None):
    # formatter for matplotlib time axis plotting
    # usage: ax.xaxis.set_major_formatter(FuncFormatter(fmt_mmss))
    # add test conditions
    # doc strings
    m = int(x // 60)
    s = x - 60*m
    return f"{m:02d}:{s:06.3f}"