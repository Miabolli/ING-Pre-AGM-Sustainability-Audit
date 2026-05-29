import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Set a random seed so your data looks the same every time you run it
np.random.seed(42)

# --- PART 1: DATA GENERATION (The Root Cause Analysis baseline) ---
print("Generating corporate client data...")
num_clients = 1000
client_ids = [f"CLI-{str(i).zfill(4)}" for i in range(1, num_clients + 1)]
industries = np.random.choice(["Logistics", "Energy", "Retail", "Manufacturing", "Agriculture"], size=num_clients)
loan_amounts = np.random.uniform(5_000_000, 60_000_000, size=num_clients).round(2)

# Simulating the Azure leak: 15% of clients are compromised (1), 85% are secure (0)
azure_flags = np.random.choice(, size=num_clients, p=[0.85, 0.15])

self_reported = np.random.uniform(1000, 50000, size=num_clients).round(2)
audited = np.copy(self_reported)
esg_risk = np.random.uniform(10.0, 30.0, size=num_clients)

# Creating the "Greenwashing" fraud logic
for i in range(num_clients):
    if azure_flags[i] == 1:
        # Breached clients have audited emissions much higher than self-reported
        audited[i] = audited[i] * np.random.uniform(1.2, 1.8)
        esg_risk[i] += np.random.uniform(5.0, 15.0) 
    else:
        # Secure clients have normal standard variations
        audited[i] = audited[i] * np.random.uniform(0.95, 1.05)
        
df = pd.DataFrame({
    "Client_ID": client_ids,
    "Industry": industries,
    "Loan_Amount_EUR": loan_amounts,
    "Self_Reported_Emissions_Tons": self_reported.round(2),
    "Audited_Emissions_Tons": audited.round(2),
    "Azure_Security_Flag": azure_flags,
    "ESG_Risk_Rating": esg_risk.round(1)
})

# Calculate the discrepancy percentage
df["Emissions_Discrepancy_%"] = (((df["Audited_Emissions_Tons"] - df["Self_Reported_Emissions_Tons"]) / df["Self_Reported_Emissions_Tons"]) * 100).round(2)

# --- PART 2: MACHINE LEARNING (Random Forest Classification) ---
print("Training Machine Learning Model...")
features = ['Loan_Amount_EUR', 'Self_Reported_Emissions_Tons', 'ESG_Risk_Rating']
X = df[features]
y = df['Azure_Security_Flag'] 

# The model learns what a 'fraudulent' profile looks like
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X, y)

# Predict the probability of fraud for all clients
df['Predicted_Fraud_Probability_%'] = (rf_model.predict_proba(X)[:, 1] * 100).round(2)

# Save the dataset to your computer
df.to_csv("mock_ing_esg_azure_leak_with_ML.csv", index=False)
print("Dataset saved as CSV: mock_ing_esg_azure_leak_with_ML.csv")

# --- PART 3: GENERATING VISUALIZATIONS ---
print("Generating Executive Visualizations...")
sns.set_theme(style="whitegrid")

# Visual 1: The Financial Risk (Bar Chart)
plt.figure(figsize=(8, 5))
risk_volume = df.groupby('Azure_Security_Flag')['Loan_Amount_EUR'].sum() / 1e9 # Convert to Billions
sns.barplot(x=['Secure (0)', 'Breached (1)'], y=risk_volume.values, palette=['#1f77b4', '#d62728'])
plt.title("Sustainable Volume at Risk (in Billions EUR)", fontsize=14, fontweight='bold')
plt.ylabel("Volume (Billions EUR)")
plt.savefig("kpi_chart.png", bbox_inches='tight')
plt.close()

# Visual 2: The Root Cause / Greenwashing Anomaly (Scatter Plot)
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Self_Reported_Emissions_Tons', y='Audited_Emissions_Tons', 
                hue='Azure_Security_Flag', palette={0: '#1f77b4', 1: '#d62728'}, alpha=0.6)
plt.plot(, , 'k--', linewidth=1) # Perfect match baseline
plt.title("Self-Reported vs. Audited Emissions", fontsize=14, fontweight='bold')
plt.savefig("scatter_plot.png", bbox_inches='tight')
plt.close()

# Visual 3: ML Early Warning System (Top 10 Risk Clients)
top_10_risk = df[df['Azure_Security_Flag'] == 0].nlargest(10, 'Predicted_Fraud_Probability_%')
plt.figure(figsize=(10, 5))
sns.barplot(data=top_10_risk, x='Predicted_Fraud_Probability_%', y='Client_ID', color='#ff7f0e')
plt.title("Top 10 Currently 'Secure' Clients at High Risk of Fraud", fontsize=14, fontweight='bold')
plt.xlabel("Predicted Probability of Fraud (%)")
plt.savefig("top_10_risk_chart.png", bbox_inches='tight')
plt.close()

