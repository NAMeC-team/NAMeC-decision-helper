# Serveur API
Ce fichier permet d'expliquer comment fonctionne la partie serveur API du decision helper.

## Objectif
Ce dossier permet de créer les routes pour l'API, qui permettront l'échange de données entre le serveur (cerveau de l'IA symbolique) et les demandes de l'utilisateur.

## Stack
- Python
- FastAPI & Swagger

## Architecture

**NB :** *On a des fichiers `__init.py__` dans le dossier. Tout ce qui est python fonctionne par module afin de faciliter les imports.*

- **main.py :** Crée un réseau de routes avec FastAPI. Permet d'avoir une jolie doc des routes. Autorise l'interface web générée avec Vite à communiquer avec, puisqu'elle est servie sur le localhost, donc un port différent.

- **schemas.py :** Définie la forme des données pour l'API. Sert au dev de l'interface pour savoir ce qu'il doit envoyer, ce qu'il peut appeler.

- **dependencies.py :** C'est là où on communique avec l'IA symbolique (le reasoner). C'est ce qui permet de récupérer les entités du réseau décisionnel pour gérer les demandes de l'utilisateur.

- **routes/ :**

  - **graph.py :** Route qui sert à obtenir le graphe de connaissance.

  - **solve.py :** Route qui sert à résoudre un problème à partir d'un symptome donné, en demandant au reasonner de lui fournir les causes du symptome.
