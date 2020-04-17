from tkinter import *

window = Tk()  # Creates the window
window.title("Datr")  # Gives the window a title


lbl = Label(window, text="Datr", font=("Arial Bold", 20))  # Creates a label
lbl.grid(column=0, row=0)  # Places the label

lbl2 = Label(window, text="Datr", font=("Arial Bold", 20))  # Creates a label
lbl2.grid(column=1, row=0)  # Places the label

window.geometry('960x720')

window.mainloop()
