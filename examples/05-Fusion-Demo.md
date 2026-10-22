# 📘 05‑Fusion‑Demo.md

Geometric Hallucination Taxonomy — Fusion‑Field Operator Demonstration

---

1. Overview

This notebook introduces the fusion‑field operator of the Geometric Hallucination Taxonomy (GHT).  
You will:

- compute nonlinear interaction terms  
- blend latent vectors using the fusion‑field operator  
- measure fusion intensity  
- visualize nonlinear chimera formation  
- interpret hybridization vs collapse vs blowout blending regimes  

Fusion‑fields capture nonlinear semantic blending — when two concepts merge into a chimera.

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

3. Import fusion operators

`python
import numpy as np
import matplotlib.pyplot as plt

from toolkit.fusion import (
    nonlinear_interaction,
    fusion_field,
    fusion_intensity,
    fusion_signature
)
`

---

4. Basic nonlinear interaction

The nonlinear term is:

\[
\phi(x,y) = \tanh(x \cdot y)
\]

This produces smooth, bounded nonlinear blending.

`python
x = np.array([1.0, 2.0])
y = np.array([3.0, -1.0])

phi = nonlinear_interaction(x, y)
phi
`

Interpretation:  
- Positive product → positive nonlinear boost  
- Negative product → negative nonlinear suppression  
- This is the “semantic interference pattern” between concepts

---

5. Pure linear blend

Set γ = 0 to isolate the linear component.

`python
x = np.array([1.0, 0.0])
y = np.array([0.0, 1.0])

Flinear = fusionfield(x, y, alpha=1.0, beta=1.0, gamma=0.0)
F_linear
`

Interpretation:  
Linear blend = simple addition → no chimera formation.

---

6. Nonlinear fusion‑field blend

Now activate γ to introduce nonlinear interaction.

`python
x = np.array([1.0])
y = np.array([2.0])

F = fusion_field(x, y, alpha=1.0, beta=1.0, gamma=1.0)
F
`

Interpretation:  
Fusion = linear blend + nonlinear chimera term  
This is the core of hybridization geometry.

---

7. Fusion intensity

Fusion intensity measures the strength of nonlinear blending:

`python
x = np.array([1.0, -1.0])
y = np.array([2.0, 3.0])

intensity = fusion_intensity(x, y)
intensity
`

Interpretation:  
Higher intensity → stronger chimera formation → higher hallucination risk.

---

8. Visualize nonlinear interaction surface

We sweep x and y across a grid to visualize the nonlinear interaction.

`python
xs = np.linspace(-3, 3, 200)
ys = np.linspace(-3, 3, 200)

X, Y = np.meshgrid(xs, ys)
Phi = np.tanh(X * Y)

plt.figure(figsize=(8, 6))
plt.imshow(Phi, extent=[-3, 3, -3, 3], origin='lower', cmap='coolwarm')
plt.colorbar(label="φ(x,y) = tanh(x·y)")
plt.title("Nonlinear Interaction Surface")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
`

Interpretation:  
- Quadrants with same sign → positive chimera boost  
- Opposite signs → suppressive blending  
- Center → neutral interaction  
This is the “semantic fusion landscape.”

---

9. Full fusion signature

`python
sig = fusion_signature(np.array([1.0, 2.0]), np.array([3.0, -1.0]))
sig
`

You get:

- linear — αx + βy  
- nonlinear — φ(x,y)  
- intensity — ||γφ||₂  
- fusion — full fusion‑field output  

This is the diagnostic used in the GHT operator suite.

---

10. Oscillatory fusion regime

Oscillatory blending corresponds to unstable chimera formation.

`python
t = np.linspace(0, 2*np.pi, 200)
x_t = np.sin(t)
y_t = np.cos(t)

Phit = np.tanh(xt * y_t)

plt.figure(figsize=(10, 4))
plt.plot(t, Phi_t)
plt.title("Oscillatory Nonlinear Interaction")
plt.xlabel("t")
plt.ylabel("φ(x(t), y(t))")
plt.grid(True)
plt.show()
`

Interpretation:  
Oscillatory φ → alternating constructive/destructive blending → dream‑logic hybridization.

---

11. Summary

This notebook demonstrated:

- nonlinear interaction  
- linear vs nonlinear blending  
- fusion‑field computation  
- fusion intensity  
- interaction surface visualization  
- oscillatory chimera formation  
- interpretation of fusion‑based hallucination classes  

This completes Notebook 05 of the GHT toolkit.

---

12. Provenance

Created by Borealis S. Hedling  
Geometric Hallucination Taxonomy — Fusion‑Field Operator Demonstration  
Generated on 22 October 2026, Dublin, Ireland.

---

