import streamlit as st
import pandas as pd

# Load datasets
cost_df = pd.read_csv("datasets/monthly_cost_summary.csv")
instance_df = pd.read_csv("datasets/instance_utilisation.csv")
tag_df = pd.read_csv("datasets/tag_compliance_report.csv")
idle_df = pd.read_csv("datasets/idle_resources.csv")
anomaly_df = pd.read_csv("datasets/anomaly_events.csv")

# Metrics
total_cost = cost_df["cost"].sum()
total_budget = cost_df["budget"].sum()
over_budget = total_cost - total_budget

# Rightsizing
rightsizing = instance_df[
    instance_df["avg_cpu"] < 20
]

rightsizing_savings = (
    rightsizing["monthly_cost"].sum() * 0.4
)

# Idle Resources
idle_cost = idle_df["monthly_cost"].sum()

# Compliance
non_compliant = tag_df[
    tag_df["compliance_status"] == "NON_COMPLIANT"
]

# Anomalies
critical_alerts = anomaly_df[
    anomaly_df["severity"] == "P1"
]

# Total Savings
total_savings = (
    rightsizing_savings + idle_cost
)

# Streamlit Config
st.set_page_config(page_title="LendFlow FinOps")

# Title
st.title("LendFlow FinOps Optimization Platform")

# Main Metrics
st.header("Executive Cloud Cost Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("AWS Cost", f"${total_cost}")
col2.metric("Budget", f"${total_budget}")
col3.metric("Over Budget", f"${over_budget}")
col4.metric("Estimated Savings", f"${total_savings:.2f}")

# Cost Chart
st.subheader("Service Cost Breakdown")
st.bar_chart(cost_df.set_index("service")["cost"])

# Rightsizing
st.subheader("Rightsizing Recommendations")
st.dataframe(rightsizing)

# Idle Resources
st.subheader("Idle Resources")
st.dataframe(idle_df)

# Compliance Dashboard
st.subheader("Non-Compliant Resources")
st.dataframe(non_compliant)

# Critical Alerts
st.subheader("Critical Cost Alerts")
st.dataframe(critical_alerts)

# Success Message
st.success(
    "FinOps Governance Engine Running Successfully"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Dashboard",
        "Rightsizing",
        "Compliance",
        "Anomalies"
    ]
)
