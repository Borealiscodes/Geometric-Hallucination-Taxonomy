import numpy as np

def spectral_drift(eigenvalues_t):
    """
    Compute the spectral drift (time derivative of eigenvalues) for
    hallucination cascade detection.

    Parameters
    ----------
    eigenvalues_t : np.ndarray
        Array of eigenvalue trajectories over time with shape (T, n),
        where T is the number of time steps and n is the number of eigenvalues.

    Returns
    -------
    np.ndarray
        Spectral drift dλ/dt for each eigenvalue across time.
    """
    eigenvalues_t = np.asarray(eigenvalues_t)
    return np.gradient(eigenvalues_t, axis=0)


def cascade_intensity(eigenvalues_t):
    """
    Compute a scalar intensity measure for spectral cascades.
    High intensity corresponds to eigenvalue explosions or rapid divergence.

    Parameters
    ----------
    eigenvalues_t : np.ndarray

    Returns
    -------
    float
        Scalar cascade intensity = max |dλ/dt|.
    """
    drift = spectral_drift(eigenvalues_t)
    return float(np.max(np.abs(drift)))


def spectral_collapse(eigenvalues_t, threshold=1e-6):
    """
    Detect spectral collapse (rank loss) by checking for eigenvalues
    approaching zero.

    Parameters
    ----------
    eigenvalues_t : np.ndarray
    threshold : float
        Collapse threshold for eigenvalues.

    Returns
    -------
    bool
        True if collapse detected, False otherwise.
    """
    eigenvalues_t = np.asarray(eigenvalues_t)
    return bool(np.any(np.abs(eigenvalues_t) < threshold))


def spectral_signature(eigenvalues_t):
    """
    Produce a structured spectral signature summarizing:
    - drift magnitude
    - cascade intensity
    - collapse flag

    Parameters
    ----------
    eigenvalues_t : np.ndarray

    Returns
    -------
    dict
        {
            "drift": np.ndarray,
            "cascade_intensity": float,
            "collapse": bool
        }
    """
    drift = spectral_drift(eigenvalues_t)
    return {
        "drift": drift,
        "cascade_intensity": float(np.max(np.abs(drift))),
        "collapse": spectral_collapse(eigenvalues_t)
    }
