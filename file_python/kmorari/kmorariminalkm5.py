
# ~ 3/km*60
# ~ n=1
# ~ 1/(km/h)/60
# ~ a=800
# ~ for x in range(500):
	# ~ if x%60==0:
		# ~ print(x)
		# ~ if x!=0:
			# ~ resto=a%x
			# ~ print("resto",resto)
			
# ~ a = 3
# ~ b = 20
# ~ tot_secondi=a*60+b
		# ~ print(x1, "min/km")
# ~ kimh=round(1/float(tot_secondi)*3600,2)	
# ~ print(kimh)

# ~ for x in range(0,420):
	
	

def ciao():
	import tkinter as tk



	root= tk.Tk()

	canvas1 = tk.Canvas(root, width = 400, height = 300)
	canvas1.pack()

	# ~ entry1 = tk.Entry (root) 
	# ~ canvas1.create_window(100, 80, window=entry1)
	entry2 = tk.Entry (root) 
	canvas1.create_window(100, 100, window=entry2)
	
	entry3 = tk.Entry (root) 
	canvas1.create_window(100, 220, window=entry3)

	entry4 = tk.Entry (root) 
	canvas1.create_window(270,100, window=entry4)

	label5 = tk.Label(root, text="convertitore velocità",font=80)
	canvas1.create_window(200, 40, window=label5)
	def minuti_al_chilometro ():  
		x3 = entry3.get()
		#entry3
		# ~ print(x1, "min/km")
		secondikim=3600/float(x3)		
		# ~ print(kimh)
		if 120<=secondikim<180:
			minuti=2
			secondi=round(secondikim-120,0)
			# ~ secondiciao=round(secondikim%120,0)
			# ~ print("secondi",secondi)
			# ~ print("secondiciao",secondiciao)
		if 180<=secondikim<240:
			minuti=3
			secondi=round(secondikim-180,0)
			
		if 240<=secondikim<300:
			minuti=4
			secondi=round(secondikim-240,0)
		if 300<=secondikim<360:
			minuti=5
			secondi=round(secondikim-300,0)
		if 360<=secondikim<420:
			minuti=6
			secondi=round(secondikim-360,0)
		# ~ minuti=round(minkim,0)
		# ~ secondi_dec=minkim-minuti
		# ~ if secondi>0:
		# ~ secondi:60=secondi_dec:10
		# ~ print(secondikim)
		# ~ secondi=secondi_dec*60/10
		# ~ print(minuti)
		# ~ print(secondi)
		# ~ label2 = tk.Label(root, text= str(secondikim))
		# ~ canvas1.create_window(400, 250, window=label2)
		label2 = tk.Label(root, text= str(minuti)+" minuti "+str(secondi)+ " secondi /km")
		canvas1.create_window(320, 250, window=label2)
	def getkmorari ():  
		#entry 2 e 4
		x2 = entry2.get()
		x4 = entry4.get()
		tot_secondi=float(x2)*60+float(x4)
		# ~ print(x1, "min/km")
		kimh=round(1/float(tot_secondi)*3600,2)	#km/s X 3600(i secondi in una ora)
		print(kimh)
		print(x2)
		print(x4)
		print(tot_secondi)
			# ~ print(kimh)
		label1 = tk.Label(root, text= str(kimh)+" km/h")
		canvas1.create_window(280, 140, window=label1)
	button1 = tk.Button(text='Get km/h', command=getkmorari)
	canvas1.create_window(200, 140, window=button1)
	button2 = tk.Button(text='get min/km', command=minuti_al_chilometro)
	canvas1.create_window(200, 250, window=button2)

	label6 = tk.Label(root, text="inserire minuti(minimo 2 massimo6)")
	canvas1.create_window(100, 70, window=label6)
	label7 = tk.Label(root, text="inserire secondi")
	canvas1.create_window(275, 70, window=label7)
	
	label8 = tk.Label(root, text="inserire km/h")
	canvas1.create_window(100, 200, window=label8)
	# ~ label3 = tk.Label(root, text="min/km")
	# ~ canvas1.create_window(400, 80, window=label3)
	label4 = tk.Label(root, text="km/h")
	canvas1.create_window(380,400, window=label4)
	root.mainloop()

ciao()
