FROM python:3.9

LABEL maintainer Adrian Smith
ENV APP_HOME /app

WORKDIR ${APP_HOME}
ENV PYTHONPATH "${PYTHONPATH}:${APP_HOME}/src"

COPY requirements.txt /tmp/requirements.txt

RUN \
    echo "Installing requirements" \
    && pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

COPY . /app
