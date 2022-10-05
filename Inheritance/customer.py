#****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: A7
#       Due Date: 10/18/2021
#       Description: This program creates a class customer.
#
#
#****************************************************************************************************

import Person
class customer(Person.Person):
    def __init__(self, n='*none*', tel='*none*', num='*none*', mail=False):
        Person.Person.__init__(self, n, tel)
        self.__number = num
        self.__mailflag = mail

#****************************************************************************************************

    @property
    def number(self):
        return self.__number

#****************************************************************************************************

    @number.setter
    def number(self, n):
        self.__number = n

#****************************************************************************************************

    @property
    def mail(self):
        return self.__mailflag

#****************************************************************************************************

    @mail.setter
    def mail(self, m):
        self.__mailflag = m

#****************************************************************************************************

    def __str__(self):
        if self.__mailflag:
            string = 'on mailing list'
        else:
            string = 'not on mailing list'

        return f'{self.name} {self.telephone} {self.number} {string}'