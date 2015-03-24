#!/bin/sh

ID=$(curl -s http://127.0.0.1:5000/api/people/foo@example.com | python -m json.tool | grep _id | cut -d: -f2 | cut -d'"' -f2)

curl \
	-s \
	-X PUT \
	-H 'Content-Type: application/json'  http://127.0.0.1:5000/api/people/$ID \
	-d '{"email": "foo@example.com","firstname": "foo", "lastname": "bar", "born": "Fri, 04 Aug 1961 00:00:00 GMT"}' \
		| python -m json.tool


curl -s http://127.0.0.1:5000/api/people/foo@example.com | python -m json.tool
