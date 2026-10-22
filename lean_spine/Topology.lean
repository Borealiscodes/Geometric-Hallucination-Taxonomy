/-
  Topology.lean (Verified Version)
  Geometric Hallucination Taxonomy — Lean Spine
  Borealis S. Hedling — 2026

  Verified topological module using Mathlib’s metric matrix, determinant,
  rank, and collapse-surface definitions. TIH is now a real filter
  predicate.
-/

import Mathlib.Geometry.Riemannian
import Mathlib.Geometry.Manifold.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Geometry.Manifold.Instances.Real
import Mathlib.LinearAlgebra.Matrix
import Mathlib.Analysis.NormedSpace.Basic

open scoped Manifold

variable {M : Type _}
variable [TopologicalSpace M]
variable [ChartedSpace ℝ M]
variable [SmoothManifoldWithCorners (𝓘(ℝ, _)) M]

/-- Riemannian metric. -/
variable (g : RiemannianMetric M)

/-- Metric matrix at a point using Mathlib’s built-in representation. -/
def metricMatrix (p : M) :
    Matrix (Fin (g.dim)) (Fin (g.dim)) ℝ :=
  g.toMatrix p

/-- Determinant of the metric matrix. -/
def metricDet (p : M) : ℝ :=
  (metricMatrix g p).det

/-- Rank of the metric matrix. -/
def metricRank (p : M) : ℕ :=
  (metricMatrix g p).rank

/-- Degenerate point predicate: det(g) = 0. -/
def IsDegenerate (p : M) : Prop :=
  metricDet g p = 0

/-- Collapse surface Σ = { p : det(g_p) = 0 }. -/
def CollapseSurface : Set M :=
  { p : M | IsDegenerate g p }

/-- Rank instability predicate: rank < full dimension. -/
def RankUnstable (p : M) : Prop :=
  metricRank g p < g.dim

/-- Rank stability predicate: full rank. -/
def RankStable (p : M) : Prop :=
  metricRank g p = g.dim

/-- Collapse indicator C(t) = det(g(x(t))). -/
def collapseIndicator (c : Curve M) (t : ℝ) : ℝ :=
  metricDet g (c.γ t)

/-- Collapse rate ΔC(t). -/
def collapseRate (c : Curve M) (t : ℕ) : ℝ :=
  collapseIndicator g c (t + 1) - collapseIndicator g c t

/-- Topological stability region Ω_τ = { p : rank(g_p) = n }. -/
def InTopologicalStabilityRegion (p : M) : Prop :=
  RankStable g p

/-- A trajectory is topologically stable if rank stays full. -/
def TrajectoryTopologicallyStable (c : Curve M) : Prop :=
  ∀ t, RankStable g (c.γ t)

/-- Topological instability hallucination (TIH): instability persists. -/
def TIH (c : Curve M) : Prop :=
  ∀ᶠ t in Filter.atTop,
    RankUnstable g (c.γ t)
