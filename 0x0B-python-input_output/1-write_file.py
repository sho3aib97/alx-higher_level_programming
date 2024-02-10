#!/usr/bin/python3
""" writing to a file """

def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
