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

# How to use it on a fresh Google Compute Engine instance? 🤔
## Create a Google Compute Engine instance
Create an instance with the following options:
* Machine configurations
    * Series: N1
    * Machine type: n1-standard-1 (1 vCPU, 3.75 GB memory)
* Boot disk
    * Ubuntu 16.04 LTS
* Firewall
    * Allow HTTP traffic
    * Allow HTTPS traffic

## Use the setup.sh script
You must create 2 files inside the GCE instance:
1. Move the content of the setup.sh file of this repository inside the GCE instance. Call it setup.sh
2. Create a .env file on the same directory as the setup.sh. This file must define some variables, here is an example
```
# Django
SECRET_KEY=l=<DJANGO_KEY>
DEBUG=1
ALLOWED_HOSTS=127.0.0.1,<YOUR_GCE_INSTANCE_IP>

# Django Testing
TOKEN_TESTING=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U

# Database
DB_HOST=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
DB_PORT=3306

# Coveralls
# NOTE: just put some random characters if you are not going to use Coveralls. Or remove it
COVERALLS_REPO_TOKEN=<COVERALLS_TOKEN>
```
>💡 It's important on the ALLOWED_HOSTS variable to do not place spaces between the IP's and just put a coma. You must put a coma between the IP's.
3. Run the setup.sh with the following command:
```sh
yes Y | sh setup.sh
```
4. Wait for the installation and *voilà*. Now you have 2 containers running within your GCE instance. One is running the API and the other a MySQL database.
5. Now if you want to try the endpoints you just have to use the following link: <YOUR_GCE_INSTANCE_IP>:8000/

>💡 This setup is not suitable for a real production app. For a real production app you should consider changing the "command" within the docker-compose file to "command: gunicorn project.wsgi -b 0.0.0.0:8000", within other changes. Check the [Django deployment checklist](https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/) to set up your project correctly

