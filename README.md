# AI Fraud Detector

A B2B AI Agent platform for detecting financial fraud patterns in transaction data, built with FastAPI and Large Language Models (LLMs).

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.142-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Problem Statement

Fintech startups and accounting firms process thousands of transactions daily. Manual audit is impossible at scale, and traditional rule-based systems miss sophisticated fraud patterns like:

- Split Invoicing: Breaking a large invoice into multiple smaller ones to bypass approval limits
- Cash Swiping: Rapid consecutive cash withdrawals to avoid detection thresholds

## Solution

This API uses an AI Agent (LLM-powered) as a Forensic Accountant to analyze transaction patterns and detect anomalies with human-readable reasoning.

## Architecture

Client/Web -> FastAPI Backend -> AI Agent (LLM) -> Multi-LLM Router (Claude, GPT, DeepSeek)

## Tech Stack

- Backend: Python 3.14, FastAPI, Uvicorn
- AI: OpenAI SDK (compatible with any OpenAI-compatible endpoint)
- LLM Router: Multi-provider fallback (Claude Sonnet, GPT, DeepSeek)
- Data Validation: Pydantic v2

## Quick Start

### Prerequisites

- Python 3.11+
- LLM endpoint (OpenAI, Anthropic, or any OpenAI-compatible router)

### Installation

    git clone https://github.com/kevinagustianawork/ai-fraud-detector.git
    cd ai-fraud-detector
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Run the Server

    uvicorn main:app --reload

Open http://127.0.0.1:8000/docs for interactive API documentation.

## API Endpoints

### GET /

Health check - returns API status.

### GET /api/v1/audit-fraud

Analyzes simulated transaction data and returns detected fraud cases.

Sample Response:

    {
      "success": true,
      "data": {
        "has_fraud": true,
        "detected_cases": [
          {
            "case_type": "Split Invoicing",
            "suspect_user": "USR_02",
            "evidence_tx_ids": ["TX1002", "TX1003", "TX1004"],
            "reasoning_english": "User USR_02 split a single office renovation project into three separate invoices..."
          },
          {
            "case_type": "Cash Swiping",
            "suspect_user": "USR_03",
            "evidence_tx_ids": ["TX1005", "TX1006", "TX1007"],
            "reasoning_english": "User USR_03 made three identical cash withdrawals..."
          }
        ]
      }
    }

## Cost Control and Error Handling

- Deterministic output: temperature=0.1 and response_format=json_object
- Fallback parsing: Extracts JSON even from malformed LLM responses
- Graceful degradation: Returns structured error object instead of crashing

## Roadmap

- [ ] Frontend dashboard (React / Next.js)
- [ ] PDF report generation
- [ ] Real-time streaming analysis
- [ ] Integration with real fintech APIs (Xendit, Midtrans)
- [ ] Fine-tuned fraud detection model

## License

MIT License

## Author

Kevin Agustiana - Full-Stack AI Engineer

- GitHub: @kevinagustianawork
- LinkedIn: Kevin Agustiana

Star this repo if you find it useful!
