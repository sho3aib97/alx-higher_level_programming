#!/usr/bin/python3
''' class of student to return dict representation of it '''

class Student:
    ''' student class with 3 public attrs and 1 public emthod '''
    def __init__(self, first_name, last_name, age):
        ''' instantiation of class with 3 public attrs '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' show dict representation of instatnce '''
        newDict = {}
        oldDict = self.__dict__

        if isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str):
                    if attr in oldDict:
                        newDict[attr] = oldDict[attr]
                    else:
                        continue
                else:
                    return self.__dict__

            return newDict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        ''' modifying public attraibutes of instance '''
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
