# Production ready project

## Setup python3 virtual environment and required libs
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Download dataset from kaggle

- Navigate to the project root
- Create `credentials/` folder
- Put `kaggle.json` into `credentials/` folder [(how to)](https://www.kaggle.com/docs/api)

- navigate to the `scripts` folder
- run `python3 download_dataset.py`

Dataset will be downloaded into the `data` folder.

## Run jupyter notebooks locally

- Add venv kernel:
```
python -m ipykernel install --user --name=.venv
```
- Run jupyter notebook
```
jupyter notebook
```
- In jupyter notebook change kernel to `.venv` (Kernel -> Change Kernel -> .venv)
- Run notebook

To remove _venv_ kernel run:
```
jupyter-kernelspec uninstall .venv
```

## Generate EDA report:

- Navigate to the `scripts` folder
- Run `generate_EDA_report.sh` script:
    ```
    bash generate_EDA_report.sh
    ```

HTML report will be generated and placed into `reports/` folder

## Models

For prototyping `LogisticRegression` and `kNN` models from `sklearn`
are used. Corresponding notebook: `notebooks/Heart-Disease-Cleveland-UCI-models.ipynb`.

## Fit and predict from command line

**Fit:**

- Navigate to the `src` folder
- Run:
  ```
  python3 main_pipeline.py --fit \
                           --X_train "data/X_train.csv" \
                           --y_train "data/y_train.csv" \
                           --model_path "models/model.sav"
  ```
  
**Predict** (Note: must be ran only after **fit**)

- Navigate to the `src` folder
- Run:
  ```
  python3 main_pipeline.py --predict \
                           --model_path "models/model.sav" \
                           --X_test "data/X_test.csv" \
                           --y_pred "data/y_pred.csv"
  ```

## Configs

Configs are also supported, example:
```
python3 main_pipeline.py --config_path configs/knn_config.yml --fit --predict
```

See all available configs in the `configs/` directory.
