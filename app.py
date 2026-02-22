from fastapi import FastAPI
from pydantic import BaseModel
from src.pd_model import PDModel
from src.decision import loan_decision

app = FastAPI(title="Credit Risk Engine API")

# Load trained model once at startup
pd_model = PDModel()
pd_model.load("models/pd_model.pkl")


class Applicant(BaseModel):
    month_duration: int
    credit_amount: float
    payment_to_income_ratio: int
    age: int
    n_credits: int
    residence_since: int


@app.get("/")
def health():
    return {"status": "Credit Risk Engine Running"}


@app.post("/predict")
def predict(applicant: Applicant):
    applicant_dict = applicant.dict()

    # Predict Probability of Default
    pd_value = pd_model.predict_pd(applicant_dict)

    # Decision Logic (PD threshold based)
    decision, risk_category = loan_decision(applicant_dict, pd_value)

    # Expected Loss Calculation
    LGD = 0.4  # assumed Loss Given Default
    expected_loss = pd_value * applicant_dict["credit_amount"] * LGD

    response = {
        "probability_of_default": round(pd_value, 4),
        "expected_loss": round(expected_loss, 2),
        "decision": decision,
        "risk_category": risk_category,
    }

    return response