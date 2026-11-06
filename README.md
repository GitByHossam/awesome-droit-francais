<!-- Fichier généré par scripts/generer_readme.py. Modifiez data/ressources.yml. -->
# Awesome Droit Français [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Ressources numériques pour le droit français : sources officielles, données ouvertes, outils libres, IA juridique, modèles, calculateurs, formations et communautés.

Cette liste s'adresse aux juristes français (avocats, juristes d'entreprise, étudiants, chercheurs) et aux développeurs qui construisent des outils pour eux.
Son objectif est de retrouver en un seul endroit des ressources vérifiées, décrites simplement et classées par usage.
Elle ne constitue ni un conseil juridique ni un annuaire commercial : vérifiez toujours un texte ou une décision sur sa source officielle.

## Sommaire

- [Sources officielles et API publiques][sources-officielles]
- [Données juridiques réutilisables][donnees]
- [Bibliothèques et clients d'API][bibliotheques]
  - [Python][bibliotheques-python]
  - [JavaScript et autres langages][bibliotheques-js]
- [IA juridique][ia]
  - [Serveurs MCP][ia-mcp]
  - [Modèles et embeddings][ia-modeles]
  - [Benchmarks et évaluation][ia-benchmarks]
  - [Anonymisation et pseudonymisation][ia-anonymisation]
- [Modèles de documents et automatisation][modeles-documents]
- [Calculateurs et simulateurs][calculateurs]
- [Outils publics et droit codé][droit-code]
- [Apprendre][]
- [Communautés, événements et veille][communautes]
- [Listes sœurs][listes-soeurs]
- [Projets archivés ou non maintenus][archives]
- [Contribuer][]
- [Licence du contenu][licence-du-contenu]

[sources-officielles]: #sources-officielles-et-api-publiques
[donnees]: #données-juridiques-réutilisables
[bibliotheques]: #bibliothèques-et-clients-dapi
[bibliotheques-python]: #python
[bibliotheques-js]: #javascript-et-autres-langages
[ia]: #ia-juridique
[ia-mcp]: #serveurs-mcp
[ia-modeles]: #modèles-et-embeddings
[ia-benchmarks]: #benchmarks-et-évaluation
[ia-anonymisation]: #anonymisation-et-pseudonymisation
[modeles-documents]: #modèles-de-documents-et-automatisation
[calculateurs]: #calculateurs-et-simulateurs
[droit-code]: #outils-publics-et-droit-codé
[apprendre]: #apprendre
[communautes]: #communautés-événements-et-veille
[listes-soeurs]: #listes-sœurs
[archives]: #projets-archivés-ou-non-maintenus
[contribuer]: #contribuer
[licence-du-contenu]: #licence-du-contenu

## Légende des étiquettes

Les étiquettes figurent entre crochets au début de chaque description.

- \[Gratuit\] : accès gratuit.
- \[Open source\] : code publié sous licence libre.
- \[Inscription\] : inscription requise, par exemple sur le portail PISTE.
- \[IA\] : ressource pensée pour l'IA (serveur MCP, jeu de données d'entraînement ou d'évaluation, modèle, API destinée aux agents).
- \[Python\] et \[JavaScript\] : bibliothèque ou outil écrit dans ce langage.
- \[Freemium\] : offre commerciale qui comporte une partie gratuite.
- \[Non maintenu\] : projet inactif depuis plus de 24 mois, à utiliser avec prudence.

## Sources officielles et API publiques

Portails et API de l'État et des institutions européennes pour accéder aux textes et à la jurisprudence.

- [AIDA (INERIS)](https://aida.ineris.fr/) - \[Gratuit\] Consultez les textes français et européens sur les installations classées, l'eau, la nature et le littoral, dont la nomenclature ICPE et les arrêtés de prescriptions par rubrique.
- [Annonces des associations (JOAFE), open data de la DILA](https://www.data.gouv.fr/datasets/associations-joafe) - \[Gratuit\] Téléchargez chaque semaine, en XML, les annonces du Journal officiel des associations et fondations d'entreprise parues depuis 1985, pour suivre la vie d'une association.
- [API BOAMP](https://www.data.gouv.fr/datasets/api-boamp) - \[Gratuit\] Recherchez par programme les avis d'appel public à la concurrence et les avis d'attribution publiés au BOAMP, mis à jour deux fois par jour ; API Opendatasoft de la DILA en accès libre.
- [API BODACC](https://www.data.gouv.fr/dataservices/api-bulletin-officiel-des-annonces-civiles-et-commerciales-bodacc) - \[Gratuit\] Interrogez sans clé les annonces du BODACC (immatriculations, ventes de fonds, procédures collectives, dépôts de comptes) par SIREN, type d'avis ou date, via l'API Opendatasoft de la DILA.
- [API Carto, module Géoportail de l'urbanisme (IGN)](https://www.data.gouv.fr/dataservices/api-carto-module-geoportail-de-lurbanisme-gpu) - \[Gratuit\] \[Open source\] Récupérez sans clé, à partir d'une géométrie ou d'un document, les zonages, prescriptions et servitudes d'utilité publique des PLU et cartes communales du Géoportail de l'urbanisme.
- [API Géorisques](https://www.data.gouv.fr/dataservices/api-georisques) - \[Gratuit\] Interrogez par programme les risques naturels et technologiques recensés par Géorisques pour un lieu donné, dont le rapport de risques ; documentation Swagger, quotas d'appels.
- [API Judilibre](https://www.data.gouv.fr/dataservices/api-judilibre) - \[Gratuit\] \[Inscription\] Recherchez dans les décisions pseudonymisées de la Cour de cassation et des juridictions judiciaires, avec leurs métadonnées (ECLI, chambre, solution) ; accès via PISTE.
- [API Légifrance](https://www.legifrance.gouv.fr/contenu/pied-de-page/open-data-et-api) - \[Gratuit\] \[Inscription\] Interrogez par programme les fonds de Légifrance (codes, textes, JORF, jurisprudence) avec des identifiants OAuth obtenus gratuitement sur le portail PISTE.
- [API Recherche d'entreprises](https://recherche-entreprises.api.gouv.fr/) - \[Gratuit\] \[Open source\] API publique sans clé pour retrouver une société par nom ou SIREN et obtenir ses dirigeants, établissements et statut ; quotas d'appels à respecter.
- [ArianeWeb (Conseil d'État)](https://www.conseil-etat.fr/arianeweb/#/recherche) - \[Gratuit\] Recherche dans les décisions marquantes du Conseil d'État et des cours administratives d'appel, avec analyses et une sélection de conclusions des rapporteurs publics.
- [Avis et conseils de la CADA](https://www.data.gouv.fr/datasets/avis-et-conseils-de-la-cada) - \[Gratuit\] Téléchargez en CSV les avis et conseils anonymisés de la CADA sur l'accès aux documents administratifs, complets depuis fin 2012 ; recherche en ligne sur cada.data.gouv.fr.
- [BANATIC (base nationale sur l'intercommunalité)](https://www.banatic.interieur.gouv.fr/) - \[Gratuit\] Identifiez quel EPCI ou syndicat exerce une compétence sur une commune : périmètres, compétences et financement des groupements, exportables par région ou département.
- [Cellar, point d'accès SPARQL (EUR-Lex)](https://op.europa.eu/en/advanced-sparql-query-editor) - \[Gratuit\] Interrogation en SPARQL des métadonnées du droit de l'Union qui alimentent EUR-Lex, pour construire des extractions ciblées. Interface en anglais.
- [data.gouv.fr](https://www.data.gouv.fr/) - \[Gratuit\] Plateforme nationale des données publiques ; elle présente les bases juridiques (LEGI, KALI, CASS, JADE) et les outils qui les réutilisent.
- [Décisions de l'Autorité de la concurrence (open data)](https://www.data.gouv.fr/datasets/decisions-publiees-par-lautorite-de-la-concurrence-depuis-1988) - \[Gratuit\] Texte intégral des décisions contentieuses, avis, mesures conservatoires et décisions de concentration publiés depuis 1988, en français et en partie en anglais ; copie Parquet sur Hugging Face.
- [Décisions du Conseil constitutionnel](https://www.conseil-constitutionnel.fr/les-decisions) - \[Gratuit\] Retrouvez les décisions DC et QPC du Conseil grâce à une recherche experte, avec les commentaires officiels et les tables analytiques.
- [Documentation juridique du Défenseur des droits](https://juridique.defenseurdesdroits.fr/) - \[Gratuit\] Recherchez en texte intégral ou par numéro les décisions, avis et recommandations du Défenseur des droits, ainsi que les textes de la HALDE, de la CNDS et du Défenseur des enfants.
- [EUR-Lex](https://eur-lex.europa.eu/homepage.html?locale=fr) - \[Gratuit\] Accès officiel au droit de l'Union européenne : Journal officiel de l'UE, traités, actes consolidés et jurisprudence, dans les 24 langues officielles.
- [HUDOC](https://hudoc.echr.coe.int/FRE) - \[Gratuit\] Base de la Cour européenne des droits de l'homme : arrêts, décisions et résumés juridiques, consultables en français et filtrables par mots-clés.
- [HUDOC-ESC (Charte sociale européenne)](https://hudoc.esc.coe.int/fre) - \[Gratuit\] Recherchez en français les décisions sur réclamations collectives et les conclusions du Comité européen des droits sociaux, qui contrôle l'application de la Charte sociale européenne.
- [InfoCuria (CJUE)](https://infocuria.curia.europa.eu/) - \[Gratuit\] Moteur de recherche de la CJUE, refondu en janvier 2026, dans les arrêts, conclusions, ordonnances et résumés de la Cour de justice et du Tribunal, en français.
- [Judilibre, moteur de recherche](https://www.courdecassation.fr/recherche-judilibre) - \[Gratuit\] Moteur de recherche gratuit des décisions pseudonymisées de la Cour de cassation, des cours d'appel et d'autres juridictions judiciaires, alimenté par l'API Judilibre.
- [Juricaf](https://juricaf.org/) - \[Gratuit\] \[Open source\] Recherchez dans les décisions des cours suprêmes de pays francophones, dont la France, et de juridictions comme la CCJA de l'OHADA, pour comparer les solutions retenues.
- [Légifrance](https://www.legifrance.gouv.fr/) - \[Gratuit\] Point d'entrée officiel pour consulter les codes et lois consolidés, le Journal officiel, les conventions collectives et la jurisprudence.
- [Open data de l'Assemblée nationale](https://data.assemblee-nationale.fr/) - \[Gratuit\] Téléchargement des données de l'Assemblée nationale (dossiers législatifs, amendements, scrutins, députés) en XML, JSON ou CSV pour suivre la procédure législative.
- [Open data de la DILA](https://echanges.dila.gouv.fr/OPENDATA/) - \[Gratuit\] Serveur qui met à disposition les archives XML des bases LEGI, JORF, KALI, CNIL, JADE, CASS, CONSTIT et d'autres, avec des mises à jour incrémentales.
- [Open data de la HATVP](https://www.hatvp.fr/open-data/) - \[Gratuit\] Téléchargez les déclarations d'intérêts et de patrimoine publiées des responsables publics (XML, CSV) et, sur une page voisine, le répertoire des représentants d'intérêts (JSON, CSV).
- [Open data de la justice administrative](https://opendata.justice-administrative.fr/) - \[Gratuit\] Téléchargez en XML les décisions du Conseil d'État, des cours administratives d'appel et des tribunaux administratifs, regroupées par juridiction et par mois.
- [Open data du Sénat](https://data.senat.fr/) - \[Gratuit\] Bases du Sénat (dossiers législatifs Dosleg, amendements Ameli, questions, comptes rendus) téléchargeables pour analyser le travail parlementaire.
- [PISTE](https://piste.gouv.fr/) - \[Gratuit\] \[Inscription\] Portail de l'État où créer un compte et des identifiants OAuth pour appeler les API Légifrance et Judilibre, avec un environnement de test (bac à sable).
- [Regafi.fr (ACPR)](https://www.regafi.fr/) - \[Gratuit\] Registre public de l'ACPR pour vérifier qu'une banque, un établissement de paiement, une entreprise d'investissement ou un assureur est autorisé en France, et pour quelles activités.
- [Sanctions et transactions de l'AMF](https://www.amf-france.org/fr/sanctions-transactions/sanctions-et-transactions-accueil) - \[Gratuit\] Décisions de la Commission des sanctions de l'AMF et transactions homologuées, filtrables par thème, personne et date ; les montants affichés sont ceux fixés avant un éventuel recours.
- [Service-Public.fr](https://www.service-public.fr/) - \[Gratuit\] Fiches pratiques de l'administration qui expliquent les droits et démarches des particuliers et des entreprises, avec les références des textes.

## Données juridiques réutilisables

Extractions, dépôts Git et jeux de données prêts à l'emploi, construits à partir des données publiques.

- [Annuaire des médiateurs de la consommation](https://data.economie.gouv.fr/explore/assets/mediation-consommation-annuaire-des-mediateurs/) - \[Gratuit\] Médiateurs de la consommation référencés par la CECMC, avec coordonnées, catégorie et secteurs couverts ; sert à trouver le médiateur compétent ou à vérifier un référencement.
- [ArGiMi French Jurisprudence](https://huggingface.co/datasets/artefactory/Argimi-Legal-French-Jurisprudence) - \[Gratuit\] \[IA\] Décisions constitutionnelles, administratives et judiciaires découpées en segments, utiles pour construire un moteur de recherche ou un système RAG.
- [BOFiP-Impôts, publications en vigueur](https://www.data.gouv.fr/datasets/bofip-impots-publications-en-vigueur) - \[Gratuit\] Export en CSV et JSON de la doctrine fiscale administrative en vigueur (BOFiP-Impôts), publié par les ministères économiques et financiers, pour la recherche ou la veille fiscale.
- [Codes en Markdown (LeMyst)](https://github.com/LeMyst/Codes) - \[Gratuit\] Dix-huit codes rangés en un fichier Markdown par article, mis à jour par commits réguliers : l'historique Git montre chaque modification.
- [colibre (ex-decp.info)](https://colibre.fr/) - \[Open source\] \[Freemium\] Explorez, filtrez et téléchargez en Excel ou CSV les marchés publics attribués (DECP consolidées) par acheteur, titulaire ou objet ; l'API et le connecteur IA sont réservés aux abonnés.
- [CONSTIT vectorisé (MediaTech, AgentPublic)](https://huggingface.co/datasets/AgentPublic/constit) - \[Gratuit\] \[IA\] Décisions du Conseil constitutionnel issues de la base CONSTIT de la DILA, découpées et vectorisées pour la recherche sémantique.
- [Conventions collectives par entreprise (SIRET)](https://www.data.gouv.fr/datasets/liste-des-conventions-collectives-par-entreprise-siret) - \[Gratuit\] Fichier du ministère du Travail qui associe chaque établissement (SIRET) aux conventions collectives (IDCC) déclarées en DSN, pour repérer la convention applicable ; décalage de quelques mois.
- [Délibérations CNIL vectorisées (MediaTech, AgentPublic)](https://huggingface.co/datasets/AgentPublic/cnil) - \[Gratuit\] \[IA\] Délibérations de la CNIL issues de l'open data de la DILA, découpées et vectorisées, pour interroger la doctrine en protection des données.
- [Dossiers législatifs DOLE vectorisés (MediaTech, AgentPublic)](https://huggingface.co/datasets/AgentPublic/dole) - \[Gratuit\] \[IA\] Dossiers législatifs de la base DOLE (exposés des motifs, étapes de la procédure) découpés et vectorisés, pour retracer la genèse d'une loi.
- [Jurisprudence (antoinejeannot)](https://huggingface.co/datasets/antoinejeannot/jurisprudence) - \[Gratuit\] \[Open source\] \[IA\] Plus d'un million de décisions judiciaires récupérées via Judilibre jusqu'en mars 2025, en JSONL et Parquet, pour l'analyse ou l'entraînement de modèles ; collecte arrêtée depuis.
- [LegalKit (jeux Hugging Face)](https://huggingface.co/louisbrulenaudet) - \[Gratuit\] \[Open source\] \[IA\] \[Python\] Jeux de données Hugging Face, un par code français, mis à jour jusqu'en septembre 2025 ; le pipeline qui les produit n'a plus de commit depuis novembre 2024.
- [LEGI vectorisé (MediaTech, AgentPublic)](https://huggingface.co/datasets/AgentPublic/legi) - \[Gratuit\] \[IA\] Codes, lois et décrets consolidés de LEGI découpés par article et vectorisés (bge-m3) par la DINUM, pour une recherche sémantique ou un RAG. Jeux voisins : CNIL, CONSTIT, DOLE.
- [Nomenclature NATINF des infractions](https://www.data.gouv.fr/datasets/liste-des-infractions-en-vigueur-de-la-nomenclature-natinf) - \[Gratuit\] Liste des infractions en vigueur tenue par le ministère de la Justice : code NATINF, libellé, nature et articles qui définissent et répriment chaque infraction ; mise à jour trimestrielle.
- [Open Terms Archive, collection France](https://github.com/OpenTermsArchive/france-versions) - \[Gratuit\] \[Open source\] Dépôt Git des versions successives des CGU et politiques de confidentialité de services en ligne utilisés en France, relevées toutes les 12 heures depuis 2022 ; utile pour dater une clause.
- [RappelConso, rappels de produits](https://www.data.gouv.fr/datasets/rappelconso-v2-rappels-de-produits) - \[Gratuit\] Fiches de rappel de produits publiées sur RappelConso par la DGCCRF et d'autres administrations, en CSV, JSON et API ; utile en droit de la consommation et de la sécurité des produits.
- [Tricoteuses LEGI](https://huggingface.co/datasets/Tricoteuses/LEGI) - \[Gratuit\] Articles de la base LEGI en vigueur au 6 avril 2025, convertis en tableau avec leurs dates et identifiants ; le même éditeur publie aussi les bases CNIL et CAPP.

## Bibliothèques et clients d'API

Code réutilisable pour interroger les API juridiques ou exploiter les bases de la DILA.

### Python

- [echr-extractor](https://github.com/maastrichtlawtech/echr-extractor) - \[Gratuit\] \[Open source\] \[Python\] Bibliothèque Python qui télécharge depuis HUDOC les métadonnées et le texte intégral des arrêts de la CEDH, y compris en français, en CSV, JSON ou DataFrame ; documentation en anglais.
- [eurlex (Python)](https://github.com/kevin91nl/eurlex) - \[Gratuit\] \[Open source\] \[Python\] Bibliothèque Python qui télécharge un acte EUR-Lex par son numéro CELEX et le découpe en tableau Pandas, article par article ; documentation en anglais.
- [legi.py](https://github.com/Legilibre/legi.py) - \[Gratuit\] \[Open source\] \[Python\] Construit et tient à jour une base SQLite à partir des archives LEGI, en reliant entre elles les versions successives d'un texte.
- [pyjudilibre](https://github.com/pauldechorgnat/pyjudilibre) - \[Gratuit\] \[Open source\] \[Inscription\] \[Python\] Client Python de l'API Judilibre pour rechercher et récupérer des décisions de justice ; nécessite des identifiants PISTE, documentation en anglais.
- [pylegifrance](https://github.com/pylegifrance/pylegifrance) - \[Gratuit\] \[Open source\] \[Inscription\] \[Python\] Fonctions Python prêtes à l'emploi pour chercher dans les codes, les lois et décrets ou la jurisprudence judiciaire via l'API Légifrance.
- [pynsee](https://github.com/InseeFrLab/pynsee) - \[Gratuit\] \[Open source\] \[Inscription\] \[Python\] Paquet Python d'InseeFrLab pour les API de l'Insee, dont Sirene (recherche d'entreprises et d'établissements par critères) ; la partie Sirene exige une clé gratuite du portail API de l'Insee.
- [python-epo-ops-client](https://github.com/ip-tools/python-epo-ops-client) - \[Gratuit\] \[Open source\] \[Inscription\] \[Python\] Client Python d'Open Patent Services (OEB) : bibliographie, familles, statut juridique et registre des brevets FR et EP ; clés OPS gratuites jusqu'à 4 Go par semaine, documentation en anglais.

### JavaScript et autres langages

- [@socialgouv/fiches-travail-data](https://github.com/SocialGouv/fiches-travail-data) - \[Gratuit\] \[Open source\] \[JavaScript\] Paquet npm qui fournit en JSON les fiches pratiques du droit du travail du site travail-emploi.gouv.fr, republiées automatiquement ; documentation succincte en anglais.
- [@socialgouv/fiches-vdd](https://github.com/SocialGouv/fiches-vdd) - \[Gratuit\] \[Open source\] \[JavaScript\] Paquet npm qui fournit en JSON les fiches Vos droits et démarches de Service-Public.fr, mises à jour chaque jour ; environ 500 Mo de données.
- [dila-api-client](https://github.com/SocialGouv/dila-api-client) - \[Gratuit\] \[Open source\] \[Inscription\] \[JavaScript\] Client Node.js qui gère l'authentification OAuth et les appels à l'API Légifrance de la DILA.
- [eurlex (R)](https://michalovadek.github.io/eurlex/) - \[Gratuit\] \[Open source\] Paquet R pour interroger EUR-Lex et le dépôt Cellar et récupérer actes, métadonnées et textes de l'UE sous forme de tableaux ; documentation en anglais.
- [kali-data](https://github.com/SocialGouv/kali-data) - \[Gratuit\] \[Open source\] \[JavaScript\] Paquet npm qui rassemble en JSON les conventions collectives extraites de l'API DILA ; projet expérimental, réservé par ses auteurs à un usage interne.
- [legi-data](https://github.com/SocialGouv/legi-data) - \[Gratuit\] \[Open source\] \[JavaScript\] Paquet npm qui fournit en JSON quatre codes (travail, sécurité sociale, rural, relations public-administration) avec une API TypeScript ; réservé par ses auteurs à un usage interne expérimental.
- [Legifrance Integration (Obsidian)](https://github.com/carnetdethese/legifrance-integration) - \[Gratuit\] \[Open source\] \[Inscription\] Plugin Obsidian qui interroge l'API Légifrance, repère les textes et décisions cités dans vos notes et en conserve le texte ; identifiants PISTE requis.

## IA juridique

Ressources pour brancher des assistants IA sur le droit français, entraîner ou évaluer des modèles et protéger les données personnelles.

### Serveurs MCP

- [data.gouv.fr MCP](https://github.com/datagouv/datagouv-mcp) - \[Gratuit\] \[Open source\] \[IA\] Serveur MCP officiel qui laisse un assistant IA chercher et analyser les jeux de données de data.gouv.fr ; une instance publique fonctionne sans compte.
- [DroitFrancaisMCP](https://github.com/jmtanguy/droit-francais-mcp) - \[Gratuit\] \[Open source\] \[Inscription\] \[IA\] \[Python\] Serveur MCP expérimental, à installer soi-même, qui interroge Légifrance et Judilibre avec vos propres identifiants PISTE.
- [EUR-Lex MCP Server](https://github.com/cyanheads/eur-lex-mcp-server) - \[Gratuit\] \[Open source\] \[IA\] \[JavaScript\] Serveur MCP qui permet à un assistant IA de chercher et lire les actes de l'UE et la jurisprudence de la CJUE sur EUR-Lex. Documentation en anglais.
- [eurlex-mcp-server](https://github.com/Honeyfield-Org/eurlex-mcp-server) - \[Gratuit\] \[Open source\] \[IA\] \[JavaScript\] Serveur MCP sans clé d'API pour interroger EUR-Lex : textes consolidés, arrêts de la CJUE et mesures nationales de transposition, en français. Documentation en anglais.
- [justicelibre](https://justicelibre.org/) - \[Gratuit\] \[IA\] Serveur MCP hébergé qui interroge la jurisprudence française et européenne (CEDH, CJUE), les codes et la doctrine administrative ; la recherche fonctionne sans compte.
- [LibreJustice](https://librejustice.fr/) - \[Gratuit\] \[Open source\] \[Inscription\] \[IA\] Moteur de recherche libre reliant jurisprudence française et européenne et textes consolidés, interrogeable en ligne, par API (clé gratuite) ou par un serveur MCP.
- [mcp-inpi-pi](https://github.com/guix77/mcp-inpi-pi) - \[Gratuit\] \[Open source\] \[Inscription\] \[IA\] \[JavaScript\] Serveur MCP non officiel qui cherche les marques françaises, de l'UE et internationales via l'API de l'INPI et fournit la classification de Nice ; compte API data.inpi.fr gratuit requis.
- [mcp-server-legifrance](https://github.com/pylegifrance/mcp-server-legifrance) - \[Gratuit\] \[Open source\] \[Inscription\] \[IA\] \[Python\] Serveur MCP expérimental pour rechercher lois, articles de code et jurisprudence judiciaire ; il demande une clé délivrée par le Lab de dassignies.

### Modèles et embeddings

- [JuriBERT](https://huggingface.co/dascim/juribert-base) - \[Gratuit\] \[IA\] Famille de modèles BERT (de 6 à 110 millions de paramètres) entraînés sur des textes de Légifrance et de la Cour de cassation, à affiner pour classer ou extraire.
- [Lemone-embed](https://huggingface.co/louisbrulenaudet/lemone-embed-pro) - \[Gratuit\] \[IA\] Famille de modèles d'embeddings spécialisés en fiscalité française (variantes s, m, l et pro), pour la recherche sémantique dans le CGI et la doctrine fiscale.
- [Rapprochements de sommaires (Cour de cassation)](https://huggingface.co/datasets/Cour-de-cassation/ccass_rapprochements_sommaires_with_sources) - \[Gratuit\] \[IA\] Paires de sommaires d'arrêts jugés similaires, publiées par la Cour de cassation pour entraîner ou évaluer des modèles de recherche sémantique.
- [Romulus](https://huggingface.co/louisbrulenaudet/Romulus-cpt-Llama-3.1-8B-v0.1-Instruct) - \[Gratuit\] \[IA\] Llama 3.1 8B dont l'entraînement a été prolongé sur du droit français ; c'est une base à affiner, non alignée pour produire directement des réponses.
- [Titrage et sommaires (Cour de cassation)](https://huggingface.co/datasets/Cour-de-cassation/alpaca_ccass_motivations_sommaires_titres) - \[Gratuit\] \[IA\] Exemples au format Alpaca publiés par la Cour de cassation pour entraîner un modèle à produire le titrage et le sommaire d'un arrêt à partir de sa motivation.

### Benchmarks et évaluation

- [BSARD](https://huggingface.co/datasets/maastrichtlawtech/bsard) - \[Gratuit\] \[IA\] Environ 1 100 questions de citoyens en français reliées par des juristes aux articles de loi belges pertinents, pour mesurer un moteur de recherche juridique.
- [LLeQA](https://huggingface.co/datasets/maastrichtlawtech/lleqa) - \[Gratuit\] \[Inscription\] \[IA\] Questions juridiques en français avec réponses d'experts et articles de loi belges, pour évaluer la génération de réponses ; accès sur demande sur Hugging Face.
- [MultiEURLEX](https://huggingface.co/datasets/coastalcph/multi_eurlex) - \[Gratuit\] \[IA\] 65 000 actes de l'UE en 23 langues, dont le français, étiquetés avec le thésaurus EuroVoc : un banc d'essai de classification multilingue.

### Anonymisation et pseudonymisation

- [EDS-Pseudo](https://github.com/aphp/eds-pseudo) - \[Gratuit\] \[Open source\] \[IA\] \[Python\] Modèle de l'AP-HP qui repère noms, adresses, dates ou numéros dans des textes en français ; conçu pour des documents médicaux, il sert de base pour pseudonymiser.
- [Label](https://github.com/Cour-de-cassation/label-back) - \[Gratuit\] \[Open source\] \[JavaScript\] Logiciel de la Cour de cassation pour relire et corriger les annotations de pseudonymisation des décisions avant publication. Interface dans le dépôt label-front.
- [Presidio](https://github.com/data-privacy-stack/presidio) - \[Gratuit\] \[Open source\] \[IA\] \[Python\] Boîte à outils de détection et de masquage de données personnelles ; prévue pour l'anglais par défaut, elle s'adapte au français avec un modèle linguistique adéquat.

## Modèles de documents et automatisation

Lettres types, formulaires et outils d'assemblage de documents.

- [Accord Project](https://accordproject.org/) - \[Gratuit\] \[Open source\] \[JavaScript\] Outils libres pour écrire des modèles de contrats qui associent texte, modèle de données et logique exécutable ; documentation en anglais.
- [Démarches et outils de Service-Public.fr](https://www.service-public.fr/particuliers/vosdroits/services-en-ligne-et-formulaires) - \[Gratuit\] Rubrique officielle qui réunit formulaires, simulateurs et modèles de lettres (démission, attestation sur l'honneur, plainte auprès du procureur).
- [Docassemble](https://docassemble.org/) - \[Gratuit\] \[Open source\] \[Python\] Plateforme libre d'entretiens guidés : elle ne pose que les questions utiles puis assemble un document DOCX ou PDF à partir des réponses.
- [Lettres types de l'INC](https://www.inc-conso.fr/content/modeles-de-lettres-pour-regler-vos-litiges) - \[Gratuit\] Modèles de lettres de l'Institut national de la consommation pour les litiges courants (banque, assurance, logement, santé), chacun avec un rappel des règles applicables.
- [Logiciel PIA (CNIL)](https://www.cnil.fr/fr/outil-pia-telechargez-et-installez-le-logiciel-de-la-cnil) - \[Gratuit\] \[Open source\] Logiciel libre de la CNIL qui guide la conduite et la rédaction d'une analyse d'impact relative à la protection des données (AIPD), avec des modèles d'analyse réutilisables.

## Calculateurs et simulateurs

Outils de calcul de délais, d'indemnités, d'intérêts et de loyers. Les résultats restent indicatifs.

- [Calcul de l'intérêt légal (justice.fr)](https://www.justice.fr/fiche/calcul-interet-legal) - \[Gratuit\] Fiche qui donne les taux semestriels de l'intérêt légal et la formule pour calculer soi-même les intérêts dus ; ce n'est pas un calculateur automatique.
- [Calcul de la révision du loyer (INC)](https://www.inc-conso.fr/content/calculez-laugmentation-de-votre-loyer-0) - \[Gratuit\] Calcule la hausse annuelle autorisée d'un loyer d'habitation à partir de l'indice de référence des loyers publié par l'Insee, pour les indices publiés depuis 2005.
- [Calculateur de délai d'appel en matière civile](https://www.simonnetavocat.fr/delai-pour-faire-appel-comment-le-calculer-automatiquement/) - \[Gratuit\] Calcule le dernier jour pour faire appel d'un jugement civil (un mois, quinze jours en référé) à partir de sa signification ; outil d'un cabinet d'avocats, à vérifier sur les textes.
- [Calculateur de délais de procédure pénale](https://www.simonnetavocat.fr/calculateur-delais-procedure-penale/) - \[Gratuit\] Outil gratuit publié par un cabinet d'avocats qui calcule l'échéance de délais de procédure pénale et cite l'article applicable ; à contrôler sur les textes.
- [Mon-entreprise (Urssaf)](https://mon-entreprise.urssaf.fr/simulateurs) - \[Gratuit\] \[Open source\] Simulateurs publics de cotisations et de revenus (salarié, indépendant, dirigeant) qui détaillent chaque étape du calcul ; le code est public.
- [Simulateur d'aide juridictionnelle](https://www.aidejuridictionnelle.justice.fr/simulateur) - \[Gratuit\] Simulateur du ministère de la Justice qui estime le droit à l'aide juridictionnelle et son taux de prise en charge selon les ressources et le patrimoine du foyer.
- [Simulateur de pension alimentaire (justice.fr)](https://www.justice.fr/fiche/simulateur-calcul-pension-alimentaire) - \[Gratuit\] Donne une estimation de la pension alimentaire selon les revenus, le nombre d'enfants et le mode de garde, résidence alternée comprise ; seul le juge fixe le montant.
- [Simulateur des droits de succession](https://www.service-public.gouv.fr/simulateur/calcul/droits-succession) - \[Gratuit\] Simulateur officiel qui estime les droits de succession à payer selon le lien de parenté, la part reçue et les dettes du défunt, hors frais de notaire.
- [Simulateurs du Code du travail numérique](https://code.travail.gouv.fr/outils) - \[Gratuit\] Estimations officielles de l'indemnité de licenciement, de la durée du préavis, de l'indemnité de rupture conventionnelle ou du salaire net.

## Outils publics et droit codé

Services publics numériques et langages qui traduisent des règles juridiques en programmes.

- [@socialgouv/modeles-social](https://github.com/SocialGouv/code-du-travail-numerique/tree/dev/packages/code-du-travail-modeles) - \[Gratuit\] \[Open source\] \[JavaScript\] Règles Publicodes des simulateurs du Code du travail numérique (préavis, indemnités de licenciement, de précarité, de départ à la retraite), avec des variantes par convention ; pas de README dédié.
- [Catala](https://catala-lang.org/) - \[Gratuit\] \[Open source\] Langage de programmation de l'Inria qui annote un texte de loi avec sa traduction en code, pensé pour un travail en binôme juriste et développeur.
- [Code du travail numérique](https://code.travail.gouv.fr/) - \[Gratuit\] \[Open source\] Service public qui répond aux questions de droit du travail en tenant compte de la convention collective applicable ; son code source est ouvert.
- [Egapro (index de l'égalité professionnelle)](https://egapro.travail.gouv.fr/) - \[Gratuit\] \[Open source\] Service du ministère du Travail pour calculer, déclarer et consulter l'index de l'égalité femmes-hommes des entreprises ; refonte en cours pour la directive (UE) 2023/970.
- [EnvErgo](https://envergo.beta.gouv.fr/) - \[Gratuit\] \[Open source\] Simulez sans compte si un projet de construction ou d'aménagement relève de la loi sur l'eau, de Natura 2000 ou de l'évaluation environnementale ; résultat indicatif.
- [Exemples Catala](https://github.com/CatalaLang/catala-examples) - \[Gratuit\] \[Open source\] Programmes Catala qui traduisent des textes français (allocations familiales, aides au logement, impôt sur le revenu) en code exécutable et testé ; documentation en anglais.
- [Explorateur DVF (valeurs foncières)](https://explore.data.gouv.fr/fr/immobilier) - \[Gratuit\] \[Open source\] Carte et tableaux des ventes immobilières des cinq dernières années (DVF, DGFiP) à la parcelle, avec export ; repère de prix, hors Alsace-Moselle et Mayotte. Réidentification interdite.
- [LexImpact (Assemblée nationale)](https://leximpact.an.fr/) - \[Gratuit\] Simulateurs de l'Assemblée nationale, fondés sur OpenFisca, qui chiffrent l'effet de réformes fiscales et sociales (PLF, PLFSS) sur des foyers types ; impact budgétaire en accès restreint.
- [Mlang](https://github.com/MLanguage/mlang) - \[Gratuit\] \[Open source\] Compilateur et interpréteur du langage M, dans lequel la DGFiP écrit le calcul de l'impôt sur le revenu ; permet d'exécuter les sources M publiées par la DGFiP. Documentation en anglais.
- [OpenFisca-Core](https://github.com/openfisca/openfisca-core) - \[Gratuit\] \[Open source\] \[Python\] Moteur Python d'OpenFisca qui exécute des législations écrites en code pour simuler impôts et prestations ; base d'OpenFisca-France, documentation en anglais.
- [OpenFisca-France](https://github.com/openfisca/openfisca-france) - \[Gratuit\] \[Open source\] \[Python\] Modèle du système socio-fiscal français écrit pour le moteur OpenFisca ; il calcule impôts et prestations et sert notamment à simuler des réformes.
- [Publicodes](https://github.com/publicodes/publicodes) - \[Gratuit\] \[Open source\] \[JavaScript\] Langage déclaratif pour modéliser des règles de calcul (cotisations, aides) qui produit automatiquement l'explication de chaque résultat.
- [Simulateur d'aides 1jeune1solution (aides-jeunes)](https://github.com/DNUM-SocialGouv/aides-jeunes) - \[Gratuit\] \[Open source\] Code ouvert du simulateur public des aides sociales pour les 15-30 ans, fondé sur OpenFisca ; utile pour lire des règles d'éligibilité traduites en code.

## Apprendre

Formations et manuels pour les juristes qui veulent comprendre ou écrire du code.

- [Apprendre à coder avec Python (FUN MOOC)](https://www.fun-mooc.fr/en/cours/apprendre-a-coder-avec-python/) - \[Gratuit\] MOOC francophone d'initiation à la programmation en Python, destiné aux débutants sans formation technique.
- [CS50 for Lawyers](https://cs50.harvard.edu/law/) - \[Gratuit\] Cours de Harvard en anglais, à suivre à son rythme, qui initie les juristes à Python, SQL et aux enjeux juridiques des choix techniques.
- [Fiches pratiques IA de la CNIL](https://www.cnil.fr/fr/les-fiches-pratiques-ia) - \[Gratuit\] \[IA\] Recommandations de la CNIL pour développer un système d'IA conforme au RGPD : base légale, intérêt légitime, annotation, sécurité, statut des modèles.
- [Guide juridique de l'open data](https://guides.data.gouv.fr/guides/guide-juridique) - \[Gratuit\] Guide de data.gouv.fr sur les obligations d'ouverture des administrations et les règles à respecter pour réutiliser des données publiques (licences, mention de la source).
- [L'Atelier RGPD (MOOC de la CNIL)](https://www.cnil.fr/fr/comprendre-le-rgpd/le-mooc-de-la-cnil) - \[Gratuit\] \[Inscription\] MOOC gratuit de la CNIL en six modules (notions clés, principes, responsabilités, DPO, collectivités, travail) pour appliquer le RGPD, avec une attestation par module.
- [Le livre Catala](https://book.catala-lang.org/fr/) - \[Gratuit\] \[Open source\] Manuel en ligne, disponible en français, qui montre comment passer d'un texte juridique à un programme Catala et comment juristes et développeurs y collaborent.
- [Objectif IA](https://openclassrooms.com/fr/courses/6417031-objectif-ia-initiez-vous-a-l-intelligence-artificielle) - \[Gratuit\] \[Inscription\] \[IA\] Cours gratuit d'initiation à l'IA de l'Institut Montaigne et d'OpenClassrooms, sans prérequis, pour comprendre le fonctionnement des outils d'IA avant de les utiliser en droit.

## Communautés, événements et veille

Associations, institutions et médias pour suivre l'actualité du droit et de la legaltech.

- [ADIJ](https://adij.legal/) - \[Gratuit\] Association qui réunit juristes et informaticiens autour du droit du numérique, avec des ateliers et des webinaires (série « Compliance numérique ») ; une partie est réservée aux adhérents.
- [DINUM et Etalab](https://www.numerique.gouv.fr/) - \[Gratuit\] Direction interministérielle du numérique ; son département Etalab pilote data.gouv.fr et la politique d'ouverture des données et des codes sources publics.
- [Juriconnexion](https://www.juriconnexion.fr/) - \[Gratuit\] Association des professionnels de l'information juridique : rendez-vous annuels, par exemple sur l'IA générative, et enquêtes sur le métier ; événements payants pour les non-adhérents.
- [Le Monde du Droit, rubrique Intelligence artificielle](https://www.lemondedudroit.fr/mag/378-intelligence-artificielle.html) - \[Gratuit\] \[IA\] Rubrique d'actualité en accès libre sur l'IA juridique et les legaltechs : lancements d'outils, levées de fonds, positions des barreaux et programmes publics.
- [LINC (laboratoire d'innovation de la CNIL)](https://linc.cnil.fr/) - \[Gratuit\] \[IA\] Laboratoire de la CNIL qui publie des articles, des cahiers et des expérimentations sur l'IA, les données et la vie privée, utiles pour la veille.
- [Open Law](https://openlaw.fr/) - \[Gratuit\] Association qui anime des programmes collaboratifs entre juristes, institutions et legaltechs (IA et droit, open data, éthique des plateformes).
- [PIBD (INPI)](https://www.inpi.fr/ressources/propriete-intellectuelle/pibd-propriete-industrielle-bulletin-documentaire) - \[Gratuit\] Bulletin documentaire gratuit de l'INPI, publié tous les quinze jours : actualité législative, jurisprudence et doctrine en propriété industrielle, en France et à l'étranger.
- [Village de la Justice](https://www.village-justice.com/articles/) - \[Gratuit\] Média en accès libre pour les professions du droit : actualité par matière, tribunes de praticiens et offres d'emploi.

## Listes sœurs

Autres listes de type awesome sur le droit, les données publiques ou la régulation de l'IA.

- [Awesome AI Regulation, Principles & Guidelines](https://github.com/EthicalML/awesome-artificial-intelligence-regulation) - \[Gratuit\] \[IA\] Liste de textes, principes et normes encadrant l'IA, classés par zone géographique, pour comparer les approches réglementaires. En anglais, sans entrée propre à la France.
- [Awesome EU AI Act](https://github.com/GenAI-Gurus/awesome-eu-ai-act) - \[Gratuit\] Sources officielles, outils et modèles de documents pour se conformer au règlement européen sur l'intelligence artificielle.
- [Awesome GDPR](https://github.com/oppoverbakke/awesome-gdpr) - \[Gratuit\] Liste de ressources sur le RGPD : lignes directrices du CEPD, AIPD, registre, sécurité, outils et autorités de contrôle, dont la CNIL. En anglais.
- [Awesome Legal Data](https://github.com/openlegaldata/awesome-legal-data) - \[Gratuit\] Sources de données juridiques du monde entier classées par pays, avec une indication sur leur caractère ouvert ou payant.
- [Awesome Legal NLP](https://github.com/maastrichtlawtech/awesome-legal-nlp) - \[Gratuit\] \[IA\] Recensement de jeux de données, modèles et articles sur le traitement automatique des textes juridiques, classés par tâche.
- [Awesome Legaltech](https://github.com/Vaquill-AI/awesome-legaltech) - \[Gratuit\] Liste internationale d'outils, de données et de ressources legaltech, à dominante américaine, maintenue par l'entreprise Vaquill AI qui y signale ses propres projets.
- [Awesome OGD Switzerland](https://github.com/rnckp/awesome-ogd-switzerland) - \[Gratuit\] Portails, API et outils de données publiques ouvertes en Suisse ; liste généraliste qui n'est pas consacrée au droit.
- [Awesome Responsible AI](https://github.com/AthenaCore/AwesomeResponsibleAI) - \[Gratuit\] \[IA\] Liste de cadres, normes, codes d'éthique et réglementations sur l'IA responsable, utile pour préparer la conformité au règlement européen sur l'IA. En anglais.
- [Legal Text Analytics](https://github.com/Liquid-Legal-Institute/Legal-Text-Analytics) - \[Gratuit\] \[IA\] Liste de méthodes, bibliothèques, corpus et outils d'annotation pour analyser automatiquement des textes juridiques. En anglais.

## Projets archivés ou non maintenus

Projets sans activité depuis plus de 24 mois. Ils restent utiles comme référence mais peuvent ne plus fonctionner.

- [Archéo Lex](https://github.com/Legilibre/Archeo-Lex) - \[Gratuit\] \[Open source\] \[Python\] \[Non maintenu\] Convertit chaque texte de la base LEGI en un fichier Markdown versionné sous Git pour comparer ses versions successives. Dernier commit en mars 2019.
- [Guide de la pseudonymisation (Etalab)](https://github.com/etalab/guides.etalab.gouv.fr/tree/master/pseudonymisation) - \[Gratuit\] \[Non maintenu\] Guide d'Etalab sur la pseudonymisation de documents textuels, illustré par les décisions de justice. Le site ne répond plus ; le lien mène aux sources du guide. Dernier commit en mai 2024.
- [Guide RGPD du développeur (CNIL)](https://www.cnil.fr/fr/technologies/guide-rgpd-du-developpeur) - \[Gratuit\] \[Open source\] \[Non maintenu\] Fiches de la CNIL pour intégrer le RGPD dans un projet logiciel (minimisation, sécurité, traceurs, durées de conservation, droits), avec extraits de code ; dernière révision fin 2021.
- [juritools (Cour de cassation)](https://github.com/Cour-de-cassation/juritools) - \[Gratuit\] \[Open source\] \[Python\] \[Non maintenu\] Bibliothèque Python de la Cour de cassation pour pseudonymiser les décisions des bases Jurinet et Jurica. Dernier commit en janvier 2024.
- [Legit.jl](https://github.com/Legilibre/Legit.jl) - \[Gratuit\] \[Open source\] \[Non maintenu\] Script expérimental en Julia qui transformait la base LEGI en dépôts Git et Markdown. Dernier commit en juillet 2015.
- [LÉTHÉ (Gendarmerie nationale)](https://github.com/GendarmerieNationale/LETHE) - \[Gratuit\] \[Open source\] \[Python\] \[Non maintenu\] Bibliothèque Python du Datalab de la Gendarmerie pour repérer et pseudonymiser les entités nommées dans des textes en français. Dernier commit en septembre 2023.
- [LEXTREME](https://github.com/JoelNiklaus/LEXTREME) - \[Gratuit\] \[IA\] \[Python\] \[Non maintenu\] Code du banc d'essai juridique multilingue LEXTREME, qui inclut des tâches en français ; le jeu de données reste publié sur Hugging Face. Dernier commit en décembre 2023.
- [loifrancaise](https://github.com/Seb35/loifrancaise) - \[Gratuit\] \[Open source\] \[Python\] \[Non maintenu\] Bibliothèque issue d'Archéo Lex pour télécharger et lire les bases LEGI, KALI, JORF ou CNIL. Dernier commit en avril 2015.
- [Pseudo App (Etalab)](https://github.com/etalab-ia/pseudo_app) - \[Gratuit\] \[Open source\] \[Python\] \[Non maintenu\] Démonstrateur de pseudonymisation de documents conçu pour le Conseil d'État ; le modèle entraîné n'est pas fourni. Dernier commit en août 2023.

## Contribuer

Les propositions sont les bienvenues. Lisez d'abord le [guide de contribution](CONTRIBUTING.md) : il précise les critères d'inclusion et la marche à suivre (formulaire d'issue ou pull request qui modifie uniquement `data/ressources.yml`).
Les participants s'engagent à respecter le [code de conduite](CODE_OF_CONDUCT.md).

## Licence du contenu

Dans la limite permise par la loi, la personne qui maintient cette liste ([GitByHossam](https://github.com/GitByHossam)) renonce à tous ses droits sur son contenu, placé sous [CC0 1.0](LICENSE). Les scripts du dossier `scripts/` sont publiés sous [licence MIT](scripts/LICENSE).
