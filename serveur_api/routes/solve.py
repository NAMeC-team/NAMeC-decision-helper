"""
Route de résolution : à partir d'un symptôme, renvoie les causes possibles
et les actions associées.
"""

from fastapi import APIRouter, HTTPException

from utils.slugify import slugify
from serveur_api.dependencies import reasoner
from serveur_api.schemas import DiagnosticResponse, SolutionItem

router = APIRouter()


@router.get("/symptomes")
def lister_symptomes():
    """Renvoie la liste des symptômes disponibles, avec leur slug d'URL."""
    return [{"slug": s["id"], "label": s["nom"]} for s in reasoner.ontologie.lister_symptomes()]


@router.get("/solve/{symptome_id}", response_model=DiagnosticResponse)
def resoudre_symptome(symptome_id: str):
    reponse = reasoner.resoudre(symptome_id)

    if reponse is None:
        raise HTTPException(
            status_code=404,
            detail=f"Symptôme '{symptome_id}' introuvable dans l'ontologie.",
        )

    return DiagnosticResponse(
        symptome=reponse.symptome,
        composants_affectes=reponse.composants_affectes,
        solutions=[
            SolutionItem(**s)
            for s in reponse.solutions
        ],
        nb_solutions_alternatives=reponse.nb_solutions_alternatives,
    )