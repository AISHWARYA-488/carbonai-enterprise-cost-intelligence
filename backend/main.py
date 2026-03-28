from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from sklearn.linear_model import LinearRegression
import random

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulated historical CO₂ data
X_history = np.array([[i] for i in range(100)])
y_history = 400 + (np.sin(X_history / 5) * 50) + np.random.normal(0, 5, (100, 1))

# Train ML model
model = LinearRegression()
model.fit(X_history, y_history)

@app.get("/api/data")
async def get_metrics():

    # Simulate real-time sensor value
    current_co2 = 400 + random.uniform(-10, 50)

    # Predict next CO₂ value
    predicted_next = model.predict([[101]])[0][0] + random.uniform(-5, 5)

    suggestion = "Maintain Flow"
    action_color = "green"
    savings = "$800/hr"

    if predicted_next > 430:
        suggestion = "Increase Amine Flow by 12%"
        action_color = "red"
        savings = "$1,500/hr"

    elif predicted_next < 390:
        suggestion = "Reduce Steam Usage by 5%"
        action_color = "blue"
        savings = "$1,000/hr"

    return {
        "current_co2": round(current_co2, 2),
        "predicted_co2": round(predicted_next, 2),
        "efficiency": "92%",
        "suggestion": suggestion,
        "status_color": action_color,
        "savings": savings
    }
