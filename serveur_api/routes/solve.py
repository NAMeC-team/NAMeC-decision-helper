"""
Route de résolution : à partir d'un symptôme, renvoie les causes possibles
et les actions associées.
"""

from pathlib import Path

from fastapi import APIRouter, HTTPException

from systeme_decisionnel.reasoner import Reasoner
from serveur_api.schemas import DiagnosticResponse, SolutionItem

router = APIRouter()

# Chemin absolu, indépendant du dossier depuis lequel uvicorn est lancé.
ONTOLOGIE_PATH = Path(__file__).parent.parent.parent / "ontologie" / "namec.ttl"

# Le Reasoner est chargé une seule fois au démarrage du serveur,
# pas à chaque requête (l'ontologie ne change pas entre deux appels).
_reasoner = Reasoner(str(ONTOLOGIE_PATH))


@router.get("/solve/{symptome_slug}", response_model=DiagnosticResponse)
def resoudre_symptome(symptome_slug: str):
    reponse = _reasoner.resoudre_par_slug(symptome_slug)

    if reponse is None:
        raise HTTPException(
            status_code=404,
            detail=f"Symptôme '{symptome_slug}' introuvable dans l'ontologie.",
        )

    return DiagnosticResponse(
        symptome=reponse.symptome,
        composants_affectes=reponse.composants_affectes,
        solutions=[
            SolutionItem(cause=s["cause"], action=s["action"])
            for s in reponse.solutions
        ],
        nb_solutions_alternatives=reponse.nb_solutions_alternatives,
    )