import tkinter
import tkinter.font
def main():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=200, height=200)
    canvas.pack()

    canvas.create_polygon(100, 25, 125, 75, 175, 75, 140, 115, 175, 175, 100, 140, 25, 175,
                          60, 115, 25, 75, 75, 75, fill='', width=3, outline='Black')
    myFont = tkinter.font.Font(family='Times New Roman', size=12)
    canvas.create_text(100, 100, text='Rei Celaj', font=myFont)
    root.mainloop()



if __name__ == '__main__':
    main()