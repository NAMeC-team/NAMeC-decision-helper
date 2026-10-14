# Interface Web
Ce fichier permet d'expliquer comment fonctionne la partie d'interface web du decision helper.

## Objectif
Ce dossier permet de générer l'interface web, grâce à Node.

## Stack
- Node (Vite) 
- JS

## Architecture
- **Node modules :** Tout le mic-mac qu'il ne faut pas importer sur github, qui apparaît dès que l'utilisateur a fait `npm install`.

- **Package, Package-lock & Vite.config :** Ce qui sert à générer l'interface avec Vite, selon la config de l'utilisateur.
- **src/ :**
  - **index.html :** Page HTML dans laquelle va s'insérer le site.
  - **main.js :** Initialise les trois panneaux qui composent l'interface :
    - *Request*
    - *Graph*
    - *Stats*

    Et crée leur structure HTML. Ils sont insérés dans index.html.
  - **api.js :** API qui répertorie toutes les requêtes possibles sur la page HTML, qui sont créées dans la partie [serveur_api](../serveur_api/) du projet.
  - **assets/ :** Ressources en dur.
    - **fonts/ :** Les polices d'écriture utilisées sur le site.
  - **components/ :** Différents composants utilisés plusieurs fois pour créer l'interface, qu'on peut appeler lors du design des panels.
  - **panels/ :** Fichiers JS des trois panels.
  - **styles/ :** Les styles en SCSS. Pour l'instant un seul, mais on pourra créer un thème sombre au besoin.