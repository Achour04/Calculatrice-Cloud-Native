import pika
import redis
import json
import os

# Variables d'environnement pour RabbitMQ et Redis
rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")
redis_host = os.getenv("REDIS_HOST", "redis-service")

# Configuration de RabbitMQ
#rabbitmq_host = "rabbitmq"  # Nom du service RabbitMQ dans le réseau Docker/Kubernetes
queue_name = "calculs"

# Configuration de Redis
#redis_host = "redis"  # Nom du service Redis dans le réseau Docker/Kubernetes
redis_port = 6379
redis_db = redis.Redis(host=redis_host, port=redis_port, db=0)

# Fonction pour effectuer le calcul
def perform_calculation(operation, operands):
    try:
        if operation == "add":
            return sum(operands)
        elif operation == "subtract":
            return operands[0] - operands[1]
        elif operation == "multiply":
            return operands[0] * operands[1]
        elif operation == "divide":
            return operands[0] / operands[1]
        else:
            raise ValueError("Unsupported operation")
    except Exception as e:
        print(f"Error performing calculation: {e}")
        return None

# Fonction appelée lorsqu'un message est reçu
def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    try:
        # Décoder le message
        message = json.loads(body)
        operation_id = message["id"]
        operation = message["operation"]
        operands = message["operands"]

        # Effectuer le calcul
        result = perform_calculation(operation, operands)

        if result is not None:
            # Stocker le résultat dans Redis
            redis_db.set(operation_id, result)
            print(f"Stored result for ID {operation_id}: {result}")
        else:
            print(f"Failed to calculate result for ID {operation_id}")

    except Exception as e:
        print(f"Error processing message: {e}")

# Connexion à RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
channel = connection.channel()

# Déclarer la queue (si elle n'existe pas déjà)
channel.queue_declare(queue=queue_name)

# Consommer les messages de RabbitMQ
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Waiting for messages. To exit, press CTRL+C")
channel.start_consuming()
