#!/usr/bin/env python
"""
Usage:
  ppctl add <data> 
  ppctl add (-f | --file) <file> 
  ppctl add --email=<email> [--firstname=<firstname>] [--lastname=<lastname>]
  
Options:
  -f --file     Data in file.
  
Arguments:
  <data>        Data in json format. 
                E.g. '[{"email": "foobar@example.com", "firstname": "foo", "lastname": "bar"},]'
  <file>        A data file in json format.
  <email>       Person's email, required must unique.
  <firstname>   Person's firstname.
  <lastname>    Person's lastname.
  
Examples:
  ppcli add '[{"email": "foobar@example.com", "firstname": "foo", "lastname": "bar"}]'
  ppcli add --email=foobar@example.com

"""
from docopt import docopt
import pp_util

def main(args):
    #print(args)
    if args['<data>']:
        add_people_data(args['<data>'])
    elif args['<file>']:
        add_people_file(args['<file>'])
    elif args['<username>']:
        add_people(args[args])
        
if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)