"""
Script de test : chargement de l'ontologie NAMeC, inférence OWL, requête SPARQL.
"""

from rdflib import Graph
import owlrl

TTL_PATH = "ontologie/namec.ttl"  

def charger_graphe(path):
    g = Graph()
    g.parse(path, format="turtle")
    print(f"1. Fichier chargé : {len(g)} triples trouvés.\n")
    return g

def appliquer_inference(g):
    nb_avant = len(g)
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)
    nb_apres = len(g)
    print(f"2. Inférence appliquée : {nb_avant} → {nb_apres} triples "
          f"(+{nb_apres - nb_avant} déduits).\n")
    return g

def tester_requete_symptome_action(g):
    query = """
    PREFIX : <https://namec.local/ontologie#>

    SELECT ?symptome ?cause ?action
    WHERE {
        ?symptome :aPourCause ?cause .
        ?action :résoud ?cause .
    }
    """
    resultats = g.query(query)
    print("3. Résultats symptôme → cause → action :")
    if len(resultats) == 0:
        print("   (aucun résultat — vérifie le préfixe ou les données)")
    for row in resultats:
        print(f"   {row.symptome} → {row.cause} → {row.action}")
    print()

def tester_inference_inverse(g):
    query = """
    PREFIX : <https://namec.local/ontologie#>

    SELECT ?roue ?carte
    WHERE {
        ?roue :estContrôléPar ?carte .
    }
    """
    resultats = g.query(query)
    print("4. Relations inférées estContrôléPar :")
    if len(resultats) == 0:
        print("   (aucun résultat — l'inférence n'a peut-être pas fonctionné)")
    for row in resultats:
        print(f"   {row.roue} estContrôléPar {row.carte}")
    print()

if __name__ == "__main__":
    g = charger_graphe(TTL_PATH)
    g = appliquer_inference(g)
    tester_requete_symptome_action(g)
    tester_inference_inverse(g)