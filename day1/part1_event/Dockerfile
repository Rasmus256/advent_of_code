
FROM python:3.13.0b4-slim

COPY main.py .
 
COPY requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]  