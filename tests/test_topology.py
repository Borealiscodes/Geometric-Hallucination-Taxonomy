import numpy as np
from toolkit.topology import (
    metric_rank,
    rank_instability,
    collapse_surface,
    topology_signature
)

def test_metric_rank_full_rank():
    # Identity metric → full rank
    g = np.eye(3)
    r = metric_rank(g)
    assert r == 3, "Metric rank should be full for identity metric."


def test_metric_rank_near_singular():
    # Slightly singular metric → stabilized rank should still be full
    g = np.array([
        [1.0, 0.0, 0.0],
        [0.0, 0.000001, 0.0],
        [0.0, 0.0, 1.0]
    ])

    r = metric_rank(g)
    assert r == 3, "Stabilized metric rank should remain full."


def test_rank_instability_detected():
    # Rank drops from 3 → 2 → instability
    g_t = np.array([
        np.eye(3),
        np.array([[1,0,0],[0,1,0],[0,0,0]]),  # rank 2
        np.array([[1,0,0],[0,1,0],[0,0,0]])   # rank 2
    ])

    assert rank_instability(g_t), "Rank instability should be detected."


def test_rank_instability_not_detected():
    # Rank stays constant → no instability
    g_t = np.array([
        np.eye(2),
        np.eye(2),
        np.eye(2)
    ])

    assert not rank_instability(g_t), "Rank instability should not be detected."


def test_collapse_surface_index():
    # Collapse occurs at index 1
    g_t = np.array([
        np.eye(2),
        np.array([[1,0],[0,0]]),  # rank drop
        np.array([[1,0],[0,0]])
    ])

    idx = collapse_surface(g_t)
    assert idx == 1, "Collapse index should be 1."


def test_topology_signature_structure():
    g_t = np.array([
        np.eye(2),
        np.array([[1,0],[0,0]])
    ])

    sig = topology_signature(g_t)

    assert "ranks" in sig
    assert "collapse" in sig
    assert "collapse_index" in sig

    assert isinstance(sig["ranks"], list)
    assert isinstance(sig["collapse"], bool)
    assert sig["collapse_index"] in (None, 0, 1)
