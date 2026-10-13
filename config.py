import os

from dotenv import load_dotenv

# Cargar .env si existe (solo en local; en Vercel las variables ya están en el entorno)
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-6-luna")

if not OPENAI_API_KEY:
    raise RuntimeError(
        "Falta la variable de entorno OPENAI_API_KEY. "
        "En local, créala en el archivo .env. "
        "En Vercel, configúrala en Settings → Environment Variables."
    )
