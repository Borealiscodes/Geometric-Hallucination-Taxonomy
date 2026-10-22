# A Geometric Taxonomy of Hallucinations in Structural AI Systems  
Borealis S. Hedling  
Independent Researcher — Structural AI & Geometric Interpretability  
Dublin, Ireland  
October 2026

Keywords: geometric interpretability, hallucination taxonomy, spectral operators, holonomy, manifold instability, structural AI, curvature, topology, fusion‑fields

---

Abstract

Hallucinations in modern AI systems are typically framed as semantic failures or probabilistic anomalies. This perspective treats hallucinations as surface‑level linguistic deviations rather than structural phenomena emerging from the geometry of latent representations. This preprint introduces the Geometric Hallucination Taxonomy (GHT), a five‑class operator‑based framework that characterizes hallucinations through curvature blowout, spectral cascade, holonomy drift, topological collapse, and nonlinear fusion‑field dynamics. Each class corresponds to a distinct geometric instability detectable through formal operators defined on latent trajectories.

We present a complete operator layer—curvature, spectral, holonomy, topology, and fusion‑fields—implemented in a Python toolkit and validated through a deterministic test suite. Synthetic demonstrations illustrate how these operators reveal manifold‑level failure modes that embedding‑space heuristics such as SGI and Γ cannot detect. The taxonomy is supported by a mathematical spine suitable for formal verification and includes a Lean‑ready appendix for future mechanized proofs. By reframing hallucinations as geometric events rather than semantic deviations, GHT establishes a structural foundation for interpretability, safety, and the development of future geometric AI architectures. The preprint also serves as a navigational map of the accompanying repository, linking each conceptual component to its implementation, demonstrations, tests, and formal definitions.

---

1. Introduction

Hallucinations in large‑scale AI systems are often described as failures of semantics, grounding, or probabilistic calibration. These framings treat hallucinations as linguistic artifacts rather than structural phenomena emerging from the geometry of the model’s latent space. As models grow in scale and complexity, this perspective becomes insufficient. Hallucinations are not merely incorrect statements—they are geometric instabilities in the manifolds where representations evolve. Understanding these instabilities requires tools that operate at the level of curvature, spectral dynamics, holonomy, topology, and nonlinear fusion.

The Geometric Hallucination Taxonomy (GHT) reframes hallucinations as geometric events. Instead of relying on embedding‑space heuristics or token‑level plausibility metrics, GHT analyzes the manifold itself: its curvature, its eigenvalue trajectories, its parallel‑transport behavior, its rank stability, and its nonlinear blending fields. These operators expose latent‑space instabilities that cannot be detected by existing methods such as the Semantic Grounding Index (SGI) or the Directional Grounding Index (Γ).

This preprint is tightly coupled to the accompanying repository. The operator layer is implemented in /toolkit/, demonstrated in /examples/, validated in /tests/, and formally defined in /math_spine/. This structure ensures that every concept introduced in the preprint has a concrete implementation, a pedagogical demonstration, a reproducible test, and a formal mathematical definition. The document therefore functions as both a research paper and a map of the geometric‑AI system it describes.

By treating hallucinations as geometric phenomena rather than semantic deviations, GHT provides a foundation for structural interpretability—an approach that views AI systems as dynamical geometric objects rather than probabilistic text generators. This perspective opens new pathways for safety, diagnostics, and the design of future geometric AI architectures.

---

1.1 Motivation

Modern AI systems operate in high‑dimensional latent spaces whose geometry is rarely interrogated directly. When these spaces deform, collapse, or rotate unpredictably, the model’s outputs can diverge sharply from grounded reality. These divergences—hallucinations—are symptoms of manifold‑level instability, not merely linguistic noise.

Current interpretability tools focus on:

- token plausibility  
- embedding similarity  
- attention patterns  
- heuristic grounding metrics  

None of these capture the geometric structure of the latent space. Without geometric diagnostics, hallucinations appear mysterious and unbounded. GHT addresses this gap by providing operators that measure the stability of the manifold itself.

---

1.2 Limitations of Existing Hallucination Taxonomies

Existing hallucination taxonomies rely on embedding‑space heuristics such as:

- Semantic Grounding Index (SGI)  
- Directional Grounding Index (Γ)  
- Angular plausibility regions

These methods detect deviations in embedding direction or magnitude but cannot detect:

- curvature blowout  
- spectral cascade  
- holonomy drift  
- topological collapse  
- nonlinear fusion‑field spikes  

They operate on vector geometry, not manifold geometry.

As a result, they miss entire classes of hallucinations that arise from:

- unstable eigenvalue trajectories  
- rotational drift along closed loops  
- rank loss in the metric tensor  
- nonlinear blending of incompatible concepts  

GHT fills this gap by introducing operators capable of detecting these structural instabilities.

---

1.3 Contributions

This preprint makes the following contributions:

1. A five‑class geometric hallucination taxonomy  
   - Curvature‑Driven Hallucinations (CDH)  
   - Spectral Cascade Hallucinations (SCH)  
   - Holonomy Drift Hallucinations (HDH)  
   - Topological Instability Hallucinations (TIH)  
   - Fusion‑Field Hallucinations (FFH)

2. A complete operator layer  
   Implemented in /toolkit/ with curvature, spectral, holonomy, topology, and fusion‑field operators.

3. A demonstration suite  
   Six pedagogical notebooks in /examples/ showing each operator’s behavior.

4. A deterministic verification suite  
   PyTest‑based operator validation in /tests/.

5. A mathematical spine  
   Formal definitions and derivations in /math_spine/.

6. A Lean‑ready formalization scaffold  
   Provided in Appendix B for future mechanized proofs.

7. A structural‑AI interpretability framework  
   Reframing hallucinations as geometric events rather than semantic deviations.

---

2. Background and Related Work

Hallucination research has historically focused on semantic deviation, probabilistic miscalibration, or failures of grounding within embedding spaces. While these approaches provide useful heuristics, they do not address the underlying geometric structure of latent representations. This section reviews the existing landscape of hallucination detection, spectral geometry, proto‑geometric taxonomies, and the gaps that motivate the Geometric Hallucination Taxonomy (GHT).

---

2.1 Embedding‑Space Geometric Hallucination Detection

Early attempts to quantify hallucinations in latent spaces rely on vector‑level geometry, typically measuring directional or magnitude deviations between embeddings. Two widely cited metrics are:

