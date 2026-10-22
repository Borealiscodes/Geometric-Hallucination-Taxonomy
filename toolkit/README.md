# 🧰 Toolkit Folder — Operator Implementation Layer

The toolkit/ directory contains the core operator implementations of the Geometric Hallucination Taxonomy (GHT).  
These operators form the mathematical and computational backbone of the project, providing stable, reproducible geometric diagnostics for hallucination analysis.

Each module implements a distinct geometric operator:

- curvature  
- spectral drift  
- holonomy  
- topology  
- fusion‑fields  
- comparison layer  

All operators are:

- architecture‑agnostic  
- mathematically grounded  
- reproducible  
- deterministic  
- aligned with the mathematical spine  
- validated by the /tests/ suite  
- demonstrated in the /examples/ suite  

This folder is the operator layer of the GHT system.

---

🌈 Color‑Tile Table — Operator Index

Each operator module is tagged with a semantic color tile indicating its geometric domain.

| Tile | Module | Operator Domain | Description |
|------|--------|-----------------|-------------|
| 🟦 | curvature.py | Geometric Expansion / Collapse | Sectional curvature, curvature signatures, blowout/collapse/oscillatory regimes. |
| 🟧 | spectral.py | Eigenvalue Dynamics | Spectral drift, cascade intensity, collapse detection, oscillatory spectral breathing. |
| 🟩 | holonomy.py | Semantic Rotation | Parallel transport, holonomy drift, magnitude/direction, closed‑loop instability. |
| 🟪 | topology.py | Manifold Degeneracy | Metric rank, rank instability, collapse surfaces, topological signatures. |
| 🟥 | fusion.py | Nonlinear Hybridization | Nonlinear interaction, fusion‑fields, chimera formation, oscillatory blending. |
| 🟨 | compare.py | Operator Benchmarking | Cross‑operator comparison (GHT vs baseline heuristics like SGI and Γ). |

---

🧠 Why the Toolkit Matters (and How It Fits Into AI Interpretability)

The toolkit/ directory is the mathematical engine of the Geometric Hallucination Taxonomy.  
It defines the operators that make geometric interpretability possible.

In other words:

> The toolkit is where hallucination geometry is computed.  
> It is the bridge between mathematical theory and empirical diagnostics.

Here’s how it fits into the broader interpretability project.

---

🔍 1. It implements the geometric operators that define GHT

The toolkit contains the actual implementations of:

- curvature blowout detection  
- spectral cascade measurement  
- holonomy drift computation  
- topology collapse detection  
- fusion‑field nonlinear blending  

These operators are the core primitives of the taxonomy.

Without them, GHT would be:

- conceptual but not executable  
- theoretical but not testable  
- geometric but not diagnostic  

The toolkit makes the geometry real.

---

🧩 2. It provides architecture‑agnostic interpretability tools

Unlike most interpretability methods, GHT operators:

- do not depend on model architecture  
- do not require gradients  
- do not require attention maps  
- do not require token‑level heuristics  

They operate on latent geometry, not model internals.

This makes the toolkit:

- portable  
- robust  
- future‑proof  
- compatible with any embedding space  

It is a structural‑AI interpretability layer, not a model‑specific hack.

---

🧪 3. It ensures reproducible geometric diagnostics

Every operator is:

- deterministic  
- numerically stable  
- validated by unit tests  
- demonstrated in examples  
- grounded in the mathematical spine  

This ensures that GHT diagnostics are:

- reproducible  
- scientifically defensible  
- suitable for peer review  
- compatible with Lean formalization  

The toolkit is the reproducibility anchor of the project.

---

🧬 4. It ties directly into hallucination taxonomy

Each operator corresponds to a hallucination class:

- Curvature blowout → expansive hallucinations  
- Spectral cascade → runaway semantic drift  
- Holonomy rotation → meaning changes along loops  
- Topology collapse → semantic implosion  
- Fusion‑field chimera → hybridized concepts  

The toolkit computes the geometric signatures that define these classes.

This is the core insight of GHT:

> Hallucinations are geometric events.  
> Operators detect those events.  
> The toolkit implements those operators.

---

📚 5. It supports the mathematical spine and Lean proofs

The toolkit is designed to match:

- operator definitions in math_spine.tex  
- formal proofs in Lean  
- experimental sections in the preprint  
- comparison layer diagnostics  

This ensures that:

- the math  
- the code  
- the proofs  
- the experiments  

all align perfectly.

This is essential for structural interpretability.

---

🧭 6. It is the foundation for the examples and tests

The toolkit is the layer that the other layers depend on:

- /examples/ demonstrates the operators  
- /tests/ validates the operators  
- /docs/ explains the operators  
- /math_spine/ defines the operators  
- /preprint/ analyzes the operators  

The toolkit is the operator implementation layer that ties the entire project together.

---

🧪 How to Use the Toolkit

Import an operator

`python
from toolkit.curvature import sectional_curvature
`

Compute a signature

`python
sig = curvature_signature(R, v)
`

Use in experiments

All operators are designed to be:

- composable  
- lightweight  
- deterministic  
- numerically stable  

They can be used directly in notebooks, scripts, or research pipelines.

---

🧾 Provenance

Toolkit — Operator Implementation Layer  
Author: Borealis S. Hedling  
Project: Geometric Hallucination Taxonomy  
Version: Toolkit‑v1.0  
Generated: 22 October 2026  
Location: Dublin, Ireland  
Context: Geometric AI • Interpretability • Operator Design • Structural Analysis

---

