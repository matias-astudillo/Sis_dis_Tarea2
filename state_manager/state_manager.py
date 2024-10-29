from kafka import KafkaConsumer, KafkaProducer
import time
import json
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://elasticsearch:9200'])

def run():
    consumer = KafkaConsumer('status_managment', bootstrap_servers='kafka:9092', group_id='state_manager_group', api_version=(0, 10, 2))
    producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(0, 10, 2))

    # Estados posibles y el siguiente estado correspondiente
    state_transitions = {
        'processing': 'preparing',
        'preparing': 'shipping',
        'shipping': 'delivered',
        'delivered': 'completed'
    }

    # Diccionario para almacenar el estado de cada pedido
    order_status = {}

    for message in consumer:
        order = message.value.decode()
        order_data = order.split(',')
        order_id = order_data[0]
        
        # Verificar si el mensaje es una solicitud de consulta de estado (contiene solo el id del pedido)
        if len(order_data) == 1:
            
            # Buscar el estado actual del pedido solicitado
            current_state = order_status.get(order_id, 'unknown')
            
            # Enviar el estado actual del pedido al topic de respuesta
            response_message = f"{order_id},{current_state}"
            response_message = response_message.encode()
            producer.send('order_status_responses', value=response_message)
            continue

        # Verificar si el pedido es nuevo o ya tiene un estado asignado
        if order_id not in order_status:
            # Si el pedido es nuevo, se inicia en 'processing'
            current_state = 'processing'
            order_status[order_id] = current_state

            # Enviar el pedido al topic 'processing'
            producer.send('processing', value=order.encode())
            continue

        # Si el pedido ya tiene un estado, obtener el estado actual
        current_state = order_status[order_id]

        # Determinar el siguiente estado según las transiciones
        next_state = state_transitions.get(current_state)

        # Actualizar el estado del pedido en el diccionario
        order_status[order_id] = next_state

        # Enviar el mensaje actualizado al siguiente microservicio de estado
        if next_state != 'completed':
            producer.send(next_state, value=order.encode())
        else:
            current_time = time.time()
            past_time = float(order_data[-1])
            elapsed_time = current_time - past_time
            document = {
            'Latencia_Ent-Fin': elapsed_time
            }
            es.index(index='metricas', body=document)
            producer.send(next_state, value=order.encode())



if __name__ == '__main__':
    run()
