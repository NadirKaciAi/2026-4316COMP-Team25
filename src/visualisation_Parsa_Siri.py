import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from data_loader_Aymen import DataLoader

# using dataloader to load data into the visualisation
loader = DataLoader()
data_raw = loader.load_data()
df = pd.DataFrame(data_raw)

# ensuring numeric columns are floats (errors='coerce' turns any bad values into NaN instead of crashing)
skill_cols = [f"Skill_{i}" for i in range(1, 11)]
cols = skill_cols + ["AI_Exposure_Index"]
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
df["Job_Title"] = df["Job_Title"].astype(str).str.strip()


# Diagram 1: Skill Correlation (Heatmap)
def plot_heatmap():
    # plt.figure() creates a new figure window with a set size
    plt.figure(figsize=(12, 8))

    # .corr() builds a correlation matrix between all numeric columns
    correlation_matrix = df[cols].corr()

    # annot=True writes the number inside each cell, fmt=".2f" rounds it to 2 decimals
    # cmap='coolwarm' = red for positive correlation, blue for negative, white for none
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f",
                cbar_kws={'label': 'Correlation coefficient'})
    plt.title("Correlation: Skills vs. AI Exposure")

    # tight_layout() stops labels from getting cut off at the edges
    plt.tight_layout()
    plt.show()


# Diagram 2: Skill Radar (Radar Chart)
def plot_radar():
    print("\nRadar Chart — Skill Profile")
    print("You can enter 1 or 2 job titles (comma-separated) to compare.")
    user_input = input("Enter job title(s) (or press Enter to use row 0): ").strip()

    # Shorter labels so they fit neatly around the radar
    labels = [f"S{i}" for i in range(1, 11)]

    # linspace generates 10 evenly spaced angles around the circle (0 to 2π radians)
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

    # Repeat the first angle at the end so the polygon closes up instead of leaving a gap
    angles += angles[:1]

    # subplot_kw=dict(polar=True) tells matplotlib to use polar (circular) coordinates instead of x/y
    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

    # If the user didn't type anything, fall back to the first row of the dataset
    if user_input == "":
        row = df.iloc[0]
        stats = row[skill_cols].values
        # Same trick as with angles — repeat the first value so the shape closes
        stats = np.concatenate((stats, [stats[0]]))
        # fill() shades the polygon, plot() draws the outline on top
        ax.fill(angles, stats, color='red', alpha=0.25)
        ax.plot(angles, stats, color='red', linewidth=2, label=row['Job_Title'])
        title = f"Skill Profile: {row['Job_Title']}"
    else:
        # Split on commas, clean whitespace, keep up to 2 jobs max
        job_inputs = [j.strip().lower() for j in user_input.split(",") if j.strip()][:2]
        colours = ['red', 'blue']
        matched = []

        for i, job in enumerate(job_inputs):
            # Case-insensitive partial match on job title
            match = df[df["Job_Title"].str.lower().str.contains(job, na=False)]
            if match.empty:
                print(f"  No match found for '{job}'.")
                continue

            row = match.iloc[0]
            stats = row[skill_cols].values
            stats = np.concatenate((stats, [stats[0]]))
            ax.fill(angles, stats, color=colours[i], alpha=0.25)
            ax.plot(angles, stats, color=colours[i], linewidth=2, label=row['Job_Title'])
            matched.append(row['Job_Title'])

        # If nothing matched at all, close the empty figure and bail out
        if not matched:
            print("  No valid jobs found — cancelling chart.")
            plt.close(fig)
            return

        title = "Skill Profile Comparison" if len(matched) > 1 else f"Skill Profile: {matched[0]}"

    # Hide the numeric ticks on the radial axis (keeps it cleaner)
    ax.set_yticklabels([])
    # Put the skill labels at each of the 10 angle points
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    # bbox_to_anchor nudges the legend outside the plot area so it doesn't overlap
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.title(title)
    plt.tight_layout()
    plt.show()


# Menu loop
def run_visualisation():
    while True:
        print("\n=== Visualisation Menu ===")
        print("1. Skill Correlation Heatmap")
        print("2. Skill Profile Radar Chart")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            plot_heatmap()
        elif choice == "2":
            plot_radar()
        elif choice == "3":
            print("Exiting Visualisation.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    run_visualisation()