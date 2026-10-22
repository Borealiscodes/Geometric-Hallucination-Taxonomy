# 📘 02‑Spectral‑Demo.md

Geometric Hallucination Taxonomy — Spectral Operator Demonstration

---

1. Overview

This notebook introduces the spectral operator suite of the Geometric Hallucination Taxonomy (GHT).  
You will:

- construct eigenvalue trajectories  
- compute spectral drift  
- measure cascade intensity  
- detect spectral collapse  
- visualize instability patterns  
- interpret spectral blowout vs collapse vs oscillatory regimes  

This follows the Dream Lab pattern:  
concept → code → interpretation → visualization → provenance.

---

2. Setup Instructions

Run in VS Code
1. Open this .md file.  
2. Press Ctrl+Shift+P → “Markdown: Open Preview to the Side”.  
3. Run Python code blocks directly.

Run in Jupyter
1. Create a new notebook.  
2. Copy each code block into cells.  
3. Execute sequentially.

---

3. Import spectral operators

`python
import numpy as np
import matplotlib.pyplot as plt

from toolkit.spectral import (
    spectral_drift,
    cascade_intensity,
    spectral_collapse,
    spectral_signature
)
`

---

4. Construct simple eigenvalue trajectories

We begin with a linear growth trajectory, which produces clean, interpretable drift.

`python
eigenvalues_t = np.array([
    [1.0, 2.0],
    [2.0, 3.0],
    [3.0, 4.0]
])

drift = spectraldrift(eigenvaluest)
drift
`

Interpretation:  
- Drift is constant → stable linear expansion  
- No cascade → no hallucination onset  
- This is a baseline regime

---

5. Visualize drift over time

`python
plt.figure(figsize=(10, 4))
plt.plot(drift[:, 0], label="λ₁ drift")
plt.plot(drift[:, 1], label="λ₂ drift")
plt.title("Spectral Drift Over Time")
plt.xlabel("Time step")
plt.ylabel("dλ/dt")
plt.grid(True)
plt.legend()
plt.show()
`

Interpretation:  
Flat drift curves → stable spectral geometry.

---

6. Spectral cascade regime

Now we create a rapidly diverging eigenvalue trajectory, characteristic of spectral blowout hallucinations.

`python
eigenvalues_cascade = np.array([
    [1.0],
    [3.0],
    [7.0],
    [15.0],
    [31.0]
])

driftcascade = spectraldrift(eigenvalues_cascade)
intensitycascade = cascadeintensity(eigenvalues_cascade)

driftcascade, intensitycascade
`

Interpretation:  
- Drift grows exponentially  
- Cascade intensity is large  
- This corresponds to spectral blowout → runaway semantic expansion

---

7. Plot cascade drift

`python
plt.figure(figsize=(10, 4))
plt.plot(drift_cascade[:, 0])
plt.title("Spectral Cascade Drift")
plt.xlabel("Time step")
plt.ylabel("dλ/dt")
plt.grid(True)
plt.show()
`

Interpretation:  
The curve steepens → instability → hallucination onset.

---

8. Spectral collapse regime

Collapse occurs when eigenvalues approach zero → rank loss → semantic contraction.

`python
eigenvalues_collapse = np.array([
    [1.0, 0.5],
    [0.8, 0.1],
    [0.7, 0.00001]
])

collapseflag = spectralcollapse(eigenvalues_collapse)
collapse_flag
`

Interpretation:  
True → collapse detected  
This corresponds to semantic implosion → collapse hallucinations.

---

9. Oscillatory spectral regime

Oscillatory eigenvalues correspond to dream‑logic spectral breathing.

`python
t = np.linspace(0, 2*np.pi, 200)
eigenvalues_osc = np.stack([np.sin(t)], axis=1)

driftosc = spectraldrift(eigenvalues_osc)
`

`python
plt.figure(figsize=(10, 4))
plt.plot(drift_osc[:, 0])
plt.title("Oscillatory Spectral Drift")
plt.xlabel("Time step")
plt.ylabel("dλ/dt")
plt.grid(True)
plt.show()
`

Interpretation:  
Drift oscillates → alternating expansion and contraction → unstable semantic breathing.

---

10. Full spectral signature

`python
sig = spectralsignature(eigenvaluescascade)
sig
`

Interpretation:  
The signature bundles:

- drift  
- cascade intensity  
- collapse flag  

This is the spectral diagnostic used in the GHT operator suite.

---

11. Summary

This notebook demonstrated:

- spectral drift  
- cascade intensity  
- collapse detection  
- oscillatory spectral regimes  
- visualization of spectral instability  
- interpretation of spectral hallucination classes  

This completes Notebook 02 of the GHT toolkit.

---

12. Provenance

Created by Borealis S. Hedling  
Geometric Hallucination Taxonomy — Spectral Operator Demonstration  
Generated on 22 October 2026, Dublin, Ireland.

---

