# ============================================================
# Customer Shopping Behavior Analysis
# Python Data Cleaning and Analysis
# ============================================================

import pandas as pd


# ============================================================
# 1. Load Dataset
# ============================================================

df = pd.read_csv(
    r"D:\Data Analytics\customer-shopping-behavior-analysis\data\Customer_details_dataset.csv"
)

print("Dataset loaded successfully!")
print("Original Shape:", df.shape)


# ============================================================
# 2. Initial Data Inspection
# ============================================================

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Description:")
print(df.describe(include="all"))

print("\nMissing Values:")
print(df.isnull().sum())


# ============================================================
# 3. Handle Missing Review Ratings
# ============================================================

df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(
    lambda x: x.fillna(x.median())
)


print("\nMissing Values After Filling Review Ratings:")
print(df.isnull().sum())


# ============================================================
# 4. Clean Column Names
# ============================================================

df.columns = (
    df.columns
    .str.replace(" ", "_")
    .str.lower()
)

print("\nCleaned Column Names:")
print(df.columns.tolist())


# ============================================================
# 5. Rename Purchase Amount Column
# ============================================================

df = df.rename(
    columns={
        "purchase_amount_(usd)": "purchase_amount"
    }
)


# ============================================================
# 6. Create Age Groups
# ============================================================

labels = [
    "Young Adult",
    "Adult",
    "Middle-aged",
    "Senior"
]

df["age_group"] = pd.qcut(
    df["age"],
    q=4,
    labels=labels
)

print("\nAge Group Distribution:")
print(df["age_group"].value_counts())


# ============================================================
# 7. Convert Purchase Frequency to Days
# ============================================================

frequency_mapping = {
    "fortnightly": 14,
    "weekly": 7,
    "monthly": 30,
    "bi-weekly": 14,
    "quarterly": 90,
    "annually": 365,
    "every 3 months": 90
}

df["purchase_frequency_days"] = (
    df["frequency_of_purchases"]
    .str.lower()
    .map(frequency_mapping)
)

print("\nPurchase Frequency Conversion:")
print(
    df[
        [
            "frequency_of_purchases",
            "purchase_frequency_days"
        ]
    ].head(10)
)


# ============================================================
# 8. Check Discount and Promo Code Relationship
# ============================================================

discount_match = (
    df["discount_applied"] == df["promo_code_used"]
).all()

print("\nDiscount and Promo Code Values Match:", discount_match)


# ============================================================
# 9. Remove Redundant Column
# ============================================================

df = df.drop(
    "promo_code_used",
    axis=1
)


# ============================================================
# 10. Final Data Validation
# ============================================================

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Columns:")
print(df.columns.tolist())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())


# ============================================================
# 11. Basic Analysis
# ============================================================

print("\nAverage Purchase Amount:")
print(round(df["purchase_amount"].mean(), 2))


print("\nAverage Review Rating:")
print(round(df["review_rating"].mean(), 2))


print("\nSales by Category:")
print(
    df.groupby("category")["purchase_amount"]
    .sum()
    .sort_values(ascending=False)
)


print("\nTop 5 Products:")
print(
    df["item_purchased"]
    .value_counts()
    .head(5)
)


print("\nSubscription Status:")
print(
    df["subscription_status"]
    .value_counts()
)


# ============================================================
# 12. Final Data Preview
# ============================================================

print("\nFinal Dataset Preview:")
print(df.head())


# ============================================================
# End of Analysis
# ============================================================

print("\nPython data cleaning and analysis completed successfully!")