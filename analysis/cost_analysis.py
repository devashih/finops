import pandas as pd

# Load datasets
cost_df = pd.read_csv("../datasets/monthly_cost_summary.csv")
instance_df = pd.read_csv("../datasets/instance_utilisation.csv")

# Total cost
total_cost = cost_df["cost"].sum()

# Budget
total_budget = cost_df["budget"].sum()

# Savings target
target_savings = 60000

# Over budget
over_budget = total_cost - total_budget

# Rightsizing recommendations
recommendations = []

for index, row in instance_df.iterrows():
    if row["avg_cpu"] < 20:
        recommendations.append({
            "instance_id": row["instance_id"],
            "current_type": row["instance_type"],
            "cpu": row["avg_cpu"],
            "monthly_cost": row["monthly_cost"],
            "recommendation": "Downsize Instance"
        })

# Estimated savings
estimated_savings = sum(
    r["monthly_cost"] * 0.4 for r in recommendations
)

# Print results
print("\n===== LendFlow FinOps Analysis =====\n")

print(f"Total AWS Monthly Cost: ${total_cost}")
print(f"Budget Limit: ${total_budget}")
print(f"Over Budget: ${over_budget}")

print("\n===== Rightsizing Recommendations =====\n")

for r in recommendations:
    print(
        f"{r['instance_id']} | "
        f"{r['current_type']} | "
        f"CPU: {r['cpu']}% | "
        f"Recommendation: {r['recommendation']}"
    )

print(f"\nEstimated Monthly Savings: ${estimated_savings:.2f}")
