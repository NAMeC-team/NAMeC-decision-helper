"""
Système décisionnel : à partir d'un symptôme, renvoie les causes possibles
et les actions pour les traiter.
"""

from .ontology_access import OntologyAccess


class ReponseDiagnostic:
    def __init__(self, symptome, composants_affectes, solutions):
        self.symptome = symptome
        self.composants_affectes = composants_affectes
        self.solutions = solutions  # liste de {"cause", "action", "description"}

    @property
    def nb_solutions_alternatives(self):
        return len(self.solutions)


class Reasoner:
    def __init__(self, dossier_ontologie: str):
        self.ontologie = OntologyAccess(dossier_ontologie)

    def resoudre(self, symptome_id: str) -> ReponseDiagnostic | None:
        """Renvoie le diagnostic, ou None si ce symptôme n'existe pas."""
        if not self.ontologie.est_un_symptome(symptome_id):
            return None
        return ReponseDiagnostic(
            symptome=self.ontologie.nom(symptome_id),
            composants_affectes=self.ontologie.composants_affectes(symptome_id),
            solutions=self.ontologie.trouver_causes_et_actions(symptome_id),
        )