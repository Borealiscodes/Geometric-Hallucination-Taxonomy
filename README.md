# 📘 Geometric Hallucination Taxonomy (GHT)

A Structural, Spectral, Holonomy‑Based, and Topological Framework for Diagnosing AI Hallucinations

---

🌌 Overview

The Geometric Hallucination Taxonomy (GHT) is a research framework and accompanying Python toolkit designed to classify, diagnose, and analyze hallucinations in modern AI systems using manifold‑level geometry rather than traditional embedding‑space heuristics.

Where prior work focuses on semantic plausibility or angular deviation (e.g., SGI, Γ), GHT introduces a five‑operator geometric spine:

- Curvature tensor \(R_{ijkl}\)  
- Spectral derivative \(\Delta_\lambda\)  
- Holonomy operator \(H = P_\gamma - I\)  
- Topological rank operator \(\tau\)  
- Fusion‑field operator \(F(x,y)\)

These operators allow hallucinations to be treated as geometric instabilities in latent space—capturing phenomena such as curvature blowout, spectral cascades, holonomy drift, collapse surfaces, and non‑linear fusion spikes.

This repository contains:

- 📄 A unified preprint (preprint.md)  
- 📐 A formal mathematical appendix (math_spine.tex)  
- 🧮 A Python toolkit implementing geometric diagnostic operators  
- 📚 Lean formalization scaffolding  
- 🖼️ Figures illustrating geometric phenomena  

---

📁 Repository Structure

`
<pre> 

GeometricHallucinationTaxonomy/
│
├── README.md
│
├── preprint/
│   ├── preprint.md                 # Unified manuscript
│   ├── math_spine.tex              # Formal math appendix
│   ├── lean_formalization/
│   │   ├── HallucinationGeometry.lean
│   │   └── Operators.lean
│   └── figures/
│       ├── spectral_cascade.png
│       ├── holonomy_loop.png
│       ├── collapse_surface.png
│       └── taxonomy_overview.png
│
├── toolkit/
│   ├── curvature.py
│   ├── spectral.py
│   ├── holonomy.py
│   ├── topology.py
│   ├── fusion.py
│   └── compare.py
│
├── tests/
│   ├── test_curvature.py
│   ├── test_spectral.py
│   ├── test_holonomy.py
│   ├── test_topology.py
│   └── test_fusion.py
│
└── examples/
    ├── curvature_demo.ipynb
    ├── spectral_demo.ipynb
    ├── holonomy_demo.ipynb
    ├── topology_demo.ipynb
    └── fusion_demo.ipynb
`

</pre>
---

🧠 Scientific Motivation

Modern AI hallucinations are not random errors—they are geometric failures in the latent manifold.  
GHT formalizes these failures using differential geometry, spectral analysis, and topological diagnostics.

Five Hallucination Classes

| Class | Operator | Phenomenology |
|-------|----------|----------------|
| Curvature‑Driven (CDH) | \(R_{ijkl}\) | bending, oscillation, semantic blowout |
| Spectral Cascade (SCH) | \(\Delta_\lambda\) | eigenvalue explosions, fractal recursion |
| Holonomy Drift (HDH) | \(H = P_\gamma - I\) | vortex logic, rotational drift |
| Topological Instability (TIH) | \(\tau\) | collapse surfaces, rank loss |
| Fusion‑Field (FFH) | \(F(x,y)\) | chimera concepts, hybridization |

These operators allow hallucinations to be measured, classified, and diagnosed with mathematical precision.

---

🧮 Mathematical Foundations (Brief)

Curvature Tensor
Hallucinations emerge when sectional curvature spikes:

\[
K = R_{ijkl} v^i v^j v^k v^l
\]

Spectral Derivative
Spectral cascades occur when eigenvalues destabilize:

\[
\Delta\lambda = \frac{d\lambdai}{dt}
\]

Holonomy Operator
Semantic drift arises from non‑trivial holonomy:

\[
H = P_\gamma - I
\]

Topological Rank Operator
Collapse surfaces appear when the metric degenerates:

\[
\tau = \text{rank}(g + \epsilon I)
\]

Fusion‑Field Operator
Non‑linear blending is captured by:

\[
F(x,y) = \alpha x + \beta y + \gamma \phi(x,y)
\]

Full derivations are in math_spine.tex.

---

🧰 Python Toolkit

Each operator has a corresponding module:

Curvature
`python
def sectional_curvature(R, v):
    return np.einsum('ijkl,i,j,k,l->', R, v, v, v, v)
`

Spectral
`python
def spectraldrift(eigenvaluest):
    return np.gradient(eigenvalues_t)
`

Holonomy
`python
def holonomy(P_gamma):
    return Pgamma - np.eye(Pgamma.shape[0])
`

Topology
`python
def rank_stability(g):
    return np.linalg.matrix_rank(g + 1e-6*np.eye(g.shape[0]))
`

Fusion
`python
def fusion_field(x, y, alpha=1, beta=1, gamma=1):
    return alphax + betay + gammanp.tanh(xy)
`

---

📚 Lean Formalization

The Lean appendix provides:

- definitions of curvature, holonomy, topology  
- operator signatures  
- theorem scaffolding  
- proof outlines  

This enables future formal verification of hallucination operators.

---

📖 Key References (APA)

Marín, J. (2026). A geometric taxonomy of hallucinations in large language models. arXiv:2602.13224.  

Wang, X., & Isola, P. (2020). Understanding contrastive representation learning through geometry.  

Ji, Z., et al. (2023). Hallucinations in large language models: A survey.  

These works motivate the need for manifold‑level operators but do not provide them—GHT fills that gap.

---

🎯 Goals of This Repository

- Provide a rigorous geometric framework for hallucination analysis  
- Enable operator‑level diagnostics  
- Support formal verification via Lean  
- Offer a reproducible toolkit for researchers  
- Establish a mathematical spine for future structural AI architectures  

---

