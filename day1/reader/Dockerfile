
FROM python:3.11-slim-buster

ADD main.py .
ADD puzzle_input.csv .

RUN pip install stomp.py
 
CMD ["python", "./main.py"] 