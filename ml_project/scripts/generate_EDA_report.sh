DATASET_PATH="../data/heart_cleveland_upload.csv"

papermill ../notebooks/Heart-Disease-Cleveland-UCI-EDA.ipynb \
          ../notebooks/Heart-Disease-Cleveland-UCI-EDA-executed.ipynb \
          -p dataset_path ${DATASET_PATH}

jupyter nbconvert ../notebooks/Heart-Disease-Cleveland-UCI-EDA-executed.ipynb \
        --to html \
        --output EDA_report.html

rm ../notebooks/Heart-Disease-Cleveland-UCI-EDA-executed.ipynb

mkdir -p ../reports/ && mv ../notebooks/EDA_report.html ../reports/EDA_report.html