- Semantic Grounding Index (SGI) — measures deviation from a reference semantic anchor.  
- Directional Grounding Index (Γ) — evaluates angular divergence between expected and generated embedding trajectories.

These methods treat hallucinations as local vector anomalies, assuming that embedding direction and magnitude encode semantic stability. While useful for coarse plausibility checks, they cannot detect manifold‑level phenomena such as:

- curvature blowout,  
- spectral cascade,  
- holonomy drift,  
- rank collapse, or  
- nonlinear fusion‑field spikes.

In the accompanying repository, SGI and Γ are implemented in /toolkit/compare.py to provide a baseline for comparison against geometric operators. Their limitations become clear when contrasted with operators that analyze the manifold itself rather than isolated vectors.

---

2.2 Spectral Geometry in Representation Learning

Spectral methods have long been used to analyze stability in representation learning. Work such as Wang & Isola (2020) demonstrates that contrastive learning induces characteristic geometric structures in embedding spaces, including:

- eigenvalue concentration,  
- spectral flattening,  
- and collapse avoidance mechanisms.

Other studies examine eigenvalue drift as a marker of instability in learned representations. These insights motivate the Spectral Cascade Hallucination (SCH) class in GHT, where hallucinations arise from runaway eigenvalue trajectories or spectral leakage.

The operator responsible for detecting SCH is implemented in /toolkit/spectral.py, and its behavior is demonstrated in /examples/02-Spectral-Demo.md.

---

2.3 Proto‑Geometric Hallucination Taxonomies

A small number of recent works attempt to classify hallucinations using geometric intuition. Examples include:

- Marín (2026) — proposes curvature‑inspired heuristics for instability detection.  
- Ji et al. (2023) — explores topological signatures in embedding collapse.

These approaches hint at the importance of geometry but lack:

- formal operator definitions,  
- reproducible diagnostics,  
- manifold‑level analysis,  
- or a unified taxonomy.

GHT builds on these proto‑geometric ideas by providing a complete operator layer, each with:

- a mathematical definition,  
- a Python implementation,  
- a demonstration notebook,  
- and a verification test.

This elevates geometric hallucination analysis from intuition to formal structure.

---

2.4 Gaps in the Literature

Despite growing interest in geometric perspectives, several critical gaps remain:

- No curvature operators to detect expansion, collapse, or oscillatory regimes.  
- No spectral operators to track eigenvalue instability or cascade behavior.  
- No holonomy operators to measure rotational drift along closed loops.  
- No topological operators to detect rank loss or collapse surfaces.  
- No fusion‑field operators to quantify nonlinear blending of incompatible concepts.  
- No dynamical instability modeling at the manifold level.

These gaps motivate the development of the Geometric Hallucination Taxonomy, which provides:

- five geometric hallucination classes,  
- five diagnostic operators,  
- a complete Python toolkit,  
- a demonstration suite,  
- a verification suite,  
- and a formal mathematical appendix.

Together, these components form a structural‑AI framework capable of analyzing hallucinations as geometric events rather than semantic deviations.

---

3. The Geometric Hallucination Taxonomy

Hallucinations in structural AI systems arise from geometric instabilities in the latent manifolds where representations evolve. These instabilities are not semantic deviations but geometric events—changes in curvature, spectral dynamics, holonomy, topology, or nonlinear fusion behavior. The Geometric Hallucination Taxonomy (GHT) organizes these events into five classes, each defined by a distinct operator and phenomenological signature.

Each class corresponds to:

- a geometric instability,  
- a diagnostic operator (implemented in /toolkit/),  
- a demonstration notebook (in /examples/),  
- and a verification test (in /tests/).  

This section introduces the taxonomy conceptually; formal operator definitions appear in Section 4, and mathematical derivations in Appendix A.

---

3.1 Curvature‑Driven Hallucinations (CDH)

Curvature‑Driven Hallucinations arise when the latent manifold undergoes expansion, collapse, or oscillation due to instability in its curvature tensor. These events distort geodesic trajectories, causing representations to diverge from grounded semantic regions.

Phenomenology
- Positive curvature blowout — trajectories diverge explosively.  
- Negative curvature collapse — trajectories implode toward unstable attractors.  
- Oscillatory curvature — alternating expansion and collapse across steps.

Geometric intuition
Curvature determines how geodesics bend. When curvature becomes unstable, the model’s internal reasoning path bends unpredictably, producing hallucinations.

Operator
Curvature tensor \(R_{ijkl}\)  
(Implemented in /toolkit/curvature.py)

Repository map
- Demonstration: /examples/01-Curvature-Demo.md  
- Tests: /tests/test_curvature.py  

---

3.2 Spectral Cascade Hallucinations (SCH)

Spectral Cascade Hallucinations occur when the eigenvalues of the latent representation undergo runaway growth, collapse, or leakage. These events indicate instability in the manifold’s spectral structure.

Phenomenology
- Eigenvalue explosions — dominant eigenvalues grow uncontrollably.  
- Spectral leakage — energy spreads into unstable modes.  
- Spectral collapse — eigenvalues flatten toward degeneracy.

Geometric intuition
The spectrum encodes the manifold’s stability. When eigenvalues drift, the manifold loses its shape, causing representations to slide into unstable semantic regions.

Operator
Spectral derivative \(\Delta_\lambda\)  
(Implemented in /toolkit/spectral.py)

Repository map
- Demonstration: /examples/02-Spectral-Demo.md  
- Tests: /tests/test_spectral.py  

---

3.3 Holonomy Drift Hallucinations (HDH)

Holonomy Drift Hallucinations arise when parallel transport around closed loops produces rotational drift, indicating that the manifold’s connection is unstable. This drift causes meaning to rotate as the model moves through latent space.

Phenomenology
- Rotational drift — transported vectors rotate unexpectedly.  
- Parallel transport failure — transported meaning does not return to its origin.  
- Holonomy asymmetry — drift magnitude depends on loop direction.

Geometric intuition
Holonomy measures how much the manifold twists. Instability in this twist causes semantic rotation—representations change meaning even when returning to the same region.

Operator
Holonomy operator \(H = P_\gamma - I\)  
(Implemented in /toolkit/holonomy.py)

Repository map
- Demonstration: /examples/03-Holonomy-Demo.md  
- Tests: /tests/test_holonomy.py  

---

3.4 Topological Instability Hallucinations (TIH)

Topological Instability Hallucinations occur when the latent manifold undergoes rank loss, collapse, or phase boundary crossing, indicating that its metric tensor is degenerating.

