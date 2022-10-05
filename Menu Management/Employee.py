#****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: Employee.py and Driver.py
#       Due Date: 10/11/2021
#       Description: This program creates a class Employee.
#
#
#****************************************************************************************************

class Employee:
    def __init__(self, name = '*none*', dep = '*none*', job = '*none*', id = 0):
        self.__name = name
        self.__department = dep
        self.__job_title = job
        self.__id = id

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
    def department(self):
        return self.__department

#****************************************************************************************************

    @department.setter
    def department(self, d):
        self.__department = d

#****************************************************************************************************

    @property
    def jobtitle(self):
        return self.__job_title

#****************************************************************************************************

    @jobtitle.setter
    def jobtitle(self, jt):
        self.__job_title = jt

#****************************************************************************************************

    @property
    def id(self):
        return self.__id

#****************************************************************************************************

    @id.setter
    def id(self, ident):
        self.__id = ident

#****************************************************************************************************

    def __str__(self):
            return f'Name: {self.__name} \nID number: {self.__id} \n' \
                f'Department: {self.__department} \nJob Title: {self.__job_title} \n'
