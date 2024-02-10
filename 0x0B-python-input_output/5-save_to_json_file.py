#!/usr/bin/python3
''' save obj file '''

import json

def save_to_json_file(my_obj, filename):
    ''' save to json file '''
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
