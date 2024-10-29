FROM python:3.9
WORKDIR /app

RUN pip install kafka-python

COPY ./processing_service.py .

CMD ["python", "processing_service.py"]