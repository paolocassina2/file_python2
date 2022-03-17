
# ~ 3/km*60
# ~ n=1
# ~ 1/(km/h)/60


def ciao():
	import tkinter as tk



	root= tk.Tk()

	canvas1 = tk.Canvas(root, width = 400, height = 300)
	canvas1.pack()

	entry1 = tk.Entry (root) 
	canvas1.create_window(200, 80, window=entry1)
	entry2 = tk.Entry (root) 
	canvas1.create_window(200, 100, window=entry2)
	
	label5 = tk.Label(root, text="convertitore velocità",font=80)
	canvas1.create_window(200, 40, window=label5)
	def minuti_al_chilometro ():  
		x2 = entry2.get()
		
		# ~ print(x1, "min/km")
		minkim=round(60/float(x2),2)
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


	label3 = tk.Label(root, text="min/km (minuti espressi in decimale)")
	canvas1.create_window(400, 80, window=label3)
	label4 = tk.Label(root, text="km/h")
	canvas1.create_window(380, 100, window=label4)
	root.mainloop()

ciao()
