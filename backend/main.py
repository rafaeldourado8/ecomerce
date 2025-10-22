from fastapi import FastAPI
from app.user import router as user_router

app = FastAPI(title="EcomerceApp", version="0.0.1")

app.include_router(user_router.router)