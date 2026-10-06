from churn_predictor import ChurnPredictor


predictor = ChurnPredictor("customers.csv")

predictor.train_model()

print("\n===== ENTER CUSTOMER DETAILS =====")

age = int(input("Age: "))
tenure = int(input("Tenure (months): "))
monthly_charges = float(input("Monthly charges: ₹"))
support_tickets = int(input("Support tickets: "))

predictor.predict_churn(
    age,
    tenure,
    monthly_charges,
    support_tickets
)