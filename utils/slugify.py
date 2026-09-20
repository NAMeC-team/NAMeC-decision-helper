"""
Utilitaires de transformation de chaînes : convertit les identifiants
lisibles de l'ontologie (avec accents, casse) en "slugs" compatibles
avec des URLs (ASCII, minuscules, tirets).

Oui, les slugs ne sont pas seulement des limaces comme dans Slugterra
pour ceux qui ont cette ref incroyable. D'ailleurs la musique est géniale.
https://www.youtube.com/watch?v=6kT0LYh81FU
"""

import unicodedata
import re


def slugify(texte: str) -> str:
    """
    Transforme une chaîne en slug compatible URL.
    Ex: "RoueBloquée" -> "roue-bloquee"
        "CâbleDébranché" -> "cable-debranche"
    """
    # Sépare les lettres accentuées de leurs accents (ex: é -> e + ́)
    texte_normalise = unicodedata.normalize("NFKD", texte)
    # Ne garde que les caractères ASCII (élimine les accents isolés)
    texte_sans_accent = texte_normalise.encode("ascii", "ignore").decode("ascii")

    # Insère un tiret avant chaque majuscule (sépare les mots en camelCase)
    texte_espace = re.sub(r"(?<!^)(?=[A-Z])", "-", texte_sans_accent)

    return texte_espace.lower()