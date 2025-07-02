ARG PYTHON_VERSION=3.10-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

ENV SECRET_KEY "pWe9yO38KHUfxMyxv8hvCqxIopsvCEL1xgRCp7kA4pgvuzIU4b"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "fly.wsgi:application", "--bind", "0.0.0.0:8000"]