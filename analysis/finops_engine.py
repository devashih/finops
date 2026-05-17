import pandas as pd

# Load datasets
cost_df = pd.read_csv("../datasets/monthly_cost_summary.csv")
instance_df = pd.read_csv("../datasets/instance_utilisation.csv")
tag_df = pd.read_csv("../datasets/tag_compliance_report.csv")
idle_df = pd.read_csv("../datasets/idle_resources.csv")
anomaly_df = pd.read_csv("../datasets/anomaly_events.csv")

# Total AWS Cost
total_cost = cost_df["cost"].sum()

# Rightsizing Recommendations
rightsizing = instance_df[instance_df["avg_cpu"] < 20]

rightsizing_savings = (
    rightsizing["monthly_cost"].sum() * 0.4
)

# Tag Compliance
non_compliant = tag_df[
    tag_df["compliance_status"] == "NON_COMPLIANT"
]

# Idle Resources
idle_cost = idle_df["monthly_cost"].sum()

# Anomaly Detection
critical_alerts = anomaly_df[
    anomaly_df["severity"] == "P1"
]

# Total Estimated Savings
total_estimated_savings = (
    rightsizing_savings + idle_cost
)

print("\n===== FINOPS PLATFORM REPORT =====\n")

print(f"Total AWS Cost: ${total_cost}")

print(
    f"\nEstimated Savings: "
    f"${total_estimated_savings:.2f}"
)

print("\n===== RIGHTSIZING =====")
print(rightsizing)

print("\n===== NON COMPLIANT RESOURCES =====")
print(non_compliant)

print("\n===== CRITICAL ALERTS =====")
print(critical_alerts)
