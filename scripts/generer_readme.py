#!/usr/bin/env python3
"""Génère README.md à partir de data/ressources.yml et de templates/README.template.md.

Usage : python scripts/generer_readme.py

Ne modifiez jamais README.md à la main : modifiez data/ressources.yml puis
relancez ce script.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from valider import ETIQUETTES, FICHIER_PAR_DEFAUT, RACINE, charger, valider  # noqa: E402

GABARIT = RACINE / "templates" / "README.template.md"
SORTIE = RACINE / "README.md"


def cle_tri(texte: str) -> str:
    """Clé de tri alphabétique insensible à la casse et aux accents."""
    sans_accents = unicodedata.normalize("NFKD", texte)
    sans_accents = "".join(c for c in sans_accents if not unicodedata.combining(c))
    return sans_accents.casefold()


def ancre(titre: str) -> str:
    """Reproduit l'ancre générée par GitHub pour un titre de section."""
    texte = titre.strip().lower()
    texte = re.sub(r"[^\w\- ]", "", texte)
    return "#" + texte.replace(" ", "-")


def echapper(texte: str) -> str:
    """Échappe les caractères qui casseraient la syntaxe Markdown d'une entrée."""
    return texte.replace("[", "\\[").replace("]", "\\]")


def formater_etiquettes(etiquettes: list[str]) -> str:
    ordonnees = [e for e in ETIQUETTES if e in etiquettes]
    return " ".join(f"\\[{ETIQUETTES[e]}\\]" for e in ordonnees)


def formater_entree(res: dict) -> str:
    etiquettes = formater_etiquettes(res["etiquettes"])
    prefixe = f"{etiquettes} " if etiquettes else ""
    return f"- [{echapper(res['nom'])}]({res['url']}) - {prefixe}{res['description'].strip()}"


def formater_liste(ressources: list[dict]) -> list[str]:
    return [formater_entree(r) for r in sorted(ressources, key=lambda r: cle_tri(r["nom"]))]


def generer(donnees: dict) -> str:
    categories = sorted(donnees["categories"].items(), key=lambda kv: kv[1]["ordre"])
    sous_categories = donnees["sous_categories"]
    ressources = list(donnees["ressources"].values())

    # Le sommaire utilise des liens par référence : awesome-lint n'accepte pas
    # d'ancre « #... » dans une liste en dehors d'une section nommée « Contents ».
    sommaire: list[str] = []
    references: list[str] = []
    corps: list[str] = []

    def ajouter_sommaire(niveau: int, ident: str, titre: str) -> None:
        # Forme « [Titre][] » quand l'identifiant se déduit du titre (règle remark-lint).
        etiquette = "" if cle_tri(titre) == ident else ident
        sommaire.append(f"{'  ' * niveau}- [{titre}][{etiquette}]")
        references.append(f"[{ident}]: {ancre(titre)}")

    for ident, cat in categories:
        titre = cat["titre"]
        ajouter_sommaire(0, ident, titre)
        corps += [f"## {titre}", "", f"{cat['description'].strip()}", ""]

        membres = [r for r in ressources if r["categorie"] == ident]
        sc_ids = sorted(cat.get("sous_categories") or [], key=lambda s: sous_categories[s]["ordre"])

        if not sc_ids:
            corps += formater_liste(membres) + [""]
            continue

        for sc in sc_ids:
            sc_titre = sous_categories[sc]["titre"]
            ajouter_sommaire(1, sc, sc_titre)
            corps += [f"### {sc_titre}", ""]
            corps += formater_liste([r for r in membres if r["sous_categorie"] == sc]) + [""]

    for ident, titre in (("contribuer", "Contribuer"), ("licence-du-contenu", "Licence du contenu")):
        ajouter_sommaire(0, ident, titre)

    gabarit = GABARIT.read_text(encoding="utf-8")
    contenu = (
        gabarit.replace("{{SOMMAIRE}}", "\n".join(sommaire + [""] + references))
        .replace("{{CATEGORIES}}", "\n".join(corps).rstrip())
        .replace("{{NOMBRE}}", str(len(ressources)))
    )
    return contenu.rstrip() + "\n"


def main() -> int:
    erreurs = valider(FICHIER_PAR_DEFAUT)
    if erreurs:
        print("data/ressources.yml est invalide, lancez scripts/valider.py.", file=sys.stderr)
        return 1
    SORTIE.write_text(generer(charger(FICHIER_PAR_DEFAUT)), encoding="utf-8")
    print(f"README.md généré ({SORTIE}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
