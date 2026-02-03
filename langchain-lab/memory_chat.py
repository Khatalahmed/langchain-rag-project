# -------------------------------
# IMPORTS
# -------------------------------

from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate


# -------------------------------
# AI BRAIN
# -------------------------------

llm = OllamaLLM(model="llama3")

print("\n🧠 Memory Chatbot Ready!\n")
print("Type 'exit' to stop the conversation.\n")


# -------------------------------
# MEMORY SYSTEM (Simple Python List)
# -------------------------------

conversation_history = []


def format_history():
    """Convert conversation history into readable text"""
    if not conversation_history:
        return "No previous conversation."
    
    formatted = []
    for message in conversation_history:
        if message['role'] == 'user':
            formatted.append(f"Human: {message['content']}")
        else:
            formatted.append(f"AI: {message['content']}")
    
    return "\n".join(formatted)


# -------------------------------
# CHAT PROMPT
# -------------------------------

chat_prompt = PromptTemplate(
    input_variables=["history", "user_input"],
    template="""
You are a friendly AI assistant that remembers past conversations.

Conversation so far:
{history}

User just said:
{user_input}

Respond naturally and helpfully. If the user refers to something from earlier, use the memory.
"""
)


# -------------------------------
# CHAT LOOP
# -------------------------------

while True:
    user_input = input("🧑 You: ")

    if user_input.lower() == "exit":
        print("\n👋 Goodbye! Your chatbot remembers this conversation.")
        break

    # Format conversation history
    history = format_history()

    # Build full AI prompt with memory + new input
    full_prompt = chat_prompt.format(
        history=history,
        user_input=user_input
    )

    # Get AI response
    ai_response = llm.invoke(full_prompt)

    # Save to memory
    conversation_history.append({"role": "user", "content": user_input})
    conversation_history.append({"role": "assistant", "content": ai_response})

    # Print AI reply
    print("\n🤖 AI:", ai_response, "\n")