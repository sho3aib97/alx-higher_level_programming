#!/usr/bin/python3
''' load from json file '''

import json

def load_from_json_file(filename):
   ''' json load '''
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
