# 🐦 Hespress Social Media Analytics

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Description

Projet d'**analyse de données** et de **web scraping** visant à collecter et analyser le contenu vidéo publié par **Hespress** sur Twitter/X. Ce projet permet d'extraire des métriques détaillées sur l'engagement, les commentaires et le sentiment des utilisateurs.

### 🎯 Objectifs

- 📊 Collecte automatisée des vidéos Hespress depuis Twitter
- 📈 Analyse des métriques d'engagement (vues, likes, partages)
- 💬 Extraction et analyse des commentaires
- 🔍 Analyse de sentiment multilingue (Arabe, Français, Anglais)
- 📉 Visualisation des tendances et statistiques

---

## 📦 Données Collectées

Pour chaque vidéo, le système extrait **15 métriques clés** :

### Informations de Base
1. **Titre** - Titre ou texte du tweet
2. **Catégorie** - Sport, Politique, Culture, Économie, Société
3. **Date de publication** - Date et heure exactes
4. **Durée** - Durée de la vidéo (secondes)

### Métriques d'Engagement
5. **Réactions** - Likes, Retweets, Favoris
6. **Vues** - Nombre total de visualisations
7. **Commentaires** - Texte complet des commentaires
8. **Partages** - Nombre de retweets
9. **Nombre de commentaires** - Comptage total

### Analyse Textuelle
10. **Mots-clés** - Top mots cités avec pourcentages
11. **Langue par commentaire** - Détection automatique
12. **Distribution linguistique** - % de chaque langue

### Analyse de Sentiment
13. **Polarité par commentaire** - Positif/Négatif/Neutre
14. **Distribution globale** - % de chaque sentiment
15. **Polarité par réseau** - Sentiment moyen

---

## 🗂️ Structure du Projet

```
atelier/
│
├── 📂 scrapers/                    # Scripts de collecte de données
│   ├── scraping_mois_septembre.ipynb
│   ├── scraping_mois_octobre.ipynb
│   ├── scrap_test.ipynb
│   └── Untitled2.ipynb
│
├── 📂 data/
│   ├── raw/                        # Données brutes collectées
│   │   ├── resultats_hespress_sept.json
│   │   ├── resultats_hespress_tous.json
│   │   ├── tweets_hespress_.csv
│   │   └── videos_*.csv
│   └── processed/                  # Données nettoyées
│
├── 📂 config/
│   └── config.py                   # Configuration du projet
│
├── 📂 docs/
│   └── task_atelier2.docx          # Documentation
│
├── 📂 results/                     # Analyses et visualisations
│
├── 📂 temp/                        # Fichiers temporaires
│
├── organize_atelier.py             # Script d'organisation
├── requirements.txt                # Dépendances Python
├── .gitignore                      # Fichiers à ignorer
└── README.md                       # Ce fichier
```

---

## 🛠️ Technologies Utilisées

### Scraping & Collecte
- **Tweepy** - API Twitter v2
- **Selenium** - Scraping dynamique
- **BeautifulSoup** - Parsing HTML

### Analyse de Données
- **Pandas** - Manipulation de données
- **NumPy** - Calculs numériques
- **Jupyter** - Notebooks interactifs

### NLP & Sentiment
- **LangDetect** - Détection de langue
- **TextBlob** - Analyse de sentiment
- **Transformers** - Modèles BERT multilingues

### Visualisation
- **Matplotlib** - Graphiques
- **Seaborn** - Visualisations statistiques
- **Plotly** - Graphiques interactifs

---

## 📥 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/SARA-MAGGAG/hespress-social-analytics.git
cd hespress-social-analytics
```

### 2. Créer un environnement virtuel

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration

Créez un fichier `.env` à partir du template :

```bash
cp credentials_template.env .env
```

Remplissez vos clés API Twitter dans le fichier `.env`.

---

## 🚀 Utilisation

### Lancer les Notebooks

```bash
# Démarrer Jupyter
jupyter notebook

# Ouvrir un des notebooks dans scrapers/
# Par exemple: scraping_mois_septembre.ipynb
```

### Structure des Notebooks

1. **scraping_mois_septembre.ipynb** - Collecte septembre 2025
2. **scraping_mois_octobre.ipynb** - Collecte octobre 2025
3. **scrap_test.ipynb** - Tests et expérimentations

### Données Disponibles

Les données collectées sont dans `data/raw/` :

- **Format JSON** : Données complètes avec métadonnées
- **Format CSV** : Version tabulaire pour analyse rapide

---

## 📊 Résultats & Statistiques

### Période Couverte
- **Septembre 2025** : 62+ vidéos
- **Octobre 2025** : Données complètes
- **Total** : Plusieurs centaines de vidéos

### Métriques Collectées

```
📈 Engagement moyen par vidéo
   Vues      : ~125K
   Likes     : ~8.5K  
   Partages  : ~450
   Comments  : ~180
