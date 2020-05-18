from tkinter import Tk, Label, Button
import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import random
import time

isOn = False
step = 1
WIDTH, HEIGHT = 1000, 1000
x = WIDTH / 2
y = (HEIGHT - 100) / 2

images = ["1.gif", "2.gif", "3.gif", "4.gif"]


# image1 = ImageTk.PhotoImage(Image.open(images[0]))
# image2 = ImageTk.PhotoImage(Image.open(images[1]))
# image3 = ImageTk.PhotoImage(Image.open(images[2]))
# image4 = ImageTk.PhotoImage(Image.open(images[3]))


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lab_9")

        self.image1 = ImageTk.PhotoImage(Image.open(images[0]))
        self.image2 = ImageTk.PhotoImage(Image.open(images[1]))
        self.image3 = ImageTk.PhotoImage(Image.open(images[2]))
        self.image4 = ImageTk.PhotoImage(Image.open(images[3]))

        self.canv = tk.Canvas(master, width=WIDTH, height=HEIGHT,
                              highlightthickness=1, highlightbackground="black")

        self.curCoords = [x, y]
        self.canv.bind("<Button-1>", self.callback)
        self.canv.pack()
        self.img = ImageTk.PhotoImage(Image.open(images[0]))
        self.canv.create_image(
            x, y, image=self.image1, anchor=tk.NW)

    def callback(self, event):
        i = 0
        while abs(self.curCoords[0] - event.x) > 0 or abs(self.curCoords[1] - event.y) > 0:
            if self.curCoords[0] != event.x:
                if self.curCoords[0] > event.x:
                    self.curCoords[0] -= 1
                else:
                    self.curCoords[0] += 1

            if self.curCoords[1] != event.y:
                if self.curCoords[1] > event.y:
                    self.curCoords[1] -= 1
                else:
                    self.curCoords[1] += 1

            cur = i % 4
            if cur == 0:
                img = self.image1
            if cur == 1:
                img = self.image2
            if cur == 2:
                img = self.image3
            if cur == 3:
                img = self.image4
            # self.img = ImageTk.PhotoImage(Image.open(images[i % 4]))
            self.canv.delete("all")
            self.canv.create_image(
                self.curCoords[0], self.curCoords[1], image=img, anchor=tk.NW)
            self.master.update()
            i += 1
            print(i)
            time.sleep(0.1)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