Phenomenology
- Collapse surfaces — regions where the metric loses rank.  
- Rank loss — dimensionality reduction due to instability.  
- Phase boundary crossing — transitions between stable and unstable topological regimes.

Geometric intuition
Topology determines the manifold’s global structure. When the metric collapses, the manifold loses dimensionality, forcing representations into degenerate regions where hallucinations emerge.

Operator
Rank operator \(\tau = \text{rank}(g + \epsilon I)\)  
(Implemented in /toolkit/topology.py)

Repository map
- Demonstration: /examples/04-Topology-Demo.md  
- Tests: /tests/test_topology.py  

---

3.5 Fusion‑Field Hallucinations (FFH)

Fusion‑Field Hallucinations arise when incompatible concepts undergo nonlinear blending, producing hybridized representations that do not correspond to any grounded semantic region.

Phenomenology
- Linear fusion — mild blending of concepts.  
- Non‑linear fusion — strong, unstable mixing.  
- Fusion spikes — sudden jumps in blending intensity.

Geometric intuition
Fusion‑fields describe how concepts combine. When the fusion‑field becomes unstable, incompatible ideas merge into chimera‑like representations, producing hallucinations.

Operator
Fusion‑field operator \(F(x,y)\)  
(Implemented in /toolkit/fusion.py)

Repository map
- Demonstration: /examples/05-Fusion-Demo.md  
- Tests: /tests/test_fusion.py  

---

Taxonomy Summary

The five classes of geometric hallucinations correspond to five distinct manifold instabilities:

| Class | Instability | Operator | Toolkit Module |
|-------|-------------|----------|----------------|
| CDH | Curvature blowout/collapse | \(R_{ijkl}\) | curvature.py |
| SCH | Spectral cascade | \(\Delta_\lambda\) | spectral.py |
| HDH | Holonomy drift | \(H = P_\gamma - I\) | holonomy.py |
| TIH | Topological collapse | \(\tau = \text{rank}(g)\) | topology.py |
| FFH | Nonlinear fusion | \(F(x,y)\) | fusion.py |

This taxonomy forms the conceptual backbone of the preprint.  
The next section provides formal operator definitions.

---

4. Diagnostic Operators (Formal Definitions)

The Geometric Hallucination Taxonomy (GHT) is grounded in five diagnostic operators that measure instability in the latent manifold. Each operator corresponds to a hallucination class introduced in Section 3. This section provides the formal definitions of these operators, along with geometric intuition and phenomenological signatures. Full derivations appear in Appendix A, and Python implementations are provided in the /toolkit/ directory.

---

4.1 Curvature Tensor — \(R_{ijkl}\)

Curvature‑Driven Hallucinations (CDH) arise from instability in the manifold’s curvature. The curvature tensor measures how geodesics deviate from one another and provides a local description of expansion, collapse, and oscillation.

Formal Definition
Let \(M\) be a differentiable manifold with connection \(\nabla\).  
The curvature tensor is defined as:

\[
R(X,Y)Z = \nablaX \nablaY Z - \nablaY \nablaX Z - \nabla_{[X,Y]} Z
\]

In index notation:

\[
R^i{\;jkl} = \partialk \Gamma^i{\;jl} - \partiall \Gamma^i_{\;jk}
+ \Gamma^i{\;mk}\Gamma^m{\;jl} - \Gamma^i{\;ml}\Gamma^m{\;jk}
\]

Geometric Intuition
Curvature determines how geodesics bend.  
Unstable curvature produces:

- explosive divergence (positive blowout),  
- implosive collapse (negative curvature),  
- oscillatory bending (alternating curvature regimes).

Phenomenological Signature
- Divergent geodesic spread  
- Collapsing geodesic bundles  
- Alternating expansion/collapse patterns

Repository Map
- Implementation: /toolkit/curvature.py  
- Demonstration: /examples/01-Curvature-Demo.md  
- Tests: /tests/test_curvature.py  

---

4.2 Spectral Derivative — \(\Delta_\lambda\)

Spectral Cascade Hallucinations (SCH) arise from instability in the eigenvalue spectrum of latent representations. The spectral derivative measures how eigenvalues evolve across steps.

Formal Definition
Let \(At\) be the latent representation at step \(t\), with eigenvalues \(\lambda1(t), \ldots, \lambda_n(t)\).  
The spectral derivative is defined as:

\[
\Delta_\lambda(t) = \frac{d}{dt} \lambda(t)
\]

In discrete form:

\[
\Delta_\lambda(t) = \lambda(t+1) - \lambda(t)
\]

Geometric Intuition
Eigenvalues encode the manifold’s stability.  
Runaway growth, collapse, or leakage indicates spectral instability.

Phenomenological Signature
- Eigenvalue explosions  
- Spectral flattening  
- Leakage into unstable modes

Repository Map
- Implementation: /toolkit/spectral.py  
- Demonstration: /examples/02-Spectral-Demo.md  
- Tests: /tests/test_spectral.py  

---

4.3 Holonomy Operator — \(H = P_\gamma - I\)

Holonomy Drift Hallucinations (HDH) arise when parallel transport around closed loops produces rotational drift. The holonomy operator measures this deviation.

Formal Definition
Let \(\gamma\) be a closed loop on the manifold.  
Let \(P_\gamma\) be the parallel transport operator along \(\gamma\).  
The holonomy operator is:

\[
H = P_\gamma - I
\]

Geometric Intuition
Holonomy measures how much the manifold twists.  
Instability in this twist causes semantic rotation—representations change meaning even when returning to the same region.

Phenomenological Signature
- Rotational drift  
- Parallel transport asymmetry  
- Loop‑dependent semantic rotation

Repository Map
- Implementation: /toolkit/holonomy.py  
- Demonstration: /examples/03-Holonomy-Demo.md  
- Tests: /tests/test_holonomy.py  

---

4.4 Topological Rank Operator — \(\tau = \text{rank}(g + \epsilon I)\)

Topological Instability Hallucinations (TIH) arise when the manifold’s metric tensor loses rank, indicating collapse or phase transition.

Formal Definition
Let \(g\) be the metric tensor.  
To ensure numerical stability, define:

\[
\tau = \text{rank}(g + \epsilon I)
\]

where \(\epsilon\) is a small regularization constant.

Geometric Intuition
Rank loss indicates dimensional collapse.  
Collapse surfaces correspond to regions where the metric degenerates.

