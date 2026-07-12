from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.tools.log_tool import log_interaction
from app.tools.edit_tool import edit_interaction
from app.tools.summary_tool import summarize_interaction
from app.tools.followup_tool import suggest_followup
from app.tools.history_tool import get_history
from app.tools.hcp_insight_tool import generate_hcp_insight


class AgentState(TypedDict):
    message: str
    currentData: dict
    tool: str
    response: dict



# ---------------- ROUTER ----------------

def router(state: AgentState):

    message = state["message"].lower().strip()

    print("USER MESSAGE:", message)


    # Edit Tool
    if any(word in message for word in [
        "edit",
        "change",
        "update",
        "modify",
        "correct"
    ]):
        state["tool"] = "edit"



    # Summary Tool
    elif any(word in message for word in [
        "summary",
        "summarize",
        "summarise"
    ]):
        state["tool"] = "summary"



    # Follow-up Tool
    elif any(word in message for word in [
        "suggest follow up",
        "suggest follow-up",
        "generate follow up",
        "generate follow-up",
        "follow up suggestions",
        "follow-up suggestions",
        "next steps",
        "follow up plan"
    ]):
        state["tool"] = "followup"



    # HCP Insight Tool
    elif any(word in message for word in [
        "insight",
        "analysis",
        "analyze",
        "analyse",
        "engagement",
        "recommendation",
        "recommend",
        "sales insight",
        "doctor insight",
        "hcp insight"
    ]):
        state["tool"] = "insight"



    # History Tool
    elif any(word in message for word in [
        "history",
        "previous interaction",
        "past interaction",
        "interaction history",
        "previous visits"
    ]):
        state["tool"] = "history"



    # Default → Log Interaction
    else:
        state["tool"] = "log"



    print("SELECTED TOOL:", state["tool"])

    return state





# ---------------- LOG TOOL ----------------

def log_node(state: AgentState):

    state["response"] = log_interaction(
        state["message"]
    )

    return state





# ---------------- EDIT TOOL ----------------

def edit_node(state: AgentState):

    state["response"] = edit_interaction(
        state["currentData"],
        state["message"]
    )

    return state





# ---------------- SUMMARY TOOL ----------------

def summary_node(state: AgentState):

    summary = summarize_interaction(
        state["currentData"]
    )

    state["response"] = {
        "summary": summary
    }

    return state





# ---------------- FOLLOW-UP TOOL ----------------

def followup_node(state: AgentState):

    followup = suggest_followup(
        state["currentData"]
    )

    state["response"] = {
        "followup": followup
    }

    return state





# ---------------- HISTORY TOOL ----------------

def history_node(state: AgentState):

    state["response"] = get_history(
        state["currentData"]
    )

    return state





# ---------------- HCP INSIGHT TOOL ----------------

def insight_node(state: AgentState):

    insight = generate_hcp_insight(
        state["currentData"]
    )

    state["response"] = {
        "insight": insight
    }

    return state





# ---------------- ROUTER DECISION ----------------

def decide_tool(state: AgentState):

    return state["tool"]





# ---------------- LANGGRAPH ----------------

builder = StateGraph(AgentState)


builder.add_node(
    "router",
    router
)


builder.add_node(
    "log",
    log_node
)


builder.add_node(
    "edit",
    edit_node
)


builder.add_node(
    "summary",
    summary_node
)


builder.add_node(
    "followup",
    followup_node
)


builder.add_node(
    "history",
    history_node
)


builder.add_node(
    "insight",
    insight_node
)



builder.set_entry_point(
    "router"
)



builder.add_conditional_edges(
    "router",
    decide_tool,
    {
        "log": "log",
        "edit": "edit",
        "summary": "summary",
        "followup": "followup",
        "history": "history",
        "insight": "insight",
    },
)



builder.add_edge("log", END)
builder.add_edge("edit", END)
builder.add_edge("summary", END)
builder.add_edge("followup", END)
builder.add_edge("history", END)
builder.add_edge("insight", END)



graph = builder.compile()