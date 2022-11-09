import pandas as pd
from sklearn.model_selection import train_test_split

def split_data_on_train_test(dataset_path="data/heart_cleveland_upload.csv",
                             test_size=0.1,
                             random_state=42):
    df = pd.read_csv(dataset_path)
    df.rename(columns={'condition':'target'}, inplace=True)

    X = df.drop("target", axis="columns")
    y = df.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test
