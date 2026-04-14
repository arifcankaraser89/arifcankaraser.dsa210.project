# arifcankaraser.dsa210.project
# 🚀 Luxury Watches as Alternative Assets: A Comparative Analysis (2005–2026)

## 🎯 Motivation
In this study, I investigate the **long-term investment performance** of luxury and mid-range watches in comparison to global macroeconomic indicators. In the modern financial landscape, luxury timepieces have transitioned from being mere accessories to significant **stores of value**. 

**Core Research Question:** Do these physical assets provide a reliable hedge against inflation, or do they simply follow broader equity market trends?

---

## 📂 Data Sources & Characteristics
The project utilizes a structured time-series dataset spanning **2005 to 2026**, merging three primary sources:

1.  **Historical Watch Market Data:** Monthly price records for iconic models (e.g., Rolex Submariner, Omega Speedmaster), segmented into *Entry-Level*, *Mid-Range*, and *Luxury*.
2.  **Global Financial Indicators (`Finance.csv`):** Macroeconomic data covering **CPI (Inflation)**, interest rates, and major indices (S&P 500, Nasdaq).
3.  **Market Supply & Demand Metrics:** Brand-specific production trends used to control for brand equity shocks.

### **Dataset Features**
* **Name & Category:** Watch model and its market segment.
* **Value (USD):** Asset price at a given time.
* **Pct_Increase:** Cumulative growth from the 2005 baseline.
* **CAGR:** Compound Annual Growth Rate for yield comparison.

---

## 🔬 Methodology

### **1. Exploratory Data Analysis (EDA)**
* **Exponential Growth:** The Luxury category showed a significant surge after 2020, suggesting a shift toward tangible assets during inflation.
* **Market Overlay:** By overlaying CPI and S&P 500, we identified clusters where watch valuations spiked following global liquidity injections.
* **Stability:** Entry-level models remained stable, while luxury models mirrored market cycles.

### **2. Hypothesis Testing**
| Hypothesis | Null Hypothesis (H₀) | Statistical Test | Rationale |
| :--- | :--- | :--- | :--- |
| **H1: Watch vs. Inflation** | No significant correlation exists. | **Spearman’s Rank Correlation** | Robust against non-linear trends and market outliers (2021-2022). |
| **H2: Market Sensitivity** | No difference in return distributions. | **Mann-Whitney U Test** | Non-parametric approach to compare segments without assuming normality. |

---

## 🏆 Findings
* **🏛 Macroeconomic Resilience:** Rejection of H₀ in Hypothesis 1 confirms that high-end timepieces serve as an **effective hedge against currency devaluation**.
* **📊 Market Segmentation:** Luxury assets function as **high-beta alternative investments**, showing higher sensitivity to global wealth indices than entry-level models.
* **💡 Strategic Insight:** While providing inflation protection, luxury watch performance is intrinsically tied to **financial market liquidity**.

---

## ⚠️ Limitations
* **Data Gaps:** Some model-year combinations contain estimated price records.
* **Hidden Costs:** Analysis does not account for transaction fees, maintenance, or illiquidity premiums.
* **Correlation vs. Causality:** Findings are observational; no direct causal claims are made.

---

## 📜 Academic Integrity Statement
This project is an original work prepared for **DSA 210 – Introduction to Data Science** (Sabancı University, Spring 2025–2026).

**AI Disclosure:** AI tools were used in a limited and assistive capacity for:
* Structuring the README and documentation layout.
* Debugging the EDA and hypothesis testing pipeline.
* Refining the written expression of methodology and findings.

*All analytical conclusions and data interpretations are the sole responsibility of the author.*
