# Projet Calculatrice Cloud Native

Bienvenue dans le projet **Calculatrice Cloud Native** ! Ce projet a pour objectif de concevoir et déployer une application cloud-native capable de gérer des opérations mathématiques simples, tout en explorant les concepts de virtualisation, de conteneurisation et d'orchestration dans Kubernetes.

## Auteur
**Othmane Achour** (monome)

---

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

### Déploiement :
1. Appliquer les fichiers de namespace :
   ```bash
   kubectl apply -f namespace.yaml
   
