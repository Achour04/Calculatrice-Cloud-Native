# Calculatrice Cloud Native

Bienvenue dans le projet **Calculatrice Cloud Native** ! Ce projet s'inscrit dans le cadre du module **Virtualisation & Cloud Computing** de Polytech Dijon. Il met en œuvre les compétences liées à la virtualisation, la conteneurisation, l'orchestration et les bonnes pratiques cloud-native pour développer et déployer une application cloud-native fonctionnelle.

---

## Auteur
**Nom complet : Othmane Achour**

---

## Objectif du Projet
Créer une application de calculatrice hébergée sur le cloud, respectant les principes cloud-native et utilisant une architecture basée sur des microservices. L'application devra permettre :
- D'effectuer des calculs (addition, soustraction, multiplication, division) via une API RESTful.
- De stocker les résultats de manière persistante avec Redis.
- D'utiliser une file d'attente RabbitMQ pour traiter les calculs de manière asynchrone.
- D'interagir avec une interface utilisateur (frontend).
- De déployer et gérer les ressources à l'aide de Kubernetes et Terraform.

---

## Structure du Projet

Le projet est organisé en trois parties principales :

1. **Fondation** : Définition et provisionnement de l'infrastructure cloud avec Terraform.
2. **Application** : Développement des microservices (frontend, backend, consumer) et gestion des conteneurs Docker.
3. **Kubernetes** : Déploiement des services dans un cluster Kubernetes.

Chaque partie est contenue dans des dossiers spécifiques :
- **foundation/** : Contient les fichiers Terraform pour la gestion de l'infrastructure.
- **application/** : Contient le code source des services et les Dockerfiles.
- **kubernetes/** : Contient les fichiers YAML pour déployer les services dans Kubernetes.

---

## Fonctionnalités de l'Application

1. **Calculs via une API REST** :
   - **POST** : Envoyer une opération à effectuer.
   - **GET** : Récupérer le résultat d'un calcul à partir d'un identifiant.

2. **Persistance des données** :
   - Utilisation de **Redis** pour stocker les résultats.

3. **Traitement asynchrone** :
   - Les calculs sont placés dans une file d'attente **RabbitMQ**, puis consommés et exécutés par un service spécifique (consumer).

4. **Interface Utilisateur** :
   - Un **frontend** permet aux utilisateurs d'envoyer des calculs et de consulter les résultats.

---

## Étapes du Développement

### 1. Fondation (Infrastructure as Code - Terraform)
La fondation est définie via Terraform en utilisant le provider **Scaleway** (cloud français). Les ressources suivantes sont provisionnées :
- Un registre de conteneurs pour stocker les images Docker.
- Un cluster Kubernetes pour déployer les services.
- Une base de données Redis pour stocker les résultats.
- Deux LoadBalancers (développement et production).
- Des entrées DNS pour résoudre les IP des LoadBalancers.



## Description du Projet

Le projet s'articule autour de trois grandes parties : **Application**, **Fondation** et **Orchestration Kubernetes**.

---

## 1. Partie Application

### Services Développés :
- **Frontend** : Interface utilisateur pour entrer les opérations.
- **Backend** : Traitement des opérations envoyées par le frontend.
- **Consumer** : Gestion de l'enregistrement et de la récupération des résultats via une base de données Redis.

### Difficultés Rencontrées :
- **Problème Redis** : La récupération des résultats des opérations via Redis ne fonctionnait pas initialement. La solution temporaire consistait à ne pas utiliser d'ID pour simplifier les tests.
  
### Création des Images Docker :
À l’aide de **Docker Compose** et **Google Cloud**, les images des trois services ont été créées avec les tags suivants :
- **Consumer** : `europe-west1-docker.pkg.dev/polytech-dijon/polytech-dijon/consumer-ao-2024:othmane-achour`
- **Frontend** : `europe-west1-docker.pkg.dev/polytech-dijon/polytech-dijon/frontend-ao-2024:othmane-achour`
- **Backend** : `europe-west1-docker.pkg.dev/polytech-dijon/polytech-dijon/backend-ao-2024:othmane-achour`

---

## 2. Partie Fondation

### Étapes Réalisées :
- **Configuration de l’environnement Docker** : Création et gestion des conteneurs.
- **Résolution des problèmes initiaux liés à la communication entre les services**.

Aucun problème majeur rencontré dans cette partie.

---

## 3. Partie Kubernetes

### Déploiements Créés :
1. **ReplicaSets** pour garantir la disponibilité des pods :
   - **frontend**
   - **backend**
   - **consumer**
2. **Services Kubernetes** pour exposer les déploiements via des **ClusterIP**.
3. **Ingress** pour gérer les routes HTTP et exposer l’application sur Internet.

### Problèmes Rencontrés :
- recupération de l'ID de la base de donnée Redis
- Initialement, un Ingress de classe **GCE** a été utilisé par erreur, ce qui causait des dysfonctionnements. Le problème a été corrigé en passant à un Ingress de classe **NGINX**.

### Configuration et Application :
- Utilisation de **WSL** pour configurer **kubectl** et le fichier `.kube/config`.
- Application des fichiers `.yaml` pour déployer les ressources Kubernetes.

---

## Fichiers Principaux

### Application
- **frontend-replicaset.yaml** : Déploiement du service frontend.
- **backend-replicaset.yaml** : Déploiement du service backend.
- **consumer-replicaset.yaml** : Déploiement du service consumer.

### Services
- **frontend-service.yaml** : Service exposant le frontend.
- **backend-service.yaml** : Service exposant le backend.
- **consumer-service.yaml** : Service exposant le consumer.

### Ingress
- **ingress.yaml** : Configuration des routes HTTP pour l’accès public.

---

## Instructions pour Lancer le Projet

### Pré-requis :
1. Installer **kubectl** et configurer l’accès à un cluster Kubernetes.
2. Cloner le projet et naviguer dans le répertoire `kubernetes`.
<img width="626" alt="Capture d’écran 2025-01-16 15085733333333333" src="https://github.com/user-attachments/assets/21cb7f5c-0721-4f51-8de3-729b5baf5b9e" />


### Déploiement :
1. Appliquer les fichiers de namespace :
   ```bash
   kubectl apply -f namespace.yaml
   
