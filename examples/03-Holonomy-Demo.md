# 📘 03‑Holonomy‑Demo.md

Geometric Hallucination Taxonomy — Holonomy Drift Demonstration

---

1. Overview

This notebook introduces the holonomy operator of the Geometric Hallucination Taxonomy (GHT).  
You will:

- construct simple connection matrices  
- perform parallel transport  
- compute holonomy drift  
- visualize semantic rotation  
- interpret drift magnitude and direction  
- explore closed‑loop transport instability  

Holonomy captures semantic rotation — how meaning changes when transported around a loop in latent space.

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

3. Import holonomy operators

`python
import numpy as np
import matplotlib.pyplot as plt

from toolkit.holonomy import (
    paralleltransportstep,
    paralleltransportloop,
    holonomy_operator,
    holonomy_magnitude,
    holonomy_signature
)
`

---

4. Basic parallel transport

We begin with a simple connection matrix that rotates vectors slightly.

`python
v0 = np.array([1.0, 0.0])

Gamma = np.array([
    [0.0, -0.1],
    [0.1,  0.0]
])

v1 = paralleltransportstep(v0, Gamma)
v1
`

Interpretation:  
This Γ induces a tiny rotation.  
Parallel transport subtracts Γv → a small semantic twist.

---

5. Transport around a closed loop

We simulate a loop using multiple small rotations.

`python
Gammas = [Gamma for _ in range(20)]  # 20 small rotations

vT = paralleltransportloop(v0, Gammas)
vT
`

Interpretation:  
Even though each step is tiny, the cumulative effect is noticeable.  
This is the essence of holonomy: transport around a loop does not return you to the same semantic state.

---

6. Compute holonomy drift

`python
H = holonomy_operator(v0, Gammas)
H
`

Interpretation:  
Holonomy drift = transported vector − original vector.  
This measures semantic rotation caused by looping through latent space.

---

7. Holonomy magnitude

`python
mag = holonomy_magnitude(v0, Gammas)
mag
`

Interpretation:  
Magnitude quantifies how far the meaning has rotated.  
Large magnitude → strong semantic drift → hallucination risk.

---

8. Holonomy signature

`python
sig = holonomy_signature(v0, Gammas)
sig
`

You get:

- drift — the holonomy vector  
- magnitude — scalar drift size  
- direction — normalized drift direction  

This is the diagnostic used in the GHT operator suite.

---

9. Visualize holonomy drift direction

`python
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, sig["direction"][0], sig["direction"][1],
           angles='xy', scale_units='xy', scale=1, color='red')

plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.title("Holonomy Drift Direction")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
`

Interpretation:  
The arrow shows the semantic rotation direction induced by the loop.  
Different loops → different drift directions → different hallucination signatures.

---

10. Oscillatory holonomy regime

We now alternate connection matrices to simulate semantic breathing.

`python
Gamma_pos = np.array([[0.0, -0.2],
                      [0.2,  0.0]])

Gamma_neg = np.array([[0.0,  0.2],
                      [-0.2, 0.0]])

Gammasosc = [Gammapos if i % 2 == 0 else Gamma_neg for i in range(40)]

sigosc = holonomysignature(v0, Gammas_osc)
sig_osc
`

Interpretation:  
Oscillatory holonomy → alternating rotation → dream‑logic drift.

---

11. Summary

This notebook demonstrated:

- parallel transport  
- holonomy drift  
- drift magnitude and direction  
- closed‑loop semantic rotation  
- oscillatory holonomy regimes  
- visualization of holonomy direction  

This completes Notebook 03 of the GHT toolkit.

---

12. Provenance

Created by Borealis S. Hedling  
Geometric Hallucination Taxonomy — Holonomy Operator Demonstration  
Generated on 22 October 2026, Dublin, Ireland.

---

