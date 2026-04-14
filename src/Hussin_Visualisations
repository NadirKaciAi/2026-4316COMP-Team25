import pandas as pd
import matplotlib.pyplot as plt
from data_loader_Aymen import DataLoader

# use the data loader
loader = DataLoader()
data = loader.load_data()

# convert loaded data to pandas DataFrame
df = pd.DataFrame(data)

# convert columns to numbers
df["AI_Exposure_Index"] = pd.to_numeric(df["AI_Exposure_Index"])
df["Automation_Probability_2030"] = pd.to_numeric(df["Automation_Probability_2030"])

# Visualisation 1
top_exposure = df.sort_values("AI_Exposure_Index", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_exposure["Job_Title"], top_exposure["AI_Exposure_Index"])
plt.xlabel("AI Exposure Index")
plt.ylabel("Job Title")
plt.title("Top 10 Jobs by AI Exposure Index")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Visualisation 2
plt.figure(figsize=(8, 6))
plt.scatter(df["AI_Exposure_Index"], df["Automation_Probability_2030"])
plt.xlabel("AI Exposure Index")
plt.ylabel("Automation Probability")
plt.title("AI Exposure vs Automation Probability")
plt.tight_layout()
plt.show()

# Visualisation 3
avg_exposure = df.groupby("Education_Level")["AI_Exposure_Index"].mean()

plt.figure(figsize=(8, 6))
avg_exposure.plot(kind="bar")
plt.xlabel("Education Level")
plt.ylabel("Average AI Exposure")
plt.title("AI Exposure by Education Level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualisation 4
filtered = df[
    (df["AI_Exposure_Index"] > 0.7) &
    (df["Automation_Probability_2030"] < 0.5)
].head(10)

plt.figure(figsize=(10, 6))
plt.barh(filtered["Job_Title"], filtered["AI_Exposure_Index"])
plt.xlabel("AI Exposure Index")
plt.ylabel("Job Title")
plt.title("High Exposure but Low Automation")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()