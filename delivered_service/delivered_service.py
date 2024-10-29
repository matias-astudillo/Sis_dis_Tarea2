from kafka import KafkaConsumer, KafkaProducer
import time
import random
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://elasticsearch:9200'])

def run():
    consumer = KafkaConsumer('delivered', bootstrap_servers='kafka:9092', group_id='delivered_group', api_version=(0, 10, 2))
    producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(0, 10, 2))

    for message in consumer:
        current_time = time.time()
        order = message.value.decode()
        parts = order.split(',')
        past_time = float(parts[-1])
        elapsed_time = current_time - past_time
        order = f"{','.join(parts[:-1])},{current_time}"

        document = {
        'Latencia_Env-Ent': elapsed_time
        }

        es.index(index='metricas', body=document)

        time.sleep(random.uniform(0.5, 1.5))
        producer.send('status_managment', value=order.encode())

if __name__ == '__main__':
    run()
