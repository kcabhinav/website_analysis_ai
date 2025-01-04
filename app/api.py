from fastapi import FastAPI, HTTPException, Request, Depends
from agent import analyser
from models import WebsiteInput, WebsiteAnalyser
import os

app = FastAPI()

SECRET_KEY = os.getenv("AUTH_KEY")

def check_authorization(request: Request):
    authorization = request.headers.get("Authorization")
    if not authorization or authorization != f"Bearer {SECRET_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/scrape", response_model=WebsiteAnalyser)
async def scrape_website(website: WebsiteInput, authorization: str = Depends(check_authorization)):
    try:
        details = await analyser(website)
        return details
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

