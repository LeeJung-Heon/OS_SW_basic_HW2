FROM python:3.13.3

RUN pip3 install django

WORKDIR /usr/src/app

COPY . .

WORKDIR ./django_project

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

EXPOSE 8000
