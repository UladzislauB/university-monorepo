try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import threading
import random
import time
from queue import *

q = Queue()


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lab_10")

        self.entry1 = Entry(self.master)
        self.entry2 = Entry(self.master)
        self.entry3 = Entry(self.master)

        self.entry1.pack()
        self.entry2.pack()
        self.entry3.pack()

    def update(self):
        test = q.get()
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry1.insert(END, test)
        self.entry2.insert(END, q.get())
        self.entry3.insert(END, q.get())
        self.master.update()
        self.master.after(2000, self.update())


def generateRandom(entry, root):
    # print(q.qsize())
    q.put(str(random.random()))
    time.sleep(2)
    generateRandom(entry, root)


if __name__ == "__main__":
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.update()

    threading.Thread(target=generateRandom, args=[my_gui.entry1, root]).start()
    threading.Thread(target=generateRandom, args=[my_gui.entry2, root]).start()
    threading.Thread(target=generateRandom, args=[my_gui.entry3, root]).start()
    root.after(2000, my_gui.update())
    # root.mainloop()
