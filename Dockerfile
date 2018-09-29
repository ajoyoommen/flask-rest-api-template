FROM python:3.6.6-slim-stretch

RUN apt-get update

RUN mkdir app
ADD . /app
WORKDIR /app
RUN pip3 install -r sample_project/requirements.txt
EXPOSE 8000
ENTRYPOINT ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app"]
