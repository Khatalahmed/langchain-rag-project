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

# -------------------------------
# SIMPLE MEMORY SYSTEM
# -------------------------------

# This is our own lightweight memory store
# It works exactly like LangChain memory, but without version issues
store = []

def get_history_text():
    return "\n".join(store)

def save_to_memory(user, ai):
    store.append(f"Human: {user}")
    store.append(f"AI: {ai}")

print("\n🧭 LangChain Router + Memory Ready (Version-Proof)!\n")
print("Try:")
print("- Explain black holes")
print("- Now give me JSON about them")
print("- Let’s just chat about space\n")

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
- If the user explicitly asks for JSON, format, list, data, or structure → structured
- If the user asks a question, clarification, opinion, or says things like:
  "is it", "why", "how", "what do you mean", "can you explain"
  → explain
- Otherwise → chat

Return ONLY one word:
explain OR structured OR chat

User input:
{user_input}
"""
)


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
        print("\n👋 Router + Memory shutting down.")
        break

    history_text = get_history_text()

    # Step 1 — Route decision
    route_decision = llm.invoke(
        router_prompt.format(
            user_input=f"Conversation:\n{history_text}\n\nNew message:\n{user_input}"
        )
    )

    route = parser.parse(route_decision).strip().lower()
    print(f"\n🧭 Route selected: {route}\n")

    # Step 2 — Run selected chain WITH memory
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

    # Save to memory
    save_to_memory(user_input, output)

    print("🤖 AI:\n")
    print(output)
    print("\n" + "-" * 40 + "\n")
