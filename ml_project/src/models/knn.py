from sklearn.neighbors import KNeighborsClassifier
import pickle


class Knn:
    def __init__(self, n_neighbors=2):
        self.__model = KNeighborsClassifier(n_neighbors=n_neighbors)

    def fit_and_save(self, X_train, y_train, model_path):
        self.__model.fit(X_train, y_train)

        with open(model_path, 'wb') as fout:
            pickle.dump(self.__model, fout)

