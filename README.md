## 🚀 Demo Flow

Customer submits ticket via Streamlit UI
        ↓
FastAPI receives the request
        ↓
CrewAI Crew kicks off — 4 agents run sequentially
        ↓
🏷️  Classifier Agent   → identifies ticket category
        ↓
⚡  Priority Agent     → assigns urgency level
        ↓
🧠  Solution Agent     → generates step-by-step resolution
        ↓
✍️  Email Drafter      → crafts professional email reply
        ↓
🔔  Task Callback      → sends email automatically via SMTP
        ↓
Streamlit displays solution to support team ✅

---

## 🤖 Agents

| Agent | Role |
|---|---|
| 🏷️ Classifier Agent | Reads ticket and classifies into Billing / Technical / Shipping / Account / General |
| ⚡ Priority Agent | Assigns urgency — Low / Medium / High / Critical + escalation decision |
| 🧠 Solution Agent | Generates detailed step-by-step resolution with estimated time |
| ✍️ Email Drafter Agent | Drafts warm, empathetic, professional email reply to customer |

---

## 🛡️ Guardrails

Guardrails validate every agent output before passing to the next task. If validation fails — the agent automatically retries.

| Agent | Guardrail Rule |
|---|---|
| 🏷️ Classifier | Category must be one of 5 valid types + confidence ≥ 0.5 |
| ⚡ Priority | Billing tickets must be High or Critical — never Low or Medium |
| 🧠 Solution | Minimum 50 words + resolution time must be specified |

---

## 🔔 Callback

Once the Email Drafter Agent completes its task — a Task Callback fires automatically:
- Reads the structured EmailDraft Pydantic output
- Sends the email directly to the customer via Gmail SMTP
- Logs confirmation in terminal

def send_email_callback(output):
    email_draft: EmailDraft = output.pydantic  # fully available in callback!
    # sends email via SMTP...

---

## 📦 Pydantic Output Models

class TicketClassification(BaseModel):
    category: Literal["Billing", "Technical", "Shipping", "Account", "General"]
    confidence_score: float
    issue_summary: str

class TicketPriority(BaseModel):
    priority_level: Literal["Low", "Medium", "High", "Critical"]
    escalate_to_human: bool
    reason: str

class TicketSolution(BaseModel):
    suggested_solution: str
    resolution_time: str
    needs_followup: bool

class EmailDraft(BaseModel):
    email_subject: str
    email_body: str
    sent_to: str

---

## 🔧 Tech Stack

| Technology | Purpose |
|---|---|
| CrewAI | Multi-agent orchestration with @CrewBase |
| DeepSeek V3 | LLM backbone |
| Pydantic | Structured outputs for every agent |
| Guardrails | Validate agent outputs — auto retry on failure |
| Task Callbacks | Trigger email sending automatically |
| FastAPI | Backend REST API |
| Streamlit | Frontend UI |
| SMTP (Gmail) | Automated email delivery |

---

## 📁 Project Structure

src/
├── Guardrails/
│   └── task_guardrail.py
├── Schema/
│   └── schemas.py
├── Callbacks/
│   └── callbacks.py
└── customer_ticket_system/
    ├── config/
    │   ├── agents.yaml
    │   └── tasks.yaml
    ├── crew.py
    ├── main.py
    ├── api.py
    ├── app.py
    └── requirements.txt

---

## ⚙️ Setup and Installation

1. Clone the Repository

```
git clone (https://github.com/nithishkumar86/crewai_customer_ticket_support_system)
cd crewai_customer_ticket_support_system

```

2. Create Virtual Environment
```
uv init
uv venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux

```

4. Install Dependencies
uv add -r requirements.txt

5. Configure .env File
DEEPSEEK_API_KEY=your_deepseek_api_key
SENDER_EMAIL=your_gmail@gmail.com
SENDER_PASSWORD=your_gmail_app_password

6. Run the Project
Terminal 1: uvicorn api:app --reload
Terminal 2: streamlit run app.py

---

## 💡 Key Concepts Learned

✅ Guardrail fires BEFORE pydantic parsing → output.pydantic = None inside guardrail → must use json.loads(output.raw) to parse
✅ Callback fires AFTER pydantic conversion → output.pydantic fully available in callback
✅ context=[] passes previous task outputs automatically → no need for manual template variables
✅ output_pydantic forces LLM to return structured JSON AND converts output for next agent
✅ @CrewBase keeps agents and tasks cleanly separated in YAML config files

---

Built to demonstrate Agentic AI Engineering using CrewAI 🚀
Looking for Agentic AI Internship or Junior AI Engineer opportunities!
</div>

<script>
function copyAll() {
  const content = document.getElementById('copy-content').innerText;
  navigator.clipboard.writeText(content).then(() => {
    const btn = document.getElementById('copyBtn');
    btn.textContent = '✅ Copied!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = '📋 Copy README';
      btn.classList.remove('copied');
    }, 2500);
  });
}
</script>

</body>
</html>


