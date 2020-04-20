from tkinter import *

window = Tk()  # Creates the window
window.title("Datr")  # Gives the window a title


lbl = Label(window, text="Datr", font=("Arial Bold", 20))  # Creates a label
lbl.grid(column=0, row=0)  # Places the label


window.geometry('960x720')  # Setting window size

txt = Entry(window, width=10)  # Adds a text area
txt.grid(column=1, row=0)


def clicked():
    res = "Weclome to " + txt.get()  # Displayes the info from the text area

    lbl.configure(text=res)


btn = Button(window, text="Add Date", bg="orange",
             command=clicked)  # Creating the Button

btn.grid(column=2, row=0)


window.mainloop()
