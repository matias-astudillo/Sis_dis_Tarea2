import grpc
from concurrent import futures
from kafka import KafkaProducer, KafkaConsumer
from order_management_pb2 import OrderResponse, OrderStatusResponse
import order_management_pb2_grpc
import time
import uuid
from elasticsearch import Elasticsearch

es = Elasticsearch(['http://elasticsearch:9200'])

class OrderManagementService(order_management_pb2_grpc.OrderManagementServicer):
    def __init__(self, kafka_producer, consumer):
        self.producer = kafka_producer
        self.consumer = consumer

    def CreateOrder(self, request, context):
        document = {
        'Pasarela_Pago': request.payment_gateway,
        'Marca_Tarjeta': request.card_brand,
        'Banco': request.bank
        }
        es.index(index='analitica', body=document)
        order_id = str(uuid.uuid4())
        order_data = f"{order_id},{request.product_name},{request.price},{request.payment_gateway},{request.card_brand},{request.bank},{request.shipping_direction},{request.email}"
        self.producer.send('status_managment', value=order_data.encode())
        return OrderResponse(order_id=order_id)

    def GetOrderStatus(self, request, context):
        # Enviar el ID del pedido al microservicio que maneja los estados
        order_id = request.order_id
        self.producer.send('status_managment', value=order_id.encode())
        
        status = 'unknown'
        
        # Leer mensajes del topic "state_responses" hasta encontrar el que corresponde al pedido solicitado
        for message in self.consumer:
            response_data = message.value.decode().split(',')
            status = response_data[1]
            if response_data[0] == order_id:
                break
            continue
                
        # Si el estado es "unknown", se devuelve que el pedido no existe
        if status == 'unknown':
            return OrderStatusResponse(status='Este pedido no existe')
        
        return OrderStatusResponse(status=f'El estado en el que se encuentra el pedido es: {status}')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kafka_producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(0, 10, 2))
    consumer = KafkaConsumer('order_status_responses', bootstrap_servers='kafka:9092', group_id='grpc_group', api_version=(0, 10, 2))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementService(kafka_producer, consumer), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
