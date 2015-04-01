#!/usr/bin/env python
"""
Usage:
  ppctl update (--email=<email> | --id=<id>) <data> 
  ppctl update (--email=<email> | --id=<id>) -f <file> 
  ppctl update --help
  
Options:
  -f --file     Data in file.
  -h, --help    Show this page.
  
Arguments:
  <data>        Data in json format. 
                E.g. '[{"firstname": "foo", "lastname": "bar"},]'
  <file>        A data file in json format.
  <email>       Person's email, required must unique.
  <id>          Person's ID.

"""
from docopt import docopt
from pp_util import api_patch, get_id, pp_json
import json
import sys

def main(args):
    data = ''
    if args['<data>']:
        data = args['<data>']
    elif args['<file>']:
        with open( args['<file>']) as data_file:
            data = data_file.read()

    if args['--email']:
        resource = "%s/%s" % (args['resource'], args['--email'])
        id = get_id(args['api_url'], resource)
    else:
        id = args['--id']

    resource = "%s/%s" % (args['resource'], id)
        
    try:
        r = api_patch(args['api_url'], resource, data)
        pp_json(r.json(), True)
        pass
    except ValueError,e:
        print(e)
        print(__doc__)
        sys.exit(1)
        
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)