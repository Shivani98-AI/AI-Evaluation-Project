from dotenv import load_dotenv
import os
from openai import OpenAI
from evaluation.evaluation import evaluate_response

# ----------------------------------------
# Load Environment Variables
# ----------------------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# ----------------------------------------
# Create Groq Client
# ----------------------------------------

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# ----------------------------------------
# Read Prompt Files
# ----------------------------------------

with open("prompts/system_prompt.txt", "r") as file:
    system_prompt = file.read()

with open("prompts/question_template.txt", "r") as file:
    question_template = file.read()

# ----------------------------------------
# User Question
# ----------------------------------------

question = input("Ask me anything: ")

formatted_question = question_template.replace("{question}", question)

# ----------------------------------------
# Show Prompt
# ----------------------------------------

print("=" * 50)
print("🤖 AI Evaluation Project (Groq)")
print("=" * 50)

print("\n==============================")
print("Prompt Sent to AI")
print("==============================")
print(formatted_question)
print("==============================")

# ----------------------------------------
# Generate AI Answer
# ----------------------------------------

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

# ----------------------------------------
# Print AI Answer
# ----------------------------------------

print("\n🤖 AI Answer:\n")

ai_answer = response.choices[0].message.content

print(ai_answer)

# ====================================================
# Rule-Based Evaluation (Python)
# ====================================================

score, feedback = evaluate_response(ai_answer)

print("\n======================")
print("Rule-Based Evaluation")
print("======================")

print("Score:", score, "/10")

print("\nFeedback:")

if len(feedback) == 0:
    print("No issues found ✅")
else:
    for item in feedback:
        print("-", item)

# ====================================================
# LLM-as-a-Judge Evaluation
# ====================================================

# Read Evaluation Prompt

with open("evaluation/evaluation_prompt.txt", "r") as file:
    evaluation_prompt = file.read()

# Replace Placeholders

evaluation_prompt = evaluation_prompt.replace("{question}", question)
evaluation_prompt = evaluation_prompt.replace("{answer}", ai_answer)

# Show Evaluation Prompt

print("\n========================")
print("Evaluation Prompt")
print("========================")
print(evaluation_prompt)

# Send to Groq Again

evaluation_response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": evaluation_prompt
        }
    ]
)

# Print LLM Evaluation

print("\n========================")
print("LLM Evaluation")
print("========================")

print(evaluation_response.choices[0].message.content)