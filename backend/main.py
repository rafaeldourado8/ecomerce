from fastapi import FastAPI
from app.user import router as user_router

from app.products.router import products_router
from app.products.router import categories_router

app = FastAPI(title="EcomerceApp", version="0.0.1")

app.include_router(user_router.router)
app.include_router(products_router) 
app.include_router(categories_router) 