from __future__ import annotations

from pathlib import Path

import pandas as pd


EXPECTED_FILES = [
    Path("data_clean/demographics.csv"),
    Path("data_clean/students.csv"),
    Path("data_clean/subsidies.csv"),
    Path("TRANSFORMATION/forecast_demographic.csv"),
    Path("TRANSFORMATION/forecast_subsidy_final.csv"),
]


def assert_file_exists(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing expected file: {path}")
    if path.stat().st_size == 0:
        raise ValueError(f"Empty file: {path}")


def validate_dataframe(path: Path, required_columns: list[str] | None = None) -> None:
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"No rows in {path}")
    if required_columns:
        missing = [c for c in required_columns if c not in df.columns]
        if missing:
            raise ValueError(f"Missing columns in {path}: {missing}")


def main() -> None:
    for path in EXPECTED_FILES:
        assert_file_exists(path)

    validate_dataframe(
        Path("data_clean/demographics.csv"),
        required_columns=["Districts & Neigbourhoods", "Year"],
    )
    validate_dataframe(
        Path("data_clean/students.csv"),
        required_columns=["education_type", "year", "students"],
    )
    validate_dataframe(
        Path("data_clean/subsidies.csv"),
        required_columns=["subsidy_year", "Education", "Care"],
    )
    validate_dataframe(
        Path("TRANSFORMATION/forecast_demographic.csv"),
        required_columns=["Neighbourhood", "Indicator", "Year", "Forecast"],
    )
    validate_dataframe(
        Path("TRANSFORMATION/forecast_subsidy_final.csv"),
        required_columns=["subsidy_year", "Education", "Care"],
    )

    print("Validation passed.")


if __name__ == "__main__":
    main()
