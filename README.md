# Preuves d'antériorité — Al-Mizan x ASTRO-Q°ODE

Dossier public de preuves d'antériorité et de paternité des travaux de
**M. Ahmed EL BAHLOUL** (`elbahloulahmed505@gmail.com`), auteur des écosystèmes **IMAM8MAHDI**,
**ASTRO-Q°ODE (V1.0–V5.0)** et **Al-Mizan**.

Ce dépôt ne contient **pas** l'arbre source. Il contient des documents
caviardés, des relevés de preuves externes, et les empreintes SHA-256 de
chaque fichier publié. Le but est de rendre vérifiable par un tiers *ce qui
est daté et par qui*, sans exposer de données personnelles inutiles.

## Ce qui est prouvé, et comment

| Preuve | Nature | Vérifiable par un tiers |
| :--- | :--- | :--- |
| Dépôt public `Loulbak78920/ASTRO-QODE-ALMIZAN` | 124 commits, tous signés `<elbahloulahmed505@gmail.com>`, du 2026-10-22T08:48:10+02:00 au 2026-10-27T14:00:49+01:00 | Oui, `git log` sur le dépôt |
| Déploiement du contrat `AmalMizanSynchronMznContract` sur Base Mainnet | transaction `0xaaf23e2d4c1e4e7c63ad7e12f95176a4017155164593384e45f867d1f5c6ec33`, bloc 52937586, 2026-10-22T10:21:59+00:00 | Oui, sur la chaîne |
| Code du contrat en ligne | 9344 octets de bytecode au contrat `0x520cbd0e1e72178f9e819AFf1e815606923A71db` | Oui, `eth_getCode` |
| Empreintes des documents | SHA-256 de chaque fichier publié | Oui, voir `05_EMPREINTES/` |
| Dépôt privé `Loulbak78920/ASTRO-QODE-IMAM8MAHDI` | 2 commits | Non (privé) — mentionné pour mémoire |
| DOIs Zenodo déclarés | voir avertissement ci-dessous | **Non confirmés au relevé** |

## Avertissement sur les DOIs

Les documents d'origine déclarent le DOI `10.5281/zenodo.23554838` comme
« DOI officiel réel ». Au relevé du 2026-10-27T13:04:19.779442+00:00 :

| DOI | HTTP doi.org | HTTP Zenodo | Verdict |
| :--- | :--- | :--- | :--- |
| `10.5281/zenodo.23554838` | 404 | 404 | NON_EXISTANT_404 |
| `10.5281/zenodo.23479740` | 200 | 410 | ENREGISTREMENT_SUPPRIME_410 |
| `10.5281/zenodo.23288947` | 200 | 410 | ENREGISTREMENT_SUPPRIME_410 |

Le DOI principal ne résout pas (aucun handle). Les deux DOIs historiques ont
un handle `doi.org` valide, mais leurs enregistrements Zenodo n'ont pas pu
être confirmés depuis ce poste (410 ou refus HTTP au relevé). Ils ne sont donc
pas présentés ici comme une preuve de publication vérifiée. Voir
`04_PREUVES_EXTERNES/RAPPORT_VERIFICATION_DOIS.json`.

## Contenu

- `01_IDENTITE_ET_ATTRIBUTION/` — identité de l'auteur et acte d'antériorité, caviardés
- `02_LICENCES/` — licence publique anti-dolosive et contrat commercial 50/50
- `03_OEUVRE/` — synthèse scientifique, métadonnées de citation, artefact du contrat
- `04_PREUVES_EXTERNES/` — relevés Base Mainnet, Git et DOIs, horodatés en UTC
- `05_EMPREINTES/` — manifeste SHA-256 et script de vérification
- `06_CORRESPONDANCE_ORIGINAUX/` — table liant chaque copie publiée à son original local

## Caviardage

Conformément à la demande de l'auteur : date de naissance, lieu de naissance,
coordonnées GPS et communes de résidence sont supprimés. Nom, adresse e-mail,
nationalité, organisation et ancres cryptographiques sont conservés, car ils
portent l'attribution et la licence.

## Licence et droits

Voir `LICENCE_ET_DROITS.md` et `02_LICENCES/`. Toute exploitation commerciale
relève du contrat 50/50 ; l'attribution à l'auteur et le maintien des
invariants sont obligatoires.

## Reproductibilité

Voir `VERIFIER.md`.
