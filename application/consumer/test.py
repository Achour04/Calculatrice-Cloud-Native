import redis

try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.ping()  # Vérifie si Redis répond
    print("Connexion Redis réussie !")
except Exception as e:
    print(f"Erreur de connexion Redis : {e}")
