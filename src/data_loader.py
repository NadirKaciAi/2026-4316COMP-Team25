import pandas as pd
from pathlib import Path


class DataLoader:
    """Loads data from the project's CSV file."""

    def __init__(self):
        # Find the project root directory
        base_dir = Path(__file__).resolve().parent.parent

        # Path to the CSV file
        self.file_path = base_dir / "data" / "data.csv"

    def load_data(self):
        """Load the CSV file and return it as a pandas DataFrame."""
        try:
            data = pd.read_csv(self.file_path)
            return data
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            return pd.DataFrame()


if __name__ == "__main__":
    loader = DataLoader()
    data = loader.load_data()
    print(data.head())