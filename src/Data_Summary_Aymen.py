from data_loader_Aymen import DataLoader
import matplotlib.pyplot as plt


# Function --> Basic Info
def show_basic_info(data, columns):
    print("\nBasic Information:")
    print(f"Total Records: {len(data)}")
    print(f"Total Columns: {len(columns)}")


# Function --> Column Names
def show_columns(columns):
    print("\nColumns:")
    for col in columns:
        print(f" - {col}")


# Function --> Missing Values
def show_missing_values(data, columns):
    missing_counts = {col: 0 for col in columns}

    for row in data:
        for col in columns:
            if row[col] == "" or row[col] is None:
                missing_counts[col] += 1

    print("\nMissing Values:")
    for col, count in missing_counts.items():
        print(f"{col}: {count}")


# Function --> Numeric Stats
def show_numeric_stats(data, numeric_columns):
    print("\nNumeric Column Statistics:")

    for col in numeric_columns:
        values = []

        for row in data:
            try:
                values.append(float(row[col]))
            except:
                continue

        if values:
            print(f"\n{col}:")
            print(f" Min: {min(values)}")
            print(f" Max: {max(values)}")
            print(f" Avg: {round(sum(values)/len(values), 2)}")


# Function --> Text Summary
def show_text_summary(data, columns, numeric_columns):
    print("\nText Column Summary:")

    for col in columns:
        if col not in numeric_columns:
            unique_values = set(row[col] for row in data if row[col])
            print(f"{col}: {len(unique_values)} unique values")


# Function --> Sample Data
def show_sample_data(data):
    print("\nSample Data (First 5 Rows):")
    for row in data[:5]:
        print(row)


# Function --> Missing Values Visualisation
def plot_missing_values(data, columns):
    missing_counts = {col: 0 for col in columns}

    for row in data:
        for col in columns:
            if row[col] == "" or row[col] is None:
                missing_counts[col] += 1

    plt.figure(figsize=(10, 5))
    plt.bar(missing_counts.keys(), missing_counts.values())
    plt.title("Missing Values per Column")
    plt.xlabel("Columns")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Function --> Salary Statistics Visualisation
def plot_salary_stats(data):
    salaries = []

    for row in data:
        try:
            salaries.append(float(row["Average_Salary"]))
        except:
            continue

    stats = {
        "Min Salary": min(salaries),
        "Avg Salary": sum(salaries) / len(salaries),
        "Max Salary": max(salaries)
    }

    plt.figure(figsize=(8, 5))
    plt.bar(stats.keys(), stats.values())
    plt.title("Salary Statistics")
    plt.ylabel("Salary (£)")
    plt.tight_layout()
    plt.show()

# Function --> Main Menu
def run_data_summary():
    loader = DataLoader()
    data = loader.load_data()

    if not data:
        print("No data loaded.")
        return

    columns = list(data[0].keys())

    # Detect numeric columns ONCE
    numeric_columns = []
    for col in columns:
        try:
            float(data[0][col])
            numeric_columns.append(col)
        except:
            pass

    # Menu loop
    while True:
        print("\n" + "="*50)
        print("            Data Summary Menu")
        print("="*50)
        print("1. Basic Info (Rows, Columns)")
        print("2. Column Names")
        print("3. Missing Values")
        print("4. Numeric Statistics")
        print("5. Text Summary (Unique Values)")
        print("6. Sample Data")
        print("7. Show Missing Values Graph")
        print("8. Salary Statistics Graph")
        print("9. Back to Main Menu")
        print("="*50)

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            show_basic_info(data, columns)

        elif choice == "2":
            show_columns(columns)

        elif choice == "3":
            show_missing_values(data, columns)

        elif choice == "4":
            show_numeric_stats(data, numeric_columns)

        elif choice == "5":
            show_text_summary(data, columns, numeric_columns)

        elif choice == "6":
            show_sample_data(data)

        elif choice == "7":
            plot_missing_values(data, columns)

        elif choice == "8":
            plot_salary_stats(data)

        elif choice == "9":
            print("Returning to main menu... Goodbye! 👋")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    run_data_summary()
