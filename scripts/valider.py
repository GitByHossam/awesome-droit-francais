#!/usr/bin/env python3
"""Valide le schéma de data/ressources.yml.

Usage : python scripts/valider.py [chemin/vers/ressources.yml]

Le script s'arrête avec un code de sortie non nul et liste les erreurs si :
  1. un champ obligatoire manque ;
  2. une catégorie, une sous-catégorie, un type, un statut ou une étiquette est inconnu ;
  3. une clé apparaît deux fois dans un même dictionnaire ;
  4. une URL apparaît deux fois ;
  5. une URL n'est pas en HTTPS (sauf si la ligne porte un commentaire
     « # http-autorise : justification ») ;
  6. une description dépasse 200 caractères.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
FICHIER_PAR_DEFAUT = RACINE / "data" / "ressources.yml"

TYPES = {
    "api",
    "donnees",
    "outil",
    "bibliotheque",
    "mcp",
    "modele",
    "formation",
    "communaute",
    "site",
}

STATUTS = {"actif", "non-maintenu", "archive"}

# Identifiant -> libellé affiché dans le README (ordre = ordre de la légende).
ETIQUETTES = {
    "gratuit": "Gratuit",
    "open-source": "Open source",
    "inscription": "Inscription",
    "ia": "IA",
    "python": "Python",
    "javascript": "JavaScript",
    "freemium": "Freemium",
    "non-maintenu": "Non maintenu",
}

CHAMPS_CATEGORIE = {"titre", "description", "ordre"}
CHAMPS_SOUS_CATEGORIE = {"titre", "ordre"}
CHAMPS_RESSOURCE = {
    "nom",
    "url",
    "categorie",
    "sous_categorie",
    "description",
    "etiquettes",
    "licence",
    "type",
    "depot_github",
    "statut",
    "verifie_le",
}

LONGUEUR_MAX_DESCRIPTION = 200
MOTIF_EXCEPTION_HTTP = re.compile(r"#\s*http-autorise\s*:\s*\S+")
MOTIF_DEPOT = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


class ErreurCleDupliquee(yaml.YAMLError):
    """Levée quand une clé apparaît deux fois dans un même dictionnaire."""


class ChargeurStrict(yaml.SafeLoader):
    """Chargeur YAML qui refuse les clés en double au lieu de les écraser."""


def _construire_mapping(chargeur: ChargeurStrict, noeud: yaml.MappingNode, deep: bool = False):
    vues: dict = {}
    for noeud_cle, _ in noeud.value:
        cle = chargeur.construct_object(noeud_cle, deep=deep)
        if cle in vues:
            ligne = noeud_cle.start_mark.line + 1
            raise ErreurCleDupliquee(
                f"clé en double « {cle} » à la ligne {ligne} "
                f"(première occurrence ligne {vues[cle]})"
            )
        vues[cle] = noeud_cle.start_mark.line + 1
    return chargeur.construct_mapping(noeud, deep=deep)


ChargeurStrict.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construire_mapping
)


def charger(chemin: Path) -> dict:
    """Charge le YAML avec détection des clés en double."""
    with chemin.open(encoding="utf-8") as flux:
        return yaml.load(flux, Loader=ChargeurStrict)  # noqa: S506 (chargeur sûr)


def _lignes_http_autorisees(chemin: Path) -> set[str]:
    """Renvoie les URL http:// dont la ligne porte un commentaire de justification."""
    autorisees = set()
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        m = re.search(r"url:\s*[\"']?(http://[^\s\"']+)", ligne)
        if m and MOTIF_EXCEPTION_HTTP.search(ligne):
            autorisees.add(m.group(1))
    return autorisees


