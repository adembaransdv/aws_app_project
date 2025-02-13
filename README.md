# Projet de Téléchargement d'Images avec Flask et AWS S3

Ce projet permet de télécharger des images vers un bucket AWS S3 en utilisant une application backend développée avec Flask et une interface frontend simple en HTML et JavaScript.

## Structure du Projet

- **Backend (`/backend`)**
  - `app.py`: Contient le code principal de l'application Flask.
  - `config.py`: Gère la configuration des variables d'environnement pour AWS.
  - `requirements.txt`: Liste des dépendances Python nécessaires.

- **Frontend (`/frontend`)**
  - `index.html`: Page HTML pour l'interface utilisateur.
  - `upload.js`: Script JavaScript pour gérer le téléchargement des fichiers.

## Fonctionnalités

- **Téléchargement de fichiers** : Permet aux utilisateurs de télécharger des fichiers via une interface web simple.
- **Stockage sur AWS S3** : Les fichiers téléchargés sont stockés dans un bucket S3 avec une URL publique accessible.

## Configuration

### Backend

1. **Variables d'environnement** :
   - Créez un fichier `.env` dans le répertoire `/backend` avec les variables suivantes :
     ```
     AWS_ACCESS_KEY_ID=votre_access_key_id
     AWS_SECRET_ACCESS_KEY=votre_secret_access_key
     ```

2. **Installation des dépendances** :
   - Exécutez la commande suivante pour installer les dépendances nécessaires :
     ```bash
     pip install -r requirements.txt
     ```

3. **Exécution de l'application** :
   - Lancez l'application Flask avec la commande :
     ```bash
     python app.py
     ```
4. **Modifiez le CORS** :
   - Modifiez le CORS dans le fichier app.py en fonction de votre infrastructure.


### Frontend

1. **Modifiez les adresses IP** :
   - Modifiez l'adresse IP dans l'upload.js, en y mettant le DNS publique de l'instance EC2

- Ouvrez le fichier `index.html` dans votre navigateur pour accéder à l'interface de téléchargement.

## Utilisation

1. **Télécharger une image** :
   - Sélectionnez un fichier image à l'aide du bouton "Choisir un fichier".
   - Cliquez sur "Envoyer" pour télécharger l'image vers le bucket S3.
   - Une alerte s'affichera pour confirmer le succès du téléchargement.

## Dépendances

- **Flask** : Framework web pour le backend.
- **Boto3** : SDK AWS pour interagir avec les services AWS.
- **python-dotenv** : Gestion des variables d'environnement.

## Remarques

- Assurez-vous que votre bucket S3 est correctement configuré pour accepter les téléchargements publics.
