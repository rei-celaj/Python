#****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: ShoppingList.py
#       Due Date: 11/17/2021
#       Description: This program adds/removes items from a list.
#
#
#
#****************************************************************************************************
import tkinter
import tkinter.messagebox as tkm

def main():
    list = ShoppingListGUI()

#****************************************************************************************************

class ShoppingListGUI():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('shopping list')
        self.topframe = tkinter.Frame(self.root)
        self.title_text = tkinter.StringVar()
        self.title_text.set('Grocery Shopping List')
        self.title_label = tkinter.Label(self.topframe,
                                         textvariable=self.title_text)
        self.midFrame = tkinter.Frame(self.root)
        self.shoppingList = tkinter.Listbox(self.midFrame,
                                            height=6,
                                            width=20,
                                            selectmode='multiple')
        self.verticalSB = tkinter.Scrollbar(self.midFrame,
                                            orient=tkinter.VERTICAL)
        self.verticalSB.config(command=self.shoppingList.yview)
        self.shoppingList.config(yscrollcommand=self.verticalSB.set)
        self.midFrame2 = tkinter.Frame(self.root)
        self.horizontalSB = tkinter.Scrollbar(self.midFrame2,
                                              orient=tkinter.HORIZONTAL)
        self.shoppingList.config(xscrollcommand=self.horizontalSB.set)
        self.horizontalSB.config(command=self.shoppingList.xview)
        self.insertFrame = tkinter.Frame(self.root)
        self.insertEntry = tkinter.Entry(self.insertFrame)
        self.addButton = tkinter.Button(self.insertFrame,
                                        text='Add',
                                        command=self.insert)
        self.bottomFrame = tkinter.Frame(self.root)
        self.deleteButton = tkinter.Button(self.bottomFrame,
                                           text='Delete Selected',
                                           command=self.deleteSelected)
        self.clearButton = tkinter.Button(self.bottomFrame,
                                          text='Clear the list',
                                          command=self.clear)
        self.quitButton = tkinter.Button(self.bottomFrame,
                                         text='Quit',
                                         command=self.root.destroy)

        self.topframe.pack(padx=10, pady=10)
        self.title_label.pack(side='bottom')
        self.midFrame.pack(padx=20)
        self.shoppingList.pack(side='left', fill='both')
        self.verticalSB.pack(side='right', fill=tkinter.Y)
        self.midFrame2.pack(fill=tkinter.X)
        self.horizontalSB.pack(fill=tkinter.X)
        self.insertFrame.pack()
        self.insertEntry.pack(padx=5, side='left')
        self.addButton.pack(side='right')
        self.bottomFrame.pack(padx=20, pady=10)
        self.deleteButton.pack(padx=5, side='left')
        self.clearButton.pack(padx=5, side='left')
        self.quitButton.pack(padx=5, side='right')
        tkinter.mainloop()

    # ****************************************************************************************************

    def insert(self):
        item = self.insertEntry.get()
        if len(item) == 0:
            tkm.showerror('Error', 'No item in entry')
        else:
            self.shoppingList.insert(0, item)
            self.insertEntry.delete(0, 'end')

    # ****************************************************************************************************

    def deleteSelected(self):
        index = self.shoppingList.curselection()
        for i in index[::-1]:
            self.shoppingList.delete(i)

    # ****************************************************************************************************

    def clear(self):
        if self.shoppingList.size() == 0:
            tkm.showerror('Error', 'List is empty')
        else:
            self.shoppingList.delete(0, 'end')

#****************************************************************************************************

if __name__ == '__main__':
    main()