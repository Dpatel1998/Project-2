#!/bin/bash

# install requirements/create venv
sudo apt-get update
sudo apt-get install python3-venv python3-pip -y 

python3 -m venv venv 
source venv/bin/activate

pip3 install -r test_requirements.txt

# pytest coverage services-1 
cd services-1
python3 -m pytest --cov=application --cov-report term-missing
cd ..

# pytest coverage services-2
cd services-2
python3 -m pytest --cov=application --cov-report term-missing
cd ..

# pytest coverage services-3 
cd services-3
python3 -m pytest --cov=application --cov-report term-missing
cd ..

# pytest coverage services-4 
cd services-4
python3 -m pytest --cov=application --cov-report term-missing
cd ..