def loan_decision(applicant, pd):
    if pd > 0.5:
        return "Rejected", "High Risk"
    elif pd > 0.3:
        return "Approved", "Medium Risk"
    else:
        return "Approved", "Low Risk"
    # Basic DTI safety check
    dti = emi / income
    if dti > 0.5:
        return "Rejected", "High Risk"

    # Hard rejection if extremely high default probability
    if pd > 0.6:
        return "Rejected", "High Risk"

    # Expected Loss calculation
    LGD = 0.4  # assume 40% loss if default
    expected_loss = pd * loan_amount * LGD

    # Decision logic based on expected loss
    if expected_loss > 100000:
        return "Rejected", "High Risk"
    elif pd < 0.2:
        return "Approved", "Low Risk"
    else:
        return "Approved", "Medium Risk"
