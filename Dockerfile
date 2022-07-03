FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app.py app.py
COPY candidate_model.py candidate_model.py
COPY galenadb.sql galenadb.sql
COPY /templates /templates
COPY /static /static
COPY /uploads /uploads
COPY __init__.py __init__.py

ENV FLASK_APP=app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
