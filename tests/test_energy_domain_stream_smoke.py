"""Smoke: HF domain charter stream schema for research-energy-climate."""

from __future__ import annotations

import json
import math
import numbers
from pathlib import Path

from datasets import load_dataset

from methodology_preamble import load_smoke_caps

_FIXTURE = Path(__file__).resolve().parent / "fixtures" / "open_meteo_stream_sample.json"
_PINNED_OPEN_METEO = "MWasil/Open_Meteo_weather_dataset_from_2024_to_2025"


def _assert_open_meteo_row_contract(row: object) -> None:
    assert isinstance(row, dict)
    assert "temperature_2m" in row and "precipitation" in row
    t_raw, p_raw = row["temperature_2m"], row["precipitation"]
    assert isinstance(t_raw, numbers.Real) and math.isfinite(float(t_raw))
    assert isinstance(p_raw, numbers.Real) and math.isfinite(float(p_raw))


def test_open_meteo_pinned_stream_offline_fixture_matches_charter_schema() -> None:
    """Pinned `datasets.yaml` stream (`MWasil/...Open_Meteo...`): schema without Hub I/O."""
    payload = json.loads(_FIXTURE.read_text(encoding="utf-8"))
    assert isinstance(payload, list)
    assert len(payload) == 12
    for row in payload:
        _assert_open_meteo_row_contract(row)


def test_open_meteo_charter_perm_budget_respects_smoke_yaml_cap() -> None:
    """`CHARTER_OPEN_METEO_STREAM_SMOKE` uses n_perm = max(39, min(149, n_perm_max))."""
    caps = load_smoke_caps()["methodology_caps"]["permutation_test"]
    n_perm_max = int(caps["n_perm_max"])
    n_perm = max(39, min(149, n_perm_max))
    assert n_perm_max >= 39, (
        "n_perm_max below 39 breaks the charter clamp vs smoke.yaml cap "
        "(notebook would run more permutations than methodology_caps allow)."
    )
    assert 39 <= n_perm <= 149
    assert n_perm <= n_perm_max


def test_open_meteo_stream_schema() -> None:
    rows = list(
        load_dataset(_PINNED_OPEN_METEO, split="train", streaming=True).take(12)
    )
    assert len(rows) == 12
    for r in rows:
        _assert_open_meteo_row_contract(r)
