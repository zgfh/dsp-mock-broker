FROM harbor.geniusafc.com/infra/python:3.6-alpine

WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app

COPY Pipfile /usr/src/app/Pipfile
COPY Pipfile.lock /usr/src/app/Pipfile.lock

RUN pip install --upgrade pip ; pip install pipenv ; pipenv install --deploy --system

COPY . /usr/src/app

CMD ["python3", "mock_broker.py"]
