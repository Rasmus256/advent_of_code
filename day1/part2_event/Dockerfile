FROM  python:3.11-slim-buster

ADD main.py .
ADD puzzle_input.csv .

ADD requirements.txt .

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]  