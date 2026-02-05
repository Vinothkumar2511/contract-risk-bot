def explain_clause(clause):
    return (
        "This clause defines obligations or restrictions. "
        "You should ensure it does not unfairly favor the other party."
    )

def renegotiation_suggestion(risk):
    if risk == "High":
        return "Consider limiting liability or making terms mutual."
    if risk == "Medium":
        return "Clarify duration, scope, or termination rights."
    return "Clause appears business-friendly."
