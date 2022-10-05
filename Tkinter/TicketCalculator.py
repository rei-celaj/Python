#****************************************************************************************************
#
#       Name: Rei Celaj
#       Course: COSC 2110 Computer Languages: Python
#       Assignment: TicketCalculator.py
#       Due Date: 11/10/2021
#       Description: This program calculates ticket price in a GUI.
#
#
#
#****************************************************************************************************
import tkinter
import tkinter.messagebox as tkm

#****************************************************************************************************

def main():
    ticket = TicketCalculatorGUI()

#****************************************************************************************************

class TicketCalculatorGUI():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Ticket Calculator")
        self.top_frame = tkinter.Frame(self.root)
        self.option = tkinter.IntVar()
        self.radio_senior = tkinter.Radiobutton(self.top_frame,
                                                text='Senior (>65)',
                                                variable=self.option,
                                                value=1)
        self.radio_adult = tkinter.Radiobutton(self.top_frame,
                                                text='Adult (15-65)',
                                                variable=self.option,
                                                value=2)
        self.radio_child = tkinter.Radiobutton(self.top_frame,
                                                text='Child (5-15)',
                                                variable=self.option,
                                                value=3)

        self.mid_frame = tkinter.Frame(self.root)
        self.enter_text = tkinter.StringVar()
        self.enter_text.set('Enter the number of tickets:')
        self.enter_label = tkinter.Label(self.mid_frame,
                                         textvariable=self.enter_text)
        self.ticket_entry = tkinter.Entry(self.mid_frame)
        self.bottom_frame = tkinter.Frame(self.root)
        self.display_button = tkinter.Button(self.bottom_frame,
                                             text='Display Charges',
                                             command=self.getChoice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                         text='Quit',
                                         command=self.root.destroy)

        self.top_frame.pack()
        self.radio_senior.pack()
        self.radio_adult.pack()
        self.radio_child.pack(side='bottom')
        self.mid_frame.pack()
        self.enter_label.pack(side='left')
        self.ticket_entry.pack(side='right')
        self.bottom_frame.pack(side='bottom')
        self.display_button.pack(side='left')
        self.quit_button.pack(side='right')

        tkinter.mainloop()

    #****************************************************************************************************

    def getChoice(self):
        SENIOR = 7
        ADULT = 12
        CHILD = 5
        choice = self.option.get()
        tickets = int(self.ticket_entry.get())

        if choice == 1:
            price = tickets * SENIOR
        elif choice == 2:
            price = tickets * ADULT
        elif choice == 3:
            price = tickets * CHILD
        else:
            price = -1

        if price == -1:
            tkm.showinfo('results', 'No choice selected')
        else:
            tkm.showinfo('results', f'Your total charges = ${price:.2f}')

#****************************************************************************************************

if __name__ == '__main__':
    main()