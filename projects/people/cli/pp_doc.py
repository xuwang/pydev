#!/usr/bin/env python
"""
Usage:
    ppctl doc [options]

Options:
    -p, --pretty-print  Pretty print the resoult
    -h, --help          Show this page
"""

from docopt import docopt
from pp_util import *

def main(args):
    resource = "%s/%s" % (args['resource'], 'docs/spec.json')
    r = api_get(args['api_url'], resource)
    pp_json(r.json(), args['--pretty-print'])
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)