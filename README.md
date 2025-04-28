# Projet 6 - Classifiez automatiquement des biens de consommation

> 🎓 OpenClassrooms • Parcours [AI Engineer](https://openclassrooms.com/fr/paths/795-ai-engineer) | 👋 *Étudiant* : [David Scanu](https://www.linkedin.com/in/davidscanu14/)

## 📝 Contexte

Dans le cadre de ma formation de [AI Engineer chez OpenClassrooms](https://openclassrooms.com/fr/paths/795-ai-engineer), ce projet s'inscrit dans un scénario professionnel où j'interviens en tant que Data Scientist au sein de l'entreprise **"Place de marché"**, qui souhaite lancer une marketplace e-commerce.

Sur cette place de marché anglophone, des vendeurs proposent des articles à des acheteurs en postant **une photo et une description**. Pour l'instant, l'attribution de la catégorie d'un article est effectuée manuellement par les vendeurs, et est donc peu fiable. De plus, le volume des articles est pour l'instant très petit.

## ⚡ Mission

> Développer un moteur de classification automatique d'articles basé sur les images et les descriptions textuelles.

Réaliser une étude de faisabilité complète comprenant :

1. **Prétraitement des données texte et image** : Nettoyage et préparation des données
2. **Extraction de features** : Approches diverses pour texte et images
   - **Pour les images** : Algorithmes SIFT/ORB/SURF et CNN Transfer Learning
   - **Pour les textes** : Bag-of-words, TF-IDF, Word2Vec/Glove/FastText, BERT, et Universal Sentence Encoder
3. **Analyse de faisabilité** : Réduction dimensionnelle et visualisation, mesure de similarité
4. **Classification supervisée** : Implémentation d'un modèle de classification d'images
5. **Test d'API** : Extraction de données de produits via l'API OpenFood Facts

## 🎯 Objectifs pédagogiques

- **Prétraiter des données textuelles et des images** pour les rendre exploitables
- **Mettre en œuvre différentes techniques d'extraction de features** adaptées aux types de données
- **Évaluer la faisabilité** d'un regroupement automatique par catégorie
- **Implémenter une classification supervisée d'images** avec data augmentation
- **Interagir avec une API externe** pour récupérer des données structurées
- **Préparer une présentation détaillée** pour communiquer les résultats

## 🗓️ Plan de travail

1. **Analyse et préparation des données**
   - Exploration du jeu de données (images et descriptions)
   - Prétraitement des textes (nettoyage, tokenisation)
   - Prétraitement des images (redimensionnement, normalisation)

2. **Extraction des features**
   - Features texte : implémentation des approches bag-of-words, TF-IDF, Word2Vec, BERT, USE
   - Features image : implémentation des algorithmes SIFT/ORB/SURF et CNN Transfer Learning

3. **Étude de faisabilité**
   - Réduction dimensionnelle en 2D (PCA, t-SNE, UMAP)
   - Visualisation graphique des produits par catégorie
   - Mesure de similarité entre catégories réelles et clusters

4. **Classification supervisée d'images**
   - Implémentation de data augmentation
   - Entraînement d'un modèle de classification d'images
   - Évaluation des performances

5. **Test de l'API OpenFood Facts**
   - Développement d'un script pour l'extraction de produits
   - Création d'un fichier CSV avec les données structurées

6. **Préparation de la présentation**
   - Synthèse des résultats et des méthodes
   - Visualisations pertinentes
   - Création du support de présentation

## 📦 Livrables

1. [Notebook 1 : Etude de faisabilité d'un moteur de classification automatique d'articles | Colab](https://colab.research.google.com/drive/11NzDz7Wy2MKWHrmCsNwvC14Z4gTM75Xe?usp=sharing)
   - Code de prétraitement des données texte et image
   - Implémentation des différentes méthodes d'extraction de features
   - Visualisations et résultats de l'étude de faisabilité

2. [Notebook 2 : Classification supervisée d'images avec data augmentation | Colab](https://colab.research.google.com/drive/1MWZzFIE2hwoj35tkJy9pA0d76buZYDxb?usp=sharing)
   - Implémentation de data augmentation
   - Code d'entraînement et d'évaluation du modèle
   - Résultats de la classification

3. [Script Python de test de l'API Openfoodfacts](openfoodfacts/produits_champagne.py)
   - Code pour interagir avec l'API OpenFood Facts
   - Extraction des 10 premiers produits à base de "champagne"
   - Fichier CSV contenant les données structurées

4. **Support de présentation**
   - Méthodologie et résultats de l'étude de faisabilité
   - Analyse de la classification supervisée
   - Présentation du test de l'API

## 🔧 Technologies utilisées

- **Langages** : Python
- **Bibliothèques Data Science** : NumPy, Pandas, Scikit-learn
- **Traitement d'images** : OpenCV, PIL, Matplotlib
- **Traitement texte** : NLTK, SpaCy
- **Deep Learning** : TensorFlow/Keras, PyTorch
- **NLP avancé** : BERT, Universal Sentence Encoder
- **Visualisation** : Matplotlib, Seaborn, Plotly
- **API** : Requests, JSON

---

Projet réalisé dans le cadre de la formation **AI Engineer** d'OpenClassrooms (2025).
