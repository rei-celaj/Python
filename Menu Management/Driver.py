# ****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: Employee.py and Driver.py
#       Due Date: 10/11/2021
#       Description: This program saves employees in a dictionary
#                    and puts them in a .dat file.
#
#
# ****************************************************************************************************

import Employee as E
import pickle as P

#****************************************************************************************************

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = 'employees.dat'

#****************************************************************************************************

def main():
    choice = 0
    emp_dict = {47899:
                    E.Employee('Susan Myers', 'Accounting', 'Vice President', 47899),
                39119: E.Employee('Mark Jones', 'IT', 'Programmer', 39119),
                81774: E.Employee('Joy Rogers', 'Manufacturing', 'Engineer', 81774)}
    save_employees(emp_dict)

    while choice != 5:
        choice = get_user_choice(emp_dict)

    save_employees(emp_dict)

#****************************************************************************************************

def save_employees(emp_dict):
    try:
        out_file = open(FILENAME, 'wb')
        P.dump(emp_dict, out_file)
        out_file.close()
    except IOError:
        print('File could not be found')

#****************************************************************************************************

def load_employees():
    new_dict = {}
    try:
        in_file = open(FILENAME, 'rb')
        new_dict = P.load(in_file)
    except IOError:
        print('File could not be opened')

    return new_dict

#****************************************************************************************************

def get_user_choice(empdict):
    print('Menu')
    print('-' * 25)
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an existing employee')
    print('4. Delete an employee')
    print('5. Quit the program\n')

    try:
        choice = input('Enter your choice: ')
        choice = int(choice)
        if choice == LOOK_UP:
            old_dict = load_employees()
            look_up(old_dict)
        elif choice == ADD:
            add(empdict)
        elif choice == CHANGE:
            change(empdict)
        elif choice == DELETE:
            delete(empdict)
        elif choice == QUIT:
            print('Goodbye')
        else:
            print('choice is incorrect. Please try again.')
    except ValueError:
        print(f'choice: {choice} is not an integer. Please try again')
        choice = 0

    return choice

#****************************************************************************************************

def look_up(empdict):
    flag = True

    while flag:
        try:
            id = int(input('Enter an employee ID number: '))
            if id in empdict.keys():
                print(empdict[id])
                flag = False
            else:
                print('Employee number invalid. Please try again.')
        except IOError:
            print('Only integers are accepted. Please try again.')

#****************************************************************************************************

def add(empdict):
        newID = int(input('Enter employee ID: '))
        if newID not in empdict.keys():
            newName = input('Enter employee name: ')
            newDep = input('Enter employee department: ')
            newTitle = input('Enter employee job title: ')
            newEmpt = E.Employee(newName, newDep, newTitle, newID)
            empdict[newID] = newEmpt
            print('Employee added successfully')
        else:
            print('Employee ID already exists. Please try again')

#****************************************************************************************************

def change(empdict):
    flag = True
    while flag:
        id = int(input('Enter employee ID: '))
        if id in empdict.keys():
            flag = False
        else:
            print('Employee ID does not exist. Please try again')

    empdict[id].name = input('Enter employee name: ')
    empdict[id].department = input('Enter employee department: ')
    empdict[id].jobtitle = input('Enter employee job title: ')
    print('Employee changed successfully')

#****************************************************************************************************

def delete(empdict):
    id = int(input('Enter employee ID: '))
    if id in empdict.keys():
        del (empdict[id])
        print('Employee has been deleted.')
    else:
        print('Employee ID already exists. Please try again')


#****************************************************************************************************

if __name__ == '__main__':
    main()

#****************************************************************************************************

'''

Menu
-------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program

Enter your choice: 0
choice is incorrect. Please try again.
Menu
-------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program

Enter your choice: p
choice: p is not an integer. Please try again
Menu
-------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program

Enter your choice: 1
Enter an employee ID number: 9876
Employee number invalid. Please try again.
Enter an employee ID number: 47899
Name: Susan Myers 
ID number: 47899 
Department: Accounting 
Job Title: Vice President 

Menu
-------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program

Enter your choice: 2
Enter employee ID: 47899
Employee ID already exists. Please try again
Menu
-------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program

Enter your choice: 2
Enter employee ID: 899
Enter employee name: Charles London
Enter employee department: Management
Enter employee job title: Manager
Employee added successfully
Menu
-------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program

Enter your choice: 3
Enter employee ID: 97767
Employee ID does not exist. Please try again
Enter employee ID: 47899
Enter employee name: Daniel Smith
Enter employee department: HR
Enter employee job title: Rep
Employee changed successfully
Menu
-------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program

Enter your choice: 4
Enter employee ID: 9874
Employee ID already exists. Please try again
Menu
-------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program

Enter your choice: 4
Enter employee ID: 47899
Employee has been deleted.
Menu
-------------------------
1. Look up an employee
2. Add a new employee
3. Change an existing employee
4. Delete an employee
5. Quit the program

Enter your choice: 5
Goodbye


'''