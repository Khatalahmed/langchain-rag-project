# -------------------------------
# IMPORTS
# -------------------------------

from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------------------------------
# AI BRAIN
# -------------------------------

llm = OllamaLLM(model="llama3")
parser = StrOutputParser()

print("\n🧭 LangChain Prompt Router Ready!\n")
print("Try:")
print("- 'Explain photosynthesis'")
print("- 'Give me JSON about economics'")
print("- 'Chat with me about space'\n")

# -------------------------------
# ROUTER PROMPT
# -------------------------------

router_prompt = PromptTemplate(
    input_variables=["user_input"],
    template="""
You are a routing system.

Classify the user's intent into ONE of these categories:
- explain
- structured
- chat

Rules:
- If the user wants data, format, JSON, or structured output → structured
- If the user wants learning or explanation → explain
- Otherwise → chat

Return ONLY one word:
explain OR structured OR chat

User input:
{user_input}
"""
)

# -------------------------------
# EXPLAIN CHAIN
# -------------------------------

explain_prompt = PromptTemplate(
    input_variables=["input"],
    template="""
You are a clear teacher.

Explain this topic in simple, beginner-friendly language:
{input}
"""
)

# -------------------------------
# STRUCTURED CHAIN
# -------------------------------

structured_prompt = PromptTemplate(
    input_variables=["input"],
    template="""
Return exactly 3 learning points in JSON format.

Each must include:
- title
- explanation
- example

Topic:
{input}

Return ONLY valid JSON.
"""
)

# -------------------------------
# CHAT CHAIN
# -------------------------------

chat_prompt = PromptTemplate(
    input_variables=["input"],
    template="""
You are a friendly conversational AI.

Respond naturally to:
{input}
"""
)

# -------------------------------
# MAIN LOOP
# -------------------------------

while True:
    user_input = input("🧑 You: ")

    if user_input.lower() == "exit":
        print("\n👋 Router shutting down.")
        break

    # Step 1 — Route decision
    route_decision = llm.invoke(
        router_prompt.format(user_input=user_input)
    )

    route = parser.parse(route_decision).strip().lower()

    print(f"\n🧭 Route selected: {route}\n")

    # Step 2 — Run selected chain
    if route == "explain":
        output = llm.invoke(
            explain_prompt.format(input=user_input)
        )

    elif route == "structured":
        output = llm.invoke(
            structured_prompt.format(input=user_input)
        )

    else:
        output = llm.invoke(
            chat_prompt.format(input=user_input)
        )

    print("🤖 AI:\n")
    print(output)
    print("\n" + "-" * 40 + "\n")
