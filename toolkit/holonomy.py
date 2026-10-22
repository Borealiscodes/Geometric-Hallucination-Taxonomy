import numpy as np

def parallel_transport_step(v, connection):
    """
    Perform a single parallel transport step using a connection matrix.

    Parameters
    ----------
    v : np.ndarray
        Tangent vector to be transported.
    connection : np.ndarray
        Connection matrix Γ representing infinitesimal transport.

    Returns
    -------
    np.ndarray
        Updated tangent vector after transport.
    """
    v = np.asarray(v)
    return v - connection @ v


def parallel_transport_loop(v0, connections):
    """
    Perform parallel transport around a closed loop γ using a sequence
    of connection matrices.

    Parameters
    ----------
    v0 : np.ndarray
        Initial tangent vector at γ(0).
    connections : list of np.ndarray
        Sequence of connection matrices Γ_k along the loop.

    Returns
    -------
    np.ndarray
        Transported vector P_γ(v0).
    """
    v = np.asarray(v0)
    for Γ in connections:
        v = parallel_transport_step(v, Γ)
    return v


def holonomy_operator(v0, connections):
    """
    Compute the holonomy operator H = P_γ - I applied to v0.

    Parameters
    ----------
    v0 : np.ndarray
        Initial tangent vector.
    connections : list of np.ndarray
        Connection matrices along the loop.

    Returns
    -------
    np.ndarray
        Holonomy drift vector H(v0).
    """
    transported = parallel_transport_loop(v0, connections)
    return transported - np.asarray(v0)


def holonomy_magnitude(v0, connections):
    """
    Compute the magnitude of holonomy drift, indicating semantic rotation.

    Parameters
    ----------
    v0 : np.ndarray
    connections : list of np.ndarray

    Returns
    -------
    float
        ||H(v0)||₂
    """
    H = holonomy_operator(v0, connections)
    return float(np.linalg.norm(H))


def holonomy_signature(v0, connections):
    """
    Produce a structured holonomy signature summarizing:
    - drift vector
    - drift magnitude
    - rotational direction (unit vector)

    Parameters
    ----------
    v0 : np.ndarray
    connections : list of np.ndarray

    Returns
    -------
    dict
        {
            "drift": np.ndarray,
            "magnitude": float,
            "direction": np.ndarray
        }
    """
    H = holonomy_operator(v0, connections)
    mag = np.linalg.norm(H)
    direction = H / (mag + 1e-8)

    return {
        "drift": H,
        "magnitude": float(mag),
        "direction": direction
    }
