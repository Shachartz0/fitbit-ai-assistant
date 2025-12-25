from langgraph.graph import StateGraph
from agents.intent_agent import detect_intent
from agents.data_selector import select_data
from agents.insight_agent import generate_insight
from agents.response_agent import synthesize_response

def build_graph(fitbit_data):
    graph = StateGraph(dict)

    def intent_node(state):
        state["intent"] = detect_intent(state["user_input"])
        return state

    def data_node(state):
        state["selected_data"] = select_data(state["intent"], fitbit_data)
        return state

    def insight_node(state):
        state["insight"] = generate_insight(
            state["selected_data"],
            fitbit_data["user_profile"]["goals"]
        )
        return state

    def response_node(state):
        state["response"] = synthesize_response(state["insight"])
        return state

    graph.add_node("intent", intent_node)
    graph.add_node("data", data_node)
    graph.add_node("insight", insight_node)
    graph.add_node("response", response_node)

    graph.set_entry_point("intent")
    graph.add_edge("intent", "data")
    graph.add_edge("data", "insight")
    graph.add_edge("insight", "response")

    return graph.compile()
