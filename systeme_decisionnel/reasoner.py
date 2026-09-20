"""
Système décisionnel : à partir d'un symptôme, détermine les causes possibles
et les actions associées.

Ce module ne connaît jamais rdflib/owlrl directement — il passe uniquement
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

    def resoudre_par_slug(self, slug: str) -> ReponseDiagnostic | None:
        """
        Comme resoudre(), mais accepte un slug d'URL (ex: 'roue-bloquee')
        au lieu de l'identifiant exact de l'ontologie. Renvoie None si
        le slug ne correspond à aucun symptôme connu.
        """
        symptome_id = self.ontologie.resoudre_slug_symptome(slug)
        if symptome_id is None:
            return None
        return self.resoudre(symptome_id)


if __name__ == "__main__":
    r = Reasoner("../ontologie/namec.ttl")
    reponse = r.resoudre("RoueBloquée")

    print(f"Symptôme : {reponse.symptome}")
    print(f"Composants affectés : {reponse.composants_affectes}")
    print(f"Solutions trouvées ({reponse.nb_solutions_alternatives}) :")
    for s in reponse.solutions:
        print(f"  - Cause : {s['cause']} → Action : {s['action']}")