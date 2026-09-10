# NAMeC Decision Helper
Système intelligent d'aide à la décision afin d'expliciter le fonctionnement des robots à NAMeC et de répondre aux questions des opérateurs.

## Problématique

Il a été observé, lors de la Robocup, que de nombreux problèmes survenaient pour des causes simples. Les personnes arrivant dans l'association n'étant pas expertes, il a été trouvé pertinent de construire un outil qui permette de répondre rapidement au problème rencontré. Cela implique que le système doit avoir une connaissance exacte du robot et de son fonctionnement.

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

