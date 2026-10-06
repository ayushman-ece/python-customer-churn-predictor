import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


class ChurnPredictor:

    def __init__(self, file_name):
        self.data = pd.read_csv(file_name)

    def prepare_data(self):
        X = self.data[
            ["Age", "Tenure", "MonthlyCharges", "SupportTickets"]
        ]

        y = self.data["Churn"]

        return X, y

    def train_model(self):
        X, y = self.prepare_data()

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        self.model = DecisionTreeClassifier(
            max_depth=5,
            random_state=42
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        accuracy = accuracy_score(y_test, predictions)

        print("\n===== MODEL TRAINED =====")
        print("Decision Tree model trained successfully. ✅")

        print("\n===== MODEL EVALUATION =====")
        print(f"Accuracy: {accuracy * 100:.2f}%")

    def predict_churn(
        self,
        age,
        tenure,
        monthly_charges,
        support_tickets
    ):
        new_customer = pd.DataFrame({
            "Age": [age],
            "Tenure": [tenure],
            "MonthlyCharges": [monthly_charges],
            "SupportTickets": [support_tickets]
        })

        prediction = self.model.predict(new_customer)

        result = "CHURN" if prediction[0] == 1 else "STAY"

        print("\n===== CUSTOMER CHURN PREDICTION =====")
        print(f"Age              : {age}")
        print(f"Tenure           : {tenure} months")
        print(f"Monthly Charges  : ₹{monthly_charges}")
        print(f"Support Tickets  : {support_tickets}")
        print(f"Predicted Result : {result}")