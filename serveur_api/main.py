"""
Point d'entrée du serveur API. Lance avec :
    uvicorn serveur_api.main:app --reload

À exécuter depuis la racine du projet (namec-decision-helper/).
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from serveur_api.routes import solve

app = FastAPI(
    title="NAMeC Decision Helper API",
    description="API de diagnostic robotique basée sur une ontologie OWL.",
    version="0.1.0",
)

# Autorise l'interface web (Vite, servie sur un autre port) à appeler l'API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(solve.router)


@app.get("/")
def racine():
    return {"message": "NAMeC Decision Helper API — voir /docs pour la documentation"}