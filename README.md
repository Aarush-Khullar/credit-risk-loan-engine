# credit-risk-loan-engine
Rule-based credit risk and loan decision engine
# Credit Risk & Loan Decision Engine

This project simulates a simplified credit risk evaluation and loan approval system inspired by real-world fintech and NBFC lending workflows.

## Features
- Rule-based credit risk scoring
- Loan approval and rejection logic
- Risk classification (Low / Medium / High)
- Explainable financial constraints

## How it works
1. Applicant data is loaded from a CSV file
2. A risk score is calculated using income, EMI burden, credit utilization, and employment stability
3. Hard constraints are applied (e.g., EMI-to-income limits)
4. Applicants are approved or rejected based on risk thresholds

## Tech Stack
- Python
- CSV data handling
- Rule-based decision logic

## Future Improvements
- Probability of default (PD) estimation using statistical models
- Loan amount and interest rate optimization
- Stress testing and scenario analysis
