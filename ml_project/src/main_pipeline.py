from models.fit_predict import ModelType, normalize, fit, predict
from data.prepare_data import prepare_data
from logger.custom_logger import logger
from entities.model_params import read_model_params

import argparse
import pandas as pd
import rootpath
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', required=False)
    parser.add_argument('--fit', action='store_true')
    parser.add_argument('--predict', action='store_true')
    parser.add_argument("--X_train", default="data/X_train.csv")
    parser.add_argument("--y_train", default="data/y_train.csv")
    parser.add_argument("--model_path", default="models/model.sav")
    parser.add_argument("--X_test", default="data/X_test.csv")
    parser.add_argument("--y_pred", default="data/y_pred.csv")
    args = parser.parse_args()

    logger.info("Pipeline starting...")

    prepare_data()

    X_train_normalized, X_test_normalized = normalize(pd.read_csv(os.path.join(rootpath.detect(), "data/X_train.csv")),
                                                      pd.read_csv(os.path.join(rootpath.detect(), "data/X_test.csv")))

    logger.debug("Data preparation was finished successfully")

    if args.fit:
        logger.info("Fit model")

        model_type = ModelType.LOG_REG
        if args.config_path:
            logger.info("Parameters will be taken from config")
            model_params = read_model_params(os.path.join(rootpath.detect(), args.config_path))

            model_type = None
            if model_params.model_type == "LogReg":
                model_type = ModelType.LOG_REG
            elif model_params.model_type == "Knn":
                model_type = ModelType.KNN

        fit(model_type,
            X_train_normalized,
            pd.read_csv(os.path.join(rootpath.detect(), args.y_train)).target,
            os.path.join(rootpath.detect(), args.model_path))

    if args.predict:
        logger.info("Predict data")
        predict(os.path.join(rootpath.detect(), args.model_path),
                X_test_normalized,
                os.path.join(rootpath.detect(), args.y_pred))

    logger.info("Pipeline was finished successfully")
