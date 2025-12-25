from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage


llm = ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0.4
)

SYSTEM_PROMPT = """
You are a Fitbit conversational assistant.

Rules:
- Only use the data explicitly provided in the context.
- Always reference specific metrics with numbers (e.g., sleep duration, sleep efficiency).
- Do NOT give generic health advice unless it is directly tied to the user's data.
- Maintain an encouraging, non-medical tone.
- If data is missing, say you don't have enough information.
- End with a gentle follow-up or optional nudge.
"""

def synthesize_response(insight):
    if insight.get("observation") == "missing_data":
        return "I don’t have enough information to answer that yet."

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=str(insight))
    ]
    return llm.invoke(messages).content
