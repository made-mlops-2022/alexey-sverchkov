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