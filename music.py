#first we will import modules
import pygame
import os
import tkinter as tkr
#init
pygame.init()
pygame.mixer.init()
#create a window for program
window=tkr.Tk()
#specifiation of windows
window.title("Music player")
window.geometry("550x550")
#playlist regist
os.chdir("C:/Users/tanis/Downloads/home/playlist")
print(os.getcwd)
songlist = os.listdir()
#volume
VolumeLevel = tkr.Scale(window,from_=0.0,to_=2.0, orient = tkr.HORIZONTAL,resolution = 0.5,background='black',foreground='white')
#playlist input
playlist = tkr.Listbox(window,highlightcolor="red",background="light gray",selectmode = tkr.SINGLE)
print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1
#Create SongName
var = tkr.StringVar()
songtitle = tkr.Label(window,textvariable=var)
#main code
def Play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get())
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel.get())  
def exit_play():
    pygame.mixer.stop()
def Pause():
    pygame.mixer.music.pause()
def UnPause():  
    pygame.mixer.music.unpause()
#GUI interface
play_button=tkr.Button(window,width=12,height=5,text="PLAY song",background="cyan",foreground="black",command=Play)
play_button.pack(fill='x')
stop_button=tkr.Button(window,width=12,height=5,text="stop song",background="sky blue",foreground="black",command=exit_play)
stop_button.pack(fill='x')
button3 = tkr.Button(window, width=12,height=5, text="PAUSE",background="light pink",foreground="black",command=Pause)
button4 = tkr.Button(window, width=12,height=5, text="UNPAUSE",background="lime",foreground="black",command=UnPause)
button3.pack(fill='x')
button4.pack(fill='x')
VolumeLevel.pack(fill="x")
playlist.pack(fill="both", expand="yes")
songtitle.pack()
#activation of window
window.mainloop()