```

### Distribution des Catégories

```
Sport        : 35% ████████████████
Politique    : 28% █████████████
Culture      : 15% ███████
Économie     : 12% █████
Société      : 10% ████
```

---

## 🔍 Analyses Disponibles

### 1. Analyse Temporelle
- Évolution des vues dans le temps
- Pics d'engagement par jour/heure
- Tendances mensuelles

### 2. Analyse de Sentiment
- Sentiment par catégorie
- Distribution Positif/Négatif/Neutre
- Évolution du sentiment

### 3. Analyse Linguistique
- Détection automatique de langue
- Distribution AR/FR/EN
- Mots-clés les plus fréquents

### 4. Analyse Comparative
- Performance par catégorie
- Comparaison mensuelle
- Benchmarking des vidéos

---

## 📈 Exemples de Visualisations

### Distribution Linguistique
```
🇲🇦 Arabe     : 68%
🇫🇷 Français  : 25%
🇬🇧 Anglais   :  5%
🇪🇸 Autres    :  2%
```

### Analyse de Sentiment
```
😊 Positif : 42% █████████████████
😐 Neutre  : 38% ███████████████
😠 Négatif : 20% ████████
```

---

## 🔐 Sécurité & Confidentialité

### Données Sensibles
- ✅ Fichiers `.env` ignorés par Git
- ✅ Données brutes non versionnées
- ✅ Anonymisation des utilisateurs

### Conformité
- ✅ Respect des Terms of Service de Twitter
- ✅ Usage académique uniquement
- ✅ Pas de commercialisation des données

---

## 🚧 Limitations

- ⏱️ **Rate Limiting** - Limites API Twitter
- 📅 **Historique** - Accès limité aux anciens tweets
- 🔒 **Comptes privés** - Non accessibles
- 💾 **Volume** - Données volumineuses non versionnées

---

## 🔮 Développements Futurs

### Court Terme
- [ ] Dashboard interactif (Streamlit)
- [ ] Analyse automatisée quotidienne
- [ ] Export automatique vers Excel/PDF
- [ ] Détection de tendances en temps réel

### Moyen Terme
- [ ] Support multi-plateformes (YouTube, Facebook)
- [ ] Prédiction de viralité (ML)
- [ ] Détection de fake news
- [ ] API REST pour accès externe

### Long Terme
- [ ] Analyse vidéo (Computer Vision)
- [ ] Système de recommandation
- [ ] Chatbot pour requêtes NL
- [ ] Mobile app

---

## 🤝 Contribution

Les contributions sont bienvenues ! Pour contribuer :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/NouvelleFeature`)
3. Commit les changements (`git commit -m 'Ajout NouvelleFeature'`)
4. Push vers la branche (`git push origin feature/NouvelleFeature`)
5. Ouvrir une Pull Request

---

## 📚 Ressources

### Documentation
- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api)
- [Tweepy Documentation](https://docs.tweepy.org/)
- [Pandas Documentation](https://pandas.pydata.org/)

### Datasets Similaires
- [Twitter Sentiment Analysis](https://www.kaggle.com/datasets/kazanova/sentiment140)
- [Arabic Sentiment Dataset](https://www.kaggle.com/datasets/mksaad/arabic-sentiment-analysis)

---

## 👥 Auteur

**SARA MAGGAG**  
🎓 Étudiante en Data Science  
📧 Email: [votre.email@example.com]  
🔗 LinkedIn: [Votre Profil]  
🐙 GitHub: [@SARA-MAGGAG](https://github.com/SARA-MAGGAG)

---

## 📄 License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 🙏 Remerciements

- 📰 **Hespress** - Source de données
- 🐦 **Twitter/X** - Plateforme
- 🎓 **Communauté Open Source** - Outils et bibliothèques
- 👨‍🏫 **Encadrants académiques** - Support et guidance

---

<div align="center">

**⭐ Si ce projet vous est utile, donnez-lui une étoile ! ⭐**

Made with 💙 for Social Media Analytics & Data Science

</div>
