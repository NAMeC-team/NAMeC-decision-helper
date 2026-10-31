"""Route d'export du graphe de connaissances (nœuds + arêtes) pour Cytoscape.js."""

from fastapi import APIRouter

from serveur_api.dependencies import reasoner

router = APIRouter()

EXCLUS = ("descripteur",)
REPLIES = ("roue_omnidirectionnelle","carte_moteur",)

@router.get("/graph")
def obtenir_graphe():
    return reasoner.ontologie.exporter_graphe(exclure=EXCLUS, replier=REPLIES)