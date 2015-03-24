#!/usr/bin/env python
"""
Usage:
    ppctl show [-p] (<email>|<id>)

Options:
    -p, --pretty-print  Pretty print the resoult
    -h, --help          Show this page
  
Arguments:
    <email>   Person's email
    <id>      Person's id
  
Examples:
    ppctl show 'foo@example.com'
    ppctl show $(ppctl id 'foo@example.com')  

"""

from docopt import docopt
from pp_util import *

def main(args):
    if args.has_key('<email>'):
        resource = "%s/%s" % (args['resource'], args['<email>'])
    else:
        resource = "%s/%s" % (args['resource'], args['<id>'])
        
    r = api_get(args['api_url'], resource)
    pp_json(r.json(), args['--pretty-print'])
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)