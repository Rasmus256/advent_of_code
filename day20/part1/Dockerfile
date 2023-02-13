FROM  python:3.11-slim-buster

ADD main.py .
ADD edges.csv .
ADD requirements.txt .

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python","./main.py"]
