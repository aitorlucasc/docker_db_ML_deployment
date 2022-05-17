from flask import Flask
import pickle
import json
from sklearn import datasets
from sklearn.model_selection import train_test_split

app = Flask(__name__)


@app.route("/predict")
def predict():
    with open('iris_trained_model.pkl', 'rb') as f:
        clf_loaded = pickle.load(f)

    # Load the data
    iris_dict = datasets.load_iris()
    X = iris_dict['data']
    y = iris_dict['target']

    # shuffle arrays since y values are in order
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

    preds = clf_loaded.predict(X_test)
    results = {
        "original_values": X_test.tolist(),
        "predictions": preds.tolist()
    }

    return json.dumps(results, indent=4, sort_keys=True)


if __name__ == "__main__":
    app.run(debug=False)
