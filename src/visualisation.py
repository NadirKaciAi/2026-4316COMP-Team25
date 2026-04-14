import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
# Import the data loader from your group's main project
from data_loader_Aymen import DataLoader

# 1. LOAD DATA
loader = DataLoader()
data_raw = loader.load_data()
df = pd.DataFrame(data_raw) # Converting to DataFrame for easier plotting

# Ensure numeric columns are floats
cols = [f"Skill_{i}" for i in range(1, 11)] + ["AI_Exposure_Index"]
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# DIAGRAM 1: Top 7 High-Risk Jobs (Bar Chart)
plt.figure(figsize=(10, 6))
top_exposed = df.nlargest(10, 'AI_Exposure_Index')
sns.barplot(x='AI_Exposure_Index', y='Job_Title', data=top_exposed, palette='Reds_r')
plt.title("Top 10 Jobs at Risk of AI Exposure")

# Diagram 2: Skill Correlation (Heatmap)
plt.figure(figsize=(12, 8))
correlation_matrix = df[cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation: Skills vs. AI Exposure")

# --- DIAGRAM 3: AI risk distribution (Box Plot) ---
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['AI_Exposure_Index'], color='lightblue')
plt.title("Distribution of AI Exposure Across All Jobs")

# --- DIAGRAM 4: Sample Skill Radar (Radar Chart)
labels = [f"S{i}" for i in range(1, 11)]
stats = df.iloc[0][cols[:-1]].values # Example using the first job in the list
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
stats = np.concatenate((stats, [stats[0]])) # Close the loop
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='red', alpha=0.25)
ax.plot(angles, stats, color='red', linewidth=2)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.title(f"Skill Profile: {df.iloc[0]['Job_Title']}")

# FINAL COMMAND TO SHOW ALL WINDOWS
plt.show()