def valider(chemin: Path) -> list[str]:
    erreurs: list[str] = []

    try:
        donnees = charger(chemin)
    except ErreurCleDupliquee as exc:
        return [str(exc)]
    except yaml.YAMLError as exc:
        return [f"YAML invalide : {exc}"]

    if not isinstance(donnees, dict):
        return ["le fichier doit contenir un dictionnaire à la racine"]

    for section in ("categories", "sous_categories", "ressources"):
        if not isinstance(donnees.get(section), dict):
            erreurs.append(f"section « {section} » manquante ou qui n'est pas un dictionnaire")
    if erreurs:
        return erreurs

    categories = donnees["categories"]
    sous_categories = donnees["sous_categories"]
    ressources = donnees["ressources"]

    # Catégories
    ordres_vus: dict[int, str] = {}
    for ident, cat in categories.items():
        if not isinstance(cat, dict):
            erreurs.append(f"catégorie {ident} : doit être un dictionnaire")
            continue
        manquants = CHAMPS_CATEGORIE - cat.keys()
        if manquants:
            erreurs.append(f"catégorie {ident} : champ(s) manquant(s) {sorted(manquants)}")
        ordre = cat.get("ordre")
        if ordre in ordres_vus:
            erreurs.append(f"catégorie {ident} : ordre {ordre} déjà utilisé par {ordres_vus[ordre]}")
        ordres_vus[ordre] = ident
        for sc in cat.get("sous_categories") or []:
            if sc not in sous_categories:
                erreurs.append(f"catégorie {ident} : sous-catégorie inconnue « {sc} »")

    # Sous-catégories
    for ident, sc in sous_categories.items():
        if not isinstance(sc, dict):
            erreurs.append(f"sous-catégorie {ident} : doit être un dictionnaire")
            continue
        manquants = CHAMPS_SOUS_CATEGORIE - sc.keys()
        if manquants:
            erreurs.append(f"sous-catégorie {ident} : champ(s) manquant(s) {sorted(manquants)}")
        parents = [c for c, v in categories.items() if sc_in(ident, v)]
        if len(parents) != 1:
            erreurs.append(f"sous-catégorie {ident} : doit appartenir à exactement une catégorie")

    # Ressources
    http_autorisees = _lignes_http_autorisees(chemin)
    urls_vues: dict[str, str] = {}
    for ident, res in ressources.items():
        prefixe = f"ressource {ident}"
        if not isinstance(res, dict):
            erreurs.append(f"{prefixe} : doit être un dictionnaire")
            continue

        manquants = CHAMPS_RESSOURCE - res.keys()
        if manquants:
            erreurs.append(f"{prefixe} : champ(s) manquant(s) {sorted(manquants)}")
        inconnus = res.keys() - CHAMPS_RESSOURCE
        if inconnus:
            erreurs.append(f"{prefixe} : champ(s) inconnu(s) {sorted(inconnus)}")

        for champ in ("nom", "url", "description", "licence"):
            valeur = res.get(champ)
            if champ in res and (not isinstance(valeur, str) or not valeur.strip()):
                erreurs.append(f"{prefixe} : le champ « {champ} » doit être un texte non vide")

        categorie = res.get("categorie")
        if categorie not in categories:
            erreurs.append(f"{prefixe} : catégorie inconnue « {categorie} »")
        else:
            sc = res.get("sous_categorie")
            autorisees = categories[categorie].get("sous_categories") or []
            if sc is not None and sc not in autorisees:
                erreurs.append(
                    f"{prefixe} : sous-catégorie « {sc} » inconnue pour la catégorie « {categorie} »"
                )
            if sc is None and autorisees:
                erreurs.append(
                    f"{prefixe} : la catégorie « {categorie} » exige une sous-catégorie parmi {autorisees}"
                )

        if res.get("type") not in TYPES:
            erreurs.append(f"{prefixe} : type inconnu « {res.get('type')} »")
        if res.get("statut") not in STATUTS:
            erreurs.append(f"{prefixe} : statut inconnu « {res.get('statut')} »")

        etiquettes = res.get("etiquettes")
        if not isinstance(etiquettes, list):
            erreurs.append(f"{prefixe} : « etiquettes » doit être une liste")
        else:
            for etq in etiquettes:
                if etq not in ETIQUETTES:
                    erreurs.append(f"{prefixe} : étiquette inconnue « {etq} »")
            if len(set(etiquettes)) != len(etiquettes):
                erreurs.append(f"{prefixe} : étiquette répétée")

        depot = res.get("depot_github")
        if depot is not None and (not isinstance(depot, str) or not MOTIF_DEPOT.match(depot)):
            erreurs.append(f"{prefixe} : depot_github doit valoir null ou « proprietaire/depot »")

        verifie = res.get("verifie_le")
        if "verifie_le" in res and not isinstance(verifie, dt.date):
            erreurs.append(f"{prefixe} : verifie_le doit être une date AAAA-MM-JJ")

        url = res.get("url")
        if isinstance(url, str):
            cle_url = url.rstrip("/")
            if cle_url in urls_vues:
                erreurs.append(f"{prefixe} : URL déjà utilisée par {urls_vues[cle_url]} ({url})")
            urls_vues[cle_url] = ident
            if not url.startswith("https://") and url not in http_autorisees:
                erreurs.append(
                    f"{prefixe} : l'URL doit commencer par https:// "
                    "(ou porter un commentaire « # http-autorise : raison »)"
                )
            if any(c.isspace() for c in url):
                erreurs.append(f"{prefixe} : l'URL contient un espace")

        description = res.get("description")
        if isinstance(description, str):
            if len(description) > LONGUEUR_MAX_DESCRIPTION:
                erreurs.append(
                    f"{prefixe} : description de {len(description)} caractères "
                    f"(maximum {LONGUEUR_MAX_DESCRIPTION})"
                )
            if not description.rstrip().endswith("."):
                erreurs.append(f"{prefixe} : la description doit se terminer par un point")

        # Cohérence entre section « archives », statut et étiquette « non-maintenu ».
        archivee = categorie == "archives"
        if archivee and res.get("statut") == "actif":
            erreurs.append(f"{prefixe} : une ressource archivée ne peut pas avoir le statut « actif »")
        if not archivee and res.get("statut") in {"non-maintenu", "archive"}:
            erreurs.append(f"{prefixe} : une ressource inactive doit être rangée dans « archives »")
        if isinstance(etiquettes, list) and archivee != ("non-maintenu" in etiquettes):
            erreurs.append(
                f"{prefixe} : l'étiquette « non-maintenu » est réservée aux ressources archivées "
                "et obligatoire pour elles"
            )

    return erreurs


def sc_in(ident: str, categorie: dict) -> bool:
    return isinstance(categorie, dict) and ident in (categorie.get("sous_categories") or [])


def main(argv: list[str]) -> int:
    chemin = Path(argv[1]) if len(argv) > 1 else FICHIER_PAR_DEFAUT
    erreurs = valider(chemin)
    if erreurs:
        print(f"{len(erreurs)} erreur(s) dans {chemin} :", file=sys.stderr)
        for erreur in erreurs:
            print(f"  - {erreur}", file=sys.stderr)
        return 1
    donnees = charger(chemin)
    print(f"{chemin.name} est valide : {len(donnees['ressources'])} ressources.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
