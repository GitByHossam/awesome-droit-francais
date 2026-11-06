# Ressources à vérifier

Ce fichier recense les ressources candidates qui ne figurent **pas** dans le README, avec la raison de leur mise à l'écart. Une ressource ne rejoint `data/ressources.yml` qu'une fois vérifiée (URL fonctionnelle, description fidèle, licence et statut exacts).

Dernière mise à jour : 2026-11-06.

## Candidats écartés

| Ressource | Adresse examinée | Raison |
| --- | --- | --- |
| OpenLegi (Le Lab de dassignies.law) | `https://mcp.openlegi.fr/` | Ressource introuvable sur son propre site : seuls des annuaires tiers de serveurs MCP la décrivent. Les conditions de l'offre gratuite et la licence n'ont pas pu être confirmées. |
| Tricoteuses, forge Git | `https://git.tricoteuses.fr/` | Ressource introuvable : le domaine n'a pas répondu et aucune recherche n'a permis de confirmer son contenu. Les jeux de données Hugging Face de Tricoteuses sont, eux, vérifiés et listés. |
| Awesome Open Legal Switzerland | non trouvée | Ressource introuvable : aucune liste portant ce nom n'a été trouvée. La liste suisse « Awesome OGD Switzerland » (données publiques) est listée à la place. |
| Archéo Lex, site de présentation | `https://archeo-lex.fr/` | Lien non vérifié : le site n'a pas répondu et n'apparaît pas dans les résultats de recherche. Le dépôt GitHub du projet est listé dans les archives. |
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
- **Corrections du 2026-11-02** (premier rapport hebdomadaire) : dépôts déplacés mis à jour (`jmtanguy/droit-francais-mcp`, `data-privacy-stack/presidio`, `publicodes/publicodes`, `LeMyst/Codes`) ; Label (dépôt archivé par la Cour de cassation) et le guide Etalab (dernier commit en mai 2024) déplacés dans les archives ; EDS-Pseudo (AP-HP) ajouté à la sous-section anonymisation.
- **justicelibre** : le dépôt GitHub `Dahliyaal/justicelibre` indique que son code n'est plus à jour et que le développement continue dans un dépôt privé. Seul le service en ligne est listé, sans l'étiquette « Open source ».

## Candidats en attente d'un contrôle HTTP

Ces adresses ne figurent pas encore dans la liste. L'étape « Contrôler les URL candidates de A_VERIFIER.md » de `liens.yml` les teste à chaque passage ; son rapport paraît dans le résumé de l'exécution (onglet Summary), jamais dans l'issue hebdomadaire. Une entrée ne rejoint `data/ressources.yml` qu'avec un code 2xx, et sa ligne quitte alors ce tableau. Un 403 ou un 429 ne prouve rien : ouvrir la page dans un navigateur et noter le résultat dans la colonne « Remarque ». Les variantes servent à choisir l'adresse canonique, en lisant la section « Redirects » du rapport.

### Candidats du premier rapport et corrections du 2026-11-03

