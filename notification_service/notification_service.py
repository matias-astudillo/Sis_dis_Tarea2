from kafka import KafkaConsumer
import smtplib
from elasticsearch import Elasticsearch
import time

es = Elasticsearch(['http://elasticsearch:9200'])

def send_email(order_id, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_user = 'testsd454@gmail.com'
    smtp_password = '** ** **'

    # Enviar el correo
    with smtplib.SMTP(smtp_server, 587) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, 
                        f"Subject: Pedido Completado\nTu pedido con ID {order_id} ha sido completado.")

def run():
    consumer = KafkaConsumer('completed', bootstrap_servers='kafka:9092', group_id='email_sender_group', api_version=(0, 10, 2))

    for message in consumer:
        order_data = message.value.decode().split(',')
        order_id = order_data[0]
        email = order_data[7]
        current_time = time.time()
        past_time = float(order_data[-2])
        elapsed_time = current_time - past_time
        document = {
        'Tiempo_Proc_total': elapsed_time
        }
        es.index(index='metricas', body=document)

        # Enviar el correo
        send_email(order_id, email)

if __name__ == '__main__':
    run()