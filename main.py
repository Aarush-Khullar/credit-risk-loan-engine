import csv
from src.scoring import calculate_risk_score
from src.decision import loan_decision
from src.loan_terms import recommend_loan_terms
from src.pd_model import PDModel

with open("data/applicants.csv", newline="") as file:
    reader = csv.DictReader(file)
    applicants = list(reader)

pd_model = PDModel()
pd_model.train("data/applicants.csv")

for idx, row in enumerate(applicants, start=1):
    applicant = {
        "age": int(row["age"]),
        "monthly_income": int(row["monthly_income"]),
        "existing_emi": int(row["existing_emi"]),
        "credit_utilization": float(row["credit_utilization"]),
        "employment_years": int(row["employment_years"]),
        "loan_amount_requested": int(row["loan_amount_requested"]),
    }

    risk_score = calculate_risk_score(applicant)
    pd = pd_model.predict_pd(applicant)
    decision, risk_category = loan_decision(applicant, risk_score)

    print(f"Applicant {idx}")
    print(f"  Risk Score: {risk_score}")
    print(f"  Probability of Default: {pd:.2f}")
    print(f"  Decision: {decision} ({risk_category})")

    if decision == "Approved":
        terms = recommend_loan_terms(applicant, risk_category)
        print(f"  Suggested Loan Amount: ₹{terms['max_loan_amount']}")
        print(f"  Interest Rate: {terms['interest_rate']}%")
        print(f"  Tenure: {terms['tenure_years']} years")

    print()
