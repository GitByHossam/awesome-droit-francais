<!-- Fichier généré par scripts/generer_readme.py. Modifiez data/ressources.yml. -->
# Awesome Droit Français [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Ressources numériques utiles au droit français : sources officielles, données ouvertes, outils libres, IA juridique, modèles, calculateurs, formations et communautés.

Cette liste s'adresse aux juristes francophones (avocats, juristes d'entreprise, étudiants, chercheurs) et aux développeurs qui construisent des outils pour eux.
Elle existe pour retrouver en un seul endroit des ressources vérifiées, décrites simplement et classées par usage.
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

- [API Judilibre](https://www.data.gouv.fr/dataservices/api-judilibre) - \[Gratuit\] \[Inscription\] Recherchez dans les décisions pseudonymisées de la Cour de cassation et des juridictions judiciaires, avec leurs métadonnées (ECLI, chambre, solution) ; accès via PISTE.
- [API Légifrance](https://www.legifrance.gouv.fr/contenu/pied-de-page/open-data-et-api) - \[Gratuit\] \[Inscription\] Interrogez par programme les fonds de Légifrance (codes, textes, JORF, jurisprudence) avec des identifiants OAuth obtenus gratuitement sur le portail PISTE.
- [data.gouv.fr](https://www.data.gouv.fr/) - \[Gratuit\] Plateforme nationale des données publiques ; elle présente les bases juridiques (LEGI, KALI, CASS, JADE) et les outils qui les réutilisent.
- [Décisions du Conseil constitutionnel](https://www.conseil-constitutionnel.fr/les-decisions) - \[Gratuit\] Retrouvez les décisions DC et QPC du Conseil grâce à une recherche experte, avec les commentaires officiels et les tables analytiques.
- [EUR-Lex](https://eur-lex.europa.eu/homepage.html?locale=fr) - \[Gratuit\] Accès officiel au droit de l'Union européenne : Journal officiel de l'UE, traités, actes consolidés et jurisprudence, dans les 24 langues officielles.
- [HUDOC](https://hudoc.echr.coe.int/FRE) - \[Gratuit\] Base de la Cour européenne des droits de l'homme : arrêts, décisions et résumés juridiques, consultables en français et filtrables par mots-clés.
- [Légifrance](https://www.legifrance.gouv.fr/) - \[Gratuit\] Point d'entrée officiel pour consulter les codes et lois consolidés, le Journal officiel, les conventions collectives et la jurisprudence.
- [Open data de la DILA](https://echanges.dila.gouv.fr/OPENDATA/) - \[Gratuit\] Serveur qui met à disposition les archives XML des bases LEGI, JORF, KALI, CNIL, JADE, CASS, CONSTIT et d'autres, avec des mises à jour incrémentales.
- [Open data de la justice administrative](https://opendata.justice-administrative.fr/) - \[Gratuit\] Téléchargez en XML les décisions du Conseil d'État, des cours administratives d'appel et des tribunaux administratifs, regroupées par juridiction et par mois.
- [Service-Public.fr](https://www.service-public.fr/) - \[Gratuit\] Fiches pratiques de l'administration qui expliquent les droits et démarches des particuliers et des entreprises, avec les références des textes.

## Données juridiques réutilisables

Extractions, dépôts Git et jeux de données prêts à l'emploi, construits à partir des données publiques.

- [ArGiMi French Jurisprudence](https://huggingface.co/datasets/artefactory/Argimi-Legal-French-Jurisprudence) - \[Gratuit\] \[IA\] Décisions constitutionnelles, administratives et judiciaires découpées en segments, utiles pour construire un moteur de recherche ou un système RAG.
- [Codes en Markdown (lemyst)](https://github.com/lemyst/codes) - \[Gratuit\] Dix-huit codes rangés en un fichier Markdown par article, mis à jour par commits réguliers : l'historique Git montre chaque modification.
- [Jurisprudence (antoinejeannot)](https://huggingface.co/datasets/antoinejeannot/jurisprudence) - \[Gratuit\] \[Open source\] \[IA\] Plus d'un million de décisions judiciaires récupérées via Judilibre et publiées en JSONL et Parquet, pratiques pour l'analyse ou l'entraînement de modèles.
- [LegalKit](https://github.com/louisbrulenaudet/legalkit-pipeline) - \[Gratuit\] \[Open source\] \[IA\] \[Python\] Chaîne de traitement qui publie les codes français sous forme de jeux de données Hugging Face (un jeu par code), avec un exemple de chargement groupé.
- [Tricoteuses LEGI](https://huggingface.co/datasets/Tricoteuses/LEGI) - \[Gratuit\] Articles en vigueur de la base LEGI convertis en tableau avec leurs dates et identifiants ; le même éditeur publie aussi les bases CNIL et CAPP.

## Bibliothèques et clients d'API

Code réutilisable pour interroger les API juridiques ou exploiter les bases de la DILA.

### Python

- [legi.py](https://github.com/Legilibre/legi.py) - \[Gratuit\] \[Open source\] \[Python\] Construit et tient à jour une base SQLite à partir des archives LEGI, en reliant entre elles les versions successives d'un texte.
- [pylegifrance](https://github.com/pylegifrance/pylegifrance) - \[Gratuit\] \[Open source\] \[Inscription\] \[Python\] Fonctions Python prêtes à l'emploi pour chercher dans les codes, les lois et décrets ou la jurisprudence judiciaire via l'API Légifrance.

### JavaScript et autres langages

- [dila-api-client](https://github.com/SocialGouv/dila-api-client) - \[Gratuit\] \[Open source\] \[Inscription\] \[JavaScript\] Client Node.js qui gère l'authentification OAuth et les appels à l'API Légifrance de la DILA.
- [kali-data](https://github.com/SocialGouv/kali-data) - \[Gratuit\] \[Open source\] \[JavaScript\] Paquet npm qui rassemble en JSON les conventions collectives extraites de l'API DILA ; projet signalé comme expérimental.
- [legi-data](https://github.com/SocialGouv/legi-data) - \[Gratuit\] \[Open source\] \[JavaScript\] Paquet npm qui fournit en JSON quelques codes (travail, sécurité sociale) avec une API TypeScript ; ses auteurs le disent expérimental.

## IA juridique

Ressources pour brancher des assistants IA sur le droit français, entraîner ou évaluer des modèles et protéger les données personnelles.

### Serveurs MCP

- [data.gouv.fr MCP](https://github.com/datagouv/datagouv-mcp) - \[Gratuit\] \[Open source\] \[IA\] Serveur MCP officiel qui laisse un assistant IA chercher et analyser les jeux de données de data.gouv.fr ; une instance publique fonctionne sans compte.
- [DroitFrancaisMCP](https://github.com/jmtanguy/DroitFrancaisMCP) - \[Gratuit\] \[Open source\] \[Inscription\] \[IA\] \[Python\] Serveur MCP à installer soi-même qui interroge Légifrance et Judilibre avec vos propres identifiants PISTE.
- [justicelibre](https://justicelibre.org/) - \[Gratuit\] \[IA\] Serveur MCP hébergé qui interroge jurisprudence, codes et doctrine administrative issus de l'open data ; la recherche fonctionne sans compte.
- [mcp-server-legifrance](https://github.com/pylegifrance/mcp-server-legifrance) - \[Gratuit\] \[Open source\] \[Inscription\] \[IA\] \[Python\] Serveur MCP expérimental pour rechercher lois, articles de code et jurisprudence judiciaire ; il demande une clé délivrée par lab.dassignies.law.

### Modèles et embeddings

- [JuriBERT](https://huggingface.co/dascim/juribert-base) - \[Gratuit\] \[IA\] Famille de modèles BERT (de 6 à 110 millions de paramètres) entraînés sur des textes de Légifrance et de la Cour de cassation, à affiner pour classer ou extraire.
- [Lemone-embed](https://huggingface.co/louisbrulenaudet/lemone-embed-pro) - \[Gratuit\] \[IA\] Modèles d'embeddings spécialisés en fiscalité française, utiles pour la recherche sémantique dans le CGI et la doctrine fiscale.
- [Romulus](https://huggingface.co/louisbrulenaudet/Romulus-cpt-Llama-3.1-8B-v0.1-Instruct) - \[Gratuit\] \[IA\] Llama 3.1 8B dont l'entraînement a été prolongé sur du droit français ; c'est une base à affiner, non alignée pour produire directement des réponses.

### Benchmarks et évaluation

- [BSARD](https://huggingface.co/datasets/maastrichtlawtech/bsard) - \[Gratuit\] \[IA\] Environ 1 100 questions de citoyens en français reliées par des juristes aux articles de loi belges pertinents, pour mesurer un moteur de recherche juridique.
- [LLeQA](https://huggingface.co/datasets/maastrichtlawtech/lleqa) - \[Gratuit\] \[Inscription\] \[IA\] Questions juridiques rédigées en français avec réponses détaillées d'experts et articles de loi belges, pour évaluer la génération de réponses.
- [MultiEURLEX](https://huggingface.co/datasets/coastalcph/multi_eurlex) - \[Gratuit\] \[IA\] 65 000 actes de l'UE en 23 langues, dont le français, étiquetés avec le thésaurus EuroVoc : un banc d'essai de classification multilingue.

### Anonymisation et pseudonymisation

- [Guide de la pseudonymisation (Etalab)](https://guides.etalab.gouv.fr/pseudonymisation/) - \[Gratuit\] Explique pourquoi et comment pseudonymiser des documents textuels, en prenant l'exemple des décisions de justice et d'une méthode fondée sur l'IA.
- [Label](https://github.com/Cour-de-cassation/label) - \[Gratuit\] \[Open source\] Logiciel de la Cour de cassation pour relire et corriger les décisions pré-annotées par un algorithme avant leur publication pseudonymisée.
- [Presidio](https://github.com/microsoft/presidio) - \[Gratuit\] \[Open source\] \[Python\] Boîte à outils de détection et de masquage de données personnelles ; prévue pour l'anglais par défaut, elle s'adapte au français avec un modèle linguistique adéquat.

## Modèles de documents et automatisation

Lettres types, formulaires et outils d'assemblage de documents.

- [Accord Project](https://accordproject.org/) - \[Gratuit\] \[Open source\] \[JavaScript\] Outils libres pour écrire des modèles de contrats qui associent texte, modèle de données et logique exécutable ; documentation en anglais.
- [Démarches et outils de Service-Public.fr](https://www.service-public.fr/particuliers/vosdroits/services-en-ligne-et-formulaires) - \[Gratuit\] Rubrique officielle qui réunit formulaires, simulateurs et modèles de lettres (démission, attestation sur l'honneur, plainte auprès du procureur).
- [Docassemble](https://docassemble.org/) - \[Gratuit\] \[Open source\] \[Python\] Plateforme libre d'entretiens guidés : elle ne pose que les questions utiles puis assemble un document DOCX ou PDF à partir des réponses.
- [Lettres types de l'INC](https://www.inc-conso.fr/content/150-lettres-types-pour-r%C3%A9gler-vos-litiges) - \[Gratuit\] Courriers prêts à compléter de l'Institut national de la consommation pour les litiges courants (banque, assurance, logement), en PDF ou Word.

## Calculateurs et simulateurs

Outils de calcul de délais, d'indemnités, d'intérêts et de loyers. Les résultats restent indicatifs.

- [Calcul de l'intérêt légal (justice.fr)](https://www.justice.fr/fiche/calcul-interet-legal) - \[Gratuit\] Fiche qui donne les taux semestriels de l'intérêt légal et la formule pour calculer soi-même les intérêts dus ; ce n'est pas un calculateur automatique.
- [Calcul de la révision du loyer (INC)](https://www.inc-conso.fr/content/calculez-laugmentation-de-votre-loyer-0) - \[Gratuit\] Calcule la hausse annuelle autorisée d'un loyer d'habitation à partir de l'indice de référence des loyers publié par l'Insee.
- [Calculateur de délais de procédure pénale](https://www.simonnetavocat.fr/calculateur-delais-procedure-penale/) - \[Gratuit\] Outil gratuit publié par un cabinet d'avocats qui calcule l'échéance d'environ 47 délais pénaux et cite l'article applicable ; à contrôler sur les textes.
- [Mon-entreprise (Urssaf)](https://mon-entreprise.urssaf.fr/simulateurs) - \[Gratuit\] \[Open source\] Simulateurs publics de cotisations et de revenus (salarié, indépendant, dirigeant) qui détaillent chaque étape du calcul ; le code est public.
- [Simulateur de pension alimentaire (justice.fr)](https://www.justice.fr/fiche/simulateur-calcul-pension-alimentaire-simulateur) - \[Gratuit\] Donne une estimation de la pension alimentaire selon les revenus, le nombre d'enfants et le mode de garde ; seul le juge fixe le montant.
- [Simulateurs du Code du travail numérique](https://code.travail.gouv.fr/outils) - \[Gratuit\] Estimations officielles de l'indemnité de licenciement, de la durée du préavis, de l'indemnité de rupture conventionnelle ou du salaire net.

## Outils publics et droit codé

Services publics numériques et langages qui traduisent des règles juridiques en programmes.

- [Catala](https://catala-lang.org/) - \[Gratuit\] \[Open source\] Langage de programmation de l'Inria qui annote un texte de loi avec sa traduction en code, pensé pour un travail en binôme juriste et développeur.
- [Code du travail numérique](https://code.travail.gouv.fr/) - \[Gratuit\] \[Open source\] Service public qui répond aux questions de droit du travail en tenant compte de la convention collective applicable ; son code source est ouvert.
- [OpenFisca-France](https://github.com/openfisca/openfisca-france) - \[Gratuit\] \[Open source\] \[Python\] Modèle du système socio-fiscal français écrit pour le moteur OpenFisca ; il calcule impôts et prestations et sert notamment à simuler des réformes.
- [Publicodes](https://github.com/betagouv/publicodes) - \[Gratuit\] \[Open source\] \[JavaScript\] Langage déclaratif pour modéliser des règles de calcul (cotisations, aides) qui produit automatiquement l'explication de chaque résultat.

## Apprendre

Formations et manuels pour les juristes qui veulent comprendre ou écrire du code.

- [Apprendre à coder avec Python (FUN MOOC)](https://www.fun-mooc.fr/en/cours/apprendre-a-coder-avec-python/) - \[Gratuit\] MOOC francophone d'initiation à la programmation en Python, destiné aux débutants sans formation technique.
- [CS50 for Lawyers](https://cs50.harvard.edu/law/) - \[Gratuit\] Cours de Harvard en anglais, à suivre à son rythme, qui initie les juristes à Python, SQL et aux enjeux juridiques des choix techniques.
- [Le livre Catala](https://book.catala-lang.org/fr/) - \[Gratuit\] \[Open source\] Manuel en ligne, disponible en français, qui montre comment passer d'un texte juridique à un programme Catala et comment juristes et développeurs y collaborent.

## Communautés, événements et veille

Associations, institutions et médias pour suivre l'actualité du droit et de la legaltech.

- [DINUM et Etalab](https://www.numerique.gouv.fr/) - \[Gratuit\] Direction interministérielle du numérique ; son département Etalab pilote data.gouv.fr et la politique d'ouverture des données et des codes sources publics.
- [Open Law](https://openlaw.fr/) - \[Gratuit\] Association qui anime des programmes collaboratifs entre juristes, institutions et legaltechs (IA et droit, open data, éthique des plateformes).
- [Village de la Justice](https://www.village-justice.com/articles/) - \[Gratuit\] Média en accès libre pour les professions du droit : actualité par matière, tribunes de praticiens et offres d'emploi.

## Listes sœurs

Autres listes de type awesome sur le droit, les données publiques ou la régulation de l'IA.

- [Awesome EU AI Act](https://github.com/GenAI-Gurus/awesome-eu-ai-act) - \[Gratuit\] Sources officielles, outils et modèles de documents pour se conformer au règlement européen sur l'intelligence artificielle.
- [Awesome Legal Data](https://github.com/openlegaldata/awesome-legal-data) - \[Gratuit\] Sources de données juridiques du monde entier classées par pays, avec une indication sur leur caractère ouvert ou payant.
- [Awesome Legal NLP](https://github.com/maastrichtlawtech/awesome-legal-nlp) - \[Gratuit\] \[IA\] Recensement de jeux de données, modèles et articles sur le traitement automatique des textes juridiques, classés par tâche.
- [Awesome Legaltech](https://github.com/Vaquill-AI/awesome-legaltech) - \[Gratuit\] Liste internationale d'outils, de données et de ressources legaltech, maintenue par une entreprise du secteur.
- [Awesome OGD Switzerland](https://github.com/rnckp/awesome-ogd-switzerland) - \[Gratuit\] Portails, API et outils de données publiques ouvertes en Suisse ; liste généraliste qui n'est pas consacrée au droit.

## Projets archivés ou non maintenus

Projets sans activité depuis plus de 24 mois. Ils restent utiles comme référence mais peuvent ne plus fonctionner.

- [Archéo Lex](https://github.com/Legilibre/Archeo-Lex) - \[Gratuit\] \[Open source\] \[Python\] \[Non maintenu\] Convertit chaque texte de la base LEGI en un fichier Markdown versionné sous Git pour comparer ses versions successives. Dernier commit en mars 2019.
- [Legit.jl](https://github.com/Legilibre/Legit.jl) - \[Gratuit\] \[Open source\] \[Non maintenu\] Script expérimental en Julia qui transformait la base LEGI en dépôts Git et Markdown. Dernier commit en juillet 2015.
- [LEXTREME](https://github.com/JoelNiklaus/LEXTREME) - \[Gratuit\] \[IA\] \[Python\] \[Non maintenu\] Code du banc d'essai juridique multilingue LEXTREME, qui inclut des tâches en français ; le jeu de données reste publié sur Hugging Face. Dernier commit en décembre 2023.
- [loifrancaise](https://github.com/Seb35/loifrancaise) - \[Gratuit\] \[Open source\] \[Python\] \[Non maintenu\] Bibliothèque issue d'Archéo Lex pour télécharger et lire les bases LEGI, KALI, JORF ou CNIL. Dernier commit en avril 2015.
- [Pseudo App (Etalab)](https://github.com/etalab-ia/pseudo_app) - \[Gratuit\] \[Open source\] \[Python\] \[Non maintenu\] Démonstrateur de pseudonymisation de documents conçu pour le Conseil d'État ; le modèle entraîné n'est pas fourni. Dernier commit en août 2023.

## Contribuer

Les propositions sont les bienvenues. Lisez d'abord le [guide de contribution](CONTRIBUTING.md) : il précise les critères d'inclusion et la marche à suivre (formulaire d'issue ou pull request qui modifie uniquement `data/ressources.yml`).
Les participants s'engagent à respecter le [code de conduite](CODE_OF_CONDUCT.md).

## Licence du contenu

Dans la limite permise par la loi, la personne qui maintient cette liste ([HossLaRue](https://github.com/HossLaRue)) renonce à tous ses droits sur son contenu, placé sous [CC0 1.0](LICENSE). Les scripts du dossier `scripts/` sont publiés sous [licence MIT](scripts/LICENSE).
