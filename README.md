# 🤖 AI Evaluation Framework

An end-to-end AI Evaluation Framework built using **Python**, **Groq LLM (Llama 3.3 70B)**, **Prompt Engineering**, **Rule-Based Evaluation**, and **LLM-as-a-Judge Evaluation**.

This project demonstrates how modern AI applications generate responses, evaluate them using predefined metrics, and improve response quality through structured prompt engineering.

---

# 🚀 Project Overview

This project allows users to ask any AI-related or software testing question through the terminal.

The application:

- Accepts a user's question
- Builds a prompt using external prompt templates
- Sends the prompt to a Large Language Model (Groq Llama 3.3)
- Generates an AI response
- Evaluates the response using Rule-Based Evaluation
- Evaluates the response again using an LLM-as-a-Judge
- Displays detailed evaluation metrics and improvement suggestions

---

# ✨ Features

- 🤖 Groq LLM Integration
- 📝 Prompt Engineering
- 📄 External Prompt Templates
- 🎯 System Prompt
- 📊 Rule-Based AI Evaluation
- 🧠 LLM-as-a-Judge Evaluation
- 🔐 Secure API Key Management (.env)
- 📁 Modular Project Structure
- ⚡ Fast AI Responses using Groq

---

# 🛠 Tech Stack

- Python 3
- Groq API
- Llama 3.3 70B Versatile
- OpenAI Python SDK (Groq Compatible)
- python-dotenv
- Git
- GitHub
- VS Code

---

# 📂 Project Structure

```text
AI-Evaluation-Project
│
├── data
│   └── sample.txt
│
├── evaluation
│   ├── evaluation.py
│   └── evaluation_prompt.txt
│
├── notebooks
│   └── testing.ipynb
│
├── prompts
│   ├── system_prompt.txt
│   ├── question_template.txt
│   └── prompt.py
│
├── llm_test.py
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> Note: `.env` is ignored by Git and is not uploaded to GitHub.

---

# ⚙️ How It Works

```
User Question
      │
      ▼
Question Template
      │
      ▼
System Prompt
      │
      ▼
Groq Llama 3.3
      │
      ▼
AI Response
      │
      ├──────────────► Rule-Based Evaluation
      │
      ▼
Evaluation Prompt
      │
      ▼
LLM-as-a-Judge
      │
      ▼
Final Evaluation Report
```

---

# 📊 Evaluation Metrics

The AI response is evaluated on:

- Accuracy
- Completeness
- Clarity
- Real-world Example
- Interview Readiness

The evaluation also provides:

- Overall Score
- Strengths
- Weaknesses
- Improvement Suggestions

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Shivani98-AI/AI-Evaluation-Project.git
```

Move into the project

```bash
cd AI-Evaluation-Project
```

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate Virtual Environment

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application

```bash
python3 llm_test.py
```

---

# 💻 Sample Output

```
Ask me anything:
What is API Testing?

AI Answer:
...

Rule-Based Evaluation:
Score: 10/10

LLM Evaluation:
Accuracy: 9/10
Completeness: 8/10
Clarity: 9/10
Overall Score: 8.2/10
```

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Prompt Engineering
- Large Language Models (LLMs)
- API Integration
- AI Evaluation
- Rule-Based Scoring
- LLM-as-a-Judge
- Python Project Structure
- Environment Variables
- Git & GitHub Workflow

---

# 🚀 Future Enhancements

- Streamlit Web Interface
- Multiple LLM Comparison
- AI Response History
- CSV Export
- RAG Integration
- DeepEval Metrics
- Dashboard Analytics
- Cloud Deployment

---

# 👩‍💻 Author

**Shivani Shete**

Software Testing | AI | Machine Learning | Generative AI

GitHub:
https://github.com/Shivani98-AI

LinkedIn:
https://www.linkedin.com/in/shivanishete23

---