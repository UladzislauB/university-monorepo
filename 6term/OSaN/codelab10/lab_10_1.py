from tkinter import *
from multiprocessing.connection import Client

address = ('localhost', 6000)
conn = Client(address, authkey=b'secret password')


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lab_10")

        shapes = [
            ("Square", "square"),
            ("Rhombus", "rhombus"),
            ("Circle", "circle"),
            ("Star", "star"),
        ]

        colors = [
            ("Red", "red"),
            ("Blue", "blue"),
            ("Green", "green"),
        ]

        self.shape = StringVar()
        self.shape.set("")  # initialize

        self.color = StringVar()
        self.color.set("")  # initialize

        for i, (text, mode) in enumerate(shapes):
            b = Radiobutton(master, text=text,
                            variable=self.shape, value=mode, command=self.callback)
            b.grid(row=i, column=0, sticky=W)

        for i, (text, mode) in enumerate(colors):
            b = Radiobutton(master, text=text,
                            variable=self.color, value=mode, command=self.callback)
            b.grid(row=i, column=1, sticky=W)

    def callback(self):
        print(self.shape.get())
        if len(self.shape.get()) == 0 or len(self.color.get()) == 0:
            return

        conn.send([self.shape.get(), self.color.get()])
        self.shape.set("")
        self.color.set("")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

# while True:
#     conn.send(input())
# # can also send arbitrary objects:
# # conn.send(['a', 2.5, None, int, sum])
# conn.close()
