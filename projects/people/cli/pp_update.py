#!/usr/bin/env python
"""
Usage:
  ppctl update (--email=<email> | --id=<id>) <data> 
  ppctl update (--email=<email> | --id=<id>) -f <file> 
  
Options:
  -f --file     Data in file.
  
Arguments:
  <data>        Data in json format. 
                E.g. '[{"firstname": "foo", "lastname": "bar"},]'
  <file>        A data file in json format.
  <email>       Person's email, required must unique.
  <id>          Person's ID.

"""
from docopt import docopt
from pp_util import *
import json

def main(args):
    #print(args)
    data = ''
    if args['<data>']:
        data = args['<data>']
    elif args['<file>']:
        with open( args['<file>']) as data_file:
            data = data_file.read()

    if args.has_key('<email>'):
        resource = "%s/%s" % (args['resource'], args['<email>'])
        id = get_id(args['api_url'], resource)
    else:
        id = args['<id>']

    resource = "%s/%s" % (args['resource'], id)
    r = api_patch(args['api_url'], resource, data)
    pp_json(r.json(), True):
        
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)