def loan_decision(applicant, risk_score):
    income = applicant["monthly_income"]
    emi = applicant["existing_emi"]

    if emi / income > 0.4:
        return "Rejected", "High Risk"

    if risk_score < 40:
        return "Approved", "Low Risk"
    elif risk_score < 70:
        return "Approved", "Medium Risk"
    else:
        return "Rejected", "High Risk"
