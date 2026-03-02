import numpy as np
import pytest

import transix as tx


def test_clarke_balanced_three_phase_signal():

    a,b,c = tx.generate_abc(rms=230,f=50,t=0.1,fs=50000)

    # Variant is not mentioned. default: power_invariant
    alpha,beta,z = tx.abc_to_ab0(a,b,c)

    assert z.all()==0

    alpha,beta,z = tx.abc_to_ab0(a,b,c,variant="power_variant")

    assert z.all()==0

    alpha,beta,z = tx.abc_to_ab0(a,b,c,variant="power_invariant")

    assert z.all()==0

def test_clarke_wrong_input_variant():

    a,b,c = tx.generate_abc(rms=230,f=50,t=0.1,fs=50000)

    with pytest.raises(ValueError, match=
    "variant must be 'power_invariant' or 'power_variant'"):
        tx.abc_to_ab0(a,b,c,variant="wrong_variant")


def test_clarke_power_variant_and_invariant():

    a,b,c = tx.generate_abc(rms=230,f=50,t=0.02,fs=50000)

    # a = np.round(a, 4)
    # b = np.round(b, 4)
    # c = np.round(c, 4)
    
    # print(a,b,c)

    # write test condition to verify types
    # clarke power calculation function is needed to verify variants

    # power-variant
    alpha,beta,z = tx.abc_to_ab0(a,b,c,variant="power_variant")

    # power-invariant
    alpha,beta,z = tx.abc_to_ab0(a,b,c,variant="power_invariant")

    # alpha = np.round(alpha, 4)
    # beta  = np.round(beta, 4)
    # z     = np.round(z, 4)

    # print(alpha,beta,z)


def test_clarke_inverse_balanced_three_phase_signal():

    a,b,c = tx.generate_abc(rms=230,f=50,t=0.1,fs=50000)

    # power-invariant
    alpha,beta,z = tx.abc_to_ab0(a,b,c)

    a1,b1,c1 = tx.ab0_to_abc(alpha,beta,z)

    assert np.allclose(a,a1) and np.allclose(b,b1) and np.allclose(c,c1)


    # power-variant
    alpha,beta,z = tx.abc_to_ab0(a,b,c,variant="power_variant")

    a1,b1,c1 = tx.ab0_to_abc(alpha,beta,z,variant="power_variant")

    assert np.allclose(a,a1) and np.allclose(b,b1) and np.allclose(c,c1)


def test_inverse_clarke_wrong_input_variant():

    a,b,c = tx.generate_abc(rms=230,f=50,t=0.1,fs=50000)

    with pytest.raises(ValueError, match=
    "variant must be 'power_invariant' or 'power_variant'"):
        tx.ab0_to_abc(a,b,c,variant="wrong_variant")