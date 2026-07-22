# model.py
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

def train_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = LogisticRegression(max_iter=200)
    clf.fit(X, y)
    joblib.dump(clf, "iris_model.pkl")

if __name__ == "__main__":
    train_model()
