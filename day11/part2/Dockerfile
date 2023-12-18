FROM python:3.11-slim-buster

COPY main.py .
COPY puzzle_input.csv .
COPY requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]   