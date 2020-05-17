try:
    from tkinter import *
except ImportError:
    from Tkinter import *

from psutil import *
from functools import partial


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lab_13")

        self.Lb1 = Listbox(root, selectmode=SINGLE)
        self.Lb1.bind("<Button-1>", self.onClick)
        self.Lb1.pack(side=LEFT)

        self.Lb2 = Listbox(root)
        self.Lb2.pack(side=RIGHT)

        self.rightClickMenu = Menu(self.Lb1, tearoff=0)
        self.master.bind("<Button-3>", self.onRightClick)
        for i in range(11):
            self.rightClickMenu.add_command(label="Priority " + str(i),
                                            command=partial(self.setPriority, i))

        self.fillProcs()

    def toString(self, proc):
        return str(proc.pid) + ' ' + str(proc.nice()) + ' ' + proc.name()

    def fillProcs(self):
        self.Lb1.delete(0, END)
        for proc_num in pids():
            proc = Process(proc_num)
            string = self.toString(proc)
            self.Lb1.insert(0, string)
        self.master.update()

    def onClick(self, event):
        self.Lb2.delete(0, END)

        print(self.Lb1.get(self.Lb1.curselection()).split(' ')[0])
        cur_num = int(self.Lb1.get(self.Lb1.curselection()).split(' ')[0])
        cur_proc = Process(cur_num)

        for proc in cur_proc.children(recursive=True):
            self.Lb2.insert(0, self.toString(proc))

        self.master.update()

    def onRightClick(self, event):
        self.rightClickMenu.tk_popup(event.x_root, event.y_root, 0)
        # self.rightClickMenu.grab_release()

    def setPriority(self, level):
        cur_num = int(self.Lb1.get(self.Lb1.curselection()).split(' ')[0])
        cur_proc = Process(cur_num)
        print(level)
        cur_proc.nice(level)
        self.fillProcs()


if __name__ == "__main__":
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
