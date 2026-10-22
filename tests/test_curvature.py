import numpy as np
from toolkit.curvature import sectional_curvature, curvature_signature

def test_sectional_curvature_basic():
    # Simple 2D curvature tensor with a known contraction
    R = np.zeros((2, 2, 2, 2))
    R[0, 0, 0, 0] = 1.0  # Only one non-zero component

    v = np.array([1.0, 0.0])

    K = sectional_curvature(R, v)
    assert K == 1.0, "Sectional curvature contraction failed for basic tensor."


def test_curvature_signature_normalization():
    R = np.zeros((2, 2, 2, 2))
    R[0, 0, 0, 0] = 2.0

    v = np.array([2.0, 0.0])

    sig = curvature_signature(R, v)

    # Expected: K = 2 * (2^4) = 2 * 16 = 32
    # Normalized: 32 / (||v||^4) = 32 / 16 = 2
    assert abs(sig - 2.0) < 1e-8, "Curvature signature normalization incorrect."
