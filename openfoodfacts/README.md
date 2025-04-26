# Collecte de produits à base de champagne via l'API Open Food Facts

## Objectif

Dans le cadre de notre projet d'expansion vers l'épicerie fine pour la place de marché e-commerce, nous avons développé un [script Python](produits_champagne.csv) permettant de collecter automatiquement des informations sur des produits à base de champagne via l'API Open Food Facts.

### Méthodologie

Nous avons utilisé l'API REST d'Open Food Facts qui ne nécessite aucune inscription, ce qui a simplifié le processus d'intégration. Notre script réalise les actions suivantes :

1. Interroge l'API Open Food Facts avec le terme de recherche **"champagne"**
2. **Récupère les 10 premiers produits correspondants**
3. Extrait pour chaque produit les champs suivants :
   - `foodId` : code-barres ou identifiant unique du produit
   - `label` : nom du produit
   - `category` : catégories auxquelles appartient le produit
   - `foodContentsLabel` : liste des ingrédients
   - `image` : URL de l'image du produit
4. **Sauvegarde les données extraites dans un fichier CSV** pour faciliter leur utilisation ultérieure

### Technologies utilisées

- Python comme langage de programmation
- Bibliothèque `requests` pour les appels API
- Bibliothèque `pandas` pour la manipulation et l'export des données

### Résultats

Le script génère un fichier [`produits_champagne.csv`](produits_champagne.csv) contenant les informations structurées des **10 premiers produits à base de champagne** disponibles dans la base de données Open Food Facts.