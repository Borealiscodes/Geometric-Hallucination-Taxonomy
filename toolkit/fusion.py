import numpy as np

def nonlinear_interaction(x, y):
    """
    Nonlinear interaction term φ(x, y) capturing chimera blending.
    Uses tanh(x * y) as a smooth, bounded nonlinearity.

    Parameters
    ----------
    x : np.ndarray
    y : np.ndarray

    Returns
    -------
    np.ndarray
        Nonlinear interaction φ(x, y).
    """
    x = np.asarray(x)
    y = np.asarray(y)
    return np.tanh(x * y)


def fusion_field(x, y, alpha=1.0, beta=1.0, gamma=1.0):
    """
    Compute the fusion-field operator:
        F(x, y) = αx + βy + γ φ(x, y)

    Parameters
    ----------
    x : np.ndarray
    y : np.ndarray
    alpha : float
    beta : float
    gamma : float

    Returns
    -------
    np.ndarray
        Fusion-field output representing blended latent concepts.
    """
    x = np.asarray(x)
    y = np.asarray(y)
    phi = nonlinear_interaction(x, y)
    return alpha * x + beta * y + gamma * phi


def fusion_intensity(x, y, gamma=1.0):
    """
    Measure the intensity of nonlinear blending.

    Parameters
    ----------
    x : np.ndarray
    y : np.ndarray
    gamma : float

    Returns
    -------
    float
        ||γ φ(x, y)||₂
    """
    phi = nonlinear_interaction(x, y)
    return float(np.linalg.norm(gamma * phi))


def fusion_signature(x, y, alpha=1.0, beta=1.0, gamma=1.0):
    """
    Produce a structured fusion-field signature summarizing:
    - linear blend
    - nonlinear interaction
    - fusion intensity
    - full fusion output

    Parameters
    ----------
    x : np.ndarray
    y : np.ndarray

    Returns
    -------
    dict
        {
            "linear": αx + βy,
            "nonlinear": φ(x, y),
            "intensity": float,
            "fusion": F(x, y)
        }
    """
    x = np.asarray(x)
    y = np.asarray(y)

    linear = alpha * x + beta * y
    nonlinear = nonlinear_interaction(x, y)
    intensity = float(np.linalg.norm(gamma * nonlinear))
    fusion = fusion_field(x, y, alpha, beta, gamma)

    return {
        "linear": linear,
        "nonlinear": nonlinear,
        "intensity": intensity,
        "fusion": fusion
    }
