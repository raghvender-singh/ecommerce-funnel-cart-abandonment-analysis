# E-Commerce Marketing Funnel & Cart Abandonment Analysis

## Project Overview

This project analyzes e-commerce customer behavior, marketing performance, conversion funnel efficiency, and cart abandonment to identify opportunities for improving business performance.

Using Python, I performed data cleaning, exploratory data analysis, conversion funnel analysis, customer segmentation, and marketing performance evaluation. The processed dataset was then used to develop an interactive Power BI dashboard to monitor key business metrics and visualize actionable insights.

The project focuses on understanding customer purchasing behavior, identifying conversion bottlenecks, and evaluating the effectiveness of different marketing channels and campaigns.

## Business Problem

E-commerce businesses attract visitors through multiple marketing channels, but not every visitor completes a purchase.

Understanding where customers drop off during their shopping journey is essential for improving conversion rates, reducing cart abandonment, and optimizing marketing performance.

### Key Business Questions

1. At which stage of the purchasing funnel do most customers drop off?
2. What is the overall cart abandonment rate?
3. Which devices and marketing channels experience higher cart abandonment?
4. How do new and returning customers differ in purchasing behavior?
5. Which marketing channels and campaigns generate the highest revenue?
6. How does cart abandonment change over time?
7. How do discounts relate to completed purchases and realized revenue?

## Tools & Technologies

- **Python:** Data analysis and business calculations
- **Pandas:** Data cleaning, manipulation, and aggregation
- **Matplotlib:** Data visualization
- **Microsoft Power BI:** Interactive dashboard development
- **DAX:** KPI calculations
- **Power Query:** Data transformation

## Project Workflow

### 1. Data Cleaning & Preparation
- Loaded and inspected the raw dataset using Pandas.
- Examined missing values, duplicate records, and data types.
- Converted date columns into datetime format.
- Transformed Yes/No funnel indicators into binary values.
- Created additional date attributes such as year, month, weekday, and quarter.
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
- Examined completed purchases with and without discounts.

### 6. Data Visualization

Created eight visualizations using Matplotlib:

1. Customer Conversion Funnel
2. Customer Drop-off by Funnel Stage
3. Cart Abandonment Rate by Device
4. Cart Abandonment Rate by Marketing Channel
5. Monthly Cart Abandonment Trend
6. Actual Revenue by Marketing Channel
7. Outcomes of Sessions That Added to Cart
8. Actual Revenue by Campaign Type

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

## Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Sessions | 120,000 |
| Product Views | 77,870 |
| Cart Additions | 27,156 |
| Checkout Started | 16,234 |
| Completed Purchases | 8,181 |
| Abandoned Carts | 18,975 |
| Total Revenue | ₹1.70 Crore |
| Purchase Conversion Rate | 6.82% |
| Cart Abandonment Rate | 69.87% |
| Average Order Value | ₹2,080 |

## Key Business Insights

### 1. Customer Conversion Funnel

- Out of 120,000 sessions, 77,870 resulted in product views.
- 27,156 sessions resulted in cart additions.
- Only 8,181 sessions resulted in completed purchases.
- The largest percentage drop-off occurred between product views and cart additions, with 50,714 sessions lost.
- This stage recorded a drop-off rate of 65.13%.

**Business Implication:** Improving product presentation, pricing strategies, and product information could help encourage more visitors to add products to their carts.

### 2. Cart Abandonment Analysis

- Overall cart abandonment rate: 69.87%.
- Total abandoned carts: 18,975.
- Completed purchases from cart additions: 8,181.

**Business Implication:** The high abandonment rate highlights an opportunity to improve the checkout experience, simplify purchasing steps, and introduce targeted cart recovery campaigns.

### 3. Cart Abandonment by Device and Marketing Channel

**Device Comparison**

| Device | Abandonment Rate |
|---|---:|
| Mobile | 70.06% |
| Desktop | 69.43% |

Mobile users recorded a slightly higher abandonment rate than desktop users.

**Marketing Channel Comparison**

| Channel | Abandonment Rate |
|---|---:|
| Social | 70.01% |
| Organic | 69.99% |
| Paid Ads | 69.99% |
| Email | 68.85% |

Social recorded the highest abandonment rate, while Email recorded the lowest.

