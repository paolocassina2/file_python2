
# ~ 3/km*60
# ~ n=1
# ~ 1/(km/h)/60


def ciao():
	import tkinter as tk



	root= tk.Tk()

	canvas1 = tk.Canvas(root, width = 400, height = 300)
	canvas1.pack()

	entry1 = tk.Entry (root) 
	canvas1.create_window(200, 100, window=entry1)
	
	def minuti_al_chilometro ():  
		x1 = entry1.get()
		
		# ~ print(x1, "min/km")
		minkim=round(60/float(x1),2)
		# ~ print(kimh)
		label2 = tk.Label(root, text= str(minkim)+" min/km")
		canvas1.create_window(280, 250, window=label2)
	def getkmorari ():  
		x1 = entry1.get()
		
		# ~ print(x1, "min/km")
		kimh=round(1/float(x1)*60,2)
		# ~ print(kimh)
		label1 = tk.Label(root, text= str(kimh)+" km/h")
		canvas1.create_window(280, 180, window=label1)
	button1 = tk.Button(text='Get km/h', command=getkmorari)
	canvas1.create_window(200, 180, window=button1)
	button2 = tk.Button(text='get min/km', command=minuti_al_chilometro)
	canvas1.create_window(200, 250, window=button2)

	root.mainloop()

ciao()
