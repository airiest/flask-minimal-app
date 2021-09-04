FROM python:3.9.5-slim-buster

RUN mkdir -p /app/config
COPY config/gunicorn_conf.py /app/config/gunicorn_conf.py
COPY requirements.txt /app/requirements.txt
COPY api/ /app/api/
COPY templates/ /app/templates/
COPY static/ /app/static/
COPY flask_app.py /app/flask_app.py

RUN pip install -r /app/requirements.txt

EXPOSE 9101

WORKDIR /app

ENTRYPOINT [ "gunicorn", "flask_app:app" ]
CMD [ "-k", "flask_sockets.worker", "-c", "/app/config/gunicorn_conf.py" ]
