FROM python:3.9
WORKDIR /app

RUN pip install kafka-python elasticsearch

COPY ./delivered_service.py .

CMD ["python", "delivered_service.py"]