import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, confusion_matrix, classification_report


class PDModel:
    def __init__(self):
        self.model = LogisticRegression(class_weight="balanced", max_iter=1000)


    def train(self, csv_path):
        # Load dataset
        df = pd.read_csv(csv_path)

        # Convert target to binary: bad = 1 (default), good = 0
        df["target"] = df["target"].map({"good": 0, "bad": 1})

        # Select numeric features only
        X = df[
            [
                "month_duration",
                "credit_amount",
                "payment_to_income_ratio",
                "age",
                "n_credits",
                "residence_since",
            ]
        ]

        y = df["target"]

        # Train-test split (80-20 split)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )

        # Train model
        self.model.fit(X_train, y_train)

        # Evaluate model
        y_pred_proba = self.model.predict_proba(X_test)[:, 1]
        y_pred = self.model.predict(X_test)

        roc = roc_auc_score(y_test, y_pred_proba)
        cm = confusion_matrix(y_test, y_pred)

        print("Model Evaluation Metrics")
        print("------------------------")
        print("ROC-AUC:", round(roc, 3))
        print("\nConfusion Matrix:")
        print(cm)
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

        # Save trained model
        joblib.dump(self.model, "models/pd_model.pkl")
        print("\nModel saved to models/pd_model.pkl")


        print("Class distribution:")
        print(y.value_counts())



    def load(self, model_path="models/pd_model.pkl"):
        import joblib
        self.model = joblib.load(model_path)
        print("Model loaded from", model_path)



    def predict_pd(self, applicant):
        X = pd.DataFrame([{
            "month_duration": applicant["month_duration"],
            "credit_amount": applicant["credit_amount"],
            "payment_to_income_ratio": applicant["payment_to_income_ratio"],
            "age": applicant["age"],
            "n_credits": applicant["n_credits"],
            "residence_since": applicant["residence_since"],
        }])

        return float(self.model.predict_proba(X)[0][1])
