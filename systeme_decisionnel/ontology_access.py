"""
Accès à l'ontologie : lit les fiches YAML (ontologie/concepts/**/fiche.yaml)
et permet de suivre les liens d'une fiche à l'autre.

C'est le seul fichier qui sait comment la connaissance est stockée.
"""

from pathlib import Path

import yaml


class OntologyAccess:
    def __init__(self, dossier_ontologie: str):
        self.fiches = {}     # id -> contenu de la fiche
        self.lignees = {}    # id -> dossiers traversés, ex: ("element_diagnostic", "symptome", "roue_bloquee")
        self._charger(Path(dossier_ontologie) / "concepts")

    def _charger(self, dossier_concepts: Path):
        if not dossier_concepts.is_dir():
            raise FileNotFoundError(f"Dossier introuvable : {dossier_concepts}")
        for chemin in sorted(dossier_concepts.rglob("fiche.yaml")):
            with open(chemin, encoding="utf-8") as f:
                fiche = yaml.safe_load(f)
            self.fiches[fiche["id"]] = fiche
            self.lignees[fiche["id"]] = chemin.relative_to(dossier_concepts).parts[:-1]

    # ---------- Lecture ----------

    def nom(self, fiche_id: str) -> str:
        return self.fiches[fiche_id]["nom"]

    def _cibles(self, fiche_id: str, lien: str) -> list[str]:
        """Ids pointés par un lien d'une fiche (liste vide si le lien n'existe pas)."""
        liens = self.fiches[fiche_id].get("liens") or {}
        return [c for c in liens.get(lien, []) if c in self.fiches]

    def est_un_symptome(self, fiche_id: str) -> bool:
        # « symptome » doit être un dossier PARENT : la catégorie elle-même n'est pas un symptôme.
        return fiche_id in self.fiches and "symptome" in self.lignees[fiche_id][:-1]

    def lister_symptomes(self) -> list[dict]:
        return [
            {"id": i, "nom": f["nom"]}
            for i, f in self.fiches.items()
            if self.est_un_symptome(i)
        ]

    def composants_affectes(self, symptome_id: str) -> list[str]:
        return [self.nom(c) for c in self._cibles(symptome_id, "affecte")]

    def trouver_causes_et_actions(self, symptome_id: str) -> list[dict]:
        """symptôme -> causes -> actions."""
        solutions = []
        for cause_id in self._cibles(symptome_id, "a_pour_cause"):
            for action_id in self._cibles(cause_id, "traitee_par"):
                solutions.append({
                    "cause": self.nom(cause_id),
                    "action": self.nom(action_id),
                    "description": self.fiches[action_id].get("description"),
                })
        return solutions

    # ---------- Export pour la visualisation ----------

    def exporter_graphe(self, exclure: tuple[str, ...] = (), replier: tuple[str, ...] = ()) -> dict:
        """
        Un nœud par fiche ; arêtes « hierarchie » (dossier parent -> enfant) et « lien » (nommées).

        exclure : ids de concepts à masquer, avec tous leurs descendants.
        replier : ids de concepts dont on cache les descendants mais pas le concept lui-même.
                  Les liens des descendants cachés sont remontés sur ce concept.
        """

        def representant(fiche_id):
            """Fiche affichée à la place de fiche_id : elle-même, son ancêtre replié, ou None si exclue."""
            lignee = self.lignees[fiche_id]
            if any(e in lignee for e in exclure):
                return None
            for ancetre in lignee[:-1]:          # du plus haut au plus proche
                if ancetre in replier and ancetre in self.fiches:
                    return ancetre
            return fiche_id

        affichees = {i for i in self.fiches if representant(i) == i}
        noeuds = [
            {"id": i, "nom": f["nom"], "symptome": self.est_un_symptome(i)}
            for i, f in self.fiches.items()
            if i in affichees
        ]

        aretes = []
        for fiche_id in affichees:
            lignee = self.lignees[fiche_id]
            if len(lignee) > 1 and lignee[-2] in affichees:
                aretes.append({"source": lignee[-2], "target": fiche_id, "label": "", "type": "hierarchie"})

        liens_vus = set()    # évite les doublons quand plusieurs enfants cachés pointent au même endroit
        for fiche_id, fiche in self.fiches.items():
            for lien in fiche.get("liens") or {}:
                for cible in self._cibles(fiche_id, lien):
                    source, destination = representant(fiche_id), representant(cible)
                    if source is None or destination is None or source == destination:
                        continue
                    if (source, destination, lien) not in liens_vus:
                        liens_vus.add((source, destination, lien))
                        aretes.append({"source": source, "target": destination, "label": lien, "type": "lien"})

        return {"nodes": noeuds, "edges": aretes}