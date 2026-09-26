import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def train():
    X, y = load_iris(return_X_y=True)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    joblib.dump(clf, "model.pkl")
    print("Model trained and saved to model.pkl")

if __name__ == "__main__":
    train()