"""
E-commerce Marketing Funnel & Cart Abandonment Analysis

Input file:
    d2c_marketing_funnel_data.csv

Required libraries:
    pandas
    matplotlib

Install:
    pip install pandas matplotlib

Keep this script and the CSV file in the same folder before running.
"""

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD DATA
# ============================================================

# Load the raw dataset.
df = pd.read_csv("d2c_marketing_funnel_data.csv")


# ============================================================
# 2. INITIAL DATA INSPECTION
# ============================================================

print("\n========== DATASET OVERVIEW ==========")
print("\nFirst five rows:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nNumeric summary:")
print(df.describe())

print("\nCategorical summary:")
print(df.describe(include="object"))

# Inspect the values available in each categorical column.
print("\n========== UNIQUE CATEGORICAL VALUES ==========")
for column in df.select_dtypes(include="object").columns:
    print(f"\n{column}:")
    print(df[column].unique())


# ============================================================
# 3. DATA CLEANING
# ============================================================

# Convert the date column into a datetime data type.
# The source dates use month/day/year format.
df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y")

# The visited_website column contains only one value ("Yes").
# Since it does not distinguish sessions, remove it from the analysis.
if "visited_website" in df.columns:
    df.drop(columns=["visited_website"], inplace=True)

# Convert Yes/No funnel fields into numeric values:
# Yes = 1 and No = 0.
binary_columns = [
    "viewed_product",
    "added_to_cart",
    "checkout_started",
    "purchase_completed",
    "discount_applied"
]

for column in binary_columns:
    df[column] = df[column].map({"Yes": 1, "No": 0})

# Check that the conversion did not create missing values.
if df[binary_columns].isnull().any().any():
    raise ValueError("Unexpected values found in one or more Yes/No columns.")

# Rebuild the month field from the date so it is consistent.
# Keep the original YYYY-MM month value as a separate field for reference.
if "month" in df.columns:
    original_month = df["month"].copy()
    date_month = df["date"].dt.strftime("%Y-%m")
    print("\nOriginal month matches date:", original_month.eq(date_month).all())
    df.drop(columns=["month"], inplace=True)

