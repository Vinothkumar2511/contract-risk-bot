RISK_KEYWORDS = {
    "High": [
        "indemnify", "penalty", "unilateral", "non-compete",
        "terminate at any time", "irrevocable"
    ],
    "Medium": [
        "auto-renewal", "lock-in", "arbitration",
        "jurisdiction", "liability"
    ]
}

def assess_clause_risk(clause):
    clause_lower = clause.lower()
    for level, words in RISK_KEYWORDS.items():
        if any(w in clause_lower for w in words):
            return level
    return "Low"

def contract_risk_score(clauses):
    scores = {"Low": 1, "Medium": 2, "High": 3}
    total = sum(scores[assess_clause_risk(c)] for c in clauses)
    return round(total / len(clauses), 2)
