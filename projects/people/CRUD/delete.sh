#!/bin/bash

ID=$(curl -s http://127.0.0.1:5000/api/people/foo1@example.com | python -m json.tool | grep _id | cut -d: -f2 | cut -d'"' -f2)


if [ -n "$ID" ]; then
	echo "Delete people/$ID"
	curl -X DELETE -s http://127.0.0.1:5000/api/people/$ID
fi

curl -s http://127.0.0.1:5000/api/people/ | python -m json.tool