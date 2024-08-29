from fastapi import FastAPI
from .routes import api_router, html_router

app = FastAPI()


app.include_router(api_router, prefix="/api")
app.include_router(html_router)
