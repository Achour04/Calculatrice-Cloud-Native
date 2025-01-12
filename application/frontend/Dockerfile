# Utiliser une image de base légère de Nginx
FROM nginx:alpine

# Copier les fichiers frontend (HTML, CSS, JS) dans le répertoire par défaut de Nginx
COPY . /usr/share/nginx/html


# Copier le fichier nginx.conf personnalisé pour configurer le proxy_pass
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exposer le port 80 pour le serveur Nginx
EXPOSE 80

# Commande par défaut pour démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]
