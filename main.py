from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from groq_service import ask_groq

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-quiz-generator-1fi9.onrender.com",
        "https://ai-code-explainer-6y77.onrender.com",
        "https://ai-notes-summarizer-gwej.onrender.com",
        "https://ai-content-writer-1.onrender.com",
        "https://ai-travel-planner-b67c.onrender.com",
        "https://ai-study-notes-generator-b2rh.onrender.com",
        "https://ai-assigment-helper.onrender.com",
        "https://ai-doubt-solver-9pvd.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/")
def chat(request: PromptRequest):
    answer = ask_groq(request.prompt)
    return {"response": answer}