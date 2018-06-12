FROM daocloud.io/python:3.6.0
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN apt-get update && apt-get -y install vim && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app

COPY Pipfile /usr/src/app/Pipfile
COPY Pipfile.lock /usr/src/app/Pipfile.lock

RUN pip install --upgrade pip ; pip install pipenv ; pipenv install && python3_link=$(which python3) && rm $python3_link && ln -s $(pipenv --py) $python3_link

COPY . /usr/src/app

CMD ["python3", "mock_broker.py"]
