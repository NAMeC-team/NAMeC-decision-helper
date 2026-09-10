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
├── systeme-decisionnel/
├── serveur-api/
└── interface-web/
```

## Installation
À documenter.

[commandes : pip install, npm install, lancement serveur + front]

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