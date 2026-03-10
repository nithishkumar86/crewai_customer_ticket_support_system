<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CrewAI Multi-Agent Customer Support Ticket System</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap');

  :root {
    --bg: #0a0a0f;
    --surface: #111118;
    --border: rgba(139,92,246,0.15);
    --purple: #7c3aed;
    --purple-light: #a78bfa;
    --text: #e2e8f0;
    --muted: #6b7280;
    --green: #10b981;
    --code-bg: #0d1117;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    line-height: 1.7;
    padding: 40px 20px;
  }

  .container {
    max-width: 860px;
    margin: 0 auto;
  }

  /* Copy Button */
  .copy-bar {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 24px;
  }
  .copy-btn {
    background: linear-gradient(135deg, #7c3aed, #4f46e5);
    color: white;
    border: none;
    padding: 12px 28px;
    border-radius: 10px;
    font-family: 'DM Sans', sans-serif;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: all 0.2s;
  }
  .copy-btn:hover { opacity: 0.9; transform: translateY(-1px); }
  .copy-btn.copied { background: linear-gradient(135deg, #059669, #047857); }

  /* Hero */
  .hero {
    background: linear-gradient(135deg, #0f0f1a, #1a0a2e, #0a1628);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 48px 40px;
    text-align: center;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 0%, rgba(139,92,246,0.1), transparent 70%);
  }
  .badge {
    display: inline-block;
    background: rgba(139,92,246,0.15);
    border: 1px solid rgba(139,92,246,0.4);
    color: var(--purple-light);
    padding: 5px 16px;
    border-radius: 100px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 16px;
  }
  .hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: 36px;
    font-weight: 800;
    background: linear-gradient(135deg, #fff, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
  }
  .hero p { color: var(--muted); font-size: 15px; }

  /* Section */
  .section {
    background: var(--surface);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 20px;
  }
  .section h2 {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: var(--purple-light);
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  /* Flow */
  .flow {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .flow-step {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 16px;
    background: rgba(124,58,237,0.05);
    border: 1px solid rgba(124,58,237,0.1);
    border-radius: 10px;
    font-size: 14px;
    color: #d1d5db;
  }
  .flow-arrow { color: var(--muted); text-align: center; font-size: 12px; padding: 2px 0; }

  /* Table */
  table { width: 100%; border-collapse: collapse; font-size: 14px; }
  th {
    text-align: left;
    padding: 10px 14px;
    background: rgba(124,58,237,0.1);
    color: var(--purple-light);
    font-weight: 600;
    font-size: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  td { padding: 12px 14px; border-bottom: 1px solid rgba(255,255,255,0.04); color: #d1d5db; }
  tr:last-child td { border-bottom: none; }

  /* Code */
  pre {
    background: var(--code-bg);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 20px;
    overflow-x: auto;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #e2e8f0;
    line-height: 1.6;
    margin-top: 12px;
  }

  /* Key concepts */
  .concept {
    display: flex;
    gap: 12px;
    padding: 12px 16px;
    background: rgba(16,185,129,0.05);
    border: 1px solid rgba(16,185,129,0.15);
    border-radius: 10px;
    margin-bottom: 10px;
    font-size: 14px;
    color: #d1d5db;
  }
  .concept .check { color: var(--green); font-size: 16px; flex-shrink: 0; }

  /* Install steps */
  .step {
    display: flex;
    gap: 16px;
    margin-bottom: 16px;
    align-items: flex-start;
  }
  .step-num {
    background: linear-gradient(135deg, var(--purple), #4f46e5);
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: 700;
    flex-shrink: 0;
    margin-top: 2px;
  }
  .step-content { flex: 1; }
  .step-title { font-weight: 600; color: #fff; margin-bottom: 6px; font-size: 14px; }

  /* Footer */
  .footer {
    text-align: center;
    padding: 32px;
    color: var(--muted);
    font-size: 14px;
  }
  .footer a {
    color: var(--purple-light);
    text-decoration: none;
    font-weight: 600;
  }

  /* Hidden content for copy */
  #copy-content { display: none; }
</style>
</head>
<body>

<div class="container">

  <!-- Copy Button -->
  <div class="copy-bar">
    <button class="copy-btn" onclick="copyAll()" id="copyBtn">
      📋 Copy README
    </button>
  </div>

  <!-- Hero -->
  <div class="hero">
    <div class="badge">⚡ CrewAI Multi-Agent</div>
    <h1>🎫 Customer Support Ticket System</h1>
    <p>End-to-end intelligent support automation — 4 AI agents, guardrails, callbacks & email delivery</p>
  </div>

  <!-- Demo Flow -->
  <div class="section">
    <h2>🚀 Demo Flow</h2>
    <div class="flow">
      <div class="flow-step">🌐 Customer submits ticket via Streamlit UI</div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">⚡ FastAPI receives POST /analyze-ticket request</div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">🚀 CrewAI Crew kicks off — 4 agents run sequentially</div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">🏷️ Classifier Agent → identifies ticket category</div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">⚡ Priority Agent → assigns urgency level</div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">🧠 Solution Agent → generates step-by-step resolution</div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">✍️ Email Drafter → crafts professional email reply</div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">🔔 Task Callback → sends email automatically via SMTP</div>
      <div class="flow-arrow">↓</div>
      <div class="flow-step">✅ Streamlit displays solution to support team</div>
    </div>
  </div>

  <!-- Agents -->
  <div class="section">
    <h2>🤖 Agents</h2>
    <table>
      <tr><th>Agent</th><th>Role</th></tr>
      <tr><td>🏷️ Classifier Agent</td><td>Reads ticket and classifies into Billing / Technical / Shipping / Account / General</td></tr>
      <tr><td>⚡ Priority Agent</td><td>Assigns urgency — Low / Medium / High / Critical + escalation decision</td></tr>
      <tr><td>🧠 Solution Agent</td><td>Generates detailed step-by-step resolution with estimated time</td></tr>
      <tr><td>✍️ Email Drafter Agent</td><td>Drafts warm, empathetic, professional email reply to customer</td></tr>
    </table>
  </div>

  <!-- Guardrails -->
  <div class="section">
    <h2>🛡️ Guardrails</h2>
    <p style="color:#9ca3af; font-size:14px; margin-bottom:16px;">Guardrails validate every agent output <strong style="color:#fff">before</strong> passing to the next task. If validation fails — the agent <strong style="color:#fff">automatically retries</strong>.</p>
    <table>
      <tr><th>Agent</th><th>Guardrail Rule</th></tr>
      <tr><td>🏷️ Classifier</td><td>Category must be one of 5 valid types + confidence ≥ 0.5</td></tr>
      <tr><td>⚡ Priority</td><td>Billing tickets must be High or Critical — never Low or Medium</td></tr>
      <tr><td>🧠 Solution</td><td>Minimum 50 words + resolution time must be specified</td></tr>
    </table>
  </div>

  <!-- Callback -->
  <div class="section">
    <h2>🔔 Callback</h2>
    <p style="color:#9ca3af; font-size:14px; margin-bottom:12px;">Once the Email Drafter Agent completes — a Task Callback fires automatically, reads the structured Pydantic output and sends the email via Gmail SMTP.</p>
    <pre>def send_email_callback(output):
    email_draft: EmailDraft = output.pydantic  # fully available in callback!
    # sends email via SMTP automatically...</pre>
  </div>

  <!-- Pydantic Models -->
  <div class="section">
    <h2>📦 Pydantic Output Models</h2>
    <pre>class TicketClassification(BaseModel):
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
    sent_to: str</pre>
  </div>

  <!-- Tech Stack -->
  <div class="section">
    <h2>🔧 Tech Stack</h2>
    <table>
      <tr><th>Technology</th><th>Purpose</th></tr>
      <tr><td>CrewAI</td><td>Multi-agent orchestration with @CrewBase</td></tr>
      <tr><td>DeepSeek V3</td><td>LLM backbone</td></tr>
      <tr><td>Pydantic</td><td>Structured outputs for every agent</td></tr>
      <tr><td>Guardrails</td><td>Validate agent outputs — auto retry on failure</td></tr>
      <tr><td>Task Callbacks</td><td>Trigger email sending automatically</td></tr>
      <tr><td>FastAPI</td><td>Backend REST API</td></tr>
      <tr><td>Streamlit</td><td>Frontend UI</td></tr>
      <tr><td>SMTP (Gmail)</td><td>Automated email delivery</td></tr>
    </table>
  </div>

  <!-- Project Structure -->
  <div class="section">
    <h2>📁 Project Structure</h2>
    <pre>src/
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
    └── requirements.txt</pre>
  </div>

  <!-- Setup -->
  <div class="section">
    <h2>⚙️ Setup & Installation</h2>
    <div class="step">
      <div class="step-num">1</div>
      <div class="step-content">
        <div class="step-title">Clone the Repository</div>
        <pre>git clone https://github.com/yourusername/customer-ticket-support-system.git
cd customer-ticket-support-system</pre>
      </div>
    </div>
    <div class="step">
      <div class="step-num">2</div>
      <div class="step-content">
        <div class="step-title">Create Virtual Environment</div>
        <pre>python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux</pre>
      </div>
    </div>
    <div class="step">
      <div class="step-num">3</div>
      <div class="step-content">
        <div class="step-title">Install Dependencies</div>
        <pre>pip install -r requirements.txt</pre>
      </div>
    </div>
    <div class="step">
      <div class="step-num">4</div>
      <div class="step-content">
        <div class="step-title">Configure .env File</div>
        <pre>DEEPSEEK_API_KEY=your_deepseek_api_key
SENDER_EMAIL=your_gmail@gmail.com
SENDER_PASSWORD=your_gmail_app_password</pre>
      </div>
    </div>
    <div class="step">
      <div class="step-num">5</div>
      <div class="step-content">
        <div class="step-title">Run FastAPI + Streamlit</div>
        <pre># Terminal 1
uvicorn api:app --reload

# Terminal 2
streamlit run app.py</pre>
      </div>
    </div>
  </div>

  <!-- Key Concepts -->
  <div class="section">
    <h2>💡 Key Concepts Learned</h2>
    <div class="concept"><span class="check">✅</span><span>Guardrail fires BEFORE pydantic parsing → output.pydantic = None inside guardrail → must use json.loads(output.raw) to parse</span></div>
    <div class="concept"><span class="check">✅</span><span>Callback fires AFTER pydantic conversion → output.pydantic fully available in callback</span></div>
    <div class="concept"><span class="check">✅</span><span>context=[] passes previous task outputs automatically → no need for manual template variables</span></div>
    <div class="concept"><span class="check">✅</span><span>output_pydantic forces LLM to return structured JSON AND converts output for next agent</span></div>
    <div class="concept"><span class="check">✅</span><span>@CrewBase keeps agents and tasks cleanly separated in YAML config files</span></div>
  </div>

  <!-- Footer -->
  <div class="footer">
    Built to demonstrate <strong>Agentic AI Engineering</strong> using CrewAI 🚀<br><br>
    Looking for <strong>Agentic AI Internship</strong> or <strong>Junior AI Engineer</strong> opportunities!<br><br>
    <a href="https://linkedin.com/in/yourprofile">LinkedIn</a> &nbsp;•&nbsp;
    <a href="https://github.com/yourusername">GitHub</a>
  </div>

</div>

<!-- Hidden text for copy -->
<div id="copy-content">
# 🎫 CrewAI Multi-Agent Customer Support Ticket System

An end-to-end intelligent customer support automation system built using CrewAI Multi-Agent Architecture. The system automatically classifies, prioritizes, resolves, and responds to customer tickets — 24/7, instantly, and professionally.

---

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
git clone https://github.com/yourusername/customer-ticket-support-system.git
cd customer-ticket-support-system

2. Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Configure .env File
DEEPSEEK_API_KEY=your_deepseek_api_key
SENDER_EMAIL=your_gmail@gmail.com
SENDER_PASSWORD=your_gmail_app_password

5. Run the Project
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
