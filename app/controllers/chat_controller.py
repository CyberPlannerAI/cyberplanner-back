from fastapi import APIRouter, HTTPException, status

from app.core.exceptions import ExternalAIServiceError
from app.models.chat_models import ChatInput, ChatOutput
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])
chat_service = ChatService()


@router.post("", response_model=ChatOutput, status_code=status.HTTP_200_OK)
async def chat_proxy(dados: ChatInput) -> ChatOutput:
    try:
        return chat_service.process_chat(dados)
    except ExternalAIServiceError as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
