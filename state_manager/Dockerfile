FROM python:3.9
WORKDIR /app

RUN pip install kafka-python elasticsearch

COPY ./state_manager.py .

CMD ["python", "state_manager.py"]