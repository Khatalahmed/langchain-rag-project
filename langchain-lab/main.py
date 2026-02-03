from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

print("\n🤖 LangChain AI Connected (Modern API)!\n")
response = llm.invoke("Explain in simple words what LangChain is doing right now")
print(response)
