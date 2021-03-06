#!/bin/sh

ID=$(curl -s http://127.0.0.1:5000/api/people/foo@example.com | python -m json.tool | grep _id | cut -d: -f2 | cut -d'"' -f2)

curl \
	-s \
	-X PATCH \
	-H 'Content-Type: application/json'  http://127.0.0.1:5000/api/people/$ID \
	-d '{"born": "Fri, 04 Aug 1961 00:00:01 GMT"}' \
		| python -m json.tool

curl -s http://127.0.0.1:5000/api/people/foo@example.com | python -m json.tool
