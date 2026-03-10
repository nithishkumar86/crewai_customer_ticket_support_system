import json
from src.Schema.schemas import TicketClassification, TicketPriority, TicketSolution


# ─────────────────────────────────────────────
# Guardrail 1 — Classifier Agent
# ─────────────────────────────────────────────
def validate_classification(output):
    try:
        data = json.loads(output.raw)
        result = TicketClassification(**data)
    except Exception as e:
        return (False, f"Output parsing failed: {str(e)}. Return valid JSON with category, confidence_score, issue_summary.")

    valid_categories = ["Billing", "Technical", "Shipping", "Account", "General"]

    if result.category not in valid_categories:
        return (False, f"Invalid category '{result.category}'. Must be one of: {valid_categories}")

    if result.confidence_score < 0.5:
        return (False, f"Confidence score {result.confidence_score} is too low. Re-analyze and classify with higher confidence.")

    if not result.issue_summary or len(result.issue_summary.strip()) < 10:
        return (False, "Issue summary is too vague. Provide a clear and meaningful summary.")

    return (True, output)


# ─────────────────────────────────────────────
# Guardrail 2 — Priority Agent
# ─────────────────────────────────────────────
def validate_priority(output):
    try:
        data = json.loads(output.raw)
        result = TicketPriority(**data)
    except Exception as e:
        return (False, f"Output parsing failed: {str(e)}. Return valid JSON with priority_level, escalate_to_human, reason.")

    valid_priorities = ["Low", "Medium", "High", "Critical"]

    if result.priority_level not in valid_priorities:
        return (False, f"Invalid priority '{result.priority_level}'. Must be one of: {valid_priorities}")

    if not result.reason or len(result.reason.strip()) < 10:
        return (False, "Priority reason is too vague. Provide a clear justification.")

    if "billing" in result.reason.lower() and result.priority_level in ["Low", "Medium"]:
        return (False, f"Billing issues must be 'High' or 'Critical'. Current: {result.priority_level}")

    return (True, output)


# ─────────────────────────────────────────────
# Guardrail 3 — Solution Agent
# ─────────────────────────────────────────────
def validate_solution(output):
    try:
        data = json.loads(output.raw)
        result = TicketSolution(**data)
    except Exception as e:
        return (False, f"Output parsing failed: {str(e)}. Return valid JSON with suggested_solution, resolution_time, needs_followup.")

    word_count = len(result.suggested_solution.split())

    if word_count < 50:
        return (False, f"Solution is too short ({word_count} words). Minimum 50 words required.")

    if not result.resolution_time or len(result.resolution_time.strip()) == 0:
        return (False, "Resolution time is missing. Always specify an estimated resolution time.")

    if result.needs_followup and word_count < 60:
        return (False, "Ticket requires follow-up but solution lacks enough detail. Expand the resolution steps.")

    return (True, output)