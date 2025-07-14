# main.py
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="DevHire JP Scraper")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "DevHire JP Scraping API is up!"}