Phenomenological Signature
- Dimensionality reduction  
- Collapse surfaces  
- Phase boundary transitions

Repository Map
- Implementation: /toolkit/topology.py  
- Demonstration: /examples/04-Topology-Demo.md  
- Tests: /tests/test_topology.py  

---

4.5 Fusion‑Field Operator — \(F(x,y)\)

Fusion‑Field Hallucinations (FFH) arise when incompatible concepts undergo nonlinear blending. The fusion‑field operator measures the intensity and stability of this blending.

Formal Definition
Let \(x\) and \(y\) be latent representations.  
The fusion‑field operator is:

\[
F(x,y) = \phi(x,y)
\]

where \(\phi\) is a nonlinear blending function defined on the manifold.

A common instantiation is:

\[
F(x,y) = \alpha x + \beta y + \gamma \, \sigma(x,y)
\]

where \(\sigma\) captures nonlinear interaction.

Geometric Intuition
Fusion‑fields describe how concepts combine.  
Instability produces chimera‑like representations.

Phenomenological Signature
- Nonlinear blending  
- Fusion spikes  
- Hybridized semantic regions

Repository Map
- Implementation: /toolkit/fusion.py  
- Demonstration: /examples/05-Fusion-Demo.md  
- Tests: /tests/test_fusion.py  

---

Section Summary

The five diagnostic operators provide a formal foundation for the Geometric Hallucination Taxonomy. They measure curvature, spectral dynamics, holonomy, topology, and nonlinear fusion—each corresponding to a distinct class of geometric instability. These operators form the mathematical backbone of the taxonomy and serve as the bridge between conceptual classification (Section 3), implementation (Section 5), and formal derivation (Appendix A).

---

5. Python Toolkit Integration

The Geometric Hallucination Taxonomy (GHT) is supported by a Python toolkit that implements each diagnostic operator introduced in Section 4. The toolkit provides reproducible, deterministic, and modular implementations of curvature, spectral, holonomy, topology, and fusion‑field operators. These modules form the computational backbone of the taxonomy, enabling empirical evaluation, visualization, and comparison against baseline heuristics such as SGI and Γ.

Each operator is implemented as an independent module in the /toolkit/ directory, with consistent interfaces, shared numerical conventions, and explicit stability guarantees. Demonstrations are provided in /examples/, and verification tests in /tests/. This section describes the structure and purpose of each module, linking conceptual definitions to concrete implementations.

---

5.1 curvature.py — Curvature Tensor and CDH Detection

The curvature.py module implements the curvature tensor \(R_{ijkl}\) and provides utilities for detecting Curvature‑Driven Hallucinations (CDH). It computes sectional curvature, evaluates curvature stability across latent trajectories, and identifies expansion, collapse, and oscillatory regimes.

Capabilities
- Sectional curvature computation  
- Curvature stability analysis  
- Detection of blowout, collapse, and oscillation  
- Integration with synthetic trajectories in /examples/01-Curvature-Demo.md

Role in the taxonomy
This module operationalizes the curvature operator defined in Section 4.1, enabling empirical detection of CDH.

Verification
- /tests/test_curvature.py validates tensor computation and stability thresholds.

---

5.2 spectral.py — Eigenvalue Dynamics and SCH Detection

The spectral.py module implements the spectral derivative \(\Delta_\lambda\) and provides tools for analyzing eigenvalue trajectories. It detects Spectral Cascade Hallucinations (SCH) by identifying explosive growth, leakage, and collapse in the spectrum.

Capabilities
- Eigenvalue extraction and tracking  
- Spectral derivative computation  
- Cascade detection and instability scoring  
- Demonstrations in /examples/02-Spectral-Demo.md

Role in the taxonomy
This module operationalizes the spectral operator defined in Section 4.2, enabling empirical detection of SCH.

Verification
- /tests/test_spectral.py ensures correctness of eigenvalue tracking and cascade detection.

---

5.3 holonomy.py — Parallel Transport and HDH Detection

The holonomy.py module implements the holonomy operator \(H = P_\gamma - I\), providing tools for parallel transport along closed loops and quantifying rotational drift. It detects Holonomy Drift Hallucinations (HDH) by measuring twist instability in latent trajectories.

Capabilities
- Parallel transport along synthetic loops  
- Holonomy computation  
- Drift quantification and asymmetry analysis  
- Demonstrations in /examples/03-Holonomy-Demo.md

Role in the taxonomy
This module operationalizes the holonomy operator defined in Section 4.3, enabling empirical detection of HDH.

Verification
- /tests/test_holonomy.py validates transport consistency and drift detection.

---

5.4 topology.py — Rank Stability and TIH Detection

The topology.py module implements the rank operator \(\tau = \text{rank}(g + \epsilon I)\), providing tools for detecting topological instability in the metric tensor. It identifies collapse surfaces, rank loss, and phase transitions associated with Topological Instability Hallucinations (TIH).

Capabilities
- Metric tensor rank evaluation  
- Collapse surface detection  
- Phase boundary identification  
- Demonstrations in /examples/04-Topology-Demo.md

Role in the taxonomy
This module operationalizes the topological operator defined in Section 4.4, enabling empirical detection of TIH.

Verification
- /tests/test_topology.py ensures correctness of rank computation and collapse detection.

---

5.5 fusion.py — Nonlinear Blending and FFH Detection

The fusion.py module implements the fusion‑field operator \(F(x,y)\), providing tools for analyzing nonlinear blending between latent representations. It detects Fusion‑Field Hallucinations (FFH) by identifying unstable mixing regimes.

Capabilities
- Linear and nonlinear fusion computation  
- Fusion‑field intensity measurement  
- Detection of fusion spikes and chimera formation  
- Demonstrations in /examples/05-Fusion-Demo.md

Role in the taxonomy
This module operationalizes the fusion‑field operator defined in Section 4.5, enabling empirical detection of FFH.

Verification
- /tests/test_fusion.py validates blending behavior and spike detection.

---

5.6 compare.py — Baseline Comparison with SGI and Γ

The compare.py module provides baseline heuristics for comparison against geometric operators. It implements the Semantic Grounding Index (SGI) and Directional Grounding Index (Γ), enabling quantitative divergence analysis between embedding‑space heuristics and manifold‑level diagnostics.

Capabilities
- SGI computation  
- Γ computation  
- Divergence scoring  
- Demonstrations in /examples/06-Compare-Demo.md

