#****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: A7
#       Due Date: 10/18/2021
#       Description: This program creates a class Person.
#
#
#****************************************************************************************************

class Person:
    def __init__(self, n = '*none*', tel = '*none*'):
        self.__name = n
        self.__telephone = tel

#****************************************************************************************************

    @property
    def name(self):
        return self.__name

#****************************************************************************************************

    @name.setter
    def name(self, n):
        self.__name = n

#****************************************************************************************************

    @property
    def telephone(self):
        return self.__telephone

#****************************************************************************************************

    @telephone.setter
    def telephone(self, t):
        self.__telephone = t