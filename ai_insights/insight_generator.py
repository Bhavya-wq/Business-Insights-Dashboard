import pandas as pd
import os

# Get absolute project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct dataset path
file_path = os.path.join(BASE_DIR, "data", "superstore.csv")

print("Loading file from:", file_path)  # debug check

# Load dataset
df = pd.read_csv(file_path)
# Category performance
category_summary = (
    df.groupby("Category")[["Sales", "Profit"]]
    .sum()
    .sort_values(by="Profit", ascending=False)
)

# Region performance
region_summary = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

# Loss-making sub-categories
loss_subcategories = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
    .head(3)
)
print("\n📊 AI GENERATED BUSINESS INSIGHTS\n")

top_category = category_summary.index[0]
worst_category = category_summary.index[-1]

top_region = region_summary.index[0]

print(f"✅ {top_category} category generates the highest overall profit.")
print(f"⚠️ {worst_category} category shows weaker profitability compared to others.")
print(f"🌍 {top_region} region contributes the most profit to the business.")

print("\n🚨 Major Loss-Making Sub-Categories:")
for sub in loss_subcategories.index:
    print(f"- {sub}")
