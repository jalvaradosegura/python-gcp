#!/bin/bash
# Run this is script with: yes Y | sh setup.sh
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic test"
sudo apt update
sudo apt install docker-ce
# Install docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# give permissions to it
sudo chmod +x /usr/local/bin/docker-compose
# Download the project
sudo git clone https://github.com/jalvaradosegura/python-gcp.git

# Environment file
ENVFILE=.env

# Move it to the project folder
sudo mv .env python-gcp/

cd python-gcp/

# Execute containers
sudo docker-compose up -d --build
