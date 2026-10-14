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
    noms = reasoner.ontologie.lister_symptomes()
    return [{"slug": slugify(nom), "label": nom} for nom in noms]


@router.get("/solve/{symptome_slug}", response_model=DiagnosticResponse)
def resoudre_symptome(symptome_slug: str):
    reponse = reasoner.resoudre_par_slug(symptome_slug)

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