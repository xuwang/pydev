#!/usr/bin/env python
"""
Usage:
  ppctl delete [-p] (<email>|<id>)
  
Arguments:
  <email>   Person's email
  <id>      Person's id
  
Examples:
  ppcli delete foo@example.com

"""

from docopt import docopt
from pp_util import *

def main(args):
    if args.has_key('<email>'):
        resource = "%s/%s" % (args['resource'], args['<email>'])
        id = get_id(args['api_url'], resource)
        resource = "%s/%s" % (args['resource'], id)
    else:
        resource = "%s/%s" % (args['resource'], args['<id>'])
        
    r = api_delete(args['api_url'], resource)
    print("Resource deleted", r.status_code)
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)