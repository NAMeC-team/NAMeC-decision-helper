"""
Point d'entrée du serveur API. Lance avec :
    uvicorn serveur_api.main:app --reload

À exécuter depuis la racine du projet (namec-decision-helper/).
"""

from fastapi import FastAPI

from serveur_api.routes import solve

app = FastAPI(
    title="NAMeC Decision Helper API",
    description="API de diagnostic robotique basée sur une ontologie OWL.",
    version="0.1.0",
)

app.include_router(solve.router)


@app.get("/")
def racine():
    return {"message": "NAMeC Decision Helper API — voir /docs pour la documentation"}