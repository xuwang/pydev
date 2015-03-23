#!/usr/bin/env python
"""
Usage:
  ppcli.py list

"""

from docopt import docopt
import pp_util

def main(args):
    #print(args)
    get_list(args)

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)