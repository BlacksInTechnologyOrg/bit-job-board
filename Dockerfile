FROM python:3.6-alpine

RUN adduser -D bjb

WORKDIR /home/bjb

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY flask_app flask_app
COPY front-end/dist front-end/dist
COPY boot.sh app.py ./
RUN chmod +x boot.sh

ENV FLASK_APP app.py

RUN chown -R bjb:bjb ./
USER bjb

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]