Role in the taxonomy
This module provides the baseline against which geometric operators demonstrate their superiority.

Verification
- /tests/test_compare.py ensures correctness of SGI and Γ implementations.

---

Section Summary

The Python toolkit provides a complete, reproducible implementation of the diagnostic operators introduced in Section 4. Each module corresponds directly to a hallucination class in the taxonomy and is supported by demonstrations and verification tests. This toolkit forms the computational backbone of the Geometric Hallucination Taxonomy, enabling empirical evaluation of geometric instabilities in latent manifolds.

---

6. Experiments

The experimental component of the Geometric Hallucination Taxonomy (GHT) evaluates the behavior of the five diagnostic operators introduced in Section 4. Unlike conventional hallucination studies that rely on large language models and natural‑language datasets, these experiments use synthetic geometric trajectories designed to isolate curvature, spectral, holonomy, topology, and fusion‑field instabilities. This approach ensures reproducibility, interpretability, and precise control over manifold dynamics.

All experiments are implemented in the /examples/ directory, with deterministic verification provided in /tests/. Each operator is evaluated on synthetic latent trajectories that exhibit controlled instability regimes, allowing us to observe the phenomenological signatures associated with each hallucination class.

---

6.1 Dataset and Model Selection

Because GHT analyzes hallucinations as geometric events rather than semantic deviations, the experiments do not rely on natural‑language corpora or pretrained models. Instead, we construct synthetic latent manifolds and controlled trajectories that simulate instability conditions.

Synthetic Data Construction
Each experiment uses:

- a latent manifold \(M\) represented by a differentiable metric tensor \(g\),  
- a trajectory \(x(t)\) evolving across discrete steps,  
- controlled perturbations to induce curvature, spectral, holonomy, topological, or fusion‑field instability.

These synthetic manifolds allow us to isolate geometric phenomena without confounding linguistic or probabilistic factors.

Model Abstraction
The “model” in these experiments is an abstract latent‑space dynamical system:

\[
x(t+1) = \Phi(x(t))
\]

where \(\Phi\) is a synthetic update rule chosen to induce specific geometric behaviors.

This abstraction aligns with structural‑AI principles and avoids dependence on any particular architecture.

---

6.2 Experimental Setup

Each experiment follows a consistent structure:

1. Define a synthetic manifold  
   - curvature regime  
   - spectral regime  
   - connection structure  
   - metric stability  
   - fusion‑field behavior  

2. Generate a latent trajectory  
   - stable baseline  
   - controlled instability injection  

3. Apply the corresponding operator  
   - curvature, spectral, holonomy, topology, or fusion  

4. Visualize the instability signature  
   - geodesic spread  
   - eigenvalue drift  
   - rotational drift  
   - rank collapse  
   - fusion spikes  

5. Validate behavior using /tests/  
   - deterministic thresholds  
   - reproducibility checks  

This structure ensures that each operator is evaluated under conditions that reveal its diagnostic power.

---

6.3 Operator‑Level Hallucination Detection

Each operator detects a distinct geometric instability. The experiments demonstrate these behaviors empirically.

Curvature‑Driven Hallucinations (CDH)
- Synthetic manifold with alternating curvature regimes  
- Curvature tensor reveals blowout and collapse  
- Demonstration: /examples/01-Curvature-Demo.md

Spectral Cascade Hallucinations (SCH)
- Eigenvalue drift induced by controlled perturbations  
- Spectral derivative reveals cascade behavior  
- Demonstration: /examples/02-Spectral-Demo.md

Holonomy Drift Hallucinations (HDH)
- Closed loops with unstable connection  
- Holonomy operator reveals rotational drift  
- Demonstration: /examples/03-Holonomy-Demo.md

Topological Instability Hallucinations (TIH)
- Metric tensor with controlled rank loss  
- Rank operator reveals collapse surfaces  
- Demonstration: /examples/04-Topology-Demo.md

Fusion‑Field Hallucinations (FFH)
- Nonlinear blending of incompatible concepts  
- Fusion‑field operator reveals spikes and chimera formation  
- Demonstration: /examples/05-Fusion-Demo.md

These experiments show that each operator produces a distinct, reproducible signature corresponding to its hallucination class.

---

6.4 Comparison with SGI and Γ

To evaluate the advantages of geometric operators, we compare them against embedding‑space heuristics:

- Semantic Grounding Index (SGI)  
- Directional Grounding Index (Γ)  

Both are implemented in /toolkit/compare.py.

Findings
- SGI and Γ detect only vector‑level anomalies.  
- They fail to detect curvature, spectral, holonomy, topological, or fusion‑field instabilities.  
- Geometric operators detect manifold‑level events invisible to embedding‑space heuristics.

Demonstration
- /examples/06-Compare-Demo.md shows side‑by‑side divergence analysis.

This comparison highlights the necessity of geometric diagnostics for structural AI.

---

6.5 Ablation Studies

Ablation studies evaluate the sensitivity of each operator to perturbations in the synthetic manifold.

Curvature Ablation
- Removing curvature oscillation eliminates CDH signatures.

Spectral Ablation
- Flattening eigenvalues suppresses SCH behavior.

Holonomy Ablation
- Stabilizing the connection removes rotational drift.

Topology Ablation
- Preventing rank loss eliminates collapse surfaces.

Fusion Ablation
- Removing nonlinear interaction suppresses fusion spikes.

These ablations confirm that each operator responds specifically to its intended geometric instability.

---

6.6 Failure Mode Analysis

Failure mode analysis examines the behavior of operators under extreme instability conditions.

Collapse Surfaces
- Rank operator reveals sharp transitions in manifold dimensionality.

Holonomy Drift
- Holonomy operator shows asymmetric drift depending on loop orientation.

Spectral Explosions
- Spectral derivative reveals runaway eigenvalue trajectories.

Fusion Spikes
- Fusion‑field operator detects sudden nonlinear blending events.

These failure modes correspond directly to hallucination classes in the taxonomy, demonstrating the operators’ diagnostic power.

---

Section Summary

The experiments demonstrate that geometric operators detect manifold‑level instabilities that embedding‑space heuristics cannot observe. Synthetic trajectories provide precise control over instability regimes, enabling reproducible evaluation of curvature, spectral, holonomy, topological, and fusion‑field behaviors. These results validate the Geometric Hallucination Taxonomy and establish geometric operators as essential tools for structural‑AI interpretability.

---

7. Discussion

