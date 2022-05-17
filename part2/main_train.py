from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle

def main():
    try:
        # Load the data
        iris_dict = datasets.load_iris()
        X = iris_dict['data']
        y = iris_dict['target']

        # shuffle arrays since y values are in order
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

        # Fit the classifier
        clf = LogisticRegression(solver='lbfgs', max_iter=1000)
        clf.fit(X_train, y_train)

        # Prediction on test set
        y_pred = clf.predict(X_test)

        # Get the accuracy score
        acc = accuracy_score(y_test, y_pred)
        print(f"Model accuracy on test set: {acc * 100}%")

        # Save the model
        with open('iris_trained_model.pkl', 'wb') as f:
            pickle.dump(clf, f)

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
