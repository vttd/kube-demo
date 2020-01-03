FROM python:3.7-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN apt-get update
RUN apt-get install libpq-dev -y

COPY . /code

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
