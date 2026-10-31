# Ontologie
Ce fichier permet d'expliquer la partie ontologie, ou IA symbolique, du decision helper.

## Objectif
Construit le réseau de neurones logique qui sert de base au système décisionnel.

## Stack
- YAML

## Architecture
***namec.ttl :** Ancienne ontologie : l'ontologie en format turtle. Chaque entité est créée dans le logiciel *Protégé*. Ensuite, des règles logiques sont créées, pour relier les entités entre elles, et ainsi construire une partie du monde centrée sur les robots et leur fonctionnement.*

Actuellement, l'ontologie est un arbre de dossiers, donc la racine est le dossier [concept](/ontologie/concepts/).

- Chaque dossier comporte un seul et unique fichier YAML, qui décrit l'élément du dossier en question, selon son nom.

- Chaque dossier **"est un"** élément du dossier parent. C'est une relation d'existence et non d'appartenance.

- Chaque entité décrite dans une fiche YAML peut posséder des liens avec une ou plusieurs autres entités. C'est ce qui permet de créer un graphe de connaissances.

- La nature de ces liens est décrite dans le fichier [liens.yaml](liens.yaml). De nouveaux liens peuvent être créés au besoin.