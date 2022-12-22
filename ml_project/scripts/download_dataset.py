import os
import json
import rootpath

KAGGLE_API_CREDENTIALS_PATH = os.path.join(rootpath.detect(), "credentials/kaggle.json")
DATASET_PATH = os.path.join(rootpath.detect(), "data")
DATASET = "cherngs/heart-disease-cleveland-uci"
DATASET_URL = "https://www.kaggle.com/datasets/" + DATASET

with open(KAGGLE_API_CREDENTIALS_PATH) as fin:
    data = json.load(fin)

os.environ['KAGGLE_USERNAME'] = data["username"]
os.environ['KAGGLE_KEY'] = data["key"]

from kaggle.api.kaggle_api_extended import KaggleApi

if __name__ == "__main__":
    api = KaggleApi()
    api.authenticate()

    os.makedirs(DATASET_PATH, exist_ok=True)
    api.dataset_download_files(dataset=DATASET,
                               path=DATASET_PATH,
                               unzip=True)

    print("Dataset was successfully downloaded")