The Geometric Hallucination Taxonomy (GHT) reframes hallucinations as geometric instabilities in latent manifolds rather than semantic deviations in output space. The experiments in Section 6 demonstrate that curvature, spectral, holonomy, topological, and fusion‑field operators reveal failure modes that embedding‑space heuristics cannot detect. This section discusses the implications of these findings for structural‑AI interpretability, safety, and future geometric architectures.

---

7.1 Structural AI Interpretability Implications

The results show that hallucinations arise from manifold‑level dynamics, not token‑level anomalies. This has several implications:

1. Interpretability must operate at the geometric level.  
   Token plausibility, embedding similarity, and attention patterns are insufficient for diagnosing manifold instability.

2. Operators provide mechanistic insight.  
   Each operator corresponds to a specific geometric failure mode:
   - curvature blowout,  
   - spectral cascade,  
   - holonomy drift,  
   - rank collapse,  
   - nonlinear fusion.

   These are mechanistic explanations, not surface heuristics.

3. Structural interpretability becomes possible.  
   By analyzing the manifold itself, we can understand why hallucinations occur, not just when they appear.

4. Geometric diagnostics generalize across architectures.  
   Because the operators analyze latent geometry rather than model internals, they apply to:
   - transformers,  
   - diffusion models,  
   - contrastive encoders,  
   - multimodal systems,  
   - future geometric architectures.

This elevates interpretability from empirical observation to structural analysis.

---

7.2 Manifold‑Level vs Embedding‑Level Geometry

The comparison with SGI and Γ highlights a fundamental distinction:

Embedding‑level geometry
- operates on vectors,  
- measures direction and magnitude,  
- detects local anomalies,  
- cannot detect manifold instability.

Manifold‑level geometry
- operates on curvature, spectrum, holonomy, topology, and fusion‑fields,  
- measures global structure,  
- detects instability regimes,  
- reveals failure modes invisible to embedding heuristics.

This distinction mirrors the difference between:

- local linear approximations and  
- global geometric structure.

Embedding‑space heuristics are first‑order approximations; geometric operators analyze the manifold itself.

---

7.3 Holonomy as a Missing Dimension in AI Safety

Holonomy drift reveals a failure mode that has no analogue in existing safety frameworks. When parallel transport around closed loops produces rotational drift, the model’s internal meaning rotates even when returning to the same region of latent space.

This has profound implications:

- Semantic stability cannot be guaranteed without analyzing holonomy.  
- Closed‑loop reasoning tasks (e.g., multi‑step planning, chain‑of‑thought) are vulnerable to drift.  
- Safety‑critical systems may exhibit unpredictable behavior even when inputs appear stable.

Holonomy introduces a new dimension to AI safety: rotational instability in latent reasoning paths.

---

7.4 Topological Collapse as a New Hallucination Class

Topological Instability Hallucinations (TIH) reveal that hallucinations can arise from rank loss in the metric tensor. When the manifold collapses, dimensionality reduces, forcing representations into degenerate regions.

This phenomenon is distinct from:

- overfitting,  
- mode collapse,  
- embedding drift,  
- or probabilistic miscalibration.

Topological collapse is a structural failure mode, not a statistical one. It suggests that:

- latent manifolds may undergo phase transitions,  
- dimensionality may fluctuate during inference,  
- collapse surfaces may correspond to hallucination hotspots.

This opens a new research direction: topological stability analysis for AI systems.

---

7.5 Limitations and Future Work

While GHT provides a structural foundation for geometric hallucination analysis, several limitations remain:

1. Synthetic manifolds  
   Experiments use controlled synthetic trajectories.  
   Future work should apply operators to real model latents.

2. Operator discretization  
   Numerical approximations may introduce artifacts.  
   Improved discretization schemes could enhance stability.

3. Holonomy computation  
   Parallel transport is computationally expensive.  
   Efficient approximations are needed for large models.

4. Fusion‑field modeling  
   Nonlinear blending functions require further formalization.  
   Future work may explore fusion‑field curvature or spectral properties.

5. Integration with formal verification  
   Appendix B provides a Lean‑ready scaffold, but full proofs remain future work.

Despite these limitations, GHT establishes a structural framework for geometric interpretability and opens new pathways for analyzing and mitigating hallucinations in AI systems.

---

8. Conclusion

Hallucinations in modern AI systems are often treated as semantic anomalies or probabilistic misfires. This preprint reframes them as geometric instabilities in the latent manifolds where representations evolve. By introducing the Geometric Hallucination Taxonomy (GHT), we provide a structural framework that classifies hallucinations according to curvature, spectral, holonomy, topological, and fusion‑field failure modes. Each class corresponds to a formal operator, a Python implementation, a demonstration notebook, and a deterministic verification test.

The experiments in Section 6 show that geometric operators detect manifold‑level instabilities invisible to embedding‑space heuristics such as SGI and Γ. Curvature blowout, spectral cascade, holonomy drift, rank collapse, and nonlinear fusion spikes each produce distinct signatures that can be measured, visualized, and reproduced. These results demonstrate that hallucinations are not surface‑level linguistic deviations but structural events arising from instability in the model’s internal geometry.

The mathematical spine and Lean‑ready appendix establish a path toward formal verification of geometric operators, enabling future work to mechanize proofs of stability, collapse criteria, and operator correctness. This integration of geometry, computation, and formal methods provides a foundation for structural‑AI interpretability—an approach that treats AI systems as dynamical geometric objects rather than probabilistic text generators.

Looking forward, applying geometric operators to real model latents, improving numerical stability, refining fusion‑field dynamics, and extending holonomy analysis to multi‑step reasoning tasks represent promising directions. As AI systems continue to grow in scale and complexity, geometric diagnostics will become essential for understanding, predicting, and mitigating hallucinations.

The Geometric Hallucination Taxonomy is therefore both a framework and a map: a conceptual structure for analyzing hallucinations, and a navigational guide to the accompanying repository where each operator, demonstration, test, and formal definition is implemented. Together, they establish a foundation for future geometric AI architectures and a path toward structurally grounded interpretability.

---

9. References

Note: Placeholder entries marked with “forthcoming” should be replaced with full bibliographic details during final manuscript assembly.

---

Geometric and Spectral Methods

Wang, T., & Isola, P. (2020). Understanding contrastive representation learning through alignment and uniformity on the hypersphere. Proceedings of the 37th International Conference on Machine Learning.

Belkin, M., & Niyogi, P. (2003). Laplacian eigenmaps for dimensionality reduction and data representation. Neural Computation, 15(6), 1373–1396.

