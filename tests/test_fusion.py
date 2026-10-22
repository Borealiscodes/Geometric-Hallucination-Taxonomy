import numpy as np
from toolkit.fusion import (
    nonlinear_interaction,
    fusion_field,
    fusion_intensity,
    fusion_signature
)

def test_nonlinear_interaction_basic():
    x = np.array([1.0, 2.0])
    y = np.array([3.0, -1.0])

    phi = nonlinear_interaction(x, y)

    # φ(x,y) = tanh(x*y)
    expected = np.tanh(np.array([3.0, -2.0]))

    assert np.allclose(phi, expected), "Nonlinear interaction φ(x,y) incorrect."


def test_fusion_field_linear_only():
    x = np.array([1.0, 0.0])
    y = np.array([0.0, 1.0])

    F = fusion_field(x, y, alpha=1.0, beta=1.0, gamma=0.0)

    expected = x + y
    assert np.allclose(F, expected), "Fusion field linear blend incorrect."


def test_fusion_field_with_nonlinearity():
    x = np.array([1.0])
    y = np.array([2.0])

    F = fusion_field(x, y, alpha=1.0, beta=1.0, gamma=1.0)

    expected = 1.0 + 2.0 + np.tanh(2.0)
    assert abs(F - expected) < 1e-8, "Fusion field nonlinear blend incorrect."


def test_fusion_intensity_positive():
    x = np.array([1.0, -1.0])
    y = np.array([2.0, 3.0])

    intensity = fusion_intensity(x, y)

    assert intensity > 0.0, "Fusion intensity should be positive for nonlinear interaction."


def test_fusion_signature_structure():
    x = np.array([1.0, 2.0])
    y = np.array([3.0, -1.0])

    sig = fusion_signature(x, y)

    assert "linear" in sig
    assert "nonlinear" in sig
    assert "intensity" in sig
    assert "fusion" in sig

    assert isinstance(sig["intensity"], float)
    assert sig["linear"].shape == x.shape
    assert sig["nonlinear"].shape == x.shape
    assert sig["fusion"].shape == x.shape
