# Méthodologie

Le présent document sert à expliciter la façon dont est faite ce système.

## Étapes de conception

Voici les différentes étapes clés nécessaires à la conception du MVP :

1. Générer le graphe des connaissances lié aux robots NAMeC.
    1. Répertorier toutes les entités spécifiques au robot (dribleur, vis de telle nature, roue, sous-composants de la roue, cartes, sous-cartes)
    2. Répertorier toutes les actions relatives à ces entités (monter, démonter, flasher), avec différentes règles logique : pourquoi / comment / avec quoi.
    3. Formaliser les connaissances.

2. Créer une interface web, qui permettra ensuite de :
    1. Visualiser le graphe des connaissances, et les règles logiques que suivent les liens.
    2. Sélectionner des items dans un pannel dédié, afin de filtrer les éléments relatifs au problème, et proposer des solutions adaptées.
    3. Montrer des statistiques généralistes, ou plus précises. Par exemple : 
        - Nombre de fois que ce problème est recherché
        - Nombre de liaisons parcourues pour arriver à la solution
        - Nombre de solutions alternatives possibles

3. Créer le système interne de décision.
    1. Entrée : un problème, fait d'entités reliées par une logique de causalité.
    2. Sortie : une solution.

4. Rendre l'expérience intuitive.

5. Rédiger un document qui explique comment le système a été fait.



## Architecture

```
namec-decision-helper/
├── ontologie/
│   └── namec.ttl              # créé dans Protégé
│
├── systeme-decisionnel/       # le "cerveau" : lit l'ontologie, raisonne
│   ├── reasoner.py            # logique de résolution de problème
│   ├── ontology_access.py     # lecture .owl + requêtes SPARQL (rdflib, owlrl)
|   ├── tests/                 # tests fonctionnels
│   └── scripts/               # tests de logique décisionnelle
│
├── serveur-api/               # expose le système décisionnel au web
│   ├── main.py                # FastAPI, déclaration des routes
│   ├── routes/
│   │   ├── graph.py
│   │   ├── solve.py
│   │   └── stats.py
│   └── schemas.py             # Pydantic
│
├── interface-web/             # ce que voit l'utilisateur
│   ├── src/
│   │   ├── main.js
│   │   ├── api.js
│   │   ├── graph-view.js      # Cytoscape.js
│   │   ├── filter-panel.js
│   │   ├── stats-panel.js
│   │   └── styles/
│   │       └── main.scss
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── requirements.txt
├── methodologie.md
├── .gitignore
└── README.md
```


