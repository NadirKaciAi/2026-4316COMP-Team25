from pathlib import Path
import csv


class DataLoader:
    """
    Loads and cleans CSV data for the group project.
    """

    def __init__(self):
        # Project root (works for all teammates)
        self.base_dir = Path(__file__).resolve().parent.parent

        # Dataset path (inside /data folder)
        self.file_path = self.base_dir / "data" / "data.csv"

    def load_data(self):
        """Load and clean dataset, return as list of dictionaries."""

        data = []

        print("\nLoading the dataset...\n")

        # Load CSV file
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    data.append(row)

        except FileNotFoundError:
            print(f"ERROR: File not found at {self.file_path}")
            return []
        
        # Get columns
        columns = list(data[0].keys()) if data else []

        # Missing values per column
        missing_counts = {col: 0 for col in columns}

        for row in data:
            for col in columns:
                if row[col] == "" or row[col] is None:
                    missing_counts[col] += 1

        # Drop empty columns
        columns_to_keep = [
            col for col in columns
            if any(row[col] not in ("", None) for row in data)
        ]

        # Cleaned dataset (in memory only)
        cleaned_data = [
            {col: row[col] for col in columns_to_keep}
            for row in data
        ]

        return cleaned_data

if __name__ == "__main__":
    loader = DataLoader()
    data = loader.load_data()

    print("\nDATA LOADED SUCCESSFULLY (:")