FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir requests

FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir requests

CMD ["python3", "app.py"]