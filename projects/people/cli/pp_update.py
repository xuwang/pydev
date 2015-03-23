#!/usr/bin/env python
"""
Usage:
  ppctl update (--email=<email> | --id=<id>) <data> 
  ppctl update (--email=<email> | --id=<id>) -f <file> 
  
Options:
  -f --file     Data in file.
  
Arguments:
  <data>        Data in json format. 
                E.g. '[{"firstname": "foo", "lastname": "bar"},]'
  <file>        A data file in json format.
  <email>       Person's email, required must unique.
  <id>          Person's ID.

"""
from docopt import docopt
import pp_util

def main(args):
    #print(args)
    
    if args['<email>']:
        id = get_id(args['<email>'])
    else:
        id = args['<id>']
        
    if args['<data>']:
        update_people_data(id, args['<data>'])
    elif args['<file>']:
        update_people_file(args[id, '<file>'])

if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)