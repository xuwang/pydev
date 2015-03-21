#!/bin/bash

PYTHONPATH="${PYTHONPATH}:/vagrant/projects/eve-docs"
export PYTHONPATH

API_LOG="api.log"

#python run.py > ${API_LOG} 2>&1  &
echo "go to http://192.168.33.101:5000/people/docs for API Docs"

python run.py