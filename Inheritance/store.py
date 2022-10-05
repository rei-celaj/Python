#****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: A7
#       Due Date: 10/18/2021
#       Description: This program creates a dictionary of customers and sales associates
#                    and displays them.
#
#
#****************************************************************************************************
from customer import customer
from sales_associate import sales_associate

#****************************************************************************************************

def main():
    dictionary = {sales_associate('jane', '123-897', 'A095', 8.7):
                  customer('Mary', '909-457', 'C921', True),
                  sales_associate('John', '905-437', 'X337', 9.5):
                  customer('Mike', '415-678', 'C100'),
                  sales_associate('Joe', '314-636', 'B522', 10.7):
                  customer('Moe', '897-909', 'C607', True)}

    output(dictionary)

#****************************************************************************************************

def output(dict):
    print('All sales:')
    print('*' * 25)
    for k in dict.keys():
        print(k)
        print()

    print()
    print('All customers:')
    print('*' * 25)
    for k in dict.keys():
        print(dict[k])
        print()

#****************************************************************************************************

if __name__ == '__main__':
    main()