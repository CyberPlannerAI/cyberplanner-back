from fastapi import APIRouter

from app.controllers.chat_controller import router as chat_router

api_router = APIRouter()
api_router.include_router(chat_router)
