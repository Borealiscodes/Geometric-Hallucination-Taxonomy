# 📘 06‑Compare‑Demo.md

Geometric Hallucination Taxonomy — Operator Comparison Demonstration

---

1. Overview

This notebook introduces the comparison layer of the Geometric Hallucination Taxonomy (GHT).  
You will:

- construct synthetic GHT signatures  
- construct baseline heuristic signatures (SGI, Γ, etc.)  
- compare curvature, spectral, holonomy, topology, and fusion operators  
- visualize differences  
- interpret divergence between GHT and baseline heuristics  

This layer is essential for:

- preprint experiments  
- operator‑equivalence analysis  
- empirical evaluation  
- diagnostic benchmarking  

Dream‑Lab pattern:  
concept → code → interpretation → visualization → provenance.

---

2. Setup Instructions

Run in VS Code
1. Open this .md file.  
2. Use “Markdown: Open Preview to the Side”.  
3. Run Python blocks directly.

Run in Jupyter
1. Create a new notebook.  
2. Copy each code block into cells.  
3. Execute sequentially.

---

3. Import comparison operators

`python
import numpy as np
import matplotlib.pyplot as plt

from toolkit.compare import (
    compare_curvature,
    compare_spectral,
    compare_holonomy,
    compare_topology,
    compare_fusion
)
`

---

4. Curvature comparison

We create a synthetic GHT curvature signature and a baseline SGI curvature proxy.

`python
K_ght = 1.2
K_baseline = 0.8

curvcmp = comparecurvature(Kght, Kbaseline)
curv_cmp
`

Interpretation:  
- Difference > 0 → GHT detects stronger curvature blowout  
- Ratio > 1 → GHT curvature expands faster than baseline  
This is typical when SGI underestimates geometric instability.

---

5. Spectral comparison

Construct synthetic spectral signatures.

`python
sig_ght = {
    "drift": np.array([1.0, 2.0]),
    "cascade_intensity": 4.0,
    "collapse": False
}

sig_baseline = {
    "drift": np.array([0.5, 1.0]),
    "cascade_intensity": 2.0,
    "collapse": False
}

speccmp = comparespectral(sigght, sigbaseline)
spec_cmp
`

Interpretation:  
GHT detects stronger spectral cascade → higher hallucination risk.

---

6. Holonomy comparison

`python
sig_ght = {
    "magnitude": 0.9,
    "direction": np.array([0.7, 0.7])
}

sig_baseline = {
    "magnitude": 0.3,
    "direction": np.array([1.0, 0.0])
}

holcmp = compareholonomy(sigght, sigbaseline)
hol_cmp
`

Interpretation:  
- GHT detects stronger semantic rotation  
- Direction difference shows divergent drift orientation  
This is typical when baseline heuristics ignore closed‑loop effects.

---

7. Topology comparison

`python
sig_ght = {
    "ranks": [3, 2, 2],
    "collapse": True,
    "collapse_index": 1
}

sig_baseline = {
    "ranks": [3, 3, 2],
    "collapse": False,
    "collapse_index": None
}

topcmp = comparetopology(sigght, sigbaseline)
top_cmp
`

Interpretation:  
GHT detects collapse earlier → more sensitive to manifold degeneracy.

---

8. Fusion‑field comparison

`python
sig_ght = {
    "intensity": 3.5,
    "nonlinear": np.array([0.8, -0.2])
}

sig_baseline = {
    "intensity": 1.0,
    "nonlinear": np.array([0.2, 0.0])
}

fuscmp = comparefusion(sigght, sigbaseline)
fus_cmp
`

Interpretation:  
GHT detects stronger nonlinear chimera formation → higher hybridization instability.

---

9. Visualizing comparison differences

`python
labels = ["Curvature", "Spectral", "Holonomy", "Topology", "Fusion"]
values = [
    curv_cmp["difference"],
    speccmp["cascadeintensity_difference"],
    holcmp["magnitudedifference"],
    topcmp["rankdifference"][1],  # collapse step
    fuscmp["intensitydifference"]
]

plt.figure(figsize=(10, 4))
plt.bar(labels, values)
plt.title("GHT vs Baseline Operator Differences")
plt.ylabel("Difference")
plt.grid(True, axis='y')
plt.show()
`

Interpretation:  
This bar plot shows how much stronger GHT detects instability compared to baseline heuristics.

---

10. Summary

This notebook demonstrated:

- curvature comparison  
- spectral comparison  
- holonomy comparison  
- topology comparison  
- fusion‑field comparison  
- visualization of operator differences  
- interpretation of diagnostic divergence  

This completes Notebook 06 and the entire GHT example‑notebook suite.

---

11. Provenance

Created by Borealis S. Hedling  
Geometric Hallucination Taxonomy — Comparison Layer Demonstration  
Generated on 22 October 2026, Dublin, Ireland.

---

