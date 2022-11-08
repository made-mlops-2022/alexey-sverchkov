from models.fit_predict import ModelType, normalize, fit, predict
from data.prepare_data import prepare_data

import argparse
import pandas as pd
import rootpath
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--fit', action='store_true')
    parser.add_argument('--predict', action='store_true')
    parser.add_argument("--X_train", default="data/X_train.csv")
    parser.add_argument("--y_train", default="data/y_train.csv")
    parser.add_argument("--model_path", default="models/model.sav")
    parser.add_argument("--X_test", default="data/X_test.csv")
    parser.add_argument("--y_pred", default="data/y_pred.csv")
    args = parser.parse_args()

    print("pipeline started")

    prepare_data()

    X_train_normalized, X_test_normalized = normalize(pd.read_csv(os.path.join(rootpath.detect(), "data/X_train.csv")),
                                                      pd.read_csv(os.path.join(rootpath.detect(), "data/X_test.csv")))

    if args.fit:
        fit(ModelType.LOG_REG,
            X_train_normalized,
            pd.read_csv(os.path.join(rootpath.detect(), args.y_train)).target,
            os.path.join(rootpath.detect(), args.model_path))

    if args.predict:
        predict(os.path.join(rootpath.detect(), args.model_path),
                X_test_normalized,
                os.path.join(rootpath.detect(), args.y_pred))

    print("pipeline finished successfully")
