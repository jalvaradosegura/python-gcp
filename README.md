[![Coverage Status](https://coveralls.io/repos/github/jalvaradosegura/python-gcp/badge.svg?branch=master)](https://coveralls.io/github/jalvaradosegura/python-gcp?branch=master)
# API for Vaccinations and Drugs 💉

# Overview 👀
* API to get, put, delete and post vaccinations and drugs
* API protected with a JWT
* It has 40+ unit tests
* It has Swagger
* Uses Docker 🐳
* Deployed on Google Compute Engine
* It has a Makefile to make life easier and it's also considered a good practice

## docker-compose.yml example ⚙️
> In a real production environment, try to use a .env file for the values of the environment variables within the docker-compose file, just like the [docker documentation](https://docs.docker.com/compose/environment-variables/#the-env-file) suggest.
```yml
version: '3.7'

services:
    web:
        build: .
        command: python /code/manage.py runserver 0.0.0.0:8000
        environment:
            - SECRET_KEY=<A_DJANGO_KEY>
            - DEBUG=1
            - TOKEN_TESTING=<JWT_TOKEN>
            - COVERALLS_REPO_TOKEN=<COVERALLS_TOKEN>
            - DB-HOST=<DB_HOST>
            - DB-USER=<A_USER>
            - DB-PASSWORD=<A_PASSWORD>
            - DB-PORT=3306
            - ALLOWED_HOSTS=127.0.0.1,localhost
        volumes:
            - .:/code
        ports:
            - 8000:8000
        depends_on:
            - db
    db:
        image: mysql:5.7
        restart: always
        environment:
            MYSQL_DATABASE: <DB_HOST>
            MYSQL_USER: <A_USER>
            MYSQL_PASSWORD: <A_PASSWORD>
            MYSQL_ROOT_PASSWORD: <A_PASSWORD>
        ports:
            - '3306:3306'
        expose:
            - '3306'
        volumes:
            - my-db:/var/lib/mysql
            
volumes:
    my-db:
```
## Compute Engine instance configuration ⚙️
* Machine configurations
  * Series: N1
  * Machine type: n1-standard-1 (1 vCPU, 3.75 GB memory)
* Boot disk
  * Ubuntu 16.04 LTS
* Firewall
  * Allow HTTP traffic
  * Allow HTTPS traffic
