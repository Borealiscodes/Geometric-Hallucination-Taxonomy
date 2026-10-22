import numpy as np

def sectional_curvature(R, v):
    """
    Compute sectional curvature signature for hallucination detection.

    Parameters
    ----------
    R : np.ndarray
        Riemann curvature tensor with shape (n, n, n, n).
    v : np.ndarray
        Tangent vector representing latent trajectory direction.

    Returns
    -------
    float
        Sectional curvature K(v) = R_{ijkl} v^i v^j v^k v^l
    """
    v = np.asarray(v)
    return np.einsum('ijkl,i,j,k,l->', R, v, v, v, v)


def curvature_signature(R, v):
    """
    Returns a normalized curvature signature for diagnostic pipelines.

    Positive → blowout
    Negative → collapse
    Oscillatory → breathing / dream logic

    Parameters
    ----------
    R : np.ndarray
    v : np.ndarray

    Returns
    -------
    float
        Normalized curvature value.
    """
    K = sectional_curvature(R, v)
    return float(K / (np.linalg.norm(v)**4 + 1e-8))
