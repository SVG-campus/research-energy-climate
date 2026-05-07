"""Smoke: HF domain charter stream schema for research-energy-climate."""

from __future__ import annotations

from datasets import load_dataset


def test_open_meteo_stream_schema() -> None:
    rows = list(
        load_dataset(
            "MWasil/Open_Meteo_weather_dataset_from_2024_to_2025",
            split="train",
            streaming=True,
        ).take(12)
    )
    assert len(rows) == 12
    for r in rows:
        assert "temperature_2m" in r and "precipitation" in r
