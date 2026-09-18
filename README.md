# NAMeC Decision Helper

Système d'aide à la décision pour les opérateurs NAMeC (association robotique visant à partir à la Robocup) : diagnostic rapide des pannes robot via un graphe de connaissances (ontologie OWL) et un moteur de raisonnement logique.

## Problématique

Il a été observé, lors de la Robocup, que de nombreux problèmes survenaient pour des causes simples. Les personnes arrivant dans l'association n'étant pas expertes, il a été trouvé pertinent de construire un outil qui permette de répondre rapidement au problème rencontré. Cela implique que le système doit avoir une connaissance exacte du robot et de son fonctionnement.

## Fonctionnement
En résumé : 

Ontologie → système décisionnel → API → interface web

## Architecture

```
namec-decision-helper/
├── ontologie/
├── systeme_decisionnel/
├── serveur_api/
└── interface_web/
```

## Installation

1. Créer un environnement virtuel.
    ```
    python -m venv namec_venv
    ```

2. L'activer.
    ```
    namec_venv\Scripts\Activate.ps1
    ```

3. Installer les prérequis.
    ```
    pip install -r requirements.txt
    ```

4. Lancer le script suivant :
    ```
    python systeme-decisionnel/main.py
    ```

## Stack

### Graphe des connaissances
- **Protégé** : création de l'ontologie (.owl)
- **rdflib** : lecture de l'ontologie et requêtes SPARQL en Python
- **owlrl** : moteur d'inférence logique

### Serveur / API
- **FastAPI** : exposition des requêtes en API REST
- **Pydantic** : validation et formalisme des données échangées
- **Uvicorn** : serveur d'exécution

### Interface web
- **Vite** : structure HTML-SCSS-JS
- **Cytoscape.js** : visualisation interactive du graphe

### Système décisionnel
- **Python**

## Aller plus loin
Voir [methodologie.md](./methodologie.md) pour la démarche complète de conception.

## Captures d'écran
À documenter.

[screenshots interface + graphe]