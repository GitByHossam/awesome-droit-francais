# Ressources à vérifier

Ce fichier recense les ressources candidates qui ne figurent **pas** dans le README, avec la raison de leur mise à l'écart. Une ressource ne rejoint `data/ressources.yml` qu'une fois vérifiée (URL fonctionnelle, description fidèle, licence et statut exacts).

Dernière mise à jour : 2026-11-03.

## Candidats écartés

| Ressource | Adresse examinée | Raison |
| --- | --- | --- |
| OpenLegi (Le Lab de dassignies.law) | `https://mcp.openlegi.fr/` | Ressource introuvable sur son propre site : seuls des annuaires tiers de serveurs MCP la décrivent. Les conditions de l'offre gratuite et la licence n'ont pas pu être confirmées. |
| Tricoteuses, forge Git | `https://git.tricoteuses.fr/` | Ressource introuvable : le domaine n'a pas répondu et aucune recherche n'a permis de confirmer son contenu. Les jeux de données Hugging Face de Tricoteuses sont, eux, vérifiés et listés. |
| Awesome Open Legal Switzerland | non trouvée | Ressource introuvable : aucune liste portant ce nom n'a été trouvée. La liste suisse « Awesome OGD Switzerland » (données publiques) est listée à la place. |
| Moteur de recherche Judilibre | `https://www.courdecassation.fr/recherche-judilibre` | URL donnée par le README du dépôt `Cour-de-cassation/judilibre-search`, mais non testée en HTTP. Seule l'API Judilibre (fiche data.gouv.fr) est listée. |
| Archéo Lex, site de présentation | `https://archeo-lex.fr/` | Lien non vérifié : le site n'a pas répondu et n'apparaît pas dans les résultats de recherche. Le dépôt GitHub du projet est listé dans les archives. |
| Calculateur de délai d'appel en matière civile (cabinet Simonnet) | `https://www.simonnetavocat.fr/?p=280672` | Adresse imprécise : seule une URL courte technique a été trouvée. Le calculateur pénal du même site est listé. |
| Calculateurs privés d'intérêts légaux (macalculatriceenligne.com, dossierjuridique.fr) | divers | Fiabilité non établie : sources et formules peu documentées. La fiche officielle de justice.fr est listée à la place. |
| LEGI (LeMoussel) sur Hugging Face | `https://huggingface.co/datasets/LeMoussel/LEGI` | Lien vérifié (licence MIT), mais non retenu car il fait doublon avec le jeu LEGI de Tricoteuses. À réexaminer si son contenu se distingue. |
| French-law-mcp (Ansvar-Systems) et Legal (BenjoNX) | annuaires glama.ai et lobehub.com | Dépôts non consultés directement ; le second est une copie de DroitFrancaisMCP. |
| LegalBench.PT, LEXam, GreekBarBench | arXiv et Hugging Face | Sujet hors périmètre : ces benchmarks ne comportent pas de données en français. |

## Contrôle HTTP des liens

Pendant la session de création, la politique réseau de l'environnement bloquait l'accès direct à la plupart des sites hors GitHub, Hugging Face, PyPI et npm : ces liens n'avaient été confirmés que par recherche web. La première exécution du workflow `liens.yml` (2026-11-02) les a contrôlés directement : 88 liens sur 89 répondaient. Le seul en échec, `https://guides.etalab.gouv.fr/pseudonymisation/`, pointe désormais vers les sources du guide sur GitHub, et l'entrée a rejoint les archives.

## Points de vigilance

- **LegalKit** : le pipeline `louisbrulenaudet/legalkit-pipeline` a atteint la limite des 24 mois le 2026-11-03. L'entrée pointe désormais vers les jeux Hugging Face de l'auteur (mis à jour jusqu'en septembre 2025), sans suivi d'activité GitHub.
- **dila-api-client** : dernier commit le 2024-11-12. Sans nouvelle activité, l'entrée devra passer dans les archives à partir du 2026-11-12.
- **Label** : le dépôt `Cour-de-cassation/label` est archivé, mais le développement continue dans `label-back` et `label-front` ; l'entrée a quitté les archives (2026-11-03).
- **Candidats confirmés seulement par recherche web** (données de l'Assemblée nationale et du Sénat, ArianeWeb, PISTE, simulateurs de Service-Public.fr, ressources de la CNIL, etc.) : à ajouter après un contrôle HTTP direct.
- **Corrections du 2026-11-02** (premier rapport hebdomadaire) : dépôts déplacés mis à jour (`jmtanguy/droit-francais-mcp`, `data-privacy-stack/presidio`, `publicodes/publicodes`, `LeMyst/Codes`) ; Label (dépôt archivé par la Cour de cassation) et le guide Etalab (dernier commit en mai 2024) déplacés dans les archives ; EDS-Pseudo (AP-HP) ajouté à la sous-section anonymisation.
- **justicelibre** : le dépôt GitHub `Dahliyaal/justicelibre` indique que son code n'est plus à jour et que le développement continue dans un dépôt privé. Seul le service en ligne est listé, sans l'étiquette « Open source ».
