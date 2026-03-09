import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.data_loader import DataLoader


def test_data_loads():
    loader = DataLoader()
    data = loader.load_data()

    # Check that something was loaded
    assert len(data) > 0


def test_rows_are_dictionaries():
    loader = DataLoader()
    data = loader.load_data()

    # Check first row is a dictionary
    assert isinstance(data[0], dict)


def test_expected_columns_exist():
    loader = DataLoader()
    data = loader.load_data()

    # Check column names exist
    expected_columns = ["name", "age", "city"]  # change to your CSV headers

    for column in expected_columns:
        assert column in data[0]