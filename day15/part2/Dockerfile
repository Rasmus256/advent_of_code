FROM python:3.13.0a6-slim

COPY main.py .
COPY puzzle_input.csv .
COPY requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["python","-u", "./main.py"]  