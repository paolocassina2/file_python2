###CARTELLA==prova
from tkinter import *	
import tkinter as tk	

# ~ def canvas1():
	# ~ canvas1.var="Ciao"
# ~ canvas1()	# ~ canvas1.var.delete(z.var)								
def entrybox():
	# ~ def entry1():
		# ~ entry1.var=""

	

	# ~ print(res)
	

	# ~ import tkinter as Tk	
	root = Tk()
	canvas1 = tk.Canvas(root, width = 1500, height =800,  relief = 'raised')
	
	def drawlabel():
		res=[x for x in range(1,10)]					#stampa per esempio in questo modo:
																		#			1 2 3
																		#			4 5 6
		canvas1.pack()													#			7 8 9
		j=0
		posX=200
		posY=200
		for x in res:
			# ~ if j>:
				# ~ j=200
			j=j+1
			# ~ j=j+1
			if j>1:
				posX=posX+40
			print(posX)
			# ~ label6.var = tk.Label(root, text="pareggio")
			# ~ label6.var.config(font=('helvetica', 14))
			# ~ canvas1.var.create_window(500, 50, window=label6.var)		
			# ~ if j==4 or j==6:
			if ((j-1)%3==0):
			#oppure ---> if (j%3==0+1):
				posX=200
				posY=posY+40
			label = tk.Label(root, text=x)
			label.config(font=('helvetica', 14))
			canvas1.create_window(posX, posY, window=label)
		# ~ def ciao():
	drawlabel()
	# ~ print(posizione)
	# ~ print(a.var)		
	root.mainloop()
entrybox()
