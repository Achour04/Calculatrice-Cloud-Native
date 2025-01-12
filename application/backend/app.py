from flask import Flask, request, jsonify
import redis
import pika
import uuid
import json
import os
# Initialisation de Flask
app = Flask(__name__)



# Variables d'environnement pour RabbitMQ et Redis
rabbitmq_host = os.getenv("RABBITMQ_HOST", "rabbitmq")
redis_host = os.getenv("REDIS_HOST", "redis-service")

# Configuration de Redis
#redis_host = "localhost"  # À changer dans Kubernetes (service name)
redis_port = 6379
redis_db = redis.Redis(host=redis_host, port=redis_port, db=0)

# Configuration de RabbitMQ
#rabbitmq_host = "rabbitmq"  # À changer dans Kubernetes (service name)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host,heartbeat=60))
channel = connection.channel()
channel.queue_declare(queue='calculs')

# Endpoint pour effectuer un calcul
@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get("operation")
    operands = data.get("operands")

    if not operation or not operands or not isinstance(operands, list) or len(operands) < 2:
        return jsonify({"error": "Invalid input"}), 400

    # Génération d'un ID unique pour l'opération
    operation_id = str(uuid.uuid4())

    # Création d'un message pour RabbitMQ
    message = {
        "id": operation_id,
        "operation": operation,
        "operands": operands
    }
    channel.basic_publish(exchange='', routing_key='calculs', body=json.dumps(message))

    # Retourner l'ID au client
    return jsonify({"id": operation_id, "message": "Calculation added to queue."}), 200

# Endpoint pour récupérer un résultat
@app.route('/api/result/<operation_id>', methods=['GET'])
def get_result(operation_id):
    result = redis_db.get(operation_id)
    if result is None:
        return jsonify({"error": "Result not found"}), 404

    return jsonify({"id": operation_id, "result": float(result)}), 200

# Démarrer le serveur Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