# Create date attributes for time-based analysis.
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month_name()
df["month_num"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["weekday"] = df["date"].dt.day_name()
df["quarter"] = df["date"].dt.quarter

# Confirm that each row represents a distinct session.
# The dataset uses one row per session, so duplicated session IDs
# would affect session-level calculations.
duplicate_sessions = df["session_id"].duplicated().sum()
print("\nDuplicate session IDs:", duplicate_sessions)

if duplicate_sessions > 0:
    raise ValueError(
        "The dataset contains repeated session IDs. "
        "Review them before calculating session-level metrics."
    )

print("\n========== CLEANED DATASET ==========")
df.info()


# ============================================================
# 4. DATA VALIDATION
# ============================================================

# Check whether the funnel stages follow the expected order.
purchased_without_checkout = df[
    (df["purchase_completed"] == 1) &
    (df["checkout_started"] == 0)
]

checkout_without_cart = df[
    (df["checkout_started"] == 1) &
    (df["added_to_cart"] == 0)
]

cart_without_product_view = df[
    (df["added_to_cart"] == 1) &
    (df["viewed_product"] == 0)
]

print("\n========== FUNNEL DATA VALIDATION ==========")
print("Purchases without checkout:", len(purchased_without_checkout))
print("Checkout without cart:", len(checkout_without_cart))
print("Cart additions without product view:", len(cart_without_product_view))


# ============================================================
# 5. CREATE CART ABANDONMENT FLAG
# ============================================================

# A cart is considered abandoned when a session added a product
# but did not complete a purchase.
df["cart_abandoned"] = (
    (df["added_to_cart"] == 1) &
    (df["purchase_completed"] == 0)
).astype(int)


# ============================================================
# 6. OVERALL BUSINESS PERFORMANCE / KEY METRICS
# ============================================================

# Each row represents one session in this dataset.
total_sessions = df["session_id"].nunique()
total_users = df["user_id"].nunique()

product_views = int(df["viewed_product"].sum())
cart_additions = int(df["added_to_cart"].sum())
checkouts = int(df["checkout_started"].sum())
purchases = int(df["purchase_completed"].sum())
abandoned_carts = int(df["cart_abandoned"].sum())

# Revenue is recorded as zero for sessions without a completed purchase.
# Therefore, total revenue is calculated directly from the revenue column.
total_revenue = df["revenue"].sum()

# Calculate average realized revenue per completed purchase.
average_revenue_per_purchase = (
    total_revenue / purchases if purchases else 0
)

average_revenue_per_session = (
    total_revenue / total_sessions if total_sessions else 0
)

print("\n========== KEY PERFORMANCE INDICATORS ==========")
print(f"Total users: {total_users:,}")
print(f"Total sessions: {total_sessions:,}")
print(f"Product views: {product_views:,}")
print(f"Cart additions: {cart_additions:,}")
print(f"Checkouts started: {checkouts:,}")
print(f"Completed purchases: {purchases:,}")
print(f"Abandoned carts: {abandoned_carts:,}")
print(f"Total actual revenue: ₹{total_revenue:,.2f}")
print(
    "Average realized revenue per purchase: "
    f"₹{average_revenue_per_purchase:,.2f}"
)
print(
    "Average revenue per session: "
    f"₹{average_revenue_per_session:,.2f}"
)


# ============================================================
# 7. CONVERSION FUNNEL ANALYSIS
# ============================================================

# Create the funnel using session counts at each stage.
funnel_stages = [
    "All Sessions",
    "Viewed Product",
    "Added to Cart",
    "Checkout Started",
    "Purchase Completed"
]

funnel_counts = [
    total_sessions,
    product_views,
    cart_additions,
    checkouts,
    purchases
]

funnel_df = pd.DataFrame({
    "Stage": funnel_stages,
    "Sessions": funnel_counts
})

# Calculate the percentage moving forward from the previous stage.
funnel_df["Conversion from Previous (%)"] = (
    funnel_df["Sessions"] /
    funnel_df["Sessions"].shift(1) * 100
).round(2)
funnel_df.loc[0, "Conversion from Previous (%)"] = 100.00

# Calculate the number and percentage lost at each stage.
funnel_df["Drop-off Sessions"] = (
    funnel_df["Sessions"].shift(1) - funnel_df["Sessions"]
)
funnel_df.loc[0, "Drop-off Sessions"] = 0
funnel_df["Drop-off Sessions"] = funnel_df["Drop-off Sessions"].astype(int)

funnel_df["Drop-off (%)"] = (
    funnel_df["Drop-off Sessions"] /
    funnel_df["Sessions"].shift(1) * 100
).round(2)
funnel_df.loc[0, "Drop-off (%)"] = 0.00

# Calculate conversion against all sessions.
funnel_df["Overall Conversion (%)"] = (
    funnel_df["Sessions"] / total_sessions * 100
).round(2)

print("\n========== CONVERSION FUNNEL ==========")
print(funnel_df.to_string(index=False))

# Identify the stage with the highest percentage drop-off.
largest_drop = funnel_df.iloc[1:].loc[
    funnel_df.iloc[1:]["Drop-off (%)"].idxmax()
]

print("\nLargest drop-off stage:", largest_drop["Stage"])
print(f"Largest drop-off rate: {largest_drop['Drop-off (%)']:.2f}%")

# Calculate key conversion rates.
view_rate = product_views / total_sessions * 100 if total_sessions else 0
add_to_cart_rate = (
    cart_additions / product_views * 100 if product_views else 0
)
checkout_rate = (
    checkouts / cart_additions * 100 if cart_additions else 0
)
purchase_rate = (
    purchases / checkouts * 100 if checkouts else 0
)
overall_conversion_rate = (
    purchases / total_sessions * 100 if total_sessions else 0
)

print("\n========== CONVERSION RATES ==========")
print(f"Product view rate: {view_rate:.2f}%")
print(f"Add-to-cart rate: {add_to_cart_rate:.2f}%")
print(f"Checkout rate: {checkout_rate:.2f}%")
print(f"Purchase rate from checkout: {purchase_rate:.2f}%")
print(f"Overall session-to-purchase rate: {overall_conversion_rate:.2f}%")


# ============================================================
# 8. CART ABANDONMENT ANALYSIS
# ============================================================

# Cart abandonment rate uses cart additions as its denominator.
cart_abandonment_rate = (
    abandoned_carts / cart_additions * 100 if cart_additions else 0
)

# Calculate completed purchases among sessions that added to cart.
completed_cart_purchases = int(
    df.loc[df["added_to_cart"] == 1, "purchase_completed"].sum()
)

cart_completion_rate = (
    completed_cart_purchases / cart_additions * 100
    if cart_additions else 0
)

print("\n========== CART ABANDONMENT ==========")
print(f"Sessions that added to cart: {cart_additions:,}")
print(f"Abandoned carts: {abandoned_carts:,}")
print(f"Completed purchases from cart: {completed_cart_purchases:,}")
print(f"Cart abandonment rate: {cart_abandonment_rate:.2f}%")
print(f"Cart completion rate: {cart_completion_rate:.2f}%")

# IMPORTANT:
# The dataset does not provide the actual contents or value of each cart.
# Its order_value field is not a confirmed cart subtotal for abandoned
# sessions. Therefore, this script does not calculate "lost revenue"
# from abandoned carts.


# ============================================================
# 9. REUSABLE SEGMENTATION ANALYSIS
# ============================================================

def abandonment_analysis(data, segment_column):
    """
    Calculate session, cart, purchase and revenue metrics
    for each category in the selected segment column.
    """

    result = (
        data.groupby(segment_column)
        .agg(
            sessions=("session_id", "nunique"),
            cart_additions=("added_to_cart", "sum"),
            abandoned_carts=("cart_abandoned", "sum"),
            purchases=("purchase_completed", "sum"),
            actual_revenue=("revenue", "sum")
        )
    )

    # Abandonment rate = abandoned carts / all cart additions.
    result["cart_abandonment_rate (%)"] = (
        result["abandoned_carts"] /
        result["cart_additions"].replace(0, pd.NA) * 100
    ).round(2)

    # Session-to-purchase conversion rate.
    result["session_conversion_rate (%)"] = (
        result["purchases"] / result["sessions"] * 100
    ).round(2)

    # Revenue generated per session in each segment.
    result["revenue_per_session"] = (
        result["actual_revenue"] / result["sessions"]
    ).round(2)

    return result.sort_values(
        "cart_abandonment_rate (%)",
        ascending=False,
        na_position="last"
    )


# Compare cart abandonment across customer and marketing segments.
segment_columns = [
    "device",
    "channel",
    "region",
    "user_type",
    "campaign_type",
    "weekday",
    "month"
]

segment_results = {}

print("\n========== CART ABANDONMENT BY SEGMENT ==========")

for column in segment_columns:
    segment_results[column] = abandonment_analysis(df, column)
    print(f"\nAnalysis by {column}:")
    print(segment_results[column])


# ============================================================
# 10. CUSTOMER TYPE ANALYSIS
# ============================================================

# Compare new and returning customers using session-level metrics.
customer_type_analysis = (
    df.groupby("user_type")
    .agg(
        sessions=("session_id", "nunique"),
        purchases=("purchase_completed", "sum"),
        actual_revenue=("revenue", "sum")
    )
)

customer_type_analysis["conversion_rate (%)"] = (
    customer_type_analysis["purchases"] /
    customer_type_analysis["sessions"] * 100
).round(2)

customer_type_analysis["revenue_per_session"] = (
    customer_type_analysis["actual_revenue"] /
    customer_type_analysis["sessions"]
).round(2)

customer_type_analysis["revenue_per_purchase"] = (
    customer_type_analysis["actual_revenue"] /
    customer_type_analysis["purchases"].replace(0, pd.NA)
).round(2)

print("\n========== CUSTOMER TYPE ANALYSIS ==========")
print(customer_type_analysis)


# ============================================================
# 11. MARKETING CHANNEL AND CAMPAIGN REVENUE ANALYSIS
# ============================================================

# Evaluate the actual revenue generated by each marketing channel.
channel_performance = (
    df.groupby("channel")
    .agg(
        sessions=("session_id", "nunique"),
        purchases=("purchase_completed", "sum"),
        actual_revenue=("revenue", "sum")
    )
)

channel_performance["conversion_rate (%)"] = (
    channel_performance["purchases"] /
    channel_performance["sessions"] * 100
).round(2)

channel_performance["revenue_per_session"] = (
    channel_performance["actual_revenue"] /
    channel_performance["sessions"]
).round(2)

# Evaluate campaign types using the same measures.
campaign_performance = (
    df.groupby("campaign_type")
    .agg(
        sessions=("session_id", "nunique"),
        purchases=("purchase_completed", "sum"),
        actual_revenue=("revenue", "sum")
    )
)

campaign_performance["conversion_rate (%)"] = (
    campaign_performance["purchases"] /
    campaign_performance["sessions"] * 100
).round(2)

campaign_performance["revenue_per_session"] = (
    campaign_performance["actual_revenue"] /
    campaign_performance["sessions"]
).round(2)

print("\n========== MARKETING CHANNEL PERFORMANCE ==========")
print(channel_performance)

print("\n========== CAMPAIGN PERFORMANCE ==========")
print(campaign_performance)


# ============================================================
# 12. PURCHASE AND DISCOUNT ANALYSIS
# ============================================================

# Analyze only completed purchases when calculating realized order revenue.
completed_purchase_data = df[df["purchase_completed"] == 1].copy()

# Revenue per completed purchase is the best available realized
# revenue-per-order measure in this dataset.
discount_analysis = (
    completed_purchase_data.groupby("discount_applied")
    .agg(
        purchases=("session_id", "nunique"),
        actual_revenue=("revenue", "sum"),
        average_revenue_per_purchase=("revenue", "mean")
    )
)

print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_analysis)


