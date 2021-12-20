from tkinter import *
from tkinter.tix import *
from tkinter import filedialog as f
from tkinter import messagebox
from tkinter.font import BOLD
from pygame import mixer

root = Tk()

class music:
    def exit_func(self):
        root.destroy()

    def open_func(self):
        self.open_music=f.askopenfilename(title="Open", filetype=(("Audio Files", "*.mp3"),))

    def play_func(self):
        if self.open_music:
            mixer.init()
            mixer.music.load(self.open_music)
            mixer.music.play()
        else:
            messagebox.showwarning(title="Warning", message="You must open an audio file before doing this")

    def pause_func(self):
        if self.open_music:
            if self.playing_music:
                mixer.music.pause()
                self.playing_music=False
            else:
                mixer.music.unpause()
                self.playing_music=True
        else:
            messagebox.showwarning(title="Warning", message="You must open an audio file before doing this") 

    def stop_func(self):
        if self.open_music:
            mixer.music.stop()
            messagebox.showinfo(title="Stopped", message="Song stopped")
        else:
            messagebox.showwarning(title="Warning", message="You must open an audio file before doing this")

    def vol_func(self, value):
        try:
            volume = int(value) / 100
            mixer.music.set_volume(volume)
        except:
            pass

    def about_func(self):
        messagebox.showinfo(title="About", message="Author: itsgerliz\nLocation: Spain\nVersion: 2.0")

    def __init__(self, root):
        root.title("Music Player V2")
        root.geometry("550x350")
        root.resizable(width=False, height=False)

        bar = Menu(root, bg="red")
        root.config(menu=bar, bg="light grey")

        self.open_music = False
        self.playing_music = False
        fontType = BOLD

        tip = Balloon(root)

        #Menu
        file_menu = Menu(bar, tearoff=0,)
        file_menu.add_command(label="Open File", command=self.open_func)

        bar.add_cascade(menu=file_menu, label="File")

        player_menu = Menu(bar, tearoff=0)
        player_menu.add_command(label="Play", command=self.play_func)
        player_menu.add_command(label="Pause", command=self.pause_func)
        player_menu.add_command(label="Stop", command=self.stop_func)

        bar.add_cascade(menu=player_menu, label="Player")

        exit_menu = Menu(bar, tearoff=0)
        exit_menu.add_command(label="Exit", command=self.exit_func)

        bar.add_cascade(menu=exit_menu, label="Quit")

        about_menu = Menu(bar, tearoff=0)
        about_menu.add_separator()
        about_menu.add_command(label="About", command=self.about_func)
        about_menu.add_separator()

        bar.add_cascade(menu=about_menu, label="Info")

        #GUI
        volLabel = Label(root, text="Volume:", font=fontType, width=10, height=2, bg="light grey", padx=120, pady=15)
        volLabel.grid(row=1, column=1)

        volScale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=self.vol_func)
        volScale.set(70)
        volScale.grid(row=1, column=2)
        tip.bind_widget(volScale, balloonmsg="Move to change the volume of the audio clip")

        playLabel = Label(root, text="Play:", font=fontType, width=10, height=2, bg="light grey", pady=15)
        playLabel.grid(row=2, column=1)

        playButt = Button(root, text="Play", command=self.play_func, bd=5)
        playButt.grid(row=2, column=2)
        tip.bind_widget(playButt, balloonmsg="Press to play the audio file")

        pauseLabel = Label(root, text="Pause:", font=fontType, width=10, height=2, bg="light grey", pady=15)
        pauseLabel.grid(row=3, column=1)

        pauseButt = Button(root, text="Pause", command=self.pause_func, bd=5)
        pauseButt.grid(row=3, column=2)
        tip.bind_widget(pauseButt, balloonmsg="Press to pause the audio file")

        stopLabel = Label(root, text="Stop:", font=fontType, width=10, height=2, bg="light grey", pady=15)
        stopLabel.grid(row=4, column=1)

        stopButt = Button(root, text="Stop", command=self.stop_func, bd=5)
        stopButt.grid(row=4, column=2)
        tip.bind_widget(stopButt, balloonmsg="Press to stop the audio file")

music(root)
root.mainloop()