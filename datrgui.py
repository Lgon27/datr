from tkinter import *
from tkinter import ttk


class App(Tk):
    def __init__(self):
        super(App, self).__init__()

        self.title("Datr")
        self.minsize(600, 400)

        tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tabControl)
        tabControl.add(self.tab1, text="Home")

        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Manage Dates")

        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="Manage Foods")

        tabControl.pack(expand=1, fill="both")

        self.widgets()

    def widgets(self):

        labelFrameHome = LabelFrame(self.tab1, text="Generate Date")
        labelFrameHome.grid(column=0, row=0, padx=8, pady=4)

        labelFrame = LabelFrame(self.tab2, text="First Tab")
        labelFrame.grid(column=0, row=0, padx=8, pady=4)

        btn1 = Button(labelFrameHome, text='Randomize')
        btn1.grid(column=0, row=0, padx=4, pady=2)

        labelFrameHome2 = LabelFrame(self.tab1, text="Generate Date")
        labelFrameHome2.grid(column=1, row=0, padx=8, pady=4)

        lbl = Label(labelFrameHome2, text="Datr", font=(
            "Arial Bold", 20))  # Creates a label

        lbl.grid(column=0, row=0, padx=4, pady=2)

        label = Label(labelFrame, text="Enter Your Name:")
        label.grid(column=0, row=0, sticky='W')

        textEdit = Entry(labelFrame, width=20)
        textEdit.grid(column=1, row=0)

        label2 = Label(labelFrame, text="Enter Your Password:")
        label2.grid(column=0, row=1)

        textEdit = Entry(labelFrame, width=20)
        textEdit.grid(column=1, row=1)

        labelFrame2 = LabelFrame(self.tab3, text="Second Tab")
        labelFrame2.grid(column=0, row=0, padx=8, pady=4)

        label = Label(labelFrame2, text="Enter Your Name:")
        label.grid(column=0, row=0, sticky='W')

        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=0)

        label2 = Label(labelFrame2, text="Enter Your Password:")
        label2.grid(column=0, row=1)

        textEdit = Entry(labelFrame2, width=20)
        textEdit.grid(column=1, row=1)


app = App()
app.mainloop()
