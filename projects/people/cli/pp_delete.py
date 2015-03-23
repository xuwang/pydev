#!/usr/bin/env python
"""
Usage:
  ppctl delete <email>
  ppctl delete -i <id>
  
Arguments:
  <email>   Person's email
  <id>      Person's id
  
Examples:
  ppcli delete foobar
  ppcli delete -i $(ppcli id 'foo@example.com')  

"""

from docopt import docopt
import pp_util

def main(args):
    #print(args)
    if args['<email>']:
        delete_people(args['<email>'])
    elif args['<id>']:
        delete_people_id(args['<id>'])

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)