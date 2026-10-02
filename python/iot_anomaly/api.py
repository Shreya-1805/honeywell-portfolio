"""FastAPI service: POST sensor readings, get anomalies back.
Run: uvicorn api:app --reload"""
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from anomaly import detect_anomalies

app = FastAPI(title="Sensor Anomaly Service")


class Readings(BaseModel):
    values: list[float] = Field(min_length=5)
    window: int = 20
    threshold: float = 3.0


@app.post("/anomalies")
def anomalies(r: Readings):
    df = detect_anomalies(pd.DataFrame({"temperature": r.values}),
                          window=r.window, threshold=r.threshold)
    idx = df.index[df["is_anomaly"]].tolist()
    return {"count": len(idx), "indices": idx}


@app.get("/health")
def health():
    return {"status": "ok"}
