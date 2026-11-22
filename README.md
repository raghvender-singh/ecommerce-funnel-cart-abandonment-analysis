# E-Commerce Marketing Funnel & Cart Abandonment Analysis

## Project Overview

This project analyzes e-commerce customer behavior to understand purchasing patterns, marketing performance, conversion funnel drop-offs, and cart abandonment.

Using Python, I performed data cleaning, exploratory data analysis, funnel analysis, customer segmentation, and marketing performance analysis. The processed dataset was then used to develop an interactive Power BI dashboard to monitor business performance and identify opportunities for improving customer conversions.

## Business Problem

E-commerce businesses attract customers through multiple marketing channels, but not every visitor completes a purchase.

The objective of this project is to understand where customers drop off during their shopping journey, identify factors associated with cart abandonment, and evaluate the performance of different marketing channels and customer segments.

### Key Business Questions

- At which stage of the purchasing funnel do most customers drop off?
- What is the overall cart abandonment rate?
- Which devices and marketing channels experience higher cart abandonment?
- How do new and returning customers differ in purchasing behavior?
- Which marketing channels and campaigns generate the highest revenue?
- How does cart abandonment change over time?
- How do discounts relate to completed purchases and realized revenue?

## Tools & Technologies

- **Python:** Data analysis and business calculations
- **Pandas:** Data cleaning, manipulation, and aggregation
- **Matplotlib:** Data visualization
- **Microsoft Power BI:** Interactive dashboard development
- **DAX:** KPI calculations
- **Power Query:** Data transformation

## Project Workflow

### 1. Data Cleaning & Preparation
- Loaded and inspected the raw dataset.
- Examined missing values, duplicate records, and data types.
- Converted date columns into datetime format.
- Transformed Yes/No funnel indicators into binary values.
- Created additional date attributes such as month, year, weekday, and quarter.
- Validated unique session IDs.

### 2. Exploratory Data Analysis
- Examined numerical and categorical variables.
- Analyzed customer sessions and purchasing activities.
- Investigated customer behavior across different segments.

### 3. Conversion Funnel Analysis

Analyzed customer progression through five purchasing stages:

1. All Sessions
2. Viewed Product
3. Added to Cart
4. Checkout Started
5. Purchase Completed

Calculated conversion rates, session drop-offs, and overall purchase conversion.

### 4. Cart Abandonment Analysis

Defined cart abandonment as a session where a customer added a product to the cart but did not complete a purchase.

Analyzed abandonment patterns across:
- Devices
- Marketing channels
- Regions
- Customer types
- Campaign types
- Weekdays
- Months

### 5. Customer & Marketing Analysis

- Compared new and returning customers.
- Analyzed marketing channel revenue and conversion rates.
- Evaluated campaign performance.
- Examined purchase revenue with and without discounts.

### 6. Data Visualization

Created visualizations using Matplotlib to understand:
- Customer conversion funnel
- Drop-off rates at different funnel stages
- Cart abandonment by device
- Cart abandonment by marketing channel
- Monthly cart abandonment trends
- Revenue by marketing channel
- Cart outcomes
- Revenue by campaign type

### 7. Power BI Dashboard

Developed an interactive dashboard featuring:

**Key Performance Indicators**
- Total Sessions
- Product Views
- Cart Additions
- Purchases
- Total Revenue
- Purchase Conversion Rate
- Cart Abandonment Rate
- Average Order Value

**Dashboard Visualizations**
- Customer Conversion Funnel
- Revenue by Marketing Channel
- Monthly Revenue Trend
- Cart Abandonment by Device
- Customer Revenue Mix

**Interactive Filters**
- Date
- Channel
- Device
- User Type
- Region

## Key Business Insights

The analysis provides insights into:

- Customer drop-offs throughout the purchasing journey.
- Marketing channels contributing to actual revenue.
- Differences in cart abandonment across customer segments.
- Purchasing behavior of new and returning customers.
- Monthly changes in cart abandonment.
- Revenue patterns across marketing campaigns.

## Business Recommendations

Based on the analysis, businesses can consider:

- Simplifying the checkout process to reduce customer drop-offs.
- Improving the mobile shopping experience.
- Evaluating marketing channels based on revenue and conversion performance.
- Developing targeted retention campaigns.
- Monitoring monthly cart abandonment trends.
- Evaluating discount strategies using completed purchase data.

## Repository Structure

```text
E-Commerce-Funnel-Cart-Abandonment-Analysis/
│
├── README.md
├── ecommerce_funnel_analysis.py
├── cart_abandonment_cleaned.csv
├── dashboard.pbix
├── dashboard_screenshot.png
│
└── .gitignore
```

## How to Run the Project

### Requirements

Install the required Python libraries:

```bash
pip install pandas matplotlib
```

### Execution

1. Clone or download the repository.
2. Place the original `d2c_marketing_funnel_data.csv` dataset in the same folder as the Python script.
3. Run the Python script:

```bash
python ecommerce_funnel_analysis.py
```

4. The script performs data cleaning and analysis, generates visualizations, and exports the cleaned dataset and analytical summaries.
5. Open `dashboard.pbix` in Microsoft Power BI Desktop to explore the interactive dashboard.

**Note:** The original input dataset is not included in this repository. It must be provided separately to reproduce the Python analysis.

## Important Analytical Considerations

- Each row represents one customer session.
- Cart abandonment is calculated as abandoned carts divided by total cart additions.
- Revenue is calculated using the actual revenue column.
- Lost revenue from abandoned carts is not estimated because confirmed cart values for abandoned sessions are unavailable.
- Average realized revenue per purchase is calculated using total actual revenue divided by completed purchases.

## Project Outcome

This project demonstrates the practical application of Python and Power BI in solving an e-commerce business problem.

It combines data cleaning, exploratory data analysis, conversion funnel analysis, customer segmentation, marketing performance evaluation, and business intelligence to transform raw data into actionable insights.

**Project Category:** E-Commerce Analytics | Marketing Analytics | Customer Behavior Analysis | Business Intelligence

**Technologies:** Python, Pandas, Matplotlib, Power BI, DAX, Power Query
