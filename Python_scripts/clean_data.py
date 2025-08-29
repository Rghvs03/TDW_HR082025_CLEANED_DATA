import pandas as pd

# Load the CSV
df = pd.read_csv("channel_master (1).csv")

print("Original shape:", df.shape)

# Step 1: Removed duplicate rows
df = df.drop_duplicates()

# Step 2: Dropped useless column (all missing)
df = df.drop(columns=["totalviews"])

# Step 3: Handled missing values
# Dropped rows where 'subscribercount' is missing
df = df.dropna(subset=["subscribercount"])

# For 'shortdescription', replaced missing with "No description"
df["shortdescription"] = df["shortdescription"].fillna("No description")

print("✅ After cleaning, shape:", df.shape)

# Saving cleaned CSV
df.to_csv("channel_master_cleaned.csv", index=False)

print("🎉 Cleaned file saved as 'channel_master_cleaned.csv'")
