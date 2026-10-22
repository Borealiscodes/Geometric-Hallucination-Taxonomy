import numpy as np

def compare_curvature(K_ght, K_baseline):
    """
    Compare GHT curvature signature against a baseline curvature heuristic.

    Parameters
    ----------
    K_ght : float
        GHT sectional curvature signature.
    K_baseline : float
        Baseline curvature measure (e.g., SGI curvature proxy).

    Returns
    -------
    dict
        {
            "ght": float,
            "baseline": float,
            "difference": float,
            "ratio": float
        }
    """
    return {
        "ght": float(K_ght),
        "baseline": float(K_baseline),
        "difference": float(K_ght - K_baseline),
        "ratio": float((K_ght + 1e-8) / (K_baseline + 1e-8))
    }


def compare_spectral(sig_ght, sig_baseline):
    """
    Compare spectral signatures (drift, cascade intensity, collapse flag).

    Parameters
    ----------
    sig_ght : dict
    sig_baseline : dict

    Returns
    -------
    dict
        Structured comparison of spectral instability.
    """
    return {
        "drift_difference": sig_ght["drift"] - sig_baseline["drift"],
        "cascade_intensity_difference":
            float(sig_ght["cascade_intensity"] - sig_baseline["cascade_intensity"]),
        "collapse_comparison":
            (sig_ght["collapse"], sig_baseline["collapse"])
    }


def compare_holonomy(sig_ght, sig_baseline):
    """
    Compare holonomy drift magnitude and direction.

    Parameters
    ----------
    sig_ght : dict
    sig_baseline : dict

    Returns
    -------
    dict
        {
            "magnitude_difference": float,
            "direction_difference": np.ndarray
        }
    """
    return {
        "magnitude_difference":
            float(sig_ght["magnitude"] - sig_baseline["magnitude"]),
        "direction_difference":
            sig_ght["direction"] - sig_baseline["direction"]
    }


def compare_topology(sig_ght, sig_baseline):
    """
    Compare rank trajectories and collapse indices.

    Parameters
    ----------
    sig_ght : dict
    sig_baseline : dict

    Returns
    -------
    dict
        {
            "rank_difference": list,
            "collapse_comparison": (bool, bool),
            "collapse_index_difference": int or None
        }
    """
    ranks_ght = sig_ght["ranks"]
    ranks_baseline = sig_baseline["ranks"]

    rank_diff = [r_g - r_b for r_g, r_b in zip(ranks_ght, ranks_baseline)]

    return {
        "rank_difference": rank_diff,
        "collapse_comparison": (sig_ght["collapse"], sig_baseline["collapse"]),
        "collapse_index_difference":
            (sig_ght["collapse_index"], sig_baseline["collapse_index"])
    }


def compare_fusion(sig_ght, sig_baseline):
    """
    Compare fusion-field intensity and nonlinear interaction.

    Parameters
    ----------
    sig_ght : dict
    sig_baseline : dict

    Returns
    -------
    dict
        {
            "intensity_difference": float,
            "nonlinear_difference": np.ndarray
        }
    """
    return {
        "intensity_difference":
            float(sig_ght["intensity"] - sig_baseline["intensity"]),
        "nonlinear_difference":
            sig_ght["nonlinear"] - sig_baseline["nonlinear"]
    }
