# -------------------------------
# IMPORTS
# -------------------------------
# OllamaLLM = Connects LangChain to your local Ollama model (llama3)
# PromptTemplate = Creates reusable, structured prompts
# StrOutputParser = Converts raw LLM output into a clean string

from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# -------------------------------
# AI BRAIN NODE
# -------------------------------
# This is your "thinking engine"
# It connects LangChain to the llama3 model running in Ollama

llm = OllamaLLM(model="llama3")


# -------------------------------
# OUTPUT CLEANING NODE
# -------------------------------
# This ensures the LLM output becomes a normal Python string
# Instead of a raw AI message object

parser = StrOutputParser()


# -------------------------------
# PROMPT NODE
# -------------------------------
# This is a TEMPLATE — not a fixed prompt
# {food} is a variable slot that will be filled at runtime

template = """You are an experienced cook.
List ingredients for the following food: {food}
"""

# Convert the text template into a LangChain PromptTemplate object
# This makes it usable inside a runnable graph

prompt = PromptTemplate.from_template(template)


# -------------------------------
# RUNNABLE GRAPH (PIPELINE)
# -------------------------------
# This line creates a SYSTEM, not just a function
#
# Think of it like a factory assembly line:
#
# 1) prompt  → builds the instruction
# 2) llm     → thinks and generates ingredients
# 3) parser → cleans and finalizes the output
#
# The "|" operator means "pass output to the next node"

pipeline = prompt | llm | parser


# -------------------------------
# USER INTERFACE LOOP
# -------------------------------
# This keeps the program running until the user types "exit"

print("\n🍳 Cook Pipeline Ready!")
print("System Architecture:")
print("User → Prompt Node → LLM Node → Parser Node → Output\n")

while True:
    # Ask user for a food name
    food = input("🧑 Enter a food (or exit): ")

    # Exit condition
    if food.lower() == "exit":
        print("\n👋 Kitchen closed.")
        break

    # -------------------------------
    # PIPELINE EXECUTION
    # -------------------------------
    # This sends data into the FIRST node (prompt)
    #
    # {"food": food}
    # fills the {food} variable in the template
    #
    # Then the result flows automatically:
    # Prompt → LLM → Parser → Output

    output = pipeline.invoke({"food": food})

    # -------------------------------
    # DISPLAY RESULT
    # -------------------------------

    print("\n🤖 Ingredients:\n")
    print(output)
    print("\n" + "-" * 40 + "\n")
