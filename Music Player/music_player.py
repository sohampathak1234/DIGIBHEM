from tkinter import filedialog
from tkinter import *
import pygame
import os
import random 

window=Tk()
window.geometry("500x300")
window.title("Music Player")

pygame.mixer.init()

menubar=Menu(window)
window.config(menu=menubar)

songs=[]
current_song=""
paused=False

def load_music():
    global current_song
    window.directory=filedialog.askdirectory()
    for song in os.listdir(window.directory):
        name,ext=os.path.splitext(song)
        if ext=='.mp3':
            songs.append(song)
            
    for song in songs:
        songlist.insert("end", song)
        
    songlist.selection_set(0)
    current_song=songs[songlist.curselection()[0]]
    
def play_music():
    global current_song,paused
    if not paused:
        pygame.mixer.music.load(os.path.join(window.directory,current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused=False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True

def next_music():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)+1)
        current_song=songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def previous_music():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)-1)
        current_song=songs[songlist.curselection()[0]]
    except:
        pass
    
def shuffle_music():
    global songs, current_song
    random.shuffle(songs)
    songlist.delete(0, END)  # Clear the current song list
    for song in songs:
        songlist.insert(END, song)
    songlist.selection_clear(0, END)
    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]
    play_music()
    pass

        

browse_menu=Menu(menubar,tearoff=0)
browse_menu.add_command(label='select folder',command=load_music)
menubar.add_cascade(label="Browse Song",menu=browse_menu)


songlist= Listbox(window,bg="black",fg="white",width=100,height=15)
songlist.pack()

play_btn_image=PhotoImage(file="image/play.png")
pause_btn_image=PhotoImage(file="image/pause.png")
next_btn_image=PhotoImage(file="image/next.png")
back_btn_image=PhotoImage(file="image/back.png")
shuffle_btn_image=PhotoImage(file="image/shuffle.png")

control=Frame(window)
control.pack()

play_btn=Button(control,image=play_btn_image, borderwidth=0,command=play_music)
pause_btn=Button(control,image=pause_btn_image, borderwidth=0,command=pause_music)
next_btn=Button(control,image=next_btn_image, borderwidth=0,command=next_music)
back_btn=Button(control,image=back_btn_image, borderwidth=0,command=previous_music)
shuffle_btn=Button(control,image=shuffle_btn_image, borderwidth=0, command=shuffle_music)

back_btn.grid(row=0,column=0,padx=7,pady=10)
play_btn.grid(row=0,column=1,padx=7,pady=10)
pause_btn.grid(row=0,column=2,padx=7,pady=10)
shuffle_btn.grid(row=0,column=3,padx=7,pady=10)
next_btn.grid(row=0,column=4,padx=7,pady=10)


window.mainloop()
