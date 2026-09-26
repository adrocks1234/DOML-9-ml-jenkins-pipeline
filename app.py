import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("model.pkl")

class PredictRequest(BaseModel):
    features: list[float]

@app.get("/")
def home():
    return {"status": "Model API is running"}

@app.post("/predict")
def predict(data: PredictRequest):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}