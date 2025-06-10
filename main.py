from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY", "sk-...")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analisa-survey")
async def analisa(request: Request):
    data = await request.json()
    surveys = data.get("surveys", [])

    prompt = "Berikut adalah daftar survey (judul, durasi dalam menit, reward RLT):\n\n"
    for s in surveys:
        prompt += f"- {s['judul']} (Durasi: {s['durasi']} menit, Reward: {s['reward']} RLT)\n"

    prompt += "\nUrutkan dari yang paling efisien (RLT per menit), dan kembalikan sebagai daftar JSON array seperti ini:\n[{'judul': ..., 'rank': 1}, ...]"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message["content"]
    return {"result": content}