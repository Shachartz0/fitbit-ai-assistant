from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage
import json

llm = ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0
)


SYSTEM_PROMPT = """
You are a health insight generator.

Rules:
- Use ONLY the provided data
- No medical diagnosis
- Be factual and numeric

Return JSON:
{
  "observation": "...",
  "evidence": "...",
  "suggestion": "..."
}
"""

def generate_insight(data, goals):
    if data is None:
        return {"observation": "missing_data"}

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=f"Data: {data}\nGoals: {goals}")
    ]
    response = llm.invoke(messages)
    return json.loads(response.content)
