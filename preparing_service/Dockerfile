FROM python:3.9
WORKDIR /app

RUN pip install kafka-python elasticsearch

COPY ./preparing_service.py .

CMD ["python", "preparing_service.py"]