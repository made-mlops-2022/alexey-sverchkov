FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

ENV PATH_TO_MODEL="/app/models/model.sav"
ENV MODEL_URL="https://drive.google.com/uc?id=1-c9NsbT79_7h6YOKrlcx2XXZRSqb3LjA"

# Install dependencies and download model
RUN pip install -r requirements.txt &&  \
    bash /app/scripts/download_model.sh

EXPOSE 5432

CMD ["python", "/app/src/app.py"]