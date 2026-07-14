from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from groq_service import ask_groq

app = FastAPI()

# CORS must be added immediately after creating the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ai-quiz-generator-1fi9.onrender.com"],   # or ["*"] while developing
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
