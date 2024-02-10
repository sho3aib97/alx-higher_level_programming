#!/usr/bin/python3
""" writing to a file """

def write_file(filename="", text=""):
    ''' writing to a file '''
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
