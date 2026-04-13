import pandas as pd
 
# Load the Dataset.
data = pd.read_csv("AI_Impact_on_Jobs_2030.csv")

#Explore the Dataset.
print("First 5 Rows:\n", data.head(), "\n")
print("Dataset Info:\n", data.info(), "\n")
print("Summary Statistics:\n",data.describe(), "\n")
print("Missing Values Per Column:\n",data.isnull().sum(), "\n")

# Drops All the Columns that Are Empty.
data = data.dropna(axis=1, how="all")
print("Columns After Dropping:\n", data.columns, "\n")

# Fill Missing Values: Numeric -> 0, Text -> "Unknown".
data = data.fillna(value={col: 0 if data[col].dtype != "object" else "Unknown" for col in data.columns})

# Clean Columns Names.
data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_", regex=True)

# Check the Dataset.
print("Cleaned Dataset:\n", data.head(), "\n")
print("Any Missing Values?\n", data.isnull().sum())

# Save the Clean Dataset.
data.to_csv("AI_Jobs_Cleaned.csv", index=False)
    
