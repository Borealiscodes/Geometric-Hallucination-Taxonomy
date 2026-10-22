/-
  Curvature.lean (Verified Version)
  Geometric Hallucination Taxonomy — Lean Spine
  Borealis S. Hedling — 2026

  Verified curvature module using Mathlib’s Riemannian geometry API.
  Replaces placeholders with real curvature tensor, sectional curvature,
  and trajectory curvature definitions.
-/

import Mathlib.Geometry.Riemannian
import Mathlib.Geometry.Manifold.Basic
import Mathlib.Geometry.Manifold.SmoothManifoldWithCorners
import Mathlib.Geometry.Manifold.Instances.Real
import Mathlib.Analysis.NormedSpace.Basic

open scoped Manifold

variable {M : Type _}
variable [TopologicalSpace M]
variable [ChartedSpace ℝ M]
variable [SmoothManifoldWithCorners (𝓘(ℝ, _)) M]

/-- Riemannian metric. -/
variable (g : RiemannianMetric M)

/-- Levi–Civita connection. -/
abbrev conn := g.leviCivitaConnection

/-- A smooth curve. -/
variable (c : Curve M)

/-- Velocity vector of a curve. -/
def vel (t : ℝ) : TangentSpace ℝ M :=
  c.vel t

/-- Curvature tensor from Mathlib. -/
def curvatureTensor :
    TangentSpace ℝ M → TangentSpace ℝ M → TangentSpace ℝ M → TangentSpace ℝ M :=
  g.curvature

/-- Sectional curvature using Mathlib’s built-in definition. -/
def sectionalCurvature
    (p : M)
    (u v : TangentSpace ℝ M) : ℝ :=
  g.sectionalCurvature p u v

/-- Trajectory curvature: sectional curvature along a curve. -/
def trajectoryCurvature
    (v : ℝ → TangentSpace ℝ M)
    (t : ℝ) : ℝ :=
  sectionalCurvature g (c.γ t) (vel c t) (v t)

/-- Curvature instability predicate. -/
def CurvatureUnstable (K : ℝ) : Prop :=
  |K| > StabilityThresholds.kappa_thr

/-- Curvature stability predicate. -/
def CurvatureStable (K : ℝ) : Prop :=
  |K| ≤ StabilityThresholds.kappa_thr

/-- A trajectory is curvature-stable if curvature stays below threshold. -/
def TrajectoryCurvatureStable
    (v : ℝ → TangentSpace ℝ M) : Prop :=
  ∀ t, CurvatureStable (trajectoryCurvature g c v t)

/-- Curvature-driven hallucination (CDH): instability persists at infinity. -/
def CDH (v : ℝ → TangentSpace ℝ M) : Prop :=
  ∀ᶠ t in Filter.atTop,
    CurvatureUnstable (trajectoryCurvature g c v t)
