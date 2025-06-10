# RollerBot Backend (FastAPI + OpenAI)

## 🚀 Cara Jalankan Lokal

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 🌐 Deploy ke Railway / Render

1. Push repo ke GitHub
2. Deploy dari GitHub di Railway
3. Tambahkan `OPENAI_API_KEY` ke Environment Variables

## 🔐 Env

Buat file `.env` berisi:

```
OPENAI_API_KEY=sk-isi-api-kamu-di-sini
```