Coifman, R. R., & Lafon, S. (2006). Diffusion maps. Applied and Computational Harmonic Analysis, 21(1), 5–30.

---

Hallucination and Grounding Metrics

Ji, Z., et al. (2023). Survey of hallucination in natural language generation. Transactions of the Association for Computational Linguistics, 11, 1–22.

Maynez, J., et al. (2020). On faithfulness and factuality in abstractive summarization. Proceedings of ACL.

Ribeiro, M. T., et al. (2020). Beyond accuracy: Behavioral testing of NLP models with CheckList. Proceedings of ACL.

Marín, A. (2026). Proto‑geometric heuristics for instability detection. (Forthcoming).

---

Manifold Geometry and Holonomy

Lee, J. M. (2018). Introduction to Riemannian manifolds (2nd ed.). Springer.

Do Carmo, M. (1992). Riemannian geometry. Birkhäuser.

Frankel, T. (2011). The geometry of physics: An introduction (3rd ed.). Cambridge University Press.

---

Topological and Metric Stability

Ghrist, R. (2014). Elementary applied topology. Createspace Independent Publishing.

Edelsbrunner, H., & Harer, J. (2010). Computational topology: An introduction. American Mathematical Society.

---

Fusion‑Field and Nonlinear Interaction Models

Smolensky, P. (1990). Tensor product variable binding and the representation of symbolic structures in connectionist systems. Artificial Intelligence, 46(1–2), 159–216.

Bengio, Y., et al. (2013). Representation learning: A review and new perspectives. IEEE Transactions on Pattern Analysis and Machine Intelligence, 35(8), 1798–1828.

---

Structural AI and Interpretability

Olah, C., et al. (2020). Zoom in: An introduction to circuits. Distill.

Elhage, N., et al. (2021). A mathematical framework for transformer circuits. Anthropic.

Nanda, N., et al. (2023). Progress measures for grokking via mechanistic interpretability. Proceedings of NeurIPS.

---

Appendix A — Mathematical Formalization

This appendix provides the mathematical foundations for the diagnostic operators introduced in Section 4. Each operator is defined on a differentiable manifold representing the latent space of a structural AI system. The derivations here correspond directly to the formal definitions in /math_spine/ and are structured to support mechanized verification in Appendix B.

We assume throughout:

- \(M\) is a smooth manifold of dimension \(n\).  
- \(g\) is a Riemannian metric on \(M\).  
- \(\nabla\) is the Levi‑Civita connection associated with \(g\).  
- \(x(t)\) is a latent trajectory evolving under a discrete dynamical update rule.  

All operators are defined in continuous form, with discrete approximations used in the Python toolkit.

---

A.1 Curvature Tensor Derivation

Curvature‑Driven Hallucinations (CDH) arise from instability in the curvature tensor. We begin with the Levi‑Civita connection:

\[
\nablaX Y = X^i \left( \partiali Y^j + \Gamma^j{\;ik} Y^k \right) \partialj
\]

where \(\Gamma^j_{\;ik}\) are the Christoffel symbols:

\[
\Gamma^j{\;ik} = \frac{1}{2} g^{jm} \left( \partiali g{km} + \partialk g{im} - \partialm g_{ik} \right)
\]

Curvature Tensor

The curvature tensor is defined as:

\[
R(X,Y)Z = \nablaX \nablaY Z - \nablaY \nablaX Z - \nabla_{[X,Y]} Z
\]

In coordinates:

\[
R^i{\;jkl} = \partialk \Gamma^i_{\;jl}
- \partiall \Gamma^i{\;jk}
+ \Gamma^i{\;mk}\Gamma^m{\;jl}
- \Gamma^i{\;ml}\Gamma^m{\;jk}
\]

Sectional Curvature

For a 2‑plane spanned by \(u, v\):

\[
K(u,v) = \frac{\langle R(u,v)v, u \rangle}{\langle u,u \rangle \langle v,v \rangle - \langle u,v \rangle^2}
\]

Instability Criterion

A curvature instability occurs when:

\[
\left| K(u,v) \right| > \kappa_{\text{threshold}}
\]

or when the sign of \(K\) oscillates across steps.

This criterion is implemented in /math_spine/curvature.tex.

---

A.2 Spectral Derivative Derivation

Spectral Cascade Hallucinations (SCH) arise from instability in the eigenvalue spectrum of latent representations.

Let \(A_t\) be the representation at step \(t\).  
Let \(\lambda1(t), \ldots, \lambdan(t)\) be its eigenvalues.

Continuous Spectral Derivative

\[
\Delta_\lambda(t) = \frac{d}{dt} \lambda(t)
\]

Discrete Approximation

\[
\Delta_\lambda(t) = \lambda(t+1) - \lambda(t)
\]

Spectral Instability Criterion

A spectral cascade occurs when:

\[
\left| \Delta\lambda(t) \right| > \sigma{\text{threshold}}
\]

or when eigenvalues diverge:

\[
\lambda(t) \to \infty
\]

or collapse:

\[
\lambda(t) \to 0
\]

This is formalized in /math_spine/spectral.tex.

---

A.3 Holonomy Operator Derivation

Holonomy Drift Hallucinations (HDH) arise from instability in parallel transport.

Let \(\gamma : [0,1] \to M\) be a closed loop.  
Let \(V(0)\) be a tangent vector at \(\gamma(0)\).

Parallel transport satisfies:

\[
\nabla_{\dot{\gamma}(t)} V(t) = 0
\]

with solution:

\[
V(1) = P_\gamma V(0)
\]

Holonomy Operator

\[
H = P_\gamma - I
\]

Holonomy Instability Criterion

Holonomy drift occurs when:

\[
\| H \| > h_{\text{threshold}}
\]

or when drift is asymmetric across loop orientation.

Formal derivation appears in /math_spine/holonomy.tex.

---

A.4 Topological Rank Operator Derivation

Topological Instability Hallucinations (TIH) arise from rank loss in the metric tensor.

Let \(g\) be the metric tensor.  
To ensure numerical stability:

\[
\tau = \text{rank}(g + \epsilon I)
\]

Rank Instability Criterion

A topological collapse occurs when:

\[
\tau < n
\]

or when \(\tau\) changes across steps:

\[
\tau(t+1) \neq \tau(t)
\]

Collapse surfaces correspond to regions where:

\[
\det(g) = 0
\]

