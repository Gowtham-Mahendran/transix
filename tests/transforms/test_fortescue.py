import numpy as np

import transix


def _alpha():
    return np.exp(1j * 2 * np.pi / 3)


def test_returns_complex_for_scalar_input():
    # passing scalar quantities
    a, b, c = 1, -0.5, 0.5

    seq = transix.abc_to_seq(a, b, c)

    # seq.zero + seq.pos + seq.neg is a tuple concatenation
    # (a0, b0, c0, a1, b1, c1, a2, b2, c2)
    for comp in seq.zero + seq.pos + seq.neg:
        # print(comp, type(comp))
        assert isinstance(comp, complex)


def test_balanced_abc_positive_sequence():
    alpha = _alpha()

    # Balanced three-phase set: same magnitude, 120° apart
    # abc sequence (counter-clockwise rotation)
    A = 2.0 * np.exp(1j * 0.3)
    a, b, c = A, (alpha * alpha) * A, alpha * A

    seq = transix.abc_to_seq(a, b, c)

    # zero and negative components should be zero
    for x in seq.zero + seq.neg:
        assert np.allclose(x, 0, atol=1e-12)

    # positive sequence should reconstruct the same set
    assert np.allclose(seq.pos[0], a, atol=1e-12)
    assert np.allclose(seq.pos[1], b, atol=1e-12)
    assert np.allclose(seq.pos[2], c, atol=1e-12)


def test_balanced_abc_negative_sequence():
    alpha = _alpha()

    # Balanced three-phase set: same magnitude, 120° apart
    # acb sequence (counter-clockwise rotation)
    A = 2.0 * np.exp(1j * 0.3)
    a, b, c = A, alpha * A, (alpha * alpha) * A

    seq = transix.abc_to_seq(a, b, c)

    # zero and positive components should be zero
    for x in seq.zero + seq.pos:
        assert np.allclose(x, 0, atol=1e-12)

    # negative sequence should reconstruct the same set
    assert np.allclose(seq.neg[0], a, atol=1e-12)
    assert np.allclose(seq.neg[1], b, atol=1e-12)
    assert np.allclose(seq.neg[2], c, atol=1e-12)


def test_pure_zero_sequence():
    # defining a three phase vectors of same magnitude and angle
    A = 2.0 * np.exp(1j * 0.3)

    seq = transix.abc_to_seq(A, A, A)

    # positive and negative components should be zero
    for x in seq.pos + seq.neg:
        assert np.allclose(x, 0, atol=1e-12)

    # zero sequence should reconstruct the same set
    assert np.allclose(seq.zero[0], A, atol=1e-12)
    assert np.allclose(seq.zero[1], A, atol=1e-12)
    assert np.allclose(seq.zero[2], A, atol=1e-12)


def test_reconstruction_principle():
    a, b, c = (0.7 + 1.1j), (-0.2 + 0.3j), (1.3 - 0.4j)

    seq = transix.abc_to_seq(a, b, c)

    # Fortescue: any vector can be decomposed to sets of balanced vectors
    # Their sums should again form the original vector
    assert np.allclose(seq.zero[0] + seq.pos[0] + seq.neg[0], a, atol=1e-12)
    assert np.allclose(seq.zero[1] + seq.pos[1] + seq.neg[1], b, atol=1e-12)
    assert np.allclose(seq.zero[2] + seq.pos[2] + seq.neg[2], c, atol=1e-12)


def test_vectorized_inputs_keep_shape():
    # Input have a (3,) shape
    a = np.array([1 + 0j, 2 + 1j, -0.5 + 0.2j])
    b = np.array([0.1 + 0.3j, -1 + 0j, 2 - 2j])
    c = np.array([0.2 - 0.1j, 0.5 + 0.5j, -1j])
    # print(a.shape)

    seq = transix.abc_to_seq(a, b, c)

    # Output should have the same shape (3,)
    for comp in seq.zero + seq.pos + seq.neg:
        # print(comp.shape)
        assert comp.shape == a.shape


def test_api_ordering_zero_pos_neg():
    # The output length should be 3 and in the order of zero, positive and negative
    seq = transix.abc_to_seq(1 + 0j, 2 + 0j, 3 + 0j)

    assert len(seq) == 3
    assert seq[0] == seq.zero
    assert seq[1] == seq.pos
    assert seq[2] == seq.neg


def test_broadcast_scalar_with_array():
    a = np.array([1 + 0j, 2 + 0j, 3 + 0j])
    b = 0.0
    c = 0.0

    seq = transix.abc_to_seq(a, b, c)

    for comp in seq.zero + seq.pos + seq.neg:
        assert comp.shape == a.shape
