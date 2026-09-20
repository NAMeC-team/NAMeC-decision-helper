"""
Schémas Pydantic : définissent la forme attendue des données échangées
avec l'API. FastAPI s'en sert pour valider automatiquement les requêtes
et générer la documentation Swagger.
"""

from pydantic import BaseModel


class SolutionItem(BaseModel):
    cause: str
    action: str


class DiagnosticResponse(BaseModel):
    symptome: str
    composants_affectes: list[str]
    solutions: list[SolutionItem]
    nb_solutions_alternatives: int