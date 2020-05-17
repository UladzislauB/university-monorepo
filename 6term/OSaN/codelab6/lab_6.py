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
        master.title("lab_6")

        self.greet_button = Button(master, text="Start", command=self.start)
        self.greet_button.pack()

        self.close_button = Button(master, text="Stop", command=self.stop)
        self.close_button.pack()

    def callback(self):
        root.after(15, self.callback)
        global x, y, step, isOn
        canvas.delete("all")
        canvas.create_text(x, y, text="codelab6")

        if not isOn:
            return

        if x == 300 or x == 200:
            step *= -1

        x += step
        y += step

    def stop(self):
        global isOn
        isOn = False

    def start(self):
        global isOn
        isOn = True


root = Tk()

root.geometry("500x500")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT - 100)
canvas.pack()

text = canvas.create_text(x, y, text="")

my_gui = MyFirstGUI(root)
root.after(50, my_gui.callback())
root.mainloop()
