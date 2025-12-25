from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage
import json

llm = ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0
)

SYSTEM_PROMPT = """
Classify the user's intent.
Possible intents:
- sleep
- activity
- heart
- comparison
- advice

Return JSON only, format:
{
  "intent": "...",
  "time_reference": "optional"
}
"""

def detect_intent(user_input: str):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(messages)
    return json.loads(response.content)
