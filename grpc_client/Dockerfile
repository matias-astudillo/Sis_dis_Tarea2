FROM python:3.9
WORKDIR /app

RUN pip install grpcio grpcio-tools Flask

COPY ./grpc_client.py .
COPY ./order_management_pb2_grpc.py .
COPY ./order_management_pb2.py .

CMD ["python", "grpc_client.py"]