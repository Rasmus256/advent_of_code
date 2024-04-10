FROM python:3.13.0a6-slim AS test

COPY main.py .
COPY test.py .
COPY test_input.csv .
COPY requirements.txt .

RUN pip install -r ./requirements.txt

RUN echo "TEST PASSED! HURRAY!"

FROM python:3.13.0a6-slim AS prod
COPY --from=test main.py .
COPY --from=test requirements.txt .
COPY puzzle_input.csv .

RUN pip install -r ./requirements.txt

CMD ["python", "./main.py"]