import pandas as pd

# Load the raw CSV file
df = pd.read_csv("video_summary_uat.csv")

# First 5 rows check karne ke liye
print(df.head())

print(df.info())       # column data types
print(df.isnull().sum())  # missing values count

# Step 3: Handle Missing Data

# Drop completely useless column (all values NaN)
if df['totalviews'].isnull().all():
    df = df.drop(columns=['totalviews'])
    print("Dropped column: totalviews (all values were NaN)")

# Drop rows where essential fields are missing
df = df.dropna(subset=['Channelid', 'channelname', 'title', 'uploader', 'channelurl'])

# Fill missing subscriber count with 0
df['subscribercount'] = df['subscribercount'].fillna(0)

# Fill missing shortdescription with "No description"
df['shortdescription'] = df['shortdescription'].fillna("No description available")

# Fill missing last_upload_date with "Unknown"
df['last_upload_date'] = df['last_upload_date'].fillna("Unknown")

print("\n✅ Missing values handled successfully!")
print("Remaining missing values per column:\n", df.isnull().sum())

# Step 4: Remove Duplicates & Reset Index

before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print(f"\n✅ Removed {before - after} duplicate rows")

# Reset index
df = df.reset_index(drop=True)
print("✅ Index reset successfully")

# Step 5: Save the Cleaned File

import os

# Create folder if not exists
output_folder = "cleaned_data"
os.makedirs(output_folder, exist_ok=True)

# Save file
output_path = os.path.join(output_folder, "video_summary_cleaned.csv")
df.to_csv(output_path, index=False)

print(f"\n✅ Cleaned file saved successfully at: {output_path}")

# Step 6: Quick Summary of Cleaned Data

print("\n📊 Quick Summary of Cleaned Data:")
print("-" * 50)

# Shape of dataset
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# Column names
print("\nColumns:", list(df.columns))

# Missing values check
print("\nMissing Values per Column:\n", df.isnull().sum())

# Data types
print("\nData Types:\n", df.dtypes)

# Few sample rows
print("\nSample Rows from Cleaned Data:")
print(df.head(5))


