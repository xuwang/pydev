#!/usr/bin/env python
"""
Usage:
  ppctl show <email>
  ppctl show -i <id>
  
Arguments:
  <email>   Person's email
  <id>      Person's id
  
Examples:
  ppcli show foobar
  ppcli show -i $(ppcli id 'foo@example.com')  

"""

from docopt import docopt
import pp_util

def main(args):
    #print(args)
    if args['<email>']:
        show_people(args['<email>'])
    elif args['<id>']:
        show_people_id(args['<id>'])

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)