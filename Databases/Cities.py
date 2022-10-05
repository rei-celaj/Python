#****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: Cities.py
#       Due Date: 12/6/2021
#       Description: This program creates a GUI and manages a database
#                    from it.
#
#
#
#****************************************************************************************************
import sqlite3, tkinter, tkinter.messagebox

#****************************************************************************************************

def main():
    gui = populationGUI()

#****************************************************************************************************

class populationGUI():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Population')
        self.topFrame = tkinter.Frame(self.root)
        self.titleLabel = tkinter.Label(self.topFrame,
                                        width= 50, height=40, anchor='n')
        self.buttonFrame = tkinter.Frame(self.root)
        self.button1 = tkinter.Button(self.buttonFrame,
                                      text = '1 - Display Cities sorted by population, '
                                             'ascending order', anchor='w', width=50,
                                      command=self.inorder)
        self.button2 = tkinter.Button(self.buttonFrame,
                                      text='2 - Display cities sorted by name',
                                      anchor='w', width=50,
                                      command=self.inorderName)
        self.button3 = tkinter.Button(self.buttonFrame,
                                      text='3 - Display total population of all cities',
                                      anchor='w', width=50,
                                      command=self.total)
        self.button4 = tkinter.Button(self.buttonFrame,
                                      text='4 - Display city with highest population',
                                      anchor='w', width=50,
                                      command=self.highest)
        self.pack()
        self.start()
        tkinter.mainloop()

    #****************************************************************************************************

    def setTitle(self, txt):
        self.titleLabel.config(text=txt, anchor='n')

    #****************************************************************************************************

    def setTitle2(self, txt):
        self.titleLabel.config(text=txt, anchor='c')

    #****************************************************************************************************

    def pack(self):
        self.topFrame.pack()
        self.titleLabel.pack()
        self.buttonFrame.pack(pady=10)
        self.button1.pack(pady=5, padx=10)
        self.button2.pack(pady=5)
        self.button3.pack(pady=5)
        self.button4.pack(pady=5)

    #****************************************************************************************************

    def start(self):
        TXT = 'Contents of cities.db/Cities table:'
        conn = None
        try:
            conn = sqlite3.connect('cities.db')
            cursor = conn.cursor()
            txt = TXT + '\n' + '-' * 50 + '\n'
            cursor.execute('''SELECT *
                                FROM Cities''')
            results = cursor.fetchall()
            for row in results:
                txt += f'{row[0]:<2} {row[1]:<20} {row[2]:,.0f} \n'
            self.setTitle(txt)
        except sqlite3.Error as err:
            tkinter.messagebox.showerror('Error', err)
        finally:
            if conn != None:
                conn.close()

    #****************************************************************************************************

    def inorder(self):
        COL1 = 'City'
        COL2 = 'Population'
        TXT = 'Cities Sorted By Population in Ascending Order:'
        conn = None
        try:
            conn = sqlite3.connect('cities.db')
            cursor = conn.cursor()
            txt = TXT + '\n' + '-' * 50 + '\n\n'
            cursor.execute('''SELECT CityName, Population
                                FROM Cities 
                                ORDER BY Population''')
            results = cursor.fetchall()
            txt += f'{COL1:<20} {COL2} \n'
            for row in results:
                txt += f'{row[0]:<20} {row[1]:,.0f} \n'
            self.setTitle(txt)
        except sqlite3.Error as err:
            tkinter.messagebox.showerror('Error', err)
        finally:
            if conn != None:
                conn.close()

    #****************************************************************************************************

    def inorderName(self):
        COL1 = 'City'
        COL2 = 'Population'
        TXT = 'Cities Sorted By Name:'
        conn = None
        try:
            conn = sqlite3.connect('cities.db')
            cursor = conn.cursor()
            txt = TXT + '\n' + '-' * 50 + '\n\n'
            cursor.execute('''SELECT CityName, Population
                                FROM Cities 
                                ORDER BY CityName''')
            results = cursor.fetchall()
            txt += f'{COL1:<20} {COL2} \n'
            for row in results:
                txt += f'{row[0]:<20} {row[1]:,.0f} \n'
            self.setTitle(txt)
        except sqlite3.Error as err:
            tkinter.messagebox.showerror('Error', err)
        finally:
            if conn != None:
                conn.close()

    #****************************************************************************************************

    def total(self):
        conn = None
        try:
            conn = sqlite3.connect('cities.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT sum(Population)
                                FROM Cities''')
            results = cursor.fetchone()
            txt = f'Total population: {results[0]:,.0f}'
            self.setTitle2(txt)
        except sqlite3.Error as err:
            tkinter.messagebox.showerror('Error', err)
        finally:
            if conn != None:
                conn.close()

    #****************************************************************************************************

    def highest(self):
        conn = None
        try:
            conn = sqlite3.connect('cities.db')
            cursor = conn.cursor()
            cursor.execute('''SELECT CityName, Population
                                FROM Cities 
                                WHERE Population = (SELECT max(Population)
                                FROM Cities)''')
            results = cursor.fetchone()
            txt = f'{results[0]} has the Highest Population: {results[1]:,.0f}'
            self.setTitle2(txt)
        except sqlite3.Error as err:
            tkinter.messagebox.showerror('Error', err)
        finally:
            if conn != None:
                conn.close()

#****************************************************************************************************

if __name__ == '__main__':
    main()