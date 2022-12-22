from schemas import Patient

import os
import pickle
import uvicorn
import pandas as pd
from fastapi import FastAPI
from fastapi_health import health

app = FastAPI()
model = None


@app.on_event("startup")
def load_model():
    with open(os.getenv("PATH_TO_MODEL"), "rb") as f:
        global model
        model = pickle.load(f)


@app.get("/")
async def root():
    return "Hello!"


@app.post("/predict")
async def predict(data: Patient):
    X = pd.DataFrame([data.dict()])
    y = model.predict(X)
    return True if not y[0] else False


def check_health():
    return model is not None


async def success_handler(**kwargs):
    return 'Model is ready'


async def failure_handler(**kwargs):
    return 'Model is not ready'


app.add_api_route("/health", health([check_health],
                                    success_handler=success_handler,
                                    failure_handler=failure_handler))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5432)