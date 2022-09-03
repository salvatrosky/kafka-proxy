#!/bin/sh

hostIP='0.0.0.0'
port='8000'
#Available enviroments: development, production
enviroment='production'

if [ "$enviroment" = "development" ]; then
    FLASK_ENV="development"
    python3 run.py
else
if [ -z "$hostIP" ] && [ -z "$port" ]; then
    echo "Yo have to set hostIP and port in this file"
else 
    uwsgi --socket $hostIP:$port --wsgi-file run.py --callable app --processes 4 --threads 2 --stats $hostIP:9191 --protocol=http 
fi 
fi