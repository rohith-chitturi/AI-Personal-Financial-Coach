from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.coordinator import coordinator_agent

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: str

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        # Run the LangGraph agent
        result = coordinator_agent.invoke({"input_text": request.message, "intent": "", "response": ""})
        return ChatResponse(response=result["response"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
