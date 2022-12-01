import json
import requests
import pandas as pd
import gdown

HOST = "localhost"
PORT = "5432"

REQUEST_URL = f"http://{HOST}:{PORT}/predict"

DATA_URL = "https://drive.google.com/uc?id=1j9O3o-NPP_fD9pCYsVnVeT5m4M_bRdb8"
DATA_PATH = "data/data.csv"

if __name__ == "__main__":
    gdown.download(DATA_URL, DATA_PATH, quiet=True)

    data = pd.read_csv(DATA_PATH)
    for record in data.to_dict(orient="records"):
        response = requests.post(REQUEST_URL, json.dumps(record))
        print(f"{response.status_code=}, {response.text=}")