#!/usr/bin/env python
"""
Usage:
  ppctl id <email>
  
Arguments:
  <email>   Person's email

"""

from docopt import docopt
import pp_util

def main(args):
    #print(args)
    get_id(args['<email>'])
        

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)