# README — Mathematical Spine (/math_spine/)

Overview

The Mathematical Spine is the formal geometric backbone of the  
Geometric Hallucination Taxonomy (GHT).  
It contains the rigorous LaTeX modules that define:

- the manifold and metric foundations,  
- the five geometric operators (curvature, spectral, holonomy, topology, fusion),  
- unified stability criteria,  
- operator‑level theorems,  
- auxiliary lemmas and numerical approximations.

These modules serve as the canonical mathematical source of truth for the entire project.  
All conceptual, experimental, and mechanized components map directly to this spine.

The spine is intentionally modular, operator‑aligned, and Lean‑compatible.

---

Directory Structure

`
/math_spine/
    00-Foundations.tex
    01-Curvature.tex
    02-Spectral.tex
    03-Holonomy.tex
    04-Topology.tex
    05-Fusion.tex
    06-StabilityCriteria.tex
    07-OperatorTheorems.tex
    08-Appendix-Misc.tex
`

Each file corresponds to one conceptual layer of the taxonomy:

00‑Foundations.tex
Defines the manifold, metric, Levi–Civita connection, geodesics, parallel transport,  
metric rank, fusion preliminaries, and stability thresholds.  
All other modules depend on this file.

01‑Curvature.tex
Formalizes curvature tensor, sectional curvature, trajectory curvature, and  
curvature‑driven instability (CDH).

02‑Spectral.tex
Defines eigenvalue dynamics, spectral derivative, spectral norm drift, and  
spectral cascade instability (SCH).

03‑Holonomy.tex
Defines parallel transport, holonomy operator, holonomy drift, and  
holonomy‑driven instability (HDH).

04‑Topology.tex
Defines metric rank, degeneracy, collapse surfaces, and  
topological instability (TIH).

05‑Fusion.tex
Defines nonlinear fusion‑field operators, interaction terms, dominance conditions,  
and fusion‑field instability (FFH).

06‑StabilityCriteria.tex
Unifies all operator‑level stability conditions into a single stability region  
\(\Omega\).  
Defines persistent instability and unified hallucination onset.

07‑OperatorTheorems.tex
Formal theorems linking operator instability → geometric divergence → hallucination.  
Includes curvature divergence, spectral cascade, holonomy drift, rank collapse,  
fusion spikes, operator interaction, and global divergence.

08‑Appendix‑Misc.tex
Auxiliary lemmas, discretization formulas, numerical approximations, and Lean alignment notes.

---

Purpose of the Mathematical Spine

The spine provides:

1. Formal mathematical grounding
Every operator in the taxonomy is defined using standard differential geometry,  
linear algebra, and nonlinear operator theory.

2. A stable reference for the preprint
The preprint cites these modules as the authoritative mathematical definitions.

3. A direct map to Lean formalization
Each .tex module corresponds to a Lean file in /lean_spine/, ensuring  
mechanized verification is structurally aligned with the math.

4. A reproducibility anchor for experiments
The Python toolkit implements discrete approximations of the operators defined here.

5. A modular architecture for future work
New operators, theorems, or geometric diagnostics can be added without disturbing  
existing modules.

---

How to Use This Directory

For readers of the preprint
Start with 00-Foundations.tex, then read the operator modules in order.  
The theorems in 07-OperatorTheorems.tex summarize the implications.

For implementers
Use the definitions in modules 01–05 to implement diagnostics in code.  
Discrete approximations are in 08-Appendix-Misc.tex.

For Lean mechanization
Translate each .tex module into its corresponding .lean file.  
Appendix B of the preprint provides scaffolding and typeclass structure.

For future extensions
Add new operators as 09-*.tex modules.  
The stability and theorem modules are designed to generalize.

---

Provenance

This mathematical spine is original research by Borealis S. Hedling,  
developed with structural‑AI assistance from Copilot.  
All geometric definitions follow standard differential geometry and Mathlib conventions.  
No external copyrighted text is included.

---

