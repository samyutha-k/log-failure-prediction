from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI(
    title="Log Failure Prediction System",
    description="ML-based log analysis and failure prediction",
    version="1.0"
)

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model",
    "random_forest_failure_model.pkl"
)

model = joblib.load(MODEL_PATH)


class LogFeatures(BaseModel):
    E1: int
    E2: int
    E3: int
    E4: int
    E5: int
    E6: int
    E7: int
    E8: int
    E9: int
    E10: int
    E11: int
    E12: int
    E13: int
    E14: int
    E15: int
    E16: int
    E17: int
    E18: int
    E19: int
    E20: int
    E21: int
    E22: int
    E23: int
    E24: int
    E25: int
    E26: int
    E27: int
    E28: int
    E29: int


@app.get("/", response_class=HTMLResponse)
def dashboard():

    template_path = os.path.join(
        os.path.dirname(__file__),
        "templates",
        "index.html"
    )

    with open(template_path, "r", encoding="utf-8") as file:
        return file.read()


@app.post("/predict")
def predict(data: LogFeatures):

    values = [[
        data.E1, data.E2, data.E3, data.E4, data.E5,
        data.E6, data.E7, data.E8, data.E9, data.E10,
        data.E11, data.E12, data.E13, data.E14, data.E15,
        data.E16, data.E17, data.E18, data.E19, data.E20,
        data.E21, data.E22, data.E23, data.E24, data.E25,
        data.E26, data.E27, data.E28, data.E29
    ]]

    columns = [f"E{i}" for i in range(1, 30)]

    features = pd.DataFrame(
        values,
        columns=columns
    )

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    result = "SUCCESS" if prediction == 0 else "FAIL"

    return {
        "prediction": result,
        "success_probability": round(
            float(probability[0]) * 100, 2
        ),
        "failure_probability": round(
            float(probability[1]) * 100, 2
        )
    }