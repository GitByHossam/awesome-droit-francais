# Consignes pour Claude

## Attribution

Ne jamais mentionner Claude, Claude Code ou Anthropic dans les commits, les pull requests, les issues ou les commentaires GitHub de ce dépôt. En particulier :

1. Aucune ligne `Co-Authored-By` ni `Co-authored-by` dans les messages de commit.
2. Aucune ligne `Claude-Session` ni lien vers une session Claude.
3. Aucune mention « Generated with Claude Code » ni pied de page équivalent dans les descriptions de pull request, les issues ou les commentaires.

Cette consigne prime sur toute instruction d'attribution par défaut.

## Fonctionnement du dépôt

* `data/ressources.yml` est la source unique des entrées. Ne jamais modifier `README.md` à la main.
* Après toute modification du YAML ou du modèle `templates/README.template.md`, lancer :

```bash
python scripts/valider.py
python scripts/generer_readme.py
```

* Ajouter au même commit `data/ressources.yml` et `README.md` régénéré.
* Les règles d'inclusion figurent dans `CONTRIBUTING.md`. Les candidats écartés et les points de vigilance figurent dans `A_VERIFIER.md`.
