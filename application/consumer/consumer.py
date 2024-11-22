import pika
import json
import redis

# Connexion à RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Connexion à Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Déclaration de la file RabbitMQ
channel.queue_declare(queue='calculation_queue')

# Fonction pour effectuer l'opération
def perform_calculation(data):
    num1 = data["num1"]
    num2 = data["num2"]
    operator = data["operator"]
    
    if operator == 'addition':
        return num1 + num2
    elif operator == 'soustraction':
        return num1 - num2
    elif operator == 'multiplication':
        return num1 * num2
    elif operator == 'division':
        if num2 == 0:
            return 'Erreur: Division par zéro'
        return num1 / num2
    else:
        return 'Opérateur invalide'

# Callback pour traiter les messages RabbitMQ
def callback(ch, method, properties, body):
    # Décoder le message JSON
    data = json.loads(body)
    calc_id = data['calc_id']
    
    print(f" [x] Reçu : {data}")

    # Effectuer le calcul
    result = perform_calculation(data)

    # Stocker le résultat dans Redis
    redis_client.set(calc_id, result)
    print(f" [x] Résultat de {calc_id}: {result}")

    # Accuser la réception du message
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Consommer les messages de la queue RabbitMQ
channel.basic_consume(queue='calculation_queue', on_message_callback=callback)

print(' [*] Attente de messages. Pour quitter appuyez sur CTRL+C')
channel.start_consuming()
