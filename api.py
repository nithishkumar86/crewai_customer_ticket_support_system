import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from src.customer_ticket_system.main import CustomerTicketCrew

load_dotenv()

app = FastAPI(title="Customer Ticket Support System")


# ─────────────────────────────────────────────
# Request Model
# ─────────────────────────────────────────────
class TicketRequest(BaseModel):
    customer_name: str
    customer_email: str
    issue: str


# ─────────────────────────────────────────────
# POST /analyze-ticket
# ─────────────────────────────────────────────
@app.post("/analyze-ticket")
def analyze_ticket(request: TicketRequest):
    try:
        crew_instance = CustomerTicketCrew()

        crew_instance.crew().kickoff(
            inputs={
                "customer_name": request.customer_name,
                "customer_email": request.customer_email,
                "issue": request.issue
            }
        )

        # ✅ Access Task 3 output directly by task name
        solution_output = json.loads(crew_instance.generate_solution_task().output.raw)

        return {
            "status": "success",
            "customer_name": request.customer_name,
            "customer_email": request.customer_email,
            "solution": solution_output
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))