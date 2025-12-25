from dotenv import load_dotenv
load_dotenv()  

import json
import os
from graph import build_graph
from memory.conversation_memory import ConversationMemory
from evaluation.llm_judge import judge

# Make sure API key is set
assert os.getenv("ANTHROPIC_API_KEY"), "ANTHROPIC_API_KEY not found"

# Load mock Fitbit data
with open("data/mock_fitbit_data.json") as f:
    fitbit_data = json.load(f)

# Build assistant graph and conversation memory
graph = build_graph(fitbit_data)
memory = ConversationMemory()

print("Starting Fitbit Assistant (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit", "q"}:
        print("Goodbye 👋")
        break

    # Prepare state
    state = {
        "user_input": user_input,
        "memory": memory.get()
    }

    # Assistant generates response
    try:
        result = graph.invoke(state)
        response = result["response"]
    except Exception as e:
        print(f"Assistant error: {e}\n")
        continue

    # Print assistant response
    print(f"Assistant: {response}\n")

    # Update conversation memory
    memory.update(user_input, response)

    # Evaluate assistant response using the judge
    try:
        evaluation = judge(user_input, response, fitbit_data)
        print(f"Evaluation:\n{evaluation}\n")
    except Exception as e:
        print(f"Evaluation error: {e}\n")
