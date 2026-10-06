# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import analyze_fraud_with_ai

app = FastAPI(title="B2B AI Fraud Auditor Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "AI Fraud Detection API is running"}

@app.get("/api/v1/audit-fraud")
def audit_financial_transactions():
    try:
        analysis_result = analyze_fraud_with_ai()
        return {"success": True, "data": analysis_result}
    except Exception as e:
        return {"success": False, "error": str(e)}

