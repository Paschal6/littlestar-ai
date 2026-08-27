"""
Littlestar AI - FastAPI Backend Server
With Explicit Render Setup Diagnostics
"""

import os
import re
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
from groq import Groq

from system_prompt import SYSTEM_PROMPT
from interpreter_knowledge import get_relevant_knowledge

# ─── ENVIRONMENT LOAD ───────────────────────────────
load_dotenv()

GROQ_KEY = os.getenv("GROQ_API_KEY", "").strip().strip("'").strip('"')

if not GROQ_KEY or "your_actual" in GROQ_KEY or len(GROQ_KEY) < 10:
    print("❌ ERROR: GROQ_API_KEY is missing from environment variables!")
    groq_client = None
else:
    try:
        groq_client = Groq(api_key=GROQ_KEY)
        print("⚡ Littlestar AI connected to Groq Engine!")
    except Exception as e:
        print(f"❌ Groq Init Error: {e}")
        groq_client = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(title="Littlestar AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    code_context: Optional[str] = None
    history: Optional[List[Message]] = []

class ChatResponse(BaseModel):
    reply: str
    success: bool
    model_used: str

STRICT_MODELS = [
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile",
    "llama3-8b-8192"
]

def prune_history_text(role: str, text: str) -> str:
    if not text:
        return ""
    if role in ["assistant", "model"]:
        text = re.sub(r'```[\s\S]*?```', '[code snippet]', text)
        if len(text) > 200:
            text = text[:200] + "..."
    else:
        if len(text) > 250:
            text = text[:250] + "..."
    return text

@app.get("/")
async def root():
    root_chat = os.path.join(BASE_DIR, "chat.html")
    if os.path.exists(root_chat):
        return FileResponse(root_chat)
        
    root_index = os.path.join(BASE_DIR, "index.html")
    if os.path.exists(root_index):
        return FileResponse(root_index)

    static_chat = os.path.join(BASE_DIR, "static", "chat.html")
    if os.path.exists(static_chat):
        return FileResponse(static_chat)

    return {"message": "🌟 Littlestar AI Server Online"}

@app.get("/health")
async def health():
    return {
        "status": "online",
        "groq_connected": groq_client is not None,
        "key_present": bool(GROQ_KEY and len(GROQ_KEY) > 10)
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # EXPLICIT ERROR IF KEY IS MISSING ON RENDER
    if not GROQ_KEY or "your_actual" in GROQ_KEY or len(GROQ_KEY) < 10:
        return ChatResponse(
            reply="❌ **API Key Missing on Render:** Please go to Render Dashboard ➔ Environment ➔ Add `GROQ_API_KEY` with your key from console.groq.com/keys.",
            success=False,
            model_used="none"
        )

    if not groq_client:
        return ChatResponse(
            reply="❌ **Server Error:** Invalid GROQ_API_KEY format.",
            success=False,
            model_used="none"
        )

    # 1. Load Dynamic RAG Knowledge
    dynamic_knowledge = get_relevant_knowledge(request.message, request.code_context or "")
    full_system_prompt = f"{SYSTEM_PROMPT}\n\n{dynamic_knowledge}"

    user_msg = request.message
    if request.code_context and request.code_context.strip():
        user_msg = f"User's Active Littlestar Code:\n```littlestar\n{request.code_context}\n```\n\nQuestion: {request.message}"

    messages = [{"role": "system", "content": full_system_prompt}]

    # 2. Add Pruned History
    recent_history = request.history[-4:] if request.history else []
    for h in recent_history:
        role = "assistant" if h.role in ["model", "assistant"] else "user"
        pruned_content = prune_history_text(role, h.content)
        messages.append({"role": role, "content": pruned_content})

    messages.append({"role": "user", "content": user_msg})

    last_error = ""

    # 3. Query Groq
    for model_name in STRICT_MODELS:
        try:
            print(f"🤖 Querying Groq [{model_name}]...")
            completion = groq_client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=0.6,
                max_tokens=1500,
            )
            raw_reply = completion.choices[0].message.content
            clean_reply = raw_reply.replace('\\n', '\n').replace('\\t', '  ')
            print(f"✅ Success using [{model_name}]")
            
            return ChatResponse(
                reply=clean_reply,
                success=True,
                model_used=model_name
            )

        except Exception as e:
            last_error = str(e)
            print(f"⚠️ Model [{model_name}] failed: {last_error}")
            time.sleep(0.2)
            continue

    return ChatResponse(
        reply=f"❌ **Groq Connection Failed:** {last_error}",
        success=False,
        model_used="none"
    )

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
