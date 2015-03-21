#!/bin/bash

#curl -s -D - http://127.0.0.1:5000/people/obama -o /dev/null

curl -s http://127.0.0.1:5000/people/ | python -m json.tool