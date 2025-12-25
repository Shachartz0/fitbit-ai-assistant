from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0
)

def judge(query, response, data):
    prompt = f"""
User query: {query}
Assistant response: {response}
Source data: {data}

Evaluate:
1. Are all claims grounded in the data?
2. Is the tone appropriate?
3. Is the advice non-medical?
"""
    messages = [
        SystemMessage(content="You are a strict evaluator."),
        HumanMessage(content=prompt)
    ]

    result = llm.invoke(messages)
    return result.content
