#****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: A7
#       Due Date: 10/18/2021
#       Description: This program creates a class sales_associate.
#
#
#****************************************************************************************************

import Person
class sales_associate(Person.Person):
    def __init__(self, n='*none*', tel='*none*', salid='*none*', rate=3):
        Person.Person.__init__(self, n, tel)
        self.__salesId = salid
        self.__commission = rate

#****************************************************************************************************

    @property
    def salesId(self):
        return self.__salesId

#****************************************************************************************************

    @salesId.setter
    def salesId(self, s):
        self.__salesId = s

#****************************************************************************************************

    @property
    def commission(self):
        return self.__commission

#****************************************************************************************************

    @commission.setter
    def commission(self, c):
        self.__commission = c

#****************************************************************************************************

    def __str__(self):
        return f'{self.name} {self.telephone} {self.salesId} {self.commission}'