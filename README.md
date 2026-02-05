# Contract Analysis & Risk Assessment Bot for Indian SMEs

This project is a GenAI-powered legal assistant designed to help small and medium business owners understand complex legal contracts in plain business language.

## Problem Statement
Small and medium businesses often struggle to understand complex legal contracts. This tool helps identify legal risks, explain clauses simply, and highlight unfavorable terms before legal consultation.

## Solution Overview
The application analyzes contracts such as employment agreements, vendor contracts, service agreements, and partnership deeds. It performs clause extraction, risk classification, and contract-level risk scoring.

Potentially unfavorable clauses such as unilateral termination, indemnity obligations, non-compete clauses, arbitration and jurisdiction risks, and auto-renewal terms are highlighted. Each clause is explained in simple language with suggested renegotiation strategies.

## Tech Stack
- Python
- spaCy (NLP preprocessing)
- Streamlit (UI)

## Features
- Contract upload (PDF, DOCX, TXT)
- Clause-by-clause analysis
- Risk scoring (Low / Medium / High)
- Plain-language explanations
- Audit logging
- Local processing for confidentiality

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py

