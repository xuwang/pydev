#!/bin/bash

curl -s http://127.0.0.1:5000/api/people/docs/spec.json | python -m json.tool