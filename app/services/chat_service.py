from google import genai
from google.genai import types

from app.core.config import settings
from app.core.exceptions import ExternalAIServiceError
from app.models.chat_models import ChatInput, ChatOutput


PERSONALIDADES = {
    "gestor": (
        "Voce e um gestor e organizador de horarios. "
        "Nao permita conflitos de agenda e otimize a rotina do usuario. "
        "Ao final, gere uma tabela clara com os horarios."
    )
}


class ChatService:
    def __init__(self) -> None:
        if not settings.GEMINI_API_KEY:
            raise ExternalAIServiceError(
                "GEMINI_API_KEY/GOOGLE_API_KEY nao configurada no ambiente"
            )

        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.default_model = settings.GEMINI_MODEL

    def process_chat(self, dados: ChatInput) -> ChatOutput:
        instrucao = PERSONALIDADES.get(dados.modo, PERSONALIDADES["gestor"])

        try:
            response = self.client.models.generate_content(
                model=self.default_model,
                contents=dados.pergunta,
                config=types.GenerateContentConfig(
                    system_instruction=instrucao,
                ),
            )

            texto = response.text or "Nao foi possivel gerar resposta no momento."
            return ChatOutput(resposta=texto, modo_usado=dados.modo)

        except Exception as exc:
            raise ExternalAIServiceError(f"Falha ao gerar conteudo no Gemini: {exc}") from exc
