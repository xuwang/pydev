#!/bin/sh

curl \
	-s \
	-H 'Content-Type: application/json'  http://127.0.0.1:5000/people \
	-d '[{"firstname": "barack", "lastname": "obama"}, {"firstname": "mitt", "lastname": "romney"}]' \
		| python -m json.tool
