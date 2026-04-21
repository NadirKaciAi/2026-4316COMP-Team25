import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from data_loader_Aymen import DataLoader

# 1. LOAD DATA
loader = DataLoader()
data_raw = loader.load_data()
df = pd.DataFrame(data_raw)

# Ensure numeric columns are floats
cols = [f"Skill_{i}" for i in range(1, 11)] + ["AI_Exposure_Index"]
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# Diagram 1: Skill Correlation (Heatmap)
plt.figure(figsize=(12, 8))
correlation_matrix = df[cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation: Skills vs. AI Exposure")

# Diagram 2: Sample Skill Radar (Radar Chart)
labels = [f"S{i}" for i in range(1, 11)]
stats = df.iloc[0][cols[:-1]].values
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
stats = np.concatenate((stats, [stats[0]]))
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, stats, color='red', alpha=0.25)
ax.plot(angles, stats, color='red', linewidth=2)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.title(f"Skill Profile: {df.iloc[0]['Job_Title']}")

plt.show()