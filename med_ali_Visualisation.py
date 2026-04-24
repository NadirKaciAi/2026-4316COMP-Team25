import sys
import os

# This tells Python to look inside the 'src' folder for your modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Now we can import your logic functions
from risk_analysis_med_ali import load_data, avg_risk_by_education, get_probability
def show_graphs():
    data = load_data()
    if not data:
        print("Could not load data.")
        return

    try:
        import matplotlib.pyplot as plt
        
        # --- Prepare Data for Bar Chart ---
        education_dict = {}
        for job in data:
            edu = job["Education_Level"]
            prob = get_probability(job)
            if edu not in education_dict:
                education_dict[edu] = []
            education_dict[edu].append(prob)

        # Calculate Averages
        names = []
        averages = []
        for edu, probs in education_dict.items():
            names.append(edu)
            averages.append(sum(probs) / len(probs))

        # --- Create the Bar Chart ---
        plt.figure(figsize=(10, 6))
        plt.bar(names, averages, color='skyblue')
        plt.title('Average AI Risk by Education Level (2030)')
        plt.ylabel('Risk Probability')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        print("Displaying Graph...")
        plt.show()

    except ImportError:
        print("\n[!] Matplotlib not found. Showing text summary instead:")
        avg_risk_by_education(data)

if __name__ == "__main__":
    show_graphs

