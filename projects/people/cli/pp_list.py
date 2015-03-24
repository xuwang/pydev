#!/usr/bin/env python
"""
Usage:
    ppcli.py list [options]

Options
    -n, --page=<page>   Page number for large list.
    -p, --pretty-print  Pretty print the resoult.
    -h, --help          Show this page

"""

from docopt import docopt
import json
from pp_util import *

def main(args):
    resource = args['resource']
    
    if args["--page"]:
       resource = "%s?page=%s" % (resource, args["--page"])
    r = api_get(args['api_url'], resource)
    pp_json(r.json(), args['--pretty-print'])
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)