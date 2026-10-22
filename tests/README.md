# 🧪 Tests Folder — Operator Validation Suite

The tests/ directory contains the unit‑test suite for the Geometric Hallucination Taxonomy (GHT).  
These tests ensure that every operator in the toolkit behaves correctly, consistently, and predictably across all supported geometric regimes.

The suite is written in PyTest, with:

- deterministic synthetic tensors  
- stable operator outputs  
- explicit geometric expectations  
- reproducible validation logic  
- academically defensible test coverage  

This folder is the verification spine of the operator layer.

---

🌈 Color‑Tile Table — Test Index

Each test file is tagged with a semantic color tile indicating its operator domain.

| Tile | Test File | Operator Domain | Description |
|------|-----------|-----------------|-------------|
| 🟦 | test_curvature.py | Curvature Operator | Validates sectional curvature, curvature signatures, blowout/collapse detection. |
| 🟧 | test_spectral.py | Spectral Operator | Tests spectral drift, cascade intensity, collapse detection, oscillatory regimes. |
| 🟩 | test_holonomy.py | Holonomy Operator | Checks parallel transport, holonomy drift, magnitude, direction, loop behavior. |
| 🟪 | test_topology.py | Topology Operator | Verifies metric rank, rank instability, collapse surfaces, topological signatures. |
| 🟥 | test_fusion.py | Fusion‑Field Operator | Tests nonlinear interaction, fusion‑field blending, intensity, chimera signatures. |
| 🟨 | test_compare.py (optional future) | Comparison Layer | Cross‑operator benchmarking tests (GHT vs baseline heuristics). |

---

🧠 Why the Tests Matter (and How They Fit Into AI Interpretability)

The tests/ directory is not just a technical requirement — it is the structural integrity layer of the Geometric Hallucination Taxonomy.  
These tests ensure that the geometric operators behave exactly as defined in the mathematical spine and produce stable, reproducible outputs.

In other words:

> The tests folder is where the geometry is verified.  
> It is the bridge between operator definitions and scientific reliability.

Here’s how it fits into the broader interpretability project.

---

🔍 1. It guarantees operator correctness

Each operator — curvature, spectral, holonomy, topology, fusion — has precise mathematical behavior.  
The tests ensure:

- correct tensor contractions  
- correct eigenvalue trajectories  
- correct parallel transport  
- correct rank detection  
- correct nonlinear blending  

This is essential for scientific validity.

---

🧩 2. It ensures geometric stability across regimes

The tests cover:

- blowout regimes  
- collapse regimes  
- oscillatory regimes  
- near‑singular metrics  
- nonlinear chimera formation  
- closed‑loop holonomy drift  

This ensures that operators behave correctly even under extreme geometric conditions, which is crucial for hallucination analysis.

---

🧪 3. It provides reproducible interpretability validation

Every test uses:

- deterministic synthetic tensors  
- reproducible vectors  
- stable expected outputs  

This makes the test suite the validation backbone of the project.

It is where:

- reviewers verify correctness  
- collaborators confirm operator behavior  
- future extensions maintain compatibility  
- regressions are prevented  

This is essential for long‑term reliability.

---

🧬 4. It anchors GHT in the broader interpretability ecosystem

Most interpretability methods lack:

- formal operator definitions  
- mathematical stability guarantees  
- reproducible validation suites  

GHT is different.

The tests folder demonstrates:

- operator‑level rigor  
- geometry‑first correctness  
- architecture‑agnostic stability  
- reproducible interpretability behavior  

This positions GHT as a structural‑AI interpretability framework, not a heuristic toolkit.

---

📚 5. It supports the mathematical spine and Lean formalization

The tests directly correspond to:

- definitions in math_spine.tex  
- operator proofs  
- Lean formalization targets  
- preprint experimental sections  

They ensure that the Python implementation matches the formal mathematical definitions, which is essential for:

- proof‑checking  
- operator equivalence  
- reproducibility  
- scientific defensibility  

---

🧭 6. It prevents silent geometric regressions

Because GHT operators are geometric, regressions can be subtle:

- a sign error in curvature  
- a missing normalization in spectral drift  
- a slight misalignment in holonomy direction  
- a tolerance issue in rank detection  
- a nonlinear blending mis-scaling  

The tests catch these immediately.

This protects the interpretability claims of the entire project.

---

🧪 How to Run the Tests

PyTest (recommended)

From the project root:

`
pytest -q
`

Run a single operator test

`
pytest tests/test_curvature.py -q
`

All tests are deterministic and require no external data.

---

🧾 Provenance

Tests Suite — Verification Layer  
Author: Borealis S. Hedling  
Project: Geometric Hallucination Taxonomy  
Version: Tests‑v1.0  
Generated: 22 October 2026  
Location: Dublin, Ireland  
Context: Geometric AI • Interpretability • Operator Validation • Structural Reliability

---

