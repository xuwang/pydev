#!/usr/bin/env python
"""
Usage:
    Comman utility functions shared by pp_*

"""
from docopt import docopt
import requests
import json

def api_post(api_url, resource, data):
    validate_json(data)
    headers = {'Content-Type': 'application/json'}
    return requests.post(endpoint(api_url, resource), data, headers=headers)

def api_patch(api_url, resource, data):
    validate_json(data)
    headers = {'Content-Type': 'application/json'}
    return requests.patch(endpoint(api_url, resource), data, headers=headers)

def api_delete(api_url, resource):
    return requests.delete(endpoint(api_url, resource))

def api_get(api_url, resource):
    return requests.get(endpoint(api_url, resource))

def get_id(api_url, resource): 
    # call with projection to reduce data traficing   
    r = api_get(api_url, resource + '?projection={"_id": 1}')
    if r.status_code == 200:
        return r.json()['_id']
    else:
        err = pp_json(r.json())
        raise ValueError(err)

def endpoint(api_url, resource):
    return '%s/%s' % (api_url, resource)
    
def validate_json(data):
    json.loads(data)
    
def pp_json(j, pretty=False):
    if pretty:
        print json.dumps(j, sort_keys=True,indent=4, separators=(',', ': '))
    else:
        print json.dumps(j)
  
if __name__ == '__main__':
   docopt(__doc__)