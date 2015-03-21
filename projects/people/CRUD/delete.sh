#!/bin/bash

LNAME=${1}
curl -X DELETE \
	-s http://127.0.0.1:5000/people/${LNAME} | python -m json.tool