Bienvenue dans mon projet de virtualisation on est entrain de faire une calculatrise cloud native
Projet de Othmane Achour (monome)
j'ai commencé par la  partie application :
j'ai créer mon frontend, backend et consumer
j'étais face a un probléme redis , j'arrivé pas a récuperer  le résuletats de mon opération à partir de ma base de données 
donc j'ai essayé de ne pas travailler avec un ID en premier temps
aprés avec le document docker-compose et gcloud j'ai créer mes images frontend , backend et consumer
avec les tagues suivant :
europe-west1-docker.pkg.dev/polytech-dijon/polytech-dijon/consumer-ao-2024:othmane-achour
europe-west1-docker.pkg.dev/polytech-dijon/polytech-dijon/frontend-ao-2024:othmane-achour
europe-west1-docker.pkg.dev/polytech-dijon/polytech-dijon/backend-ao-2024:othmane-achour
pour la partie fondation y'avais pas vraiment des soucis 
pour la partie kubernetes on a créer des replicaset et des fichier service et aussi le fichier ingress
au début j'avis des erreur pour ce qui concerne ingress j'ai fait un ingress de class GCE au lieu de NGNIX 
avec WSL  j'ai télecharger kubectl et j'ai configurer mon fichier .kube 
j'ai apply tout les fichier .yaml 
