import pandas as pd

# -------------------------------
# 1. EXTRACT
# -------------------------------
print("📥 Extracting data from CSV...")

df = pd.read_csv("online_retail.csv")

print("\nOriginal Data:")
print(df.head())


# -------------------------------
# 2. TRANSFORM
# -------------------------------
print("\n🔧 Transforming data...")

# Rule 1: Remove rows with empty Customer ID
df = df.dropna(subset=["Customer ID"])

# Rule 2: Convert InvoiceDate to YYYY-MM-DD format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors='coerce')
df = df.dropna(subset=["InvoiceDate"])   # remove invalid dates
df["InvoiceDate"] = df["InvoiceDate"].dt.strftime("%Y-%m-%d")

print("\nCleaned / Transformed Data:")
print(df.head())


# -------------------------------
# 3. LOAD
# -------------------------------
print("\n📤 Loading cleaned data into cleaned_output.csv ...")

df.to_csv("cleaned_output.csv", index=False)

print("\nETL Completed Successfully!")
print("Cleaned file saved as: cleaned_output.csv")


# Display loaded output
loaded_df = pd.read_csv("cleaned_output.csv")
print("\n📄 Loaded Data:")
print(loaded_df.head())
