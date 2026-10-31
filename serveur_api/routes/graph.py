"""Route d'export du graphe de connaissances (nœuds + arêtes) pour Cytoscape.js."""

from fastapi import APIRouter

from serveur_api.dependencies import reasoner

router = APIRouter()


@router.get("/graph")
def obtenir_graphe():
    return reasoner.ontologie.exporter_graphe()