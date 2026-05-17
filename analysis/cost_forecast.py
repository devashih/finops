import pandas as pd
from prophet import Prophet

# Load dataset
df = pd.read_csv("../datasets/forecast_data.csv")

# Rename columns
df.columns = ["ds", "y"]

# Create model
model = Prophet()

# Train model
model.fit(df)

# Future dates
future = model.make_future_dataframe(
    periods=3,
    freq='ME'
)

# Predict
forecast = model.predict(future)

# Show results
print(
    forecast[["ds", "yhat"]].tail(3)
)
