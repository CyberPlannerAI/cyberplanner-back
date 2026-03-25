from pydantic import BaseModel, Field


class ChatInput(BaseModel):
    pergunta: str = Field(..., min_length=1, description="Pergunta do usuario")
    modo: str = Field(default="gestor", description="Modo/persona para resposta")


class ChatOutput(BaseModel):
    resposta: str
    modo_usado: str