| Identifiant prévu | Adresse à contrôler | Remarque |
| --- | --- | --- |
| infocuria | `https://infocuria.curia.europa.eu/` | nouveau moteur de la CJUE (janvier 2026) |
| infocuria (variante) | `https://infocuria.curia.europa.eu/tabs/affair?lang=fr` | recherche par affaire |
| simulateur-aide-juridictionnelle | `https://www.aidejuridictionnelle.justice.fr/simulateur` | adresse citée par justice.fr |
| fiches-ia-cnil | `https://www.cnil.fr/fr/les-fiches-pratiques-ia` | adresse citée par la CNIL |
| fiches-ia-cnil (variante) | `https://www.cnil.fr/fr/developpement-des-systemes-dia-les-recommandations-de-la-cnil-pour-respecter-le-rgpd` | page indexée |
| objectif-ia | `https://openclassrooms.com/fr/courses/6417031-objectif-ia-initiez-vous-a-l-intelligence-artificielle` | |
| objectif-ia (variante) | `https://openclassrooms.com/us/courses/6417031-objectif-ia-initiez-vous-a-l-intelligence-artificielle` | seule variante indexée |
| justice-pension-alimentaire (proposée) | `https://www.justice.fr/fiche/simulateur-calcul-pension-alimentaire` | |
| justice-pension-alimentaire (fusionnée le 2026-11-03) | `https://www.justice.fr/simulateurs/pensions-alimentaire` | |
| justice-pension-alimentaire (avant le 2026-11-03) | `https://www.justice.fr/fiche/simulateur-calcul-pension-alimentaire-simulateur` | |
| inc-lettres-types (proposée) | `https://www.inc-conso.fr/content/modeles-de-lettres-pour-regler-vos-litiges` | |
| inc-lettres-types (fusionnée le 2026-11-03) | `https://www.inc-conso.fr/content/lettres-types-pour-regler-vos-litiges` | |
| inc-lettres-types (avant le 2026-11-03) | `https://www.inc-conso.fr/content/150-lettres-types-pour-r%C3%A9gler-vos-litiges` | |
| inc-revision-loyer (proposée, adresse d'avant le 2026-11-03) | `https://www.inc-conso.fr/content/calculez-laugmentation-de-votre-loyer-0` | |
| inc-revision-loyer (fusionnée le 2026-11-03) | `https://www.inc-conso.fr/content/logement/calculez-laugmentation-de-votre-loyer` | |
| guide-juridique-open-data (ancienne) | `https://guides.data.gouv.fr/guides-open-data/guide-juridique` | pour information ; l'entrée utilise `/guides/` |
| adij (ancienne) | `https://www.adij.fr/` | pour information ; l'entrée utilise adij.legal |

### Nouveaux domaines du droit (recherche du 2026-11-06)

| Identifiant prévu | Adresse à contrôler | Remarque |
| --- | --- | --- |
| api-bodacc | `https://www.data.gouv.fr/dataservices/672cf66ea47b8d4c15d13d5b` | fiche de l'API |
| data-inpi | `https://data.inpi.fr/` | |
| decisions-autorite-concurrence | `https://www.data.gouv.fr/datasets/decisions-publiees-par-lautorite-de-la-concurrence-depuis-1988` | |
| api-boamp | `https://www.data.gouv.fr/datasets/587ccbcd88ee382c669b81a4` | préférer la fiche de l'API si elle existe |
| colibre | `https://colibre.fr/` | nouveau nom de decp.info (2026) |
| daj-commande-publique | `https://www.economie.gouv.fr/daj/marches-publics/conseil-aux-acheteurs-et-autorites-concedantes` | site refondu fin 2025 |
| regafi | `https://www.regafi.fr/` | |
| amf-sanctions | `https://www.amf-france.org/fr/sanctions-transactions/sanctions-et-transactions-accueil` | |
| pibd | `https://pibd.inpi.fr/` | |
| pibd (variante) | `https://www.inpi.fr/propriete-intellectuelle-bulletin-documentaire-pibd` | si la racine ne répond pas |
| avis-cada | `https://www.data.gouv.fr/datasets/avis-et-conseils-de-la-cada` | |
| opendata-hatvp | `https://www.hatvp.fr/open-data/` | |
| defenseur-des-droits-juridique | `https://juridique.defenseurdesdroits.fr/` | |
| banatic | `https://www.banatic.interieur.gouv.fr/` | |
| banatic (variante) | `https://banatic.interieur.gouv.fr/` | sans www |
| api-carto-gpu | `https://www.data.gouv.fr/dataservices/api-carto-module-geoportail-de-lurbanisme-gpu` | |
| api-carto-gpu (variante) | `https://apicarto.ign.fr/api/doc/gpu` | documentation servie par le code |
| envergo | `https://envergo.beta.gouv.fr/` | |
| aida-ineris | `https://aida.ineris.fr/` | |
| api-georisques | `https://www.data.gouv.fr/dataservices/api-georisques` | |
| juricaf | `https://juricaf.org/` | |
| hudoc-esc | `https://hudoc.esc.coe.int/fre` | adresse déduite du modèle de HUDOC |
| joafe-opendata | `https://www.data.gouv.fr/datasets/associations-joafe` | |
| egapro | `https://egapro.travail.gouv.fr/` | racine déduite du lien du simulateur |
| conventions-collectives-siret | `https://www.data.gouv.fr/datasets/liste-des-conventions-collectives-par-entreprise-siret` | |
| simulateur-impot-revenu | `https://simulateur-ir-ifi.impots.gouv.fr/calcul_impot/2026/` | |
| simulateur-impot-revenu (variante) | `https://simulateur-ir-ifi.impots.gouv.fr/calcul_impot/2026/simplifie/index.htm` | page indexée |
| pia-cnil | `https://www.cnil.fr/fr/outil-pia-telechargez-et-installez-le-logiciel-de-la-cnil` | lien du README de LINCnil/pia |
| pia-cnil (variante) | `https://www.cnil.fr/fr/PIA-privacy-impact-assessment` | |
| guide-rgpd-developpeur | `https://www.cnil.fr/fr/le-guide-rgpd-du-developpeur` | entrée destinée aux archives |
| natinf | `https://www.data.gouv.fr/datasets/liste-des-infractions-en-vigueur-de-la-nomenclature-natinf` | |
| rappelconso | `https://www.data.gouv.fr/datasets/rappelconso-v2-rappels-de-produits` | |
| mediateurs-consommation | `https://data.economie.gouv.fr/explore/dataset/annuaire-des-mediateurs-de-la-consommation/` | |
| mediateurs-consommation (variante) | `https://data.economie.gouv.fr/explore/assets/mediation-consommation-annuaire-des-mediateurs/` | page plus récente |
| dvf-explorateur | `https://explore.data.gouv.fr/fr/immobilier` | |
| dvf-explorateur (variante) | `https://app.dvf.etalab.gouv.fr/` | application d'Etalab |
