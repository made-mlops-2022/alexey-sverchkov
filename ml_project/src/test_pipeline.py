from models.fit_predict import ModelType, normalize, fit, predict
from data.prepare_data import prepare_data

import unittest
import os
import rootpath
import pandas as pd


DATASET_PATH = os.path.join(rootpath.detect(), "data/heart_cleveland_upload.csv")
X_TRAIN_PATH = os.path.join(rootpath.detect(), "data/X_train.csv")
Y_TRAIN_PATH = os.path.join(rootpath.detect(), "data/y_train.csv")
X_TEST_PATH = os.path.join(rootpath.detect(), "data/X_test.csv")
Y_TEST_PATH = os.path.join(rootpath.detect(), "data/y_test.csv")
Y_PRED_PATH = os.path.join(rootpath.detect(), "data/y_pred.csv")
LOG_REG_MODEL_PATH = os.path.join(rootpath.detect(), "models/log_reg.sav")
KNN_MODEL_PATH = os.path.join(rootpath.detect(), "models/knn.sav")

MODELS = [ModelType.LOG_REG, ModelType.KNN]

MODEL_TO_PATH = {
    ModelType.LOG_REG : LOG_REG_MODEL_PATH,
    ModelType.KNN : KNN_MODEL_PATH
}

MODEL_TO_SCORE = {
    ModelType.LOG_REG: 0.83,
    ModelType.KNN: 0.85
}


class TestFit(unittest.TestCase):
    def setUp(self):
        prepare_data()

    def test_fit(self):
        for model in MODELS:
            fit(model,
                pd.read_csv(X_TRAIN_PATH),
                pd.read_csv(Y_TRAIN_PATH).target,
                MODEL_TO_PATH[model])
            self.assertTrue(os.path.exists(MODEL_TO_PATH[model]))


class TestPredict(unittest.TestCase):
    def test_predict(self):
        for model in MODELS:
            predict(MODEL_TO_PATH[model],
                    pd.read_csv(X_TEST_PATH),
                    Y_PRED_PATH)
            self.assertTrue(os.path.exists(Y_PRED_PATH))