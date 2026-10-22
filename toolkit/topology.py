import numpy as np

def metric_rank(g, epsilon=1e-6):
    """
    Compute the stabilized rank of the metric tensor g.
    This detects topological collapse surfaces where rank drops.

    Parameters
    ----------
    g : np.ndarray
        Metric tensor with shape (n, n).
    epsilon : float
        Stabilization constant to avoid numerical singularities.

    Returns
    -------
    int
        Rank of (g + εI).
    """
    g = np.asarray(g)
    stabilized = g + epsilon * np.eye(g.shape[0])
    return int(np.linalg.matrix_rank(stabilized))


def rank_instability(g_t, epsilon=1e-6):
    """
    Detect rank instability across a trajectory of metric tensors g(t).

    Parameters
    ----------
    g_t : np.ndarray
        Array of metric tensors over time with shape (T, n, n).
    epsilon : float

    Returns
    -------
    bool
        True if any rank drop is detected.
    """
    g_t = np.asarray(g_t)
    ranks = [metric_rank(g, epsilon) for g in g_t]
    return any(ranks[t] < ranks[t - 1] for t in range(1, len(ranks)))


def collapse_surface(g_t, epsilon=1e-6):
    """
    Identify the time index where topological collapse occurs.

    Parameters
    ----------
    g_t : np.ndarray

    Returns
    -------
    int or None
        Index of collapse event, or None if no collapse detected.
    """
    g_t = np.asarray(g_t)
    ranks = [metric_rank(g, epsilon) for g in g_t]

    for t in range(1, len(ranks)):
        if ranks[t] < ranks[t - 1]:
            return t
    return None


def topology_signature(g_t, epsilon=1e-6):
    """
    Produce a structured topological instability signature summarizing:
    - rank trajectory
    - collapse flag
    - collapse index

    Parameters
    ----------
    g_t : np.ndarray

    Returns
    -------
    dict
        {
            "ranks": list[int],
            "collapse": bool,
            "collapse_index": int or None
        }
    """
    g_t = np.asarray(g_t)
    ranks = [metric_rank(g, epsilon) for g in g_t]
    collapse = rank_instability(g_t, epsilon)
    collapse_index = collapse_surface(g_t, epsilon)

    return {
        "ranks": ranks,
        "collapse": collapse,
        "collapse_index": collapse_index
    }
