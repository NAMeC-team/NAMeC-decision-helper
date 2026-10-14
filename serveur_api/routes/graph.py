"""
Route d'export du graphe de connaissances, au format nœuds/arêtes
consommable directement par Cytoscape.js.
"""

from fastapi import APIRouter

from serveur_api.dependencies import reasoner

router = APIRouter()


@router.get("/graph")
def obtenir_graphe():
    return reasoner.ontologie.exporter_graphe()