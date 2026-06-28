"""Smoke test for Grid Stability & Climate Complexity Collapse logic."""

from __future__ import annotations

import sys
from pathlib import Path

# Resolve path
ROOT = Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(ROOT))

from scripts.run_climate_grid_complexity_collapse import simulate_grid_manifold, run_kaggle_baseline

def test_grid_stability_simulation_and_baseline_contract() -> None:
    # 1. Simulate a small batch of grid states
    X_raw, X_clean, y, coords = simulate_grid_manifold(n_samples=200, n_features=10, noise_level=0.5)
    
    assert X_raw.shape == (200, 10)
    assert X_clean.shape == (200, 10)
    assert y.shape == (200,)
    assert coords.shape == (200, 3)
    
    # 2. Run Kaggle baseline evaluations
    f1_raw, t_raw = run_kaggle_baseline(X_raw, y)
    assert 0.0 <= f1_raw <= 1.0
    assert 0.2 <= t_raw <= 0.8
    
    print(f"Verified grid stability contract: F1={f1_raw:.4f} at threshold {t_raw:.3f}")
