from tkinter import *

window = Tk()  # Creates the window
window.title("Datr")  # Gives the window a title


lbl = Label(window, text="Datr", font=("Arial Bold", 20))  # Creates a label
lbl.grid(column=0, row=0)  # Places the label

lbl2 = Label(window, text="Datr", font=("Arial Bold", 20))  # Creates a label
lbl2.grid(column=1, row=1)  # Places the label

window.geometry('960x720')  # Setting window size


def clicked():
    lbl.configure(text="Butoon was clicked !!")


btn = Button(window, text="Add Date", bg="orange", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()
