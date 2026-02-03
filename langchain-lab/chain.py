from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Connect to your local AI model
llm = OllamaLLM(model="llama3")

print("\n🧠 Smart Chain System Ready!\n")

# -------------------------------
# STEP 1 — THINKING PROMPT
# -------------------------------
think_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
You are an expert thinker.

Your job is to analyze the topic deeply and extract exactly 3 important learning points.
Keep the points short and clear.

Topic:
{topic}

Return only the 3 points as a numbered list.
"""
)

# -------------------------------
# STEP 2 — TEACHING PROMPT
# -------------------------------
teach_prompt = PromptTemplate(
    input_variables=["points"],
    template="""
You are a beginner-friendly teacher.

Explain each of these points in very simple and clear language.
Use short sentences.
Make it feel friendly and easy to understand.

Points:
{points}
"""
)

# -------------------------------
# RUN THE CHAIN
# -------------------------------
topic = input("📘 Enter a topic you want to learn: ")

print("\n🧠 Thinking...\n")
points = llm.invoke(think_prompt.format(topic=topic))

print("📝 Key Points Found:\n")
print(points)

print("\n📚 Teaching...\n")
final_answer = llm.invoke(teach_prompt.format(points=points))

print("🎯 Final Explanation:\n")
print(final_answer)
