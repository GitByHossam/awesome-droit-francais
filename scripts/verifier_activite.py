#!/usr/bin/env python3
"""Vérifie l'activité des dépôts GitHub référencés dans data/ressources.yml.

Usage :
    GITHUB_TOKEN=... python scripts/verifier_activite.py [--sortie rapport.md]

Pour chaque ressource qui renseigne « depot_github », le script interroge
l'API GitHub (date du dernier commit sur la branche par défaut, archivage,
existence du dépôt) et signale les incohérences :

- dépôt introuvable ou inaccessible ;
- dépôt archivé sur GitHub ;
- dernier commit il y a plus de 24 mois alors que la ressource n'est pas
  rangée dans « archives » ;
- ressource rangée dans « archives » alors que le dépôt est de nouveau actif.

Le rapport est écrit en Markdown sur la sortie standard (ou dans le fichier
indiqué par --sortie). Code de sortie : 0 sans anomalie, 1 sinon, 2 en cas
d'erreur technique.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from valider import FICHIER_PAR_DEFAUT, charger  # noqa: E402

API = "https://api.github.com"
SEUIL_JOURS = 730  # 24 mois


def appeler_api(chemin: str, jeton: str | None) -> dict | list | None:
    requete = urllib.request.Request(f"{API}{chemin}")
    requete.add_header("Accept", "application/vnd.github+json")
    requete.add_header("X-GitHub-Api-Version", "2022-11-28")
    requete.add_header("User-Agent", "awesome-droit-francais-verifier-activite")
    if jeton:
        requete.add_header("Authorization", f"Bearer {jeton}")
    try:
        with urllib.request.urlopen(requete, timeout=30) as reponse:
            return json.load(reponse)
    except urllib.error.HTTPError as exc:
        if exc.code in (404, 451):
            return None
        raise


def date_dernier_commit(depot: str, branche: str, jeton: str | None) -> dt.date | None:
    commits = appeler_api(f"/repos/{depot}/commits?sha={branche}&per_page=1", jeton)
    if not commits:
        return None
    horodatage = commits[0]["commit"]["committer"]["date"]
    return dt.datetime.fromisoformat(horodatage.replace("Z", "+00:00")).date()


def verifier(donnees: dict, jeton: str | None, aujourd_hui: dt.date) -> tuple[list[str], list[str]]:
    anomalies: list[str] = []
    lignes: list[str] = []

    for ident, res in sorted(donnees["ressources"].items()):
        depot = res.get("depot_github")
        if not depot:
            continue
        archivee = res["categorie"] == "archives"

        infos = appeler_api(f"/repos/{depot}", jeton)
        if infos is None:
            anomalies.append(f"`{ident}` : dépôt `{depot}` introuvable ou inaccessible.")
            lignes.append(f"| `{ident}` | `{depot}` | introuvable | - |")
            continue

        nom_reel = infos.get("full_name", depot)
        if nom_reel.lower() != depot.lower():
            anomalies.append(f"`{ident}` : le dépôt `{depot}` a été déplacé vers `{nom_reel}`.")

        dernier = date_dernier_commit(nom_reel, infos.get("default_branch", "main"), jeton)
        age = (aujourd_hui - dernier).days if dernier else None
        etat = "archivé" if infos.get("archived") else "actif"
        lignes.append(f"| `{ident}` | `{nom_reel}` | {etat} | {dernier or 'inconnu'} |")

        if infos.get("archived") and not archivee:
            anomalies.append(
                f"`{ident}` : `{nom_reel}` est archivé sur GitHub ; "
                "déplacez l'entrée dans la catégorie « archives »."
            )
        if age is not None and age > SEUIL_JOURS and not archivee:
            anomalies.append(
                f"`{ident}` : dernier commit le {dernier} (plus de 24 mois) ; "
                "déplacez l'entrée dans la catégorie « archives »."
            )
        if archivee and age is not None and age <= SEUIL_JOURS and not infos.get("archived"):
            anomalies.append(
                f"`{ident}` : rangé dans « archives » mais un commit date du {dernier} ; "
                "l'entrée peut revenir dans sa catégorie d'origine."
            )

    return anomalies, lignes


def rapport(anomalies: list[str], lignes: list[str], aujourd_hui: dt.date) -> str:
    sortie = [f"## Activité des dépôts GitHub ({aujourd_hui})", ""]
    if anomalies:
        sortie += [f"{len(anomalies)} anomalie(s) :", ""]
        sortie += [f"- {a}" for a in anomalies]
    else:
        sortie.append("Aucune anomalie.")
    sortie += [
        "",
        "<details><summary>Détail par dépôt</summary>",
        "",
        "| Ressource | Dépôt | État | Dernier commit |",
        "| --- | --- | --- | --- |",
        *lignes,
        "",
        "</details>",
    ]
    return "\n".join(sortie) + "\n"


def main() -> int:
    analyseur = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analyseur.add_argument("--sortie", type=Path, help="fichier Markdown où écrire le rapport")
    args = analyseur.parse_args()

    jeton = os.environ.get("GITHUB_TOKEN")
    if not jeton:
        print("Avertissement : GITHUB_TOKEN absent, l'API limite fortement le nombre d'appels.",
              file=sys.stderr)

    aujourd_hui = dt.date.today()
    try:
        anomalies, lignes = verifier(charger(FICHIER_PAR_DEFAUT), jeton, aujourd_hui)
    except (urllib.error.URLError, TimeoutError) as exc:
        print(f"Erreur d'accès à l'API GitHub : {exc}", file=sys.stderr)
        return 2

    texte = rapport(anomalies, lignes, aujourd_hui)
    if args.sortie:
        args.sortie.write_text(texte, encoding="utf-8")
    print(texte)
    return 1 if anomalies else 0


if __name__ == "__main__":
    sys.exit(main())
