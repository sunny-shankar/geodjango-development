FROM python:3.9-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update &&\
    apt-get install -y netcat gcc  postgresql postgresql-contrib postgis postgresql-13-postgis-3 binutils libproj-dev gdal-bin python3-gdal

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python","manage.py","runserver","0.0.0.0:8080" ]