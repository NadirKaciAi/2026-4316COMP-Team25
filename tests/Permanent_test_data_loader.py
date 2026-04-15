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

        # =========================
        # Load CSV file
        # =========================
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    data.append(row)

        except FileNotFoundError:
            print(f"ERROR: File not found at {self.file_path}")
            return []

        # =========================
        # Basic info
        # =========================
        print("First 5 Rows:\n", data[:5], "\n")
        print("Total Rows:", len(data), "\n")

        # Get columns
        columns = list(data[0].keys()) if data else []
        print("Columns:\n", columns, "\n")

        # =========================
        # Missing values per column
        # =========================
        missing_counts = {col: 0 for col in columns}

        for row in data:
            for col in columns:
                if row[col] == "" or row[col] is None:
                    missing_counts[col] += 1

        print("Missing Values Per Column:\n", missing_counts, "\n")

        # =========================
        # Drop empty columns
        # =========================
        columns_to_keep = [
            col for col in columns
            if any(row[col] not in ("", None) for row in data)
        ]

        print("Columns After Dropping:\n", columns_to_keep, "\n")

        # =========================
        # Cleaned dataset (in memory only)
        # =========================
        cleaned_data = [
            {col: row[col] for col in columns_to_keep}
            for row in data
        ]

        print("Cleaned Dataset Preview:\n", cleaned_data[:5], "\n")

        return cleaned_data


# =========================
# THIS FIX MAKES IT RUN
# =========================
if __name__ == "__main__":
    loader = DataLoader()
    data = loader.load_data()

    print("\nDATA LOADED SUCCESSFULLY (:")