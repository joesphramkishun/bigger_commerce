
FROM python:3.6.3-stretch

EXPOSE 8000

WORKDIR /var/lib/bigger_commerce
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ENV PYTHONPATH="/var/lib/bigger_commerce"  PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
CMD ["/bin/bash", "-c", "gunicorn --bind 0.0.0.0:8000 --workers 3 app.bigger_commerce:__hug_wsgi__", ">> logs/hug_me.log 2>&1"]
