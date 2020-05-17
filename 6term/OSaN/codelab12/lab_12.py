try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import threading
import random
import time
from queue import *



class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("lab_12")
        self.color = "black"
        self.canv = Canvas(master=self.master, width=1000, height=1000)
        self.canv.pack()
    
    def update(self):
        self.master.update()
        print(self.color)
        self.canv.config(background=self.color)
        self.master.update()
        root.after(1250, self.update)
        
# lock = threading.Lock()    
lock = threading.Event() 
lock.set()   

def tryChange(canv, my_gui, color):
    print("COLORED")
    global lock
    # lock.acquire()
    lock.wait()
    lock.clear()
    my_gui.color = color
    time.sleep(1)
    lock.set()
    # lock.release()
    time.sleep(2.6)
    tryChange(canv,my_gui, color)
    
        

if __name__ == "__main__":   
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.update()
    
    
    threading.Thread(target=tryChange, args=[my_gui.canv, my_gui, "red"]).start()
    threading.Thread(target=tryChange, args=[my_gui.canv, my_gui, "green"]).start()
    threading.Thread(target=tryChange, args=[my_gui.canv, my_gui, "blue"]).start()
    root.after(1000, my_gui.update)
    root.mainloop()
    