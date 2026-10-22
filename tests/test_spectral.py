import numpy as np
from toolkit.spectral import (
    spectral_drift,
    cascade_intensity,
    spectral_collapse,
    spectral_signature
)

def test_spectral_drift_constant():
    # Eigenvalues do not change over time → drift should be zero
    eigenvalues_t = np.array([
        [1.0, 2.0],
        [1.0, 2.0],
        [1.0, 2.0]
    ])

    drift = spectral_drift(eigenvalues_t)
    assert np.allclose(drift, 0.0), "Drift should be zero for constant eigenvalues."


def test_spectral_drift_linear():
    # Linear increase → drift should be constant
    eigenvalues_t = np.array([
        [1.0, 2.0],
        [2.0, 3.0],
        [3.0, 4.0]
    ])

    drift = spectral_drift(eigenvalues_t)
    expected = np.array([
        [1.0, 1.0],
        [1.0, 1.0],
        [1.0, 1.0]
    ])

    assert np.allclose(drift, expected), "Drift incorrect for linear eigenvalue growth."


def test_cascade_intensity():
    eigenvalues_t = np.array([
        [1.0],
        [3.0],
        [7.0]
    ])

    intensity = cascade_intensity(eigenvalues_t)

    # Drift is [2, 4] → max = 4
    assert abs(intensity - 4.0) < 1e-8, "Cascade intensity incorrect."


def test_spectral_collapse_detected():
    eigenvalues_t = np.array([
        [1.0, 0.5],
        [0.8, 0.1],
        [0.7, 0.00001]  # collapse threshold
    ])

    assert spectral_collapse(eigenvalues_t), "Collapse should be detected."


def test_spectral_signature_structure():
    eigenvalues_t = np.array([
        [1.0],
        [2.0],
        [4.0]
    ])

    sig = spectral_signature(eigenvalues_t)

    assert "drift" in sig
    assert "cascade_intensity" in sig
    assert "collapse" in sig

    assert isinstance(sig["cascade_intensity"], float)
    assert isinstance(sig["collapse"], bool)
