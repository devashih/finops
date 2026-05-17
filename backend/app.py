from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# ==============================
# HOME ROUTE
# ==============================

@app.route("/")
def home():
    return jsonify({
        "message": "LendFlow FinOps API Running Successfully"
    })


# ==============================
# HEALTH CHECK
# ==============================

@app.route("/health")
def health():
    return jsonify({
        "status": "running",
        "application": "LendFlow FinOps Platform"
    })


# ==============================
# COST SUMMARY API
# ==============================

@app.route("/cost-summary")
def cost_summary():

    cost_df = pd.read_csv(
        "../datasets/monthly_cost_summary.csv"
    )

    total_cost = cost_df["cost"].sum()
    total_budget = cost_df["budget"].sum()
    over_budget = total_cost - total_budget

    return jsonify({
        "total_aws_cost": float(total_cost),
        "budget": float(total_budget),
        "over_budget": float(over_budget)
    })


# ==============================
# SERVICE COST BREAKDOWN
# ==============================

@app.route("/service-breakdown")
def service_breakdown():

    cost_df = pd.read_csv(
        "../datasets/monthly_cost_summary.csv"
    )

    return jsonify(
        cost_df.to_dict(orient="records")
    )


# ==============================
# RIGHTSIZING RECOMMENDATIONS
# ==============================

@app.route("/rightsizing")
def rightsizing():

    instance_df = pd.read_csv(
        "../datasets/instance_utilisation.csv"
    )

    recommendations = instance_df[
        instance_df["avg_cpu"] < 20
    ]

    estimated_savings = (
        recommendations["monthly_cost"].sum() * 0.4
    )

    return jsonify({
        "estimated_savings": float(
            estimated_savings
        ),
        "recommendations": recommendations.to_dict(
            orient="records"
        )
    })


# ==============================
# IDLE RESOURCES
# ==============================

@app.route("/idle-resources")
def idle_resources():

    idle_df = pd.read_csv(
        "../datasets/idle_resources.csv"
    )

    total_idle_cost = idle_df[
        "monthly_cost"
    ].sum()

    return jsonify({
        "total_idle_resource_cost": float(
            total_idle_cost
        ),
        "resources": idle_df.to_dict(
            orient="records"
        )
    })


# ==============================
# TAG COMPLIANCE
# ==============================

@app.route("/tag-compliance")
def tag_compliance():

    tag_df = pd.read_csv(
        "../datasets/tag_compliance_report.csv"
    )

    non_compliant = tag_df[
        tag_df["compliance_status"]
        == "NON_COMPLIANT"
    ]

    compliance_score = (
        (
            len(tag_df) - len(non_compliant)
        ) / len(tag_df)
    ) * 100

    return jsonify({
        "compliance_score": round(
            compliance_score,
            2
        ),
        "non_compliant_resources":
        non_compliant.to_dict(
            orient="records"
        )
    })


# ==============================
# ANOMALY DETECTION
# ==============================

@app.route("/anomalies")
def anomalies():

    anomaly_df = pd.read_csv(
        "../datasets/anomaly_events.csv"
    )

    return jsonify({
        "critical_alerts":
        anomaly_df.to_dict(
            orient="records"
        )
    })


# ==============================
# FINOPS EXECUTIVE SUMMARY
# ==============================

@app.route("/executive-summary")
def executive_summary():

    cost_df = pd.read_csv(
        "../datasets/monthly_cost_summary.csv"
    )

    instance_df = pd.read_csv(
        "../datasets/instance_utilisation.csv"
    )

    idle_df = pd.read_csv(
        "../datasets/idle_resources.csv"
    )

    total_cost = cost_df["cost"].sum()

    rightsizing = instance_df[
        instance_df["avg_cpu"] < 20
    ]

    rightsizing_savings = (
        rightsizing["monthly_cost"].sum() * 0.4
    )

    idle_savings = idle_df[
        "monthly_cost"
    ].sum()

    total_savings = (
        rightsizing_savings + idle_savings
    )

    optimized_cost = (
        total_cost - total_savings
    )

    return jsonify({

        "current_monthly_cost":
        float(total_cost),

        "estimated_savings":
        float(round(total_savings, 2)),

        "optimized_monthly_cost":
        float(round(optimized_cost, 2)),

        "annual_savings":
        float(round(total_savings * 12, 2))
    })


# ==============================
# START APPLICATION
# ==============================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