**Business Implication:** Businesses should investigate mobile shopping usability and evaluate the quality of traffic generated through different marketing channels.

### 4. New vs Returning Customer Analysis

| Metric | New Customers | Returning Customers |
|---|---:|---:|
| Sessions | 77,969 | 42,031 |
| Purchases | 5,398 | 2,783 |
| Conversion Rate | 6.92% | 6.62% |
| Revenue per Session | ₹143.98 | ₹137.77 |
| Revenue per Purchase | ₹2,079.62 | ₹2,080.78 |

**Key Findings:**
- New customers recorded a slightly higher conversion rate.
- New customers generated higher total revenue due to their larger session volume.
- Returning customers recorded slightly higher average revenue per purchase.

**Business Implication:** Businesses can focus on customer retention strategies and personalized campaigns to encourage repeat purchases.

### 5. Marketing Channel & Campaign Performance

**Revenue by Marketing Channel**

| Channel | Revenue |
|---|---:|
| Paid Ads | ₹75.36 Lakh |
| Organic | ₹50.91 Lakh |
| Social | ₹25.78 Lakh |
| Email | ₹18.11 Lakh |

Paid Ads generated the highest revenue, followed by Organic.

**Revenue by Campaign Type**

| Campaign Type | Revenue |
|---|---:|
| Discount | ₹85.27 Lakh |
| New Launch | ₹51.23 Lakh |
| Influencer | ₹33.67 Lakh |

Discount campaigns generated the highest total revenue.

**Business Implication:** Businesses should evaluate campaign performance using revenue, conversion rates, and profitability rather than revenue alone.

### 6. Monthly Cart Abandonment Trend

| Month | Cart Abandonment Rate |
|---|---:|
| July | 69.06% |
| August | 70.37% |
| September | 69.05% |
| October | 70.27% |
| November | 71.06% |
| December | 69.39% |

**Key Findings:**
- November recorded the highest abandonment rate at 71.06%.
- September recorded the lowest abandonment rate at 69.05%.
- December showed an improvement compared with November.

**Business Implication:** Businesses should investigate monthly changes in customer behavior and identify factors contributing to increased cart abandonment.

### 7. Discount Analysis

| Metric | No Discount | Discount Applied |
|---|---:|---:|
| Completed Purchases | 3,719 | 4,462 |
| Actual Revenue | ₹81.85 Lakh | ₹88.31 Lakh |
| Average Revenue per Purchase | ₹2,200.98 | ₹1,979.19 |

**Key Findings:**
- Discount-applied purchases accounted for approximately 54.5% of completed purchases.
- Discount-applied purchases generated higher total revenue.
- Average revenue per purchase was approximately 10.1% lower for discounted purchases.

**Business Implication:** Discounts may encourage higher purchase volume, but businesses should evaluate their impact on average order value and profitability.

## Business Recommendations

Based on the analysis, businesses can consider:

- Improving product presentation and pricing strategies to increase product-to-cart conversion.
- Simplifying the checkout process to reduce customer drop-offs.
- Improving the mobile shopping experience.
- Evaluating marketing channels based on revenue and conversion performance.
- Developing targeted retention campaigns for returning customers.
- Monitoring monthly cart abandonment trends.
- Evaluating discount strategies based on purchase volume, average order value, and profitability.

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

**Note:** The original input dataset is not included in this repository and must be provided separately to reproduce the Python analysis.

## Important Analytical Considerations

- Each row in the dataset represents one customer session.
- Cart abandonment is calculated as abandoned carts divided by total cart additions.
- Revenue is calculated using the actual revenue column.
- Lost revenue from abandoned carts is not estimated because confirmed cart values for abandoned sessions are unavailable.
- Average Order Value is calculated as total actual revenue divided by completed purchases.
- Discount comparisons are observational and do not establish that discounts caused changes in purchasing behavior.

## Project Outcome

This project demonstrates the practical application of Python and Power BI in solving an e-commerce business problem.

By combining data cleaning, exploratory data analysis, conversion funnel analysis, customer segmentation, marketing performance evaluation, and interactive visualization, the project transforms raw data into actionable business insights.

**Project Category:** E-Commerce Analytics | Marketing Analytics | Customer Behavior Analysis | Business Intelligence

**Technologies:** Python, Pandas, Matplotlib, Microsoft Power BI, DAX, Power Query
