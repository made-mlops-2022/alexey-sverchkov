from enum import Enum
import pickle
import pandas as pd

from models.log_reg import LogReg
from models.knn import Knn
from logger.custom_logger import logger


class ModelType(Enum):
    LOG_REG = 1,
    KNN = 2


def normalize(X_train, X_test):
    X_train = (X_train - X_train.min()) / (X_train.max() - X_train.min()).values
    X_test = (X_test - X_test.min()) / (X_test.max() - X_test.min()).values
    logger.debug("X_train, X_test are normalized")
    return X_train, X_test

def fit(model_type: ModelType, X_train, y_train, model_path):
    if model_type == ModelType.LOG_REG:
        model = LogReg()
        logger.debug("Current model is Logistic Regression")
    elif model_type == ModelType.KNN:
        logger.debug("Current model is kNN")
        model = Knn()
    model.fit_and_save(X_train, y_train, model_path)

def predict(model_path, X_test, pred_output_path):
    with open(model_path, "rb") as fin:
        model = pickle.load(fin)
    y_pred = model.predict(X_test)
    logger.debug("Data was predicted successfully")
    pd.DataFrame(y_pred).to_csv(pred_output_path)
