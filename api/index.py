import os
import sys

# Asegura que la raíz del proyecto esté en el path de Python
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # noqa: E402, F401

# Vercel busca un objeto llamado `app`, `application` o `handler`.
# app.py ya define `app = Flask(...)`, así que lo reexportamos.
