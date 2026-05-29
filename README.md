--------------------------------------------------------------------------------
# Pre-AGM Sustainability Audit & Root Cause Analysis

*Disclaimer: This is a simulated data analytics portfolio project. The dataset was synthetically generated using Python. The business context and risk factors are drawn from publicly available ING 2026 documents for structural realism, but do not represent actual internal company data.*

## 1. Executive Summary & Business Context
ING’s Annual General Meeting (AGM) is scheduled for April 14, 2026, where the Executive Board will discuss the 2025 Sustainability Statement. With the potential presence of activist groups anticipated at the event, ensuring the integrity of ING's sustainability reporting is a critical priority.

ING monitors significant operational risks, including breaches of security, inadequate controls regarding third-party vendors, and flawed outputs from AI algorithms [4]. In this simulated scenario, an anomaly was detected involving a third-party server leak that potentially exposed falsified corporate carbon emissions (greenwashing). This threatens a portion of ING's €34 billion in "sustainable volume mobilised" and risks damaging the bank's Sustainalytics ESG risk rating of 18.0 (low risk).

## 2. The Business Question
To cut through the noise and drive executive action, this project aims to answer both descriptive and predictive questions:
> *"Which corporate clients are flagging for ESG data discrepancies (greenwashing/fraud) due to the third-party server leak, and which of our remaining 'secure' clients have the highest probability of currently undetected greenwashing prior to the April 14 AGM?"*

## 3. Key Performance Indicators (KPIs)
To provide an effective, functional tool for risk executives, the analysis tracks only three critical KPIs:
*   **Sustainable Volume at Risk:** The total loan amount (in EUR) tied to the compromised corporate clients.
*   **Compliance Flag Rate:** The percentage of the loan portfolio exhibiting self-reporting anomalies vs. audited emissions.
*   **ESG Risk Rating Impact:** Tracking the negative impact of the breached data against ING’s target 18.0 ESG rating.

## 4. Methodology: Root Cause Analysis & Machine Learning
This project utilizes a structured Root Cause Analysis and Machine Learning to investigate the drivers behind the problem and proactively protect resources.
*   **Data Generation:** Utilized Python (`pandas`, `numpy`) to simulate a 1,000-row dataset of corporate loans, modeling realistic standard variations and fraud discrepancies.
*   **Segmentation:** Segmented the massive dataset by industry and security flag status to identify exactly where the anomalies were concentrated.
*   **Machine Learning (Random Forest Classifier):** Addressed AI vulnerability risks by training a classification model to learn the mathematical profile of a compromised account. The model successfully scanned un-breached accounts to predict their "Fraud Probability Score."

## 5. Visual Insights & Dashboard
*The visuals below translate the technical data and Machine Learning predictions into actionable business insights.* 

### A. The Financial Risk (KPIs)
![Financial Risk Bar Chart](kpi_chart.png)
*Insight:* The leak has exposed up to €4.8B of ING's €34B sustainable volume to greenwashing claims.

### B. The Root Cause: Greenwashing Anomaly
![Emissions Scatter Plot](scatter_plot.png)
*Insight:* Cross-referencing self-reported data against audited logs reveals that compromised clients inflated their sustainability metrics by 20% to 80%.

### C. Machine Learning Early Warning System
![Top 10 Risk Chart](top_10_risk_chart.png)
*Insight:* The Random Forest classification model identified the top 10 currently "secure" clients whose reporting behaviors mathematically mirror the fraudulent accounts. **Recommendation: Immediately audit these 10 accounts prior to the AGM.** 

## 6. Deliverables & Recommendations
Because an executive preparing for a board meeting requires rapid, actionable insights, the final output is translated into plain-language business recommendations.

**Repository Files:**
*   `data_generation.py`: The Python script used to model the business scenario, synthesize the data, and train the Random Forest ML model.
*   `mock_ing_esg_azure_leak_with_ML.csv`: The generated synthetic dataset with ML predictions.
*   `ING_Pre_AGM_Audit_Dashboard.pbix`: **The interactive Power BI dashboard containing the KPI tracking and ML risk visualizations.**
*   `Pre_AGM_Executive_Deck.pdf`: A 3-slide executive presentation leading with action titles, designed to present the root cause and advise the Executive Board on immediate mitigation strategies prior to the AGM.

--------------------------------------------------------------------------------
