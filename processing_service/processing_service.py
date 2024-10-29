from kafka import KafkaConsumer, KafkaProducer
import time
import random

def run():
    consumer = KafkaConsumer('processing', bootstrap_servers='kafka:9092', group_id='processing_group', api_version=(0, 10, 2))
    producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(0, 10, 2))

    for message in consumer:
        current_time = time.time()
        order = message.value.decode()
        order = f"{order},{current_time},{current_time}"

        time.sleep(random.uniform(0.5, 1.5))
        producer.send('status_managment', value=order.encode())

if __name__ == '__main__':
    run()
