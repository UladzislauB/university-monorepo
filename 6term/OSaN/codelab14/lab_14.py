try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import threading
import random
import time
from queue import *
from psutil import *
from functools import partial
import re
import pathlib
import os


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lab_14")

        self.entry = Entry()
        self.entry.pack(side=TOP)

        self.button = Button(master, text="Search", command=self.search, width=17)
        self.button.pack()

        self.Lb1 = Listbox(root, selectmode=SINGLE)
        self.Lb1.pack()

    def search(self):
        self.Lb1.delete(0, END)
        pattern = re.compile(self.entry.get())
        for dirpath, dirnames, files in os.walk(pathlib.Path().absolute()):
            for fl in files:
                # print(fl)
                # print(dirpath + fl)
                try:
                    # print(dirpath + dirnames + fl)
                    path = dirpath + '/' + fl
                    for i, line in enumerate(open(path)):
                        # print(line)
                        for match in re.finditer(pattern, line):
                            print('Found on line %s: %s' % (i + 1, match.group()))
                            for partOfPath in path.split('/'):
                                self.Lb1.insert(END, partOfPath)
                            return
                except:
                    pass


if __name__ == "__main__":
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
