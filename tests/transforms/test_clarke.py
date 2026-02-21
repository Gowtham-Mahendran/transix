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