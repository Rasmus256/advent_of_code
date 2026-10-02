
FROM python:3.14.8-slim

COPY main.py .
 
COPY requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]  