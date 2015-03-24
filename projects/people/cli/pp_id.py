#!/usr/bin/env python
"""
Usage:
  ppctl id <email>
  
Arguments:
  <email>   Person's email

"""

from docopt import docopt
from pp_util import *

def main(args):
    resource = "%s/%s" % (args['resource'], args['<email>'])
    print get_id(args['api_url'], resource)
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)