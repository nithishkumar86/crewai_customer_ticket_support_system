import streamlit as st
import requests

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Support Desk",
    page_icon="🎫",
    layout="centered"
)

# ─────────────────────────────────────────────
# Custom CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

* { font-family: 'DM Sans', sans-serif; }

.main { background: #0a0a0f; }

h1, h2, h3 { font-family: 'Syne', sans-serif !important; }

/* Hero Header */
.hero {
    background: linear-gradient(135deg, #0f0f1a 0%, #1a0a2e 50%, #0a1628 100%);
    border: 1px solid rgba(139, 92, 246, 0.3);
    border-radius: 24px;
    padding: 48px 40px;
    text-align: center;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 50% 50%, rgba(139,92,246,0.08) 0%, transparent 60%);
    pointer-events: none;
}
.hero-badge {
    display: inline-block;
    background: rgba(139, 92, 246, 0.15);
    border: 1px solid rgba(139, 92, 246, 0.4);
    color: #a78bfa;
    padding: 6px 16px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 16px;
}
.hero h1 {
    font-size: 42px !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #ffffff 0%, #a78bfa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 12px 0 !important;
}
.hero p {
    color: #6b7280;
    font-size: 16px;
    margin: 0;
}

/* Agent Steps */
.agent-pipeline {
    display: flex;
    justify-content: space-between;
    gap: 8px;
    margin-bottom: 32px;
}
.agent-step {
    flex: 1;
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 12px 8px;
    text-align: center;
    font-size: 11px;
    color: #6b7280;
}
.agent-step .icon { font-size: 20px; display: block; margin-bottom: 4px; }
.agent-step .label { font-weight: 600; color: #9ca3af; }

/* Solution Card */
.solution-card {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
    border: 1px solid rgba(139, 92, 246, 0.2);
    border-radius: 20px;
    padding: 32px;
    margin: 16px 0;
}
.solution-title {
    font-family: 'Syne', sans-serif;
    font-size: 22px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.solution-body {
    color: #d1d5db;
    font-size: 15px;
    line-height: 1.8;
    border-left: 3px solid #7c3aed;
    padding-left: 20px;
}

/* Metric Cards */
.metric-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 20px;
}
.metric-card {
    border-radius: 16px;
    padding: 20px 24px;
    position: relative;
    overflow: hidden;
}
.metric-card.time {
    background: linear-gradient(135deg, #064e3b, #065f46);
    border: 1px solid rgba(16, 185, 129, 0.3);
}
.metric-card.followup-yes {
    background: linear-gradient(135deg, #451a03, #78350f);
    border: 1px solid rgba(245, 158, 11, 0.3);
}
.metric-card.followup-no {
    background: linear-gradient(135deg, #064e3b, #065f46);
    border: 1px solid rgba(16, 185, 129, 0.3);
}
.metric-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.5);
    margin-bottom: 8px;
}
.metric-value {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #ffffff;
}

/* Email Banner */
.email-banner {
    background: linear-gradient(135deg, #1e3a5f, #1e1b4b);
    border: 1px solid rgba(59, 130, 246, 0.3);
    border-radius: 16px;
    padding: 20px 28px;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-top: 20px;
}
.email-icon { font-size: 32px; }
.email-text { color: #93c5fd; font-size: 15px; font-weight: 500; }
.email-sub { color: #6b7280; font-size: 13px; margin-top: 2px; }

/* Success Banner */
.success-banner {
    background: linear-gradient(135deg, #064e3b, #065f46);
    border: 1px solid rgba(16,185,129,0.4);
    border-radius: 14px;
    padding: 16px 24px;
    color: #6ee7b7;
    font-weight: 600;
    font-size: 15px;
    text-align: center;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Hero Section
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">⚡ Powered by CrewAI</div>
    <h1>AI Support Desk</h1>
    <p>4 specialized agents analyze your ticket, generate a solution & email you instantly</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Agent Pipeline Visual
# ─────────────────────────────────────────────
st.markdown("""
<div class="agent-pipeline">
    <div class="agent-step"><span class="icon">🏷️</span><span class="label">Classify</span></div>
    <div class="agent-step"><span class="icon">⚡</span><span class="label">Prioritize</span></div>
    <div class="agent-step"><span class="icon">🧠</span><span class="label">Solve</span></div>
    <div class="agent-step"><span class="icon">📧</span><span class="label">Email</span></div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Input Form
# ─────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    customer_name = st.text_input("👤 Full Name", placeholder="Rahul Kumar")
with col2:
    customer_email = st.text_input("📧 Email Address", placeholder="rahul@gmail.com")

issue = st.text_area("📝 Describe Your Issue", placeholder="Tell us what's going wrong...", height=130)

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Submit Button
# ─────────────────────────────────────────────
if st.button("🚀 Analyze My Ticket", use_container_width=True):
    if not customer_name or not customer_email or not issue:
        st.warning("⚠️ Please fill in all fields before submitting!")
    else:
        with st.spinner("🤖 AI Agents are working on your ticket..."):
            try:
                response = requests.post(
                    "http://localhost:8000/analyze-ticket",
                    json={
                        "customer_name": customer_name,
                        "customer_email": customer_email,
                        "issue": issue
                    }
                )

                if response.status_code == 200:
                    data = response.json()
                    solution = data["solution"]

                    # ── Success Banner ──
                    st.markdown("""
                    <div class="success-banner">
                        ✅ Ticket Analyzed Successfully — Solution Generated!
                    </div>
                    """, unsafe_allow_html=True)

                    # ── Solution Card ──
                    followup = solution["needs_followup"]
                    followup_class = "followup-yes" if followup else "followup-no"
                    followup_text = "⚠️ Follow-up Required" if followup else "✅ No Follow-up Needed"

                    st.markdown(f"""
                    <div class="solution-card">
                        <div class="solution-title">🧠 AI Generated Solution</div>
                        <div class="solution-body">{solution["suggested_solution"]}</div>
                        <div class="metric-row">
                            <div class="metric-card time">
                                <div class="metric-label">⏱️ Resolution Time</div>
                                <div class="metric-value">{solution["resolution_time"]}</div>
                            </div>
                            <div class="metric-card {followup_class}">
                                <div class="metric-label">🔄 Follow-up Status</div>
                                <div class="metric-value">{followup_text}</div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # ── Email Banner ──
                    st.markdown(f"""
                    <div class="email-banner">
                        <div class="email-icon">📬</div>
                        <div>
                            <div class="email-text">Professional email response sent!</div>
                            <div class="email-sub">Check your inbox at {customer_email}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                else:
                    st.error(f"❌ Error: {response.json()['detail']}")

            except Exception as e:
                st.error(f"❌ Failed to connect to backend: {str(e)}")