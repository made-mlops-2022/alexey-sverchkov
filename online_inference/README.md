# Online inference (hw-2)

## Local docker image build and run

- Verify that you are at root folder `online_inference`
- Run
  ```
  bash scripts/build_and_run.sh
  ```

## Pull docker image from Docker Hub:

Run the following commands:
- `docker pull 72396544/online_inference:1.0.0`
- `docker run -p 5432:5432 72396544/online_inference:1.0.0`

## REST API

- Setup venv and dependencies
  ```
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```

- To get prediction on test data just run:
  `python src/predict.py`

Data and model are hosted and downloaded from _Google Drive_.


### Docker images size optimization:

1. Choose more lightweight basic image (slim version)
2. Minimize number of layers, use only necessary (e.g. one `COPY` and one `RUN` instructions)
3. Exclude some files from image build via `.dockerignore`
4. Keep `requirements.txt` with only needed dependencies