from typing import Dict, Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.agents.langgraph_agent import graph

router = APIRouter()


class ChatRequest(BaseModel):
    message: str
    currentData: Dict[str, Any] = Field(default_factory=dict)


@router.post("/chat")
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "message": request.message,
            "currentData": request.currentData,
            "tool": "",
            "response": {}
        }
    )

    return result["response"]