from pydantic import BaseModel
from typing import Literal


class TicketClassification(BaseModel):
    category: Literal["Billing", "Technical", "Shipping", "Account", "General"]
    confidence_score: float  # 0.0 to 1.0
    issue_summary: str


class TicketPriority(BaseModel):
    priority_level: Literal["Low", "Medium", "High", "Critical"]
    escalate_to_human: bool
    reason: str


class TicketSolution(BaseModel):
    suggested_solution: str
    resolution_time: str  # e.g. "2 hours", "24 hours"
    needs_followup: bool


class EmailDraft(BaseModel):
    email_subject: str
    email_body: str
    sent_to: str