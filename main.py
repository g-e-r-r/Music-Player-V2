from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()

class music:
    def exit_func(self):
        root.destroy()

    def open_func(self):
        pass

    def __init__(self, root):
        root.title("Music Player V2")
        root.geometry("500x260")
        root.resizable(width=False, height=False)

        bar = Menu(root)
        root.config(menu=bar)

        exit_menu = Menu(bar, tearoff=0)
        exit_menu.add_command(label="Exit", command=self.exit_func)

        bar.add_cascade(menu=exit_menu, label="Quit")

        file_menu = Menu(bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_func)

        bar.add_cascade(menu=file_menu, label="File")

    
    
    


music(root)
root.mainloop()