# agent.py
import os
import json
from openai import OpenAI
from database import get_simulated_transactions

# KONEKSI KE NINE ROUTER (meja operator otak kita)
client = OpenAI(
    api_key=os.getenv("NINE_ROUTER_KEY", "sk-b7ada2740c573685-vmz05d-bbf08208"),
    base_url="http://127.0.0.1:20128/v1"
)

def analyze_fraud_with_ai():
    transactions = get_simulated_transactions()

    system_instruction = (
        "You are an expert Forensic Accountant and AI Fraud Auditor for Fintech startups. "
        "Analyze the provided transaction list and detect financial fraud patterns, specifically:\n"
        "1. Split Invoicing (breaking a large invoice into multiple smaller invoices under "
        "approval limits within a short time).\n"
        "2. Cash Swiping (repetitive cash withdrawals in a very short interval).\n\n"
        "Provide your analysis in structured JSON format with keys: 'has_fraud' (boolean), "
        "'detected_cases' (list of objects containing 'case_type', 'suspect_user', "
        "'evidence_tx_ids', and 'reasoning_english')."
    )

    response = client.chat.completions.create(
        model="Hermes-Combo",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Transactions Data: {json.dumps(transactions)}"}
        ],
        temperature=0.1
    )

    raw = response.choices[0].message.content
    
    # Coba parse JSON
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Kalau gagal, coba ekstrak JSON dari teks
        import re
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            return {"error": "AI tidak mengembalikan JSON", "raw": raw}

if __name__ == "__main__":
    # Bisa dijalankan langsung: python3 agent.py
    result = analyze_fraud_with_ai()
    print(json.dumps(result, indent=2, ensure_ascii=False))

