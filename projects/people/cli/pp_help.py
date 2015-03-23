#!/usr/bin/env python
"""
Usage:
  ppctl help [<command>]
  
"""

from docopt import docopt
from subprocess import call

def main(args):
    if args['<command>']:
        exit(call(['python', "pp_%s.py" % args['<command>'], '--help']))
    else:
        exit(call(['python', 'ppctl', '--help']))
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)