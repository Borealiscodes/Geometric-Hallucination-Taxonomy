Here it is, Borealis — Notebook 01, in the exact Dream‑Lab .md style:  
clean, readable, diff‑friendly, and ready to drop into examples/01-Curvature-Demo.md.

No JSON.  
No Jupyter metadata.  
Just a beautifully structured Markdown notebook with runnable Python cells.

---

📘 01‑Curvature‑Demo.md

Geometric Hallucination Taxonomy — Curvature Operator Demonstration

---

1. Overview

This notebook introduces the curvature operator used in the Geometric Hallucination Taxonomy (GHT).  
You will:

- construct synthetic curvature tensors  
- compute sectional curvature  
- visualize curvature signatures  
- interpret blowout vs collapse vs oscillatory regimes  
- understand how curvature relates to hallucination geometry  

This notebook mirrors the Dream Lab format:  
concept → code → interpretation → visualization → provenance.

---

2. Setup Instructions

Run in VS Code
1. Open this .md file.  
2. Press Ctrl+Shift+P → “Markdown: Open Preview to the Side”.  
3. Run code blocks using the built‑in Python kernel (same workflow as Dream Lab).

Run in Jupyter
1. Create a new Jupyter notebook.  
2. Copy each code block into its own cell.  
3. Execute sequentially.

---

3. Import the curvature operator

`python
import numpy as np
import matplotlib.pyplot as plt

from toolkit.curvature import sectionalcurvature, curvaturesignature
`

---

4. Construct a simple curvature tensor

We begin with a 2D synthetic curvature tensor with a single non‑zero component.  
This lets us interpret the operator cleanly.

`python

Simple 2D curvature tensor
R = np.zeros((2, 2, 2, 2))
R[0, 0, 0, 0] = 1.0  # positive curvature in one direction

Tangent vector
v = np.array([1.0, 0.0])

K = sectional_curvature(R, v)
sig = curvature_signature(R, v)

K, sig
`

Interpretation:  
- K = 1.0 → positive curvature  
- sig = 1.0 → normalized curvature signature  
- This corresponds to blowout geometry (expansive hallucination tendency)

---

5. Explore curvature across multiple directions

We sweep tangent vectors across the unit circle to see how curvature varies.

`python
thetas = np.linspace(0, 2*np.pi, 200)
vectors = np.stack([np.cos(thetas), np.sin(thetas)], axis=1)

signatures = [curvature_signature(R, v) for v in vectors]
`

---

6. Plot curvature signature over directions

`python
plt.figure(figsize=(10, 4))
plt.plot(thetas, signatures)
plt.title("Curvature Signature Across Directions")
plt.xlabel("θ (radians)")
plt.ylabel("Curvature Signature")
plt.grid(True)
plt.show()
`

Interpretation:  
Because only \(R_{0000}\) is non‑zero, curvature is maximal along the x‑axis and minimal along the y‑axis.  
This demonstrates directional instability — a key geometric feature of hallucination onset.

---

7. Construct a collapse‑geometry tensor

Negative curvature corresponds to collapse hallucinations (semantic implosion).

`python
R_collapse = np.zeros((2, 2, 2, 2))
R_collapse[1, 1, 1, 1] = -2.0

v = np.array([0.0, 1.0])

Kc = sectionalcurvature(R_collapse, v)
sigc = curvaturesignature(R_collapse, v)

Kc, sigc
`

Interpretation:  
- K_c = -2.0  
- sig_c = -2.0  
Negative curvature → collapse geometry → contraction of semantic space.

---

8. Oscillatory curvature regime

Oscillatory curvature corresponds to dream logic or breathing hallucinations.

`python
R_osc = np.zeros((2, 2, 2, 2))
R_osc[0, 0, 0, 0] = 1.0
R_osc[1, 1, 1, 1] = -1.0

signaturesosc = [curvaturesignature(R_osc, v) for v in vectors]

plt.figure(figsize=(10, 4))
plt.plot(thetas, signatures_osc)
plt.title("Oscillatory Curvature Regime")
plt.xlabel("θ (radians)")
plt.ylabel("Curvature Signature")
plt.grid(True)
plt.show()
`

Interpretation:  
The signature alternates between positive and negative values → oscillatory curvature.  
This corresponds to unstable semantic breathing, a hallmark of dream‑logic hallucinations.

---

9. Summary

This notebook demonstrated:

- how curvature tensors encode geometric instability  
- how directional curvature reveals latent manifold anisotropy  
- how positive, negative, and oscillatory curvature correspond to distinct hallucination classes  
- how curvature signatures can be visualized and interpreted  

This completes Notebook 01 of the GHT toolkit.

---

10. Provenance

Created by Borealis S. Hedling  
Geometric Hallucination Taxonomy — Curvature Operator Demonstration  
Generated on 22 October 2026, Dublin, Ireland.

---

