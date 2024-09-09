
FROM python:3.13.0rc2-slim

COPY main.py .
 
COPY requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]  