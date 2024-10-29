FROM python:3.9
WORKDIR /app

RUN pip install pandas requests

COPY ./traffic_generator.py .
COPY ./Data2_SD.csv .

CMD ["python", "traffic_generator.py"]