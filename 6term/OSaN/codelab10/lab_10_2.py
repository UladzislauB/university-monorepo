#!/usr/bin/python

from multiprocessing.connection import Listener
from tkinter import *


# print ('connection accepted from', listener.last_accepted)

class MyFirstGUI:
    def __init__(self, master, conn):
        self.master = master
        self.conn = conn
        master.title("lab_10")

        self.canv = Canvas(master, width=1000, height=1000)
        self.canv.bind("<Button-1>", self.callback)

        self.canv.pack()

    def callback(self, event):
        msg = self.conn.recv()
        if msg == 0:
            return

        print(msg[0], msg[1])

        shape = msg[0]
        color = msg[1]

        if shape == "rhombus":
            self.canv.create_polygon(200, 200, 0, 400, 200, 600, 400, 400, fill=color)

        if shape == "square":
            print("LOLA")
            self.canv.create_rectangle(400, 400, 800, 800, fill=color)

        if shape == "circle":
            self.canv.create_oval(500 - 200, 500 - 200, 500 + 200, 500 + 200, fill=color)
        if shape == "star":
            self.canv.create_polygon(600, 900, 0, 400, 200, 600, 400, 400, 600, 600, fill=color)

        self.master.update()
        return


if __name__ == "__main__":
    address = ('localhost', 6000)
    listener = Listener(address, authkey=b'secret password')
    conn = listener.accept()

    print("?")
    root = Tk()
    my_gui = MyFirstGUI(root, conn)
    root.mainloop()

while True:
    msg = conn.recv()
    # do something with msg
    if msg == 'close':
        print(msg)
        conn.close()
        break
listener.close()
