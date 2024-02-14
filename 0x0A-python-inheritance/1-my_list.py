#!/usr/bin/python3
''' class that rearrage lists '''

class Mylist(list):
    ''' class of my arranged lists '''
    def print_sorted(self):
        ''' prints sorted lists (ascending) '''
        print(sorted(self))
