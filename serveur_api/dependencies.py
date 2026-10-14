"""
Instance partagée du Reasoner. Toutes les routes importent ce module
plutôt que de créer chacune leur propre instance — l'ontologie n'est
chargée et inférée qu'une seule fois, au démarrage du serveur.
"""

from pathlib import Path

from systeme_decisionnel.reasoner import Reasoner

ONTOLOGIE_PATH = Path(__file__).parent.parent / "ontologie" / "namec.ttl"

reasoner = Reasoner(str(ONTOLOGIE_PATH))