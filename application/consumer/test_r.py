import pika

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    print("Connexion RabbitMQ réussie !")
    connection.close()
except Exception as e:
    print(f"Erreur de connexion RabbitMQ : {e}")
