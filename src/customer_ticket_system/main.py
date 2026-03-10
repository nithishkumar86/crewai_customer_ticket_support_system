from src.customer_ticket_system.main_crew import CustomerTicketCrew

def main_crew_all(customer_name: str, customer_email: str, issue: str):
    result = CustomerTicketCrew().crew().kickoff(
        inputs={
            "customer_name": customer_name,
            "customer_email": customer_email,
            "issue": issue
        }
    )
    return result
