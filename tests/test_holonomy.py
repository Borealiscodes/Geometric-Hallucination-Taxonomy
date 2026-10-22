import numpy as np
from toolkit.holonomy import (
    parallel_transport_step,
    parallel_transport_loop,
    holonomy_operator,
    holonomy_magnitude,
    holonomy_signature
)

def test_parallel_transport_step_identity():
    # Γ = 0 → transport should not change the vector
    v = np.array([1.0, 2.0])
    Γ = np.zeros((2, 2))

    transported = parallel_transport_step(v, Γ)
    assert np.allclose(transported, v), "Parallel transport with zero connection should be identity."


def test_parallel_transport_step_simple():
    # Simple connection matrix
    v = np.array([1.0, 0.0])
    Γ = np.array([[0.0, 1.0],
                  [0.0, 0.0]])

    # v' = v - Γv = [1,0] - [0,0] = [1,0]
    transported = parallel_transport_step(v, Γ)
    assert np.allclose(transported, np.array([1.0, 0.0])), "Parallel transport step incorrect."


def test_parallel_transport_loop_multiple_steps():
    v0 = np.array([1.0, 0.0])
    Γ1 = np.array([[0.0, 1.0],
                   [0.0, 0.0]])
    Γ2 = np.array([[0.0, 0.0],
                   [1.0, 0.0]])

    transported = parallel_transport_loop(v0, [Γ1, Γ2])

    # First step: v1 = [1,0]
    # Second step: v2 = v1 - Γ2 v1 = [1,0] - [0,1] = [1,-1]
    expected = np.array([1.0, -1.0])

    assert np.allclose(transported, expected), "Parallel transport loop incorrect."


def test_holonomy_operator_zero_loop():
    # No change along loop → holonomy should be zero
    v0 = np.array([1.0, 2.0])
    Γs = [np.zeros((2, 2)) for _ in range(3)]

    H = holonomy_operator(v0, Γs)
    assert np.allclose(H, 0.0), "Holonomy should be zero for identity loop."


def test_holonomy_magnitude_positive():
    v0 = np.array([1.0, 0.0])
    Γs = [np.array([[0.0, 0.0],
                    [1.0, 0.0]])]

    mag = holonomy_magnitude(v0, Γs)
    assert mag > 0.0, "Holonomy magnitude should be positive for non-zero drift."


def test_holonomy_signature_structure():
    v0 = np.array([1.0, 0.0])
    Γs = [np.array([[0.0, 0.0],
                    [1.0, 0.0]])]

    sig = holonomy_signature(v0, Γs)

    assert "drift" in sig
    assert "magnitude" in sig
    assert "direction" in sig

    assert isinstance(sig["magnitude"], float)
    assert sig["direction"].shape == v0.shape
