from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
import pandas as pd
from pydantic import BaseModel
import os

# Ensure the correct path
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")

# Initialize FastAPI app
app = FastAPI()

# Load model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Define input schema
class InputData(BaseModel):
    Number_of_Vehicles: int
    Time_24hr: float
    First_Road_Class: int
    Road_Surface: int
    Lighting_Conditions: int
    Weather_Conditions: int
    Casualty_Severity: int
    Sex_of_Casualty: int
    Age_of_Casualty: float
    Type_of_Vehicle: int
    age_group: int
    vehicle_group: int

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    try:
        # Convert input data to a list in the correct order
        input_list = [
            data.Number_of_Vehicles,
            data.Time_24hr,
            data.First_Road_Class,
            data.Road_Surface,
            data.Lighting_Conditions,
            data.Weather_Conditions,
            data.Casualty_Severity,
            data.Sex_of_Casualty,
            data.Age_of_Casualty,
            data.Type_of_Vehicle,
            data.age_group,
            data.vehicle_group
        ]

        # Convert to numpy array and reshape
        input_array = np.array(input_list).reshape(1, -1)

        # Apply scaling (if used)
        #input_scaled = scaler.transform(input_array)  # If no scaler, use input_array directly

        # Make prediction
        prediction = model.predict(input_array).tolist()

        return {"prediction": prediction}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run using: uvicorn api.app:app --reload