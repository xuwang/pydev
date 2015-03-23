#!/usr/bin/env python
"""
Usage:
    Comman utility functions shared by pp_*

"""
from docopt import docopt
import json
import pycurl
from StringIO import StringIO
        
def get_list(args):
    raise NotImplementedError
    
def add_people_data(data):
    raise NotImplementedError
    
def add_people_file(file):
    raise NotImplementedError

def update_people_data(id, data):
    raise NotImplementedError
    
def update_people_file(id, file):
    raise NotImplementedError
        
def delete_people(e):
    raise NotImplementedError
    
def delete_people_id(id):
    raise NotImplementedError
    
def show_people(e):
    raise NotImplementedError
    
def show_people_id(id):
    raise NotImplementedError
        
def get_id(e):
    raise NotImplementedError


if __name__ == '__main__':
   docopt(__doc__)