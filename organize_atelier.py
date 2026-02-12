#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'Organisation Automatique - Projet Hespress
===================================================
Organisation des fichiers du dossier atelier

Auteur: SARA MAGGAG
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

def organize_atelier():
    """Organise automatiquement le dossier atelier"""
    
    # Chemin du dossier
    base_path = Path(r"C:\Users\dell\Documents\atelier")
    
    print("="*70)
    print("🗂️  ORGANISATION AUTOMATIQUE DU PROJET HESPRESS")
    print("="*70)
    print(f"📂 Dossier: {base_path}\n")
    
    # 1. Créer une sauvegarde
    backup_folder = base_path / f"_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print("📦 Création d'une sauvegarde...")
    backup_folder.mkdir(exist_ok=True)
    
    # Copier tous les fichiers dans le backup
    for item in base_path.iterdir():
        if item.name.startswith('_backup_') or item.name in ['.git', '__pycache__', '.ipynb_checkpoints']:
            continue
        if item.is_file():
            shutil.copy2(item, backup_folder / item.name)
    
    print(f"✅ Sauvegarde créée: {backup_folder.name}\n")
    
    # 2. Créer la structure de dossiers
    print("📁 Création de la structure de dossiers...\n")
    
    folders = {
        'scrapers': 'Scripts Python et notebooks de scraping',
        'data/raw': 'Données brutes collectées (JSON, CSV)',
        'data/processed': 'Données nettoyées et traitées',
        'config': 'Fichiers de configuration',
        'docs': 'Documentation et rapports',
        'results': 'Résultats et analyses',
        'temp': 'Fichiers temporaires',
    }
    
    for folder, description in folders.items():
        folder_path = base_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {folder:25} - {description}")
    
    print()
    
    # 3. Définir les règles de déplacement
    moves = {
        # Notebooks de scraping
        'scraping_mois_octobre.ipynb': 'scrapers/',
        'scraping_mois_septembre.ipynb': 'scrapers/',
        'scrap_test.ipynb': 'scrapers/',
        'Untitled2.ipynb': 'scrapers/',
        
        # Configuration
        'config.py': 'config/',
        
        # Données JSON (résultats bruts)
        'resultats_hespress_62.json': 'data/raw/',
        'resultats_hespress_sept.json': 'data/raw/',
        'resultats_hespress_tous.json': 'data/raw/',
        'video_hespress_x.json': 'data/raw/',
        
        # Données CSV (résultats)
        'resultats_hespress_sept.csv': 'data/raw/',
        'resultats_hespress_tous.csv': 'data/raw/',
        'tweets_data_extrait.csv': 'data/raw/',
        'tweets_hespress_.csv': 'data/raw/',
        'videos_hespresse_20251017_212404.csv': 'data/raw/',
        'videos_twitter_20251022_193906.csv': 'data/raw/',
        'video_hespress_x.csv': 'data/raw/',
        'urls_hesspress_pour_scraping.csv': 'data/raw/',
        
        # Fichiers temporaires
        'twitter_urls_temporaire.txt': 'temp/',
        
        # Documentation
        'task_atelier2.docx': 'docs/',
    }
    
    # 4. Déplacer les fichiers
    print("🔄 Déplacement des fichiers...\n")
    
    moved_count = 0
    errors = []
    
    for filename, target_folder in moves.items():
        source = base_path / filename
        
        if not source.exists():
            continue
        
        target = base_path / target_folder / filename
        
        try:
            # Vérifier si le fichier existe déjà
            if target.exists():
                # Ajouter timestamp
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                stem = source.stem
                suffix = source.suffix
                new_name = f"{stem}_{timestamp}{suffix}"
                target = base_path / target_folder / new_name
            
            shutil.move(str(source), str(target))
            print(f"  ✓ {filename:45} → {target_folder}")
            moved_count += 1
            
        except Exception as e:
            error_msg = f"Erreur avec {filename}: {str(e)}"
            errors.append(error_msg)
            print(f"  ✗ {error_msg}")
    
    print(f"\n✅ {moved_count} fichiers déplacés")
    
    if errors:
        print(f"\n⚠️  {len(errors)} erreurs:")
        for error in errors:
            print(f"  - {error}")
    
    # 5. Nettoyer les dossiers système
    print("\n🧹 Nettoyage des dossiers système...")
    
    system_folders = ['__pycache__', '.ipynb_checkpoints']
    for folder in system_folders:
        folder_path = base_path / folder
        if folder_path.exists():
            shutil.rmtree(folder_path)
            print(f"  ✓ Supprimé: {folder}")
    
    # 6. Créer des fichiers README
    print("\n📝 Création des fichiers README...\n")
    
    readme_contents = {
        'scrapers/README.md': """# Scripts de Scraping

Ce dossier contient tous les notebooks Jupyter pour le scraping des données Hespress depuis Twitter.

## Notebooks disponibles :
- `scraping_mois_septembre.ipynb` - Scraping du mois de septembre
- `scraping_mois_octobre.ipynb` - Scraping du mois d'octobre
- `scrap_test.ipynb` - Tests et expérimentations
""",
        
        'data/raw/README.md': """# Données Brutes

Ce dossier contient toutes les données collectées directement depuis Twitter.

## Fichiers JSON :
- Résultats complets avec métadonnées

## Fichiers CSV :
- Versions tabulaires des données
- URLs et extraits de tweets
""",
        
        'config/README.md': """# Configuration

Fichiers de configuration du projet.

- `config.py` - Configuration principale
""",
        
        'docs/README.md': """# Documentation

Documentation et rapports du projet.

- `task_atelier2.docx` - Description des tâches
"""
    }
    
    for filepath, content in readme_contents.items():
        readme_path = base_path / filepath
        readme_path.write_text(content, encoding='utf-8')
        print(f"  ✓ Créé: {filepath}")
    
    # 7. Générer un résumé
    print("\n" + "="*70)
    print("📊 RÉSUMÉ DE L'ORGANISATION")
    print("="*70)
    
    summary = {}
    for folder in folders.keys():
        folder_path = base_path / folder
        if folder_path.exists():
            files = [f for f in folder_path.iterdir() if f.is_file() and not f.name.startswith('.')]
            
            # Compter par type
            types = {}
            total_size = 0
            for f in files:
                ext = f.suffix.lower() or 'sans_extension'
                types[ext] = types.get(ext, 0) + 1
                total_size += f.stat().st_size
            
            summary[folder] = {
                'count': len(files),
                'types': types,
                'size': total_size
            }
    
    for folder, info in sorted(summary.items()):
        size_mb = info['size'] / (1024 * 1024)
        print(f"\n📁 {folder}")
        print(f"   Fichiers: {info['count']}")
        print(f"   Taille: {size_mb:.2f} MB")
        if info['types']:
            print(f"   Types: {', '.join([f'{k}({v})' for k, v in info['types'].items()])}")
    
    print("\n" + "="*70)
    print("✨ Organisation terminée avec succès!")
    print(f"💾 Sauvegarde: {backup_folder.name}")
    print("="*70)


if __name__ == "__main__":
    try:
        organize_atelier()
        input("\nAppuyez sur Entrée pour fermer...")
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        input("\nAppuyez sur Entrée pour fermer...")
