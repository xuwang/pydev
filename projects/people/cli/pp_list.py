#!/usr/bin/env python
"""
Usage:
    ppcli.py list [options]

Options
    -p, --pretty-print  Pretty print the resoult
    -h, --help          Show this page

"""

from docopt import docopt
import json
from pp_util import *

def main(args):
    r = api_get(args['api_url'], args['resource'])
    pp_json(r.json(), args['--pretty-print'])
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)