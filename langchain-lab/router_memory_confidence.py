# -------------------------------
# IMPORTS
# -------------------------------

import re
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------------------------------
# AI BRAIN
# -------------------------------

llm = OllamaLLM(model="llama3")
parser = StrOutputParser()

# -------------------------------
# SIMPLE MEMORY SYSTEM (VERSION-PROOF)
# -------------------------------

# Lightweight in-memory store
store = []

def get_history_text():
    return "\n".join(store)

def save_to_memory(user, ai):
    store.append(f"Human: {user}")
    store.append(f"AI: {ai}")

# -------------------------------
# UI
# -------------------------------

print("\n🧭 LangChain Router + Memory + Confidence Ready!\n")
print("Try:")
print("- Explain black holes")
print("- Now give me JSON about them")
print("- is it real?")
print("- Let’s just chat about space\n")

# -------------------------------
# ROUTER PROMPT (WITH CONFIDENCE)
# -------------------------------
router_prompt = PromptTemplate(
    input_variables=["input"],
    template="""
You are an intent classifier.

Choose ONE mode:
- explain
- structured
- chat

Also give a confidence score between 0 and 1.

Rules:
- If the user explicitly asks for JSON, format, list, table, bullet points, or structured output → structured
- If the user asks for clarification, deeper understanding, or uses phrases like:
  "why", "how", "what", "explain", "define", "elaborate", "tell me more"
  → explain
- Otherwise → chat

Return format EXACTLY:
MODE | CONFIDENCE

Example:
explain | 0.82

User input:
{input}
"""
)

# -------------------------------
# ROUTE PARSER
# -------------------------------

def parse_route(text):
    match = re.match(r"(explain|structured|chat)\s*\|\s*([0-9.]+)", text.strip(), re.I)
    if not match:
        return "explain", 0.0
    return match.group(1).lower(), float(match.group(2))

# -------------------------------
# EXPLAIN PROMPT
# -------------------------------

explain_prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are a clear teacher who remembers the conversation.

Conversation so far:
{history}

Explain this in simple, beginner-friendly language:
{input}
"""
)

# -------------------------------
# STRUCTURED PROMPT
# -------------------------------

structured_prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are a data generator who remembers the conversation.

Conversation so far:
{history}

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
# CHAT PROMPT
# -------------------------------

chat_prompt = PromptTemplate(
    input_variables=["history", "input"],
    template="""
You are a friendly conversational AI who remembers what was said before.

Conversation so far:
{history}

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
        print("\n👋 System shutting down.")
        break

    history_text = get_history_text()

    # -------------------------------
    # STEP 1 — ROUTE DECISION (WITH HISTORY)
    # -------------------------------

    route_raw = llm.invoke(
        router_prompt.format(
            input=f"Conversation:\n{history_text}\n\nNew message:\n{user_input}"
        )
    )

    route, confidence = parse_route(route_raw)

    # -------------------------------
    # FALLBACK LOGIC
    # -------------------------------

    if confidence < 0.6:
        route = "explain"

    print("\n🧭 Router Decision")
    print(f"Mode      : {route}")
    print(f"Confidence: {confidence:.2f}\n")

    # -------------------------------
    # STEP 2 — RUN SELECTED CHAIN
    # -------------------------------

    if route == "explain":
        output = llm.invoke(
            explain_prompt.format(history=history_text, input=user_input)
        )

    elif route == "structured":
        output = llm.invoke(
            structured_prompt.format(history=history_text, input=user_input)
        )

    else:
        output = llm.invoke(
            chat_prompt.format(history=history_text, input=user_input)
        )

    # -------------------------------
    # SAVE MEMORY
    # -------------------------------

    save_to_memory(user_input, output)

    # -------------------------------
    # OUTPUT
    # -------------------------------

    print("🤖 AI:\n")
    print(output)
    print("\n" + "-" * 50 + "\n")
