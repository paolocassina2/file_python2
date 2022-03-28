from tkinter import *
import tkinter as tk
root = Tk()

def key(event):
    print ("pressed", repr(event.char))

def callback(event):
	# ~ print ("clicked at", event.x, event.y)

	if (event.x >0 and event.x<400) and (event.y>0 and event.y<200):
		print("ciao")
		
	else:
		print("abcdef")
canvas = tk.Canvas(root, width = 1500, height =800,  relief = 'raised')
# ~ canvas= Canvas(root, width=100, height=100)
canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack()

root.mainloop()
