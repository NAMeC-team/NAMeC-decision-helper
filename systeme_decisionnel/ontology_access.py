"""
Accès à l'ontologie NAMeC : chargement du fichier .ttl, application de
l'inférence OWL, et exécution de requêtes SPARQL.

Ce module est la seule couche du projet à connaître rdflib/owlrl.
reasoner.py ne doit jamais importer rdflib directement — il passe
toujours par les fonctions exposées ici.
"""

from pathlib import Path
from rdflib import Graph
import owlrl

from utils.slugify import slugify

NS = "https://namec.local/ontologie#"


class OntologyAccess:
    def __init__(self, ttl_path: str):
        self.ttl_path = Path(ttl_path)
        self.graph = Graph()
        self._charger()
        self._appliquer_inference()

    def _charger(self):
        if not self.ttl_path.exists():
            raise FileNotFoundError(f"Fichier introuvable : {self.ttl_path}")
        self.graph.parse(self.ttl_path, format="turtle")

    def _appliquer_inference(self):
        owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(self.graph)

    def query(self, sparql: str):
        """Exécute une requête SPARQL brute et renvoie les résultats."""
        prefixe = f"PREFIX : <{NS}>\n"
        return self.graph.query(prefixe + sparql)

    def trouver_causes_et_actions(self, symptome_id: str):
        """
        Étant donné l'identifiant court d'un symptôme (ex: 'RoueBloquée'),
        renvoie la liste des (cause, action) possibles.
        """
        sparql = """
        SELECT ?cause ?action
        WHERE {
            :%s :aPourCause ?cause .
            ?action :résoud ?cause .
        }
        """ % symptome_id

        resultats = self.query(sparql)
        return [
            {
                "cause": self._nom_court(row.cause),
                "action": self._nom_court(row.action),
            }
            for row in resultats
        ]

    def composants_affectes(self, symptome_id: str):
        """Renvoie la liste des composants affectés par un symptôme."""
        sparql = """
        SELECT ?composant
        WHERE {
            :%s :symptômeAffecte ?composant .
        }
        """ % symptome_id

        resultats = self.query(sparql)
        return [self._nom_court(row.composant) for row in resultats]

    def lister_symptomes(self):
        """Renvoie la liste de tous les identifiants de symptômes connus."""
        sparql = """
        SELECT ?symptome
        WHERE {
            ?symptome a :Symptôme .
        }
        """
        resultats = self.query(sparql)
        return [self._nom_court(row.symptome) for row in resultats]

    def resoudre_slug_symptome(self, slug: str) -> str | None:
        """
        Retrouve l'identifiant réel d'un symptôme à partir de son slug
        (ex: 'roue-bloquee' -> 'RoueBloquée'). Renvoie None si aucun
        symptôme ne correspond.
        """
        for symptome in self.lister_symptomes():
            if slugify(symptome) == slug:
                return symptome
        return None

    @staticmethod
    def _nom_court(uri):
        """Extrait le nom court d'une URI complète (après le '#')."""
        return str(uri).split("#")[-1]