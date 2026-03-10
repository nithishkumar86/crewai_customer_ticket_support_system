from crewai import Agent, Task, Crew, Process, LLM
from crewai.project import CrewBase, agent, task, crew
from src.Schema.schemas import TicketClassification, TicketPriority, TicketSolution, EmailDraft
from src.Guardrails.task_guardrial import validate_classification, validate_priority, validate_solution
from src.Callbacks.task_callbacks import send_email_callback
import os
from dotenv import load_dotenv
load_dotenv()


@CrewBase
class CustomerTicketCrew():
    """Customer Support Ticket System Crew"""

    agents_config = "config/agents.yaml"
    tasks_config  = "config/tasks.yaml"

    # llm = LLM(  
    #     model="ollama/deepseek-v3.1:671b-cloud",
    #     base_url="http://localhost:11434",
    #     temperature=0.5
    # )   

    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        temperature=0.5
    )

    # ─────────────────────────────────────────────
    # Agents
    # ─────────────────────────────────────────────

    @agent
    def classifier_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["classifier_agent"],
            llm=self.llm
        )

    @agent
    def priority_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["priority_agent"],
            llm=self.llm
        )

    @agent
    def solution_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["solution_agent"],
            llm=self.llm
        )

    @agent
    def email_drafter_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["email_drafter_agent"],
            llm=self.llm
        )

    # ─────────────────────────────────────────────
    # Tasks
    # ─────────────────────────────────────────────

    @task
    def classify_ticket_task(self) -> Task:
        return Task(
            config=self.tasks_config["classify_ticket_task"],
            output_pydantic=TicketClassification,
            guardrail=validate_classification
        )

    @task
    def prioritize_ticket_task(self) -> Task:
        return Task(
            config=self.tasks_config["prioritize_ticket_task"],
            output_pydantic=TicketPriority,
            guardrail=validate_priority
        )

    @task
    def generate_solution_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_solution_task"],
            output_pydantic=TicketSolution,
            guardrail=validate_solution,
            context=[
                self.classify_ticket_task(),
                self.prioritize_ticket_task()
            ]
        )

    @task
    def draft_email_task(self) -> Task:
        return Task(
            config=self.tasks_config["draft_email_task"],
            output_pydantic=EmailDraft,
            callback=send_email_callback,
            context=[
                self.classify_ticket_task(),
                self.prioritize_ticket_task(),
                self.generate_solution_task()
            ]
        )

    # ─────────────────────────────────────────────
    # Crew
    # ─────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.classifier_agent(),
                self.priority_agent(),
                self.solution_agent(),
                self.email_drafter_agent()
            ],
            tasks=[
                self.classify_ticket_task(),
                self.prioritize_ticket_task(),
                self.generate_solution_task(),
                self.draft_email_task()
            ],
            process=Process.sequential,
            verbose=True
        )