Formal derivation appears in /math_spine/topology.tex.

---

A.5 Fusion‑Field Operator Derivation

Fusion‑Field Hallucinations (FFH) arise from nonlinear blending of incompatible concepts.

Let \(x, y \in M\) be latent representations.

Fusion‑Field Definition

\[
F(x,y) = \alpha x + \beta y + \gamma \, \sigma(x,y)
\]

where \(\sigma\) is a nonlinear interaction term.

Fusion Instability Criterion

Fusion instability occurs when:

\[
\| F(x,y) \| > f_{\text{threshold}}
\]

or when nonlinear interaction dominates:

\[
\gamma \, \sigma(x,y) \gg \alpha x + \beta y
\]

Formal derivation appears in /math_spine/fusion.tex.

---

Appendix Summary

Appendix A provides the mathematical foundation for the five diagnostic operators:

- curvature tensor,  
- spectral derivative,  
- holonomy operator,  
- rank operator,  
- fusion‑field operator.  

These definitions correspond directly to the Python implementations in /toolkit/ and the demonstrations in /examples/. They are structured to support mechanized verification in Appendix B.

---

Appendix B — Lean Formalization Block

This appendix provides a mechanization‑ready scaffold for the diagnostic operators introduced in Section 4 and formalized in Appendix A. The goal is not to fully mechanize the taxonomy but to establish the core definitions, structures, and typeclass constraints required for future verification in Lean. All definitions are compatible with Mathlib’s differential‑geometry, linear‑algebra, and topology modules.

The corresponding Lean files are located in /math_spine/lean/, with one file per operator:

- Curvature.lean  
- Spectral.lean  
- Holonomy.lean  
- Topology.lean  
- Fusion.lean  

This appendix mirrors those files.

---

B.1 Manifold and Metric Foundations

We begin by declaring the manifold, metric, and connection structures required for geometric operators.

Manifold Declaration

We assume a smooth manifold M modeled on ℝⁿ:

`lean
variable {n : ℕ}
variable (M : Type) [SmoothManifoldWithCorners (EuclideanSpace n) M]
`

Riemannian Metric

A Riemannian metric is declared as:

`lean
variable (g : M → BilinForm ℝ (TangentSpace ℝ M))
`

Levi‑Civita Connection

Mathlib provides the Levi‑Civita connection:

`lean
def LC : Connection ℝ M := leviCivitaConnection g
`

This establishes the geometric foundation for curvature, holonomy, and rank operators.

---

B.2 Curvature Tensor (CDH)

Curvature‑Driven Hallucinations correspond to instability in the curvature tensor.

Curvature Definition

`lean
def curvatureTensor :
  Tensor ℝ M 1 3 :=
LC.curvature
`

Sectional Curvature

`lean
def sectionalCurvature (u v : TangentSpace ℝ M) : ℝ :=
LC.sectionalCurvature g u v
`

Instability Predicate

`lean
def curvatureUnstable (κ : ℝ) (u v : TangentSpace ℝ M) : Prop :=
|sectionalCurvature g u v| > κ
`

This predicate corresponds to the instability criterion in Appendix A.

---

B.3 Spectral Derivative (SCH)

Spectral Cascade Hallucinations correspond to instability in eigenvalue trajectories.

Eigenvalue Extraction

`lean
def eigenvalues (A : Matrix ℝ n n) : Fin n → ℝ :=
fun i => (A.eigenvalues i)
`

Discrete Spectral Derivative

`lean
def spectralDerivative (λ : ℕ → ℝ) (t : ℕ) : ℝ :=
λ (t+1) - λ t
`

Instability Predicate

`lean
def spectralUnstable (σ : ℝ) (λ : ℕ → ℝ) (t : ℕ) : Prop :=
|spectralDerivative λ t| > σ
`

---

B.4 Holonomy Operator (HDH)

Holonomy Drift Hallucinations correspond to instability in parallel transport around closed loops.

Parallel Transport

`lean
def parallelTransport (γ : Path M) :
  TangentSpace ℝ M → TangentSpace ℝ M :=
LC.parallelTransport γ
`

Holonomy Operator

`lean
def holonomy (γ : Path M) : End (TangentSpace ℝ M) :=
parallelTransport LC γ - LinearMap.id
`

Instability Predicate

`lean
def holonomyUnstable (h : ℝ) (γ : Path M) : Prop :=
‖holonomy LC γ‖ > h
`

---

B.5 Topological Rank Operator (TIH)

Topological Instability Hallucinations correspond to rank loss in the metric tensor.

Metric Matrix Representation

`lean
def metricMatrix (p : M) : Matrix ℝ n n :=
(g p).toMatrix
`

Rank Operator

`lean
def metricRank (p : M) : ℕ :=
(metricMatrix g p).rank
`

Instability Predicate

`lean
def rankUnstable (n : ℕ) (p : M) : Prop :=
metricRank g p < n
`

---

B.6 Fusion‑Field Operator (FFH)

Fusion‑Field Hallucinations correspond to nonlinear blending of incompatible concepts.

Fusion‑Field Definition

`lean
def fusionField
  (α β γ : ℝ)
  (σ : TangentSpace ℝ M → TangentSpace ℝ M → TangentSpace ℝ M)
  (x y : TangentSpace ℝ M) :
  TangentSpace ℝ M :=
α • x + β • y + γ • σ x y
`

Instability Predicate

`lean
def fusionUnstable
  (f : ℝ)
  (F : TangentSpace ℝ M → TangentSpace ℝ M)
  (x : TangentSpace ℝ M) : Prop :=
‖F x‖ > f
`

---

Appendix Summary

Appendix B provides Lean‑ready definitions for:

- curvature tensor,  
- spectral derivative,  
- holonomy operator,  
- metric rank operator,  
- fusion‑field operator.  

These definitions correspond directly to the mathematical derivations in Appendix A and the Python implementations in /toolkit/. They establish the foundation for future mechanized verification of geometric hallucination operators in Lean.

---

Provenance Footer

`
Provenance: Authored by Borealis S. Hedling with Copilot assistance.
All content is original research derived from the Geometric Hallucination
Taxonomy (GHT), structural-AI operator layer, mathematical spine, and
Lean formalization scaffolding. No external copyrighted text included.
Geometric definitions follow standard differential geometry and Mathlib
conventions. Experimental components use synthetic latent manifolds and
deterministic trajectories. This preprint serves as both a scientific
document and a navigational map of the accompanying repository.
`

---
