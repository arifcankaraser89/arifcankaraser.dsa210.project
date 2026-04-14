# arifcankaraser.dsa210.project
DSA210 Project — Luxury Watches as Alternative Assets: A Comparative Analysis Against Macroeconomic Indicators
Motivation
In this study, I investigate the long-term investment performance of luxury and mid-range watches in comparison to global macroeconomic indicators between 2005 and 2026. I selected this topic because of my growing interest in alternative assets and wealth management. In the modern financial landscape, luxury timepieces have transitioned from being mere accessories to significant stores of value, often behaving differently than traditional stock markets or currencies. My core research question is: do these physical assets provide a hedge against inflation, or do they simply follow broader market trends?

Data
Three primary data sources were used:
1. Historical Watch Market Data: Monthly and annual price records for models such as the Rolex Submariner and Omega Speedmaster, including primary and secondary market valuations in USD. Models are segmented into Entry-Level, Mid-Range, and Luxury categories based on mean price points.
2. Global Financial Indicators (Finance.csv): Key macroeconomic data covering inflation rates (CPI), interest rates, and major stock market indices.
3. Market Supply & Demand Metrics: Historical data points reflecting brand-specific production trends and collector demand, used to control for brand equity shocks.
Dataset Characteristics
The final merged dataset is a structured time-series and panel data spanning 2005 to 2026. Key variables include:

Name: Watch model (e.g., Rolex Submariner)
Category: Luxury / Mid-Range / Entry-Level
Year: 2005–2026
Value: Asset price in USD
Pct_Increase: Cumulative growth since the 2005 baseline
Indicator_Name: Macroeconomic benchmarks (inflation, GDP growth, S&P 500 equivalent)
CAGR: Compound Annual Growth Rate, derived to compare smoothed annual yields across asset classes


Methodology
Exploratory Data Analysis (EDA)
Price trends reveal that while all segments experienced growth, the Luxury category showed the most significant exponential surge after 2020, suggesting a broad investor shift toward tangible assets during periods of elevated inflation. Entry-level watches remained relatively stable, whereas mid-range and luxury models displayed higher sensitivity to market cycles. When the Consumer Price Index and S&P 500 were overlaid with watch prices, clear clusters emerged where watch valuations spiked following major liquidity events in the global economy.
Hypothesis Testing
Hypothesis 1 — Luxury Watches vs. Inflation

H₀: No significant correlation exists (p > 0.05)
H₁: Luxury watch prices are positively correlated with inflation, functioning as a store of value
Test: Spearman's Rank Correlation — chosen for its robustness against non-linear trends and outliers (e.g., 2021–2022 anomalies) where Pearson's method would be unreliable

Hypothesis 2 — Market Sensitivity: Luxury vs. Entry-Level

H₀: No significant difference in return distributions between segments
H₁: Luxury watches exhibit higher sensitivity to stock market movements (S&P 500) than entry-level models
Test: Mann-Whitney U Test — a non-parametric approach that compares groups without assuming a normal distribution


Findings
The statistical analysis confirms that luxury watches function as more than consumer goods — they operate as legitimate financial instruments.
Macroeconomic Resilience: The rejection of H₀ in Hypothesis 1 demonstrates a statistically significant positive correlation between luxury watch prices and inflation, confirming that high-end timepieces serve as an effective hedge against currency devaluation.
Market Segmentation: The Mann-Whitney U test confirms that the Luxury segment operates on a meaningfully different volatility scale than Entry-Level models. Luxury assets show higher sensitivity to global wealth indices such as the S&P 500, positioning them as high-beta alternative investments.
Strategic Insight: While luxury watches offer inflation protection, their performance is closely tied to broader financial market liquidity. Successful exposure to this asset class therefore requires a sophisticated understanding of macroeconomic cycles.

Limitations

The dataset spans 2005–2026; some model-year combinations may contain estimated or incomplete price records.
Prices reflect secondary market valuations and do not account for transaction costs, authentication fees, or illiquidity premiums.
All correlation findings are observational — no causal claims are made.
Qualitative factors such as brand image shocks and limited production decisions could not be formally incorporated into the model.


Academic Integrity Statement
This project is an original work prepared for DSA 210 – Introduction to Data Science (Sabancı University, Spring 2025–2026).
AI tools were used in a limited and assistive capacity for the following purposes:

Drafting the project structure and README layout
Implementing and debugging the EDA and hypothesis testing pipeline
Converting the analysis into a step-by-step Jupyter Notebook format
Refining the written expression of methodology and findings sections

High-level prompts used:

"Build a pipeline to merge watch price data with macroeconomic indicators, run EDA, and conduct hypothesis tests for the 2005–2026 period."
"Convert the analysis into a step-by-step Jupyter Notebook covering data cleaning, visualization, and statistical testing."
"Add an academic integrity section and improve the README structure."
