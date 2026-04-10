import csv
from pathlib import Path

    # Class to create a list of dictionairies for the data (each line is a dictionary)
class DataLoader:
    """Loads and validates data from the project's CSV file."""

    def __init__(self):
        # Find the project root directory
        base_dir = Path(__file__).resolve().parent.parent
        
        # Path to the CSV file
        self.file_path = base_dir / "data" / "data.csv"


    def load_data(self):
        """Load the CSV file and return the data as a list of dictionaries."""
        
        data = []

        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    data.append(row)

        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")

        return data   
    
if __name__ == "__main__":
    loader = DataLoader()
    data = loader.load_data()
    
