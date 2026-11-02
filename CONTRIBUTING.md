# Guide de contribution

Merci de vouloir enrichir cette liste. Ce guide explique ce qui peut y figurer et comment proposer une ressource.

En participant, vous acceptez de respecter le [code de conduite](CODE_OF_CONDUCT.md).

## Critères d'inclusion

Une ressource peut être ajoutée si elle remplit toutes les conditions suivantes :

1. Elle est utile pour le droit français ou pour des juristes francophones.
2. Elle est accessible publiquement, éventuellement après une inscription gratuite.
3. Elle dispose d'une documentation minimale qui permet de comprendre à quoi elle sert et comment l'utiliser.
4. S'il s'agit d'un projet open source, il a connu une activité (au moins un commit) au cours des 24 derniers mois. À défaut, il est rangé dans la section « Projets archivés ou non maintenus », avec l'étiquette `non-maintenu`.

Un outil commercial n'est accepté que s'il propose une offre gratuite ou une API publique réellement utile. Il porte alors l'étiquette `freemium`.

## Critères d'exclusion

Ne sont pas acceptés :

- l'autopromotion purement commerciale, sans offre gratuite ;
- les contenus piratés ou les outils qui contournent un paywall ou des conditions d'accès ;
- les outils sans aucune documentation ;
- les ressources dont on ne peut pas vérifier le fonctionnement.

## Comment proposer une ressource

### Option 1 : ouvrir une issue

Utilisez le formulaire [Proposer une ressource](../../issues/new?template=proposer-ressource.yml). Une personne qui maintient la liste vérifiera la ressource et l'ajoutera si elle répond aux critères.

### Option 2 : ouvrir une pull request

1. Modifiez **uniquement** le fichier `data/ressources.yml`. Ne modifiez jamais `README.md` à la main : il est généré automatiquement.
2. Ajoutez votre entrée dans la bonne catégorie en respectant le schéma ci-dessous.
3. Installez la seule dépendance nécessaire : `pip install pyyaml`.
4. Lancez la validation : `python scripts/valider.py`.
5. Régénérez le README : `python scripts/generer_readme.py`.
6. Ajoutez à votre commit `data/ressources.yml` et `README.md`, puis ouvrez la pull request en remplissant le modèle proposé.

L'intégration continue vérifie que le YAML est valide, que le README correspond au YAML et que la liste respecte les règles d'[awesome-lint](https://github.com/sindresorhus/awesome-lint).

### Schéma d'une entrée

```yaml
  identifiant-unique:
    nom: "Nom de la ressource"
    url: "https://exemple.fr/"
    categorie: sources-officielles      # identifiant d'une catégorie existante
    sous_categorie: null                # obligatoire si la catégorie a des sous-catégories
    description: "Une phrase orientée usage, terminée par un point."
    etiquettes: [gratuit]               # voir la liste ci-dessous
    licence: "Licence Ouverte 2.0"
    type: site                          # api | donnees | outil | bibliotheque | mcp | modele | formation | communaute | site
    depot_github: null                  # "proprietaire/depot" si le code est sur GitHub
    statut: actif                       # actif | non-maintenu | archive
    verifie_le: 2026-11-02              # date de votre vérification
```

Étiquettes disponibles : `gratuit`, `open-source`, `inscription`, `ia`, `python`, `javascript`, `freemium` et `non-maintenu`. Leur signification est donnée dans la légende du README.

Les URL doivent être en HTTPS. Une exception n'est possible que si la ligne porte un commentaire du type `# http-autorise : le site ne propose pas de HTTPS`.

## Rédiger une description

- Une ou deux phrases, 200 caractères au maximum, terminées par un point.
- Une phrase orientée usage : dites à quoi la ressource sert pour un juriste ou un développeur.
- Utilisez vos propres mots. Ne copiez pas la description du site ou du dépôt.
- Pas de superlatif (« le meilleur », « révolutionnaire »), pas de langage promotionnel, pas d'émoji.
- Signalez les limites utiles : inscription requise, documentation en anglais, projet expérimental.

## Vérification hebdomadaire

Chaque lundi, un workflow vérifie les liens du README et l'activité des dépôts GitHub référencés. En cas d'anomalie, il ouvre ou met à jour l'issue « Rapport hebdomadaire des liens ». Toute aide pour la traiter est la bienvenue.
