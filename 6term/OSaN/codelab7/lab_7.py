from tkinter import Tk, Label, Button
import tkinter as tk

isOn = False
step = 1
WIDTH, HEIGHT = 500, 500
x = WIDTH / 2
y = (HEIGHT - 100) / 2


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lab_7")

        self.Lb1 = tk.Listbox(root)
        self.Lb1.pack(side=tk.LEFT)

        self.Lb2 = tk.Listbox(root)
        self.Lb2.pack(side=tk.RIGHT)

        self.Ed = tk.Entry(root)
        self.Ed.pack(side=tk.TOP)

        self.greet_button = Button(master, text="Add", command=self.add)
        self.greet_button.pack()

        self.close_button = Button(master, text="Clear", command=self.clear)
        self.close_button.pack()

        self.close_button = Button(
            master, text="To right", command=self.toRight)
        self.close_button.pack()

        self.close_button = Button(master, text="Delete", command=self.delete)
        self.close_button.pack()

    def add(self):
        entry = self.Ed.get()
        if entry not in self.Lb1.get(0, "end"):
            self.Lb1.insert(0, self.Ed.get())

    def clear(self):
        self.Lb1.delete(0, "end")
        self.Lb2.delete(0, "end")

    def toRight(self):
        string = self.Lb1.get(self.Lb1.curselection()[0])
        if string not in self.Lb2.get(0, "end"):
            self.Lb2.insert(0, string)

    def delete(self):
        try:
            self.Lb1.delete(self.Lb1.curselection()[0])
        except:
            pass
        try:
            self.Lb2.delete(self.Lb2.curselection()[0])
        except:
            pass


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
