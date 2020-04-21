from tkinter import *
from tkinter import ttk

window = Tk()
# window.config(height=500, width=500)
window.title("Datr")

tab_control = ttk.Notebook(window)
window.geometry('960x720')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Home')
tab_control.add(tab2, text='Manage Dates')
tab_control.add(tab3, text='Manage Food')


lbl1 = Label(tab1, text='Generate Date')
lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text='Manage Dates')
lbl2.grid(column=0, row=0)

lbl3 = Label(tab3, text='Manage Food')
lbl3.grid(column=0, row=0)


tab_control.pack(expand=1, fill='both')

window.mainloop()
