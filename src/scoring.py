def calculate_risk_score(applicant):
    income = applicant["monthly_income"]
    emi = applicant["existing_emi"]
    utilization = applicant["credit_utilization"]
    employment_years = applicant["employment_years"]

    score = 0

    # Income stability
    if income >= 100000:
        score += 10
    elif income >= 60000:
        score += 20
    else:
        score += 30

    # EMI burden
    dti = emi / income
    if dti > 0.4:
        score += 35
    elif dti > 0.25:
        score += 20
    else:
        score += 10

    # Credit utilization penalty
    score += utilization * 30

    # Employment stability bonus
    if employment_years >= 10:
        score -= 10
    elif employment_years >= 5:
        score -= 5

    return min(int(score), 100)
