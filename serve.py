from pathlib import Path
from typing import Optional

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="Car Price Prediction API",
    version="1.0.0",
    description="Predict car selling price using the trained machine learning model.",
    docs_url="/docs",
)

model_path = Path(__file__).with_name("car_price_model.pkl")
model = joblib.load(model_path)


class CarFeatures(BaseModel):
    Make: str
    Model: str
    Year: int
    Fuel_Type: str
    Transmission: Optional[str] = None
    Engine_Size: Optional[float] = None
    Mileage: Optional[int] = None
    Horsepower: Optional[float] = None
    Torque: Optional[float] = None
    Owners: Optional[int] = None
    Accident_History: Optional[float] = None
    Service_History: Optional[str] = None
    Color: Optional[str] = None
    Body_Type: Optional[str] = None
    Drivetrain: Optional[str] = None
    Fuel_Efficiency: Optional[float] = None
    Location: Optional[str] = None


class PredictionResponse(BaseModel):
    predicted_selling_price: float


@app.get("/")
def home() -> dict:
    return {"message": "FastAPI model server is running. Use /predict to POST car features."}


@app.get("/health")
def health() -> dict:
    """Health check endpoint returns model load status."""
    try:
        return {"status": "ok", "model_loaded": True}
    except Exception:
        return {"status": "error", "model_loaded": False}


@app.post("/predict", response_model=PredictionResponse)
def predict(features: CarFeatures) -> PredictionResponse:
    try:
        input_frame = pd.DataFrame([features.model_dump()])
        prediction = model.predict(input_frame)
        return PredictionResponse(predicted_selling_price=float(prediction[0]))
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.on_event("startup")
def write_openapi_file():
    """Write the OpenAPI schema to openapi.json at startup for reference."""
    try:
        schema = app.openapi()
        out = Path(__file__).with_name("openapi.json")
        import json

        with open(out, "w", encoding="utf-8") as f:
            json.dump(schema, f, indent=2)
    except Exception:
        pass

if __name__ == "__main__":
    uvicorn.run("serve:app", host="0.0.0.0", port=8000, reload=False)
