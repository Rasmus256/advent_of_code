FROM python:3.11-slim-buster AS test

ADD main.py .
ADD test.py .
ADD test_input.csv .
ADD requirements.txt .

RUN pip install -r ./requirements.txt

RUN ["python", "./test.py"]

RUN echo "TEST PASSED! HURRAY!"

FROM python:3.11-slim-buster AS prod
COPY --from=test main.py .
COPY --from=test requirements.txt .
ADD puzzle_input.csv .

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]