import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset
df = pd.read_csv(
    "../datasets/forecast_data.csv"
)

# Train model
model = IsolationForest(
    contamination=0.2
)

df["anomaly"] = model.fit_predict(
    df[["cost"]]
)

# Print anomalies
print(df)
