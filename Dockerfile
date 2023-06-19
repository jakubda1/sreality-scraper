FROM python:3.8-slim-buster
LABEL authors="David Jakubec"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/reality-app

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles

EXPOSE 8080
WORKDIR /$APP_HOME
COPY . $APP_HOME/.
RUN pip install -r $APP_HOME/requirements.txt

RUN chmod +x $APP_HOME/docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]