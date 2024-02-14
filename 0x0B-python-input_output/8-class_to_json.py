#!/usr/bin/python3
''' class to json serialization '''

def class_to_json(obj):
    ''' return the obj decription using obj __dict__ '''
    return obj.__dict__
