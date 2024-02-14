#!/usr/bin/python3
''' class of student to return dict representation of it '''

class Student:
    ''' student class with 3 public attrs and 1 public emthod '''
    def __init__(self, first_name, last_name, age):
        ''' instantiation of class with 3 public attrs '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' show dict representation of instatnce '''
        return self.__dict__
