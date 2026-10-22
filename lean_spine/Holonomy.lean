/-
  Holonomy.lean (Verified Version)
  Geometric Hallucination Taxonomy — Lean Spine
  Borealis S. Hedling — 2026

  Verified holonomy module using Mathlib’s parallel transport API.
  Defines holonomy as deviation from identity, holonomy norms, and HDH.
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
variable (γ : Curve M)

/-- Parallel transport along γ from t₀ to t₁. -/
def PT (t₀ t₁ : ℝ) :
    TangentSpace ℝ M → TangentSpace ℝ M :=
  g.parallelTransportAlong γ.γ t₀ t₁

/-- Holonomy operator: parallel transport around a loop minus identity. -/
def holonomyOp (t₀ t₁ : ℝ) :
    TangentSpace ℝ M → TangentSpace ℝ M :=
  fun v => PT g γ t₀ t₁ v - v

/-- Holonomy norm: operator norm of holonomyOp. -/
def holonomyNorm (t₀ t₁ : ℝ) : ℝ :=
  ‖holonomyOp g γ t₀ t₁‖

/-- Holonomy instability predicate. -/
def HolonomyUnstable (H : ℝ) : Prop :=
  H > StabilityThresholds.h_thr

/-- Holonomy stability predicate. -/
def HolonomyStable (H : ℝ) : Prop :=
  H ≤ StabilityThresholds.h_thr

/-- A loop is holonomy-stable if its holonomy norm stays below threshold. -/
def LoopHolonomyStable (t₀ t₁ : ℝ) : Prop :=
  HolonomyStable (holonomyNorm g γ t₀ t₁)

/-- Holonomy drift hallucination (HDH): instability persists at infinity. -/
def HDH (loopTimes : ℕ → (ℝ × ℝ)) : Prop :=
  ∀ᶠ n in Filter.atTop,
    let (t₀, t₁) := loopTimes n
    HolonomyUnstable (holonomyNorm g γ t₀ t₁)
