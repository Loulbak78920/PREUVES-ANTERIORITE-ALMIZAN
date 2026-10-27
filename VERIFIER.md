# Vérifier ce dépôt

## 1. Empreintes des fichiers

```bash
py -3 05_EMPREINTES/verifier_empreintes.py
```

Sortie attendue : `RESULT OK` et code de retour 0. Le script recalcule le
SHA-256 de chaque fichier listé dans `05_EMPREINTES/MANIFESTE_SHA256.json` et
signale tout écart, fichier manquant ou fichier supplémentaire.

## 2. Transaction on-chain

```bash
curl -s https://mainnet.base.org -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"eth_getTransactionReceipt","params":["0xaaf23e2d4c1e4e7c63ad7e12f95176a4017155164593384e45f867d1f5c6ec33"]}'
```

Vérifier `status = 0x1`, `contractAddress = 0x520cbd0e1e72178f9e819AFf1e815606923A71db`, puis
`eth_getCode` sur ce contrat.

## 3. Historique Git

```bash
git clone https://github.com/Loulbak78920/ASTRO-QODE-ALMIZAN
git -C ASTRO-QODE-ALMIZAN log --format='%H %aI <%ae> %s'
```

## 4. DOIs

```bash
curl -s https://doi.org/api/handles/10.5281/zenodo.23554838
curl -s -o /dev/null -w '%{http_code}\n' https://zenodo.org/api/records/23554838
```

Comparer avec `04_PREUVES_EXTERNES/RAPPORT_VERIFICATION_DOIS.json`.

## 5. Horodatage tiers (non effectué)

Pour obtenir un horodatage indépendant de l'historique Git :

```bash
curl -X POST https://archive.softwareheritage.org/api/1/origin/save/git/url/https%3A%2F%2Fgithub.com%2FLoulbak78920%2FASTRO-QODE-ALMIZAN/
```

Cette action crée un enregistrement public chez Software Heritage. Elle n'a pas
été exécutée au moment de la publication de ce dépôt.
