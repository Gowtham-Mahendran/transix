import numpy as np

import transix


def test_generate_sine_input_parameters():

    mag, f, t, fs = 1, 1, 1, 1000

    a = transix.generate_sine(mag=mag, f=f, t=t, fs=fs)

    # Magnitude check
    assert np.allclose(np.max(a)/np.sqrt(2), mag, atol=1e-7)

    # Sampling frequency check
    assert len(a) == fs+1


def test_generate_abc_input_parameters():

    mag, f, t, fs = 1, 1, 1, 1000

    r,y,b = transix.generate_abc(mag=mag, f=f, t=t, fs=fs)

    # Magnitude check
    assert np.allclose(np.max(r)/np.sqrt(2), mag, atol=1e-7)
    assert np.allclose(np.max(y)/np.sqrt(2), mag, atol=1e-7)
    assert np.allclose(np.max(b)/np.sqrt(2), mag, atol=1e-7)

    # Sampling frequency check
    assert len(r) == fs+1
    assert len(r) == len(y)
    assert len(r) == len(b)


def test_generate_sine_output_parameters():

    mag, f, t, fs = 1, 1, 1, 5000

    a = transix.generate_sine(mag=mag, f=f, t=t, fs=fs)

    # Output magnitude check
    assert np.isclose(a[0], mag * np.sqrt(2) * np.sin(2*np.pi*f*0), atol=1e-7)
    assert np.isclose(a[-1], mag * np.sqrt(2) * np.sin(2*np.pi*f*t), atol=1e-7)
    assert np.isclose(a[0], a[-1], atol=1e-7)

    # Output peak value check
    expected_peak = np.sqrt(2) * mag
    
    assert np.allclose(np.max(a), expected_peak, atol=1e-7)

def test_generate_abc_output_parameters():

    mag, f, t, fs = 1, 1, 1, 5000

    r,y,b = transix.generate_abc(mag=mag, f=f, t=t, fs=fs)

    # Output magnitude check
    assert np.isclose(
        r[0], mag * np.sqrt(2) * np.sin(2*np.pi*f*0), atol=1e-7)
    assert np.isclose(
        y[0], mag * np.sqrt(2) * np.sin(2*np.pi*f*0 + np.deg2rad(-120)), atol=1e-7)
    assert np.isclose(
        b[0], mag * np.sqrt(2) * np.sin(2*np.pi*f*0 + np.deg2rad(-240)), atol=1e-7)
    assert np.isclose(r[0], r[-1], atol=1e-7)
    assert np.isclose(y[0], y[-1], atol=1e-7)
    assert np.isclose(b[0], b[-1], atol=1e-7)

    # Output peak value check
    expected_peak = np.sqrt(2) * mag
    
    assert np.allclose(np.max(r), expected_peak, atol=1e-7)
    assert np.allclose(np.max(y), expected_peak, atol=1e-7)
    assert np.allclose(np.max(b), expected_peak, atol=1e-7)

def test_generate_sine_phase_shift():

    mag, f, t, fs = 1, 1, 1, 5000

    a = transix.generate_sine(mag=mag, f=f, t=t, fs=fs)

    # Phase_shift by default is 0deg
    assert np.isclose(a[0], 0, atol=1e-7)

    # Shifting 90deg will make positive peak appear at time=0
    phase_shift = 90
    a = transix.generate_sine(mag=mag, f=f, t=t, fs=fs, phase_shift=phase_shift)

    assert np.isclose(a[0], mag * np.sqrt(2), atol=1e-7)

    # Shifting -90deg will make negative peak appear at time=0
    phase_shift = -90
    a = transix.generate_sine(mag=mag, f=f, t=t, fs=fs, phase_shift=phase_shift)
    
    assert np.isclose(a[0], -(mag * np.sqrt(2)), atol=1e-7)


def test_generate_abc_phase_shift():

    mag, f, t, fs = 1, 1, 1, 5000

    for shift in [0,90,180,270,360]:
        r, y, b = transix.generate_abc(mag=mag, f=f, t=t, fs=fs, phase_shift=shift)

        a_ref = transix.generate_sine(mag=mag, f=f, t=t, fs=fs, phase_shift=0 + shift)
        b_ref = transix.generate_sine(mag=mag, f=f, t=t, fs=fs, phase_shift=-120 + shift)
        c_ref = transix.generate_sine(mag=mag, f=f, t=t, fs=fs, phase_shift=-240 + shift)

        assert np.allclose(r,a_ref,atol=1e-12)
        assert np.allclose(y,b_ref,atol=1e-12)
        assert np.allclose(b,c_ref,atol=1e-12)
        assert r.shape == y.shape == b.shape