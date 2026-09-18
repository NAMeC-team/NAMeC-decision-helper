"""
Système décisionnel : à partir d'un symptôme, détermine les causes possibles
et les actions associées.

Ce module ne connaît pas rdflib/owlrl. Il passe
par OntologyAccess.
"""

from .ontology_access import OntologyAccess


class ReponseDiagnostic:
    def __init__(self, symptome, composants_affectes, solutions):
        self.symptome = symptome
        self.composants_affectes = composants_affectes
        self.solutions = solutions  # liste de {"cause": ..., "action": ...}

    @property
    def nb_solutions_alternatives(self):
        return len(self.solutions)

    def __repr__(self):
        return (
            f"<ReponseDiagnostic symptome={self.symptome} "
            f"nb_solutions={self.nb_solutions_alternatives}>"
        )


class Reasoner:
    def __init__(self, ttl_path: str):
        self.ontologie = OntologyAccess(ttl_path)

    def resoudre(self, symptome_id: str) -> ReponseDiagnostic:
        """
        Point d'entrée principal : prend un symptôme, renvoie toutes les
        causes possibles et leur action de résolution associée.
        """
        composants = self.ontologie.composants_affectes(symptome_id)
        solutions = self.ontologie.trouver_causes_et_actions(symptome_id)

        return ReponseDiagnostic(
            symptome=symptome_id,
            composants_affectes=composants,
            solutions=solutions,
        )