# ============================================================
# 13. VISUALIZATIONS
# ============================================================

# Chart 1: Number of sessions at each funnel stage.
plt.figure(figsize=(10, 5))
plt.bar(funnel_df["Stage"], funnel_df["Sessions"])
plt.title("Customer Conversion Funnel")
plt.xlabel("Funnel Stage")
plt.ylabel("Number of Sessions")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.show()

# Chart 2: Percentage of sessions lost between funnel stages.
plt.figure(figsize=(10, 5))
plt.bar(
    funnel_df["Stage"].iloc[1:],
    funnel_df["Drop-off (%)"].iloc[1:]
)
plt.title("Customer Drop-off by Funnel Stage")
plt.xlabel("Funnel Stage")
plt.ylabel("Drop-off (%)")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.show()

# Chart 3: Cart abandonment rate by device.
device_results = segment_results["device"]

plt.figure(figsize=(6, 4))
device_results["cart_abandonment_rate (%)"].dropna().plot(kind="bar")
plt.title("Cart Abandonment Rate by Device")
plt.xlabel("Device")
plt.ylabel("Cart Abandonment Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Chart 4: Cart abandonment rate by marketing channel.
channel_abandonment = segment_results["channel"]

plt.figure(figsize=(7, 4))
channel_abandonment["cart_abandonment_rate (%)"].dropna().plot(kind="bar")
plt.title("Cart Abandonment Rate by Marketing Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("Cart Abandonment Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Chart 5: Monthly cart abandonment trend in calendar order.
month_order = [
    "July", "August", "September",
    "October", "November", "December"
]

monthly_results = segment_results["month"].reindex(month_order)

plt.figure(figsize=(9, 4))
plt.plot(
    monthly_results.index,
    monthly_results["cart_abandonment_rate (%)"],
    marker="o"
)
plt.title("Monthly Cart Abandonment Trend")
plt.xlabel("Month")
plt.ylabel("Cart Abandonment Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Chart 6: Actual revenue generated by each marketing channel.
plt.figure(figsize=(8, 4))
channel_performance["actual_revenue"].sort_values(
    ascending=False
).plot(kind="bar")
plt.title("Actual Revenue by Marketing Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("Actual Revenue (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Chart 7: Cart outcomes among sessions that added a product.
# These two groups are mutually exclusive within cart-addition sessions.
plt.figure(figsize=(6, 6))
plt.pie(
    [abandoned_carts, completed_cart_purchases],
    labels=["Cart Abandoned", "Purchase Completed"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Outcomes of Sessions That Added to Cart")
plt.tight_layout()
plt.show()

# Chart 8: Actual revenue by campaign type.
plt.figure(figsize=(8, 4))
campaign_performance["actual_revenue"].sort_values(
    ascending=False
).plot(kind="bar")
plt.title("Actual Revenue by Campaign Type")
plt.xlabel("Campaign Type")
plt.ylabel("Actual Revenue (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ============================================================
# 14. EXPORT CLEANED DATA AND ANALYSIS TABLES
# ============================================================

# Export the cleaned session-level dataset for SQL or Power BI.
df.to_csv("cart_abandonment_cleaned.csv", index=False)

# Export the overall funnel metrics.
funnel_df.to_csv("funnel_metrics.csv", index=False)

# Export abandonment analysis for each segment.
for column, result in segment_results.items():
    result.to_csv(f"abandonment_by_{column}.csv")

# Export customer and marketing performance summaries.
customer_type_analysis.to_csv("customer_type_analysis.csv")
channel_performance.to_csv("channel_performance.csv")
campaign_performance.to_csv("campaign_performance.csv")
discount_analysis.to_csv("discount_analysis.csv")

print("\n========== PROJECT COMPLETED ==========")
print("Cleaned data and analysis tables have been exported successfully.")
