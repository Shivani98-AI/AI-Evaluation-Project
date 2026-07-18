from dotenv import load_dotenv
import os
import streamlit as st
from openai import OpenAI

from evaluation.evaluation import evaluate_response

# -------------------------------------------------------
# Load Environment Variables
# -------------------------------------------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# -------------------------------------------------------
# Load Prompt Files
# -------------------------------------------------------

with open("prompts/system_prompt.txt") as f:
    system_prompt = f.read()

with open("prompts/question_template.txt") as f:
    question_template = f.read()

with open("evaluation/evaluation_prompt.txt") as f:
    evaluation_prompt = f.read()

# -------------------------------------------------------
# Streamlit Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Evaluation Framework",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

with st.sidebar:

    st.title("🤖 AI Evaluation")

    st.success("🟢 System Online")

    st.markdown("---")

    st.subheader("LLM")

    st.info("Groq • Llama 3.3 70B")

    st.subheader("Pipeline")

    st.write("✅ Prompt Engineering")
    st.write("✅ Rule-Based Evaluation")
    st.write("✅ LLM-as-a-Judge")

    st.markdown("---")

    st.subheader("Author")

    st.write("👩 Shivani Shete")

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.title("🤖 AI Evaluation Framework")

st.caption(
    "Prompt Engineering • Groq Llama 3.3 • Rule Evaluation • LLM-as-a-Judge"
)

st.divider()

# -------------------------------------------------------
# Question
# -------------------------------------------------------

question = st.text_area(
    "💬 Ask your Question",
    placeholder="Example: Explain API Testing with an example",
    height=180
)

# -------------------------------------------------------
# Button
# -------------------------------------------------------

if st.button("🚀 Generate AI Answer"):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Generating Answer..."):

        formatted_question = question_template.replace(
            "{question}",
            question
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": formatted_question
                }
            ]
        )

        ai_answer = response.choices[0].message.content

        # Rule Evaluation

        score, feedback = evaluate_response(ai_answer)

        # LLM Evaluation

        llm_prompt = evaluation_prompt.replace(
            "{question}",
            question
        )

        llm_prompt = llm_prompt.replace(
            "{answer}",
            ai_answer
        )

        evaluation = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": llm_prompt
                }
            ]
        )

        llm_feedback = evaluation.choices[0].message.content

    # ===================================================
    # Question
    # ===================================================

    st.divider()

    st.subheader("📌 Question")

    st.info(question)

    # ===================================================
    # Dashboard
    # ===================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rule Score", f"{score}/10")

    with col2:
        st.metric("Model", "Llama 3.3")

    with col3:
        st.metric("Status", "Completed")

    with col4:

        if score >= 9:
            grade = "Excellent"
        elif score >= 7:
            grade = "Good"
        else:
            grade = "Needs Work"

        st.metric("Overall", grade)

    st.divider()

    # ===================================================
    # Tabs
    # ===================================================

    tab1, tab2, tab3 = st.tabs(
        [
            "🤖 AI Answer",
            "✅ Rule Evaluation",
            "🧠 LLM Judge"
        ]
    )

    # ---------------------------------------------------

    with tab1:

        st.subheader("AI Answer")

        st.write(ai_answer)

    # ---------------------------------------------------

    with tab2:

        st.subheader("Rule-Based Evaluation")

        if len(feedback) == 0:

            st.success("No issues found ✅")

        else:

            for item in feedback:
                st.write("✔", item)

    # ---------------------------------------------------

    with tab3:

        st.subheader("LLM-as-a-Judge")

        st.markdown(llm_feedback)

    # ===================================================
    # Prompt Viewer
    # ===================================================

    st.divider()

    with st.expander("📄 Prompt Sent to LLM"):

        st.code(formatted_question)

    # ===================================================
    # Download Report
    # ===================================================

    report = f"""
Question
--------
{question}

AI Answer
---------
{ai_answer}

Rule Score
----------
{score}/10

LLM Evaluation
--------------
{llm_feedback}
"""

    st.download_button(
        "⬇ Download Evaluation Report",
        report,
        file_name="evaluation_report.txt"
    )

    st.divider()

    st.success("🎉 Evaluation Completed Successfully!")