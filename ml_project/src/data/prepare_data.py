import os
from data.split_data_on_train_test import split_data_on_train_test
import rootpath

DATASET_PATH = os.path.join(rootpath.detect(), "data/heart_cleveland_upload.csv")
X_TRAIN_PATH = os.path.join(rootpath.detect(), "data/X_train.csv")
Y_TRAIN_PATH = os.path.join(rootpath.detect(), "data/y_train.csv")
X_TEST_PATH = os.path.join(rootpath.detect(), "data/X_test.csv")
Y_TEST_PATH = os.path.join(rootpath.detect(), "data/y_test.csv")

def prepare_data():
    X_train, X_test, y_train, y_test = split_data_on_train_test(DATASET_PATH)

    X_train.to_csv(X_TRAIN_PATH)
    y_train.to_csv(Y_TRAIN_PATH)
    X_test.to_csv(X_TEST_PATH)
    y_test.to_csv(Y_TEST_PATH)