#!/usr/bin/env python
"""
Usage:
  ppctl add <data> 
  ppctl add (-f | --file) <file> 
  ppctl add --email=<email> [--firstname=<firstname>] [--lastname=<lastname>]
  ppctl add --help
  
Options:
  -f --file     Data in file.
  --help        Show this page
  
Arguments:
  <data>        Data in json format. 
                E.g. '[{"email": "foobar@example.com", "firstname": "foo", "lastname": "bar"},]'
  <file>        A data file in json format.
  <email>       Person's email, required must unique.
  <firstname>   Person's firstname.
  <lastname>    Person's lastname.
  
Examples:
  ppctl add '[{"email": "foobar@example.com", "firstname": "foo", "lastname": "bar"}]'
  ppctl add --email=foobar@example.com

"""
import sys
from docopt import docopt
from pp_util import api_post, pp_json
import json

def main(args):
    data = ''
    if args['<data>']:
        data = args['<data>']
    elif args['<file>']:
        with open( args['<file>']) as data_file:
            data = data_file.read()
    elif args['--email']:
        item = {}
        item['email'] = args['--email']
        if args['--firstname']:
            item['firstname'] = args['--firstname']
        if args['--lastname']:
            item['lastname'] = args['--lastname']
        data = json.dumps(item)
        
    try:
        add_items(args, data)
        pass
    except ValueError,e:
        print(e)
        print(__doc__)
        sys.exit(1)
        
def add_items(args, data):
    r = api_post(args['api_url'], args['resource'], data)
    pp_json(r.json(), True)
                    
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)