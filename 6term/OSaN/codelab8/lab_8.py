from tkinter import Tk, Label, Button
import tkinter as tk
from tkinter import PhotoImage
import random

isOn = False
step = 1
WIDTH, HEIGHT = 500, 500
x = WIDTH / 2
y = (HEIGHT - 100) / 2


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lab_8")

        self.canv = tk.Canvas(master, width=WIDTH, height=HEIGHT,
                              highlightthickness=1, highlightbackground="black")
        self.canv.pack(side=tk.RIGHT)

        self.imagetest1 = PhotoImage(file="1.gif")
        self.greet_button = Button(
            master, text="Draw", image=self.imagetest1, command=self.draw)
        self.greet_button.pack()

        self.imagetest2 = PhotoImage(file="2.gif")
        self.close_button = Button(
            master, text="Clear", image=self.imagetest2, command=self.clear)
        self.close_button.pack()

        # self.canv.create_image(320, 240, image=imagetest1)

    def draw(self):
        self.canv.create_line(0, 0, 200, 100)
        self.canv.create_line(0, 100, 40, 0, fill="red", dash=(4, 4))
        self.canv.create_rectangle(50, 200, 10, 75, fill="blue")
        self.canv.create_rectangle(100, 200, 10, 300, fill="red")

        for _ in range(16):
            self.canv.create_polygon(
                [random.randint(50, 500) for _ in range(random.randrange(0, 32, 2))], fill="red", outline="blue")

    def clear(self):
        self.canv.delete("all")


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
