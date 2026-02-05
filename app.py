import streamlit as st
from contract_parser import extract_text, extract_clauses
from risk_engine import assess_clause_risk, contract_risk_score
from explainer import explain_clause, renegotiation_suggestion
from utils import log_audit

st.set_page_config(page_title="Contract Risk Bot")

st.title("📜 Contract Analysis & Risk Assessment Bot")

uploaded = st.file_uploader("Upload Contract", type=["pdf", "docx", "txt"])

if uploaded:
    text = extract_text(uploaded)
    clauses = extract_clauses(text)

    st.subheader("📊 Contract Risk Summary")
    score = contract_risk_score(clauses)
    st.metric("Overall Risk Score", score)

    st.subheader("🔍 Clause Analysis")
    results = []

    for i, clause in enumerate(clauses):
        risk = assess_clause_risk(clause)
        st.markdown(f"### Clause {i+1} — Risk: **{risk}**")
        st.write(clause)
        st.info(explain_clause(clause))
        st.warning(renegotiation_suggestion(risk))

        results.append({"clause": clause, "risk": risk})

    log_audit(uploaded.name, results)

    st.success("✅ Analysis completed & audit log saved.")
