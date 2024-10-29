FROM python:3.9
WORKDIR /app

RUN pip install grpcio grpcio-tools kafka-python elasticsearch

COPY ./order_management.py .
COPY ./order_management_pb2_grpc.py .
COPY ./order_management_pb2.py .

CMD ["python", "order_management.py"]