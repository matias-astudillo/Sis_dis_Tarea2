FROM python:3.9
WORKDIR /app

RUN pip install kafka-python elasticsearch

COPY ./notification_service.py .

CMD ["python", "notification_service.py"]