# 📘 04‑Topology‑Demo.md

Geometric Hallucination Taxonomy — Topological Instability Demonstration

---

1. Overview

This notebook introduces the topological instability operator of the Geometric Hallucination Taxonomy (GHT).  
You will:

- compute stabilized metric rank  
- detect rank instability across time  
- identify collapse surfaces  
- visualize rank trajectories  
- interpret collapse vs stable vs oscillatory topological regimes  

Topology captures manifold degeneracy — when the latent space loses dimensionality and semantic structure collapses.

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

3. Import topology operators

`python
import numpy as np
import matplotlib.pyplot as plt

from toolkit.topology import (
    metric_rank,
    rank_instability,
    collapse_surface,
    topology_signature
)
`

---

4. Compute metric rank

We begin with a simple metric tensor.

`python
g = np.eye(3)
metric_rank(g)
`

Interpretation:  
Rank = 3 → full‑dimensional manifold → stable geometry.

---

5. Near‑singular metric

A metric with a tiny eigenvalue still stabilizes to full rank.

`python
g_singular = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1e-6, 0.0],
    [0.0, 0.0, 1.0]
])

metricrank(gsingular)
`

Interpretation:  
Stabilization prevents false collapse detection.  
This is crucial for noisy latent manifolds.

---

6. Rank instability across time

We now simulate a metric trajectory with a rank drop.

`python
g_t = np.array([
    np.eye(3),
    np.array([[1,0,0],[0,1,0],[0,0,0]]),  # rank 2
    np.array([[1,0,0],[0,1,0],[0,0,0]])   # rank 2
])

instability = rankinstability(gt)
instability
`

Interpretation:  
True → rank instability detected → topological collapse.

---

7. Identify collapse surface

`python
collapseidx = collapsesurface(g_t)
collapse_idx
`

Interpretation:  
Collapse occurs at index 1 → the moment the manifold loses dimensionality.

---

8. Visualize rank trajectory

`python
ranks = [metricrank(g) for g in gt]

plt.figure(figsize=(10, 4))
plt.plot(ranks, marker='o')
plt.title("Metric Rank Over Time")
plt.xlabel("Time step")
plt.ylabel("Rank")
plt.grid(True)
plt.show()
`

Interpretation:  
Rank drops from 3 → 2 → topological collapse.  
This is the geometric signature of semantic implosion.

---

9. Oscillatory topology regime

Oscillatory rank corresponds to unstable manifold breathing.

`python
g_osc = [
    np.eye(2),
    np.array([[1,0],[0,0]]),
    np.eye(2),
    np.array([[1,0],[0,0]])
]

ranksosc = [metricrank(g) for g in g_osc]

plt.figure(figsize=(10, 4))
plt.plot(ranks_osc, marker='o')
plt.title("Oscillatory Rank Regime")
plt.xlabel("Time step")
plt.ylabel("Rank")
plt.grid(True)
plt.show()
`

Interpretation:  
Rank alternates → topological breathing → dream‑logic instability.

---

10. Full topology signature

`python
sig = topologysignature(gt)
sig
`

You get:

- ranks — rank trajectory  
- collapse — collapse flag  
- collapse_index — where collapse occurs  

This is the topological diagnostic used in the GHT operator suite.

---

11. Summary

This notebook demonstrated:

- stabilized metric rank  
- rank instability detection  
- collapse‑surface identification  
- oscillatory topological regimes  
- visualization of manifold degeneracy  
- interpretation of topological hallucination classes  

This completes Notebook 04 of the GHT toolkit.

---

12. Provenance

Created by Borealis S. Hedling  
Geometric Hallucination Taxonomy — Topological Instability Demonstration  
Generated on 22 October 2026, Dublin, Ireland.

---

