
from tkinter import *
import pygame
root=Tk()
root.title("ciao")
# ~ root.iconbitmap("c:/gui/codemy.ico")
root.geometry("500x400")
pygame.mixer.init()
def play():
	pygame.mixer.music.load("C:\\Users\\Attilio\\Desktop\\Paolo\\materiale_rosanna\Franco Bastelli Cento Di Questi Giorni.mp3")
	pygame.mixer.music.play(loops=0)
mybutton=Button(root,text="playsong")

mybutton.pack(pady=20)
root.mainloop()
