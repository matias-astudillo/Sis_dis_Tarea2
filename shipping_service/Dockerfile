FROM python:3.9
WORKDIR /app

RUN pip install kafka-python elasticsearch

COPY ./shipping_service.py .

CMD ["python", "shipping_service.py"]