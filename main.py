from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from groq_service import ask_groq

app = FastAPI()

# CORS must be added immediately after creating the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],   # or ["*"] while developing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/chat")
def chat(request: PromptRequest):
    answer = ask_groq(request.prompt)
    return {"response": answer}