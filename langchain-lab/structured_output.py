# -------------------------------
# IMPORTS
# -------------------------------

from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

import json
import os
from datetime import datetime


# -------------------------------
# SETTINGS
# -------------------------------

OUTPUT_DIR = "outputs"
LOG_FILE = "system.log"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------
# AI BRAIN
# -------------------------------

llm = OllamaLLM(model="llama3")

# -------------------------------
# OUTPUT PARSER (SCHEMA)
# -------------------------------

parser = JsonOutputParser()

# -------------------------------
# PROMPT
# -------------------------------

prompt = PromptTemplate(
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
    template="""
You are a data generator.

Create structured learning data about this topic:
{topic}

{format_instructions}

Rules:
- Return exactly 3 learning points
- Each must contain:
  - title
  - explanation
  - real_world_example
- Output must be valid JSON
"""
)

# -------------------------------
# LOGGING FUNCTION
# -------------------------------

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


# -------------------------------
# FILE SAVE FUNCTION
# -------------------------------

def save_output(topic, data):
    safe_name = topic.replace(" ", "_").lower()
    filename = f"{safe_name}_{datetime.now().strftime('%H%M%S')}.json"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return path


# -------------------------------
# SELF-REPAIR FUNCTION
# -------------------------------

def repair_output(raw_text):
    repair_prompt = f"""
The following output is supposed to be valid JSON but is broken.

Fix it and return ONLY valid JSON.

Broken output:
{raw_text}
"""
    return llm.invoke(repair_prompt)


# -------------------------------
# MAIN LOOP
# -------------------------------

print("\n🏭 Production AI System Ready!")
print("Outputs will be saved in /outputs and logged in system.log")
print("Type 'exit' to quit.\n")

while True:
    topic = input("📘 Enter a topic: ")

    if topic.lower() == "exit":
        print("\n👋 System shutting down.")
        log_event("System stopped by user")
        break

    log_event(f"Topic received: {topic}")

    # Generate output
    raw_output = llm.invoke(prompt.format(topic=topic))

    print("\n🧠 Raw Output:\n")
    print(raw_output)

    # Try parsing
    try:
        structured_data = parser.parse(raw_output)
        log_event("Output parsed successfully")

    except Exception:
        log_event("Parsing failed — attempting self-repair")
        print("\n⚠️ Parsing failed. Attempting self-repair...\n")

        repaired = repair_output(raw_output)

        try:
            structured_data = parser.parse(repaired)
            log_event("Self-repair successful")
        except Exception:
            log_event("Self-repair failed — output discarded")
            print("❌ Could not repair output. Try again.")
            continue

    # Save result
    file_path = save_output(topic, structured_data)
    log_event(f"Output saved to {file_path}")

    print("\n✅ Final Structured Data:\n")
    print(structured_data)
    print(f"\n💾 Saved to: {file_path}")
    print("\n" + "-" * 50 + "\n")
