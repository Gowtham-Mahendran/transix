import transix as tx


def test_fmt_mmss_zero():
    # 2 decimal for minute
    # 2 decimal for second
    # 3 for millisecond
    assert tx.fmt_mmss(0) == "00:00.000"

def test_fmt_mmss_float():
    assert tx.fmt_mmss(5.7) == "00:05.700"

def test_fmt_mmss_rollover():
    # 61s should be 1 minute and 1 second
    assert tx.fmt_mmss(61) == "01:01.000"

def test_fmt_mmss_rounding():
    # 59.9999 rounds to 1 minute
    assert tx.fmt_mmss(59.9999) == "01:00.000"

def test_fmt_mmss_negative_rollover():
    # -61 should be -01:01.000
    assert tx.fmt_mmss(-61) == "-01:01.000"

def test_fmt_mmss_negative_rounding():
    # 59.9999 rounds to 1 minute
    assert tx.fmt_mmss(-59.9999) == "-01:00.000"