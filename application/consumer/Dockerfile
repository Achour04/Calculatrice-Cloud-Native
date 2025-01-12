# Utilisation de l'image officielle Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code du Consumer
COPY . .

# Définir la commande pour démarrer le Consumer
CMD ["python", "consumer.py"]
