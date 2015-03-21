#!/bin/bash

#curl -s -D - http://127.0.0.1:5000/people/obama -o /dev/null

LNAME=${1}
curl -s http://127.0.0.1:5000/people/${LNAME} | python -m json.tool