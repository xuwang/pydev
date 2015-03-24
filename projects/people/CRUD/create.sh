#!/bin/sh

curl \
	-s \
	-H 'Content-Type: application/json'  http://127.0.0.1:5000/people \
	-d '[{"email": "foo@example.com","firstname": "foo", "lastname": "bar"}, {"email": "foo1@example.com","firstname": "foo1", "lastname": "bar1"}]' \
		| python -m json.tool
