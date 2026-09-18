"""
Point d'entrée pour faire tourner le système décisionnel en local,
sans passer par l'API.
"""

from pathlib import Path
from .reasoner import Reasoner

ONTOLOGIE_PATH = Path(__file__).parent.parent / "ontologie" / "namec.ttl"

def main():
    r = Reasoner(ONTOLOGIE_PATH)
    reponse = r.resoudre("RoueBloquée")

    print(f"Symptôme : {reponse.symptome}")
    print(f"Composants affectés : {reponse.composants_affectes}")
    print(f"Solutions trouvées ({reponse.nb_solutions_alternatives}) :")
    for s in reponse.solutions:
        print(f"  - Cause : {s['cause']} → Action : {s['action']}")


if __name__ == "__main__":
    main()