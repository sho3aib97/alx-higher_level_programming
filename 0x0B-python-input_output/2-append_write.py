#!/usr/bin/python3
''' append func '''

def append_write(filename="", text=""):
    ''' appending to a file '''
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
