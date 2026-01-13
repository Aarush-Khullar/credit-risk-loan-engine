import csv
from src.scoring import calculate_risk_score
from src.decision import loan_decision

with open("data/applicants.csv", newline="") as file:
    reader = csv.DictReader(file)
    applicants = list(reader)

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
    decision, risk_category = loan_decision(applicant, risk_score)

    print(f"Applicant {idx}")
    print(f"  Risk Score: {risk_score}")
    print(f"  Decision: {decision} ({risk_category})\n")
