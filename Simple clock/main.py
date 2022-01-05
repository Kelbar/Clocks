import time
from tkinter import Tk
from tkinter import Label

root = Tk()
root.title('Clock')


def clock():
    time_string = time.strftime("%H:%M:%S")
    lbl.config(text = time_string)
    lbl.after(200, clock)

# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),background='white', foreground='purple')

# Placing clock at the centre
# of the tkinter window
lbl.pack()

clock()

root.mainloop()
