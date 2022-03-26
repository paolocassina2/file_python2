#sistemare punteggio e scritte -->forse non e necessario ripetere label 12 e altre tante voltep-->magari basta definirla una volta dentro la funyione cartaforbice
def game():
	while turn<10:
		abc=["c","f","s"]
		turn=turn+1
		
		print("turn ", turn)
		
		# ~ print(b)		
		import random
		if turn<=10:
			CA.var=random.choice(abc)
			# ~ print(CA)	
			SCE.var=str(input("C F S "))
		if CA.var==SCE.var:
			print("rund ",turn,"pari")	
			a=a+1
			b=b+1
			print(a)
			print(b)
			print("")
		elif CA.var=="c" and SCE.var=="s":
			print("cm wins "+"rund ",turn)	
			a=a+2
			print(a)
			print(b)
			print("")
		elif CA.var=="s" and SCE.var=="c":
			print("gamer wins "+"rund ",turn)	
				
			b=b+2
			print(a)
			print(b)
			print("")
		elif CA.var=="f" and SCE.var=="c":
			print("cm wins"+"rund ",turn)	
			a=a+2
			print(a)
			print("")
		elif CA.var=="c" and SCE.var=="f":
			
			
			print("gamer wins "+"rund ",turn)	
				
			b=b+2
			
			print(a)
			print(b)
			print("")
		elif CA.var=="s" and SCE.var=="f":
			print("cm wins")	
			a=a+2
			
			print(a)
			print(b)
			print("")
		elif CA.var=="f" and SCE.var=="s":
				
			
			print("gamer wins"+ "rund ",turn)	
				
			b=b+2
			print(a)
			print(b)
			print("")
		
		
	if turn>=10:
		if a>b:
			print("cm is the winner")	
		elif a==b:
			print("draw")
		elif a<b:	
			print("gamer is the winner")
			

		
# ~ immagine()		
def x1():
	x1.var=""
x1()
# ~ entrybox1()
def label7():
		label7.var=""
label7()
def label6():
		label6.var=""
label6()
def img():
		img.var=""
				
img()
def img2():
		img2.var=""
				
img2()
def indirizzo1():
			indirizzo1.var=""
indirizzo1()
def indirizzo2():
	indirizzo2.var=""
indirizzo2()
def indirizzo3():
	indirizzo3.var=""
indirizzo3()

def CA():
		CA.var=""
CA()
def SCE():
	SCE.var=2
SCE()




def image1():
			a=0
			b=0
			# ~ if SCE.var=='c':
					# ~ img.var = tk.PhotoImage(file=indirizzo2.var)
			
			# ~ elif SCE.var=='f':
					# ~ img.var = tk.PhotoImage(file=indirizzo2.var)
			# ~ elif SCE.var=='s':
					# ~ img.var = tk.PhotoImage(file=indirizzo3.var)
		
			indirizzo1.var="C:\\Users\\Paul9\\Desktop\\provagithub\\work-space-paolo\\2versioni-randomqrcode\\qrcodefolder\\qrfolder2-infotrasportatore\\forbici.png"
			indirizzo2.var="C:\\Users\\Paul9\\Desktop\\provagithub\\work-space-paolo\\2versioni-randomqrcode\\qrcodefolder\\qrfolder2-infotrasportatore\\rock.png"
			indirizzo3.var="C:\\Users\\Paul9\\Desktop\\provagithub\\work-space-paolo\\2versioni-randomqrcode\\qrcodefolder\\qrfolder2-infotrasportatore\\carta.png"
			
		
		
			import tkinter as tk

			root= tk.Tk()
			# ~ aliditalia
			
			
			# ~ image2()
			canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
			canvas1.pack()
			
			
			
			
			
			
					
			
			
			
			
			
			
			
			
			label6.var = tk.Label(root, text="ciao")
			label6.var.config(font=('helvetica', 10))

			canvas1.create_window(0, 400, window=label6.var)
			
			label7.var = tk.Label(root, text="ciao")
			label7.var.config(font=('helvetica', 10))

			canvas1.create_window(1000, 800, window=label7.var)
			
			
			label11 = tk.Label(root, text="")
			label11.config(font=('helvetica', 10))

			canvas1.create_window(300, 50, window=label11)
			
		
			label12 = tk.Label(root, text="")
			label12.config(font=('helvetica', 10))

			canvas1.create_window(300, 50, window=label12)
			
			
			label8 = tk.Label(root, text="giocatore1")
			label8.config(font=('helvetica', 10))

			canvas1.create_window(300, 180, window=label8)
			label9 = tk.Label(root, text="computer")
			label9.config(font=('helvetica', 10))

			canvas1.create_window(0, 180, window=label9)
			
			entry1 = tk.Entry (root) 
			canvas1.create_window(200, 100, window=entry1)	
			
			# ~ x1.var = entry1.get()	
			def immagine():
				label6.var.destroy()
			
				# ~ qrcode5680464906meanings.TIFF
				# ~ immagine()

				if x1.var=="c":
					img.var = tk.PhotoImage(file=indirizzo3.var)
				
				if x1.var=="f":
					img.var = tk.PhotoImage(file=indirizzo1.var)
				
				if x1.var=="s":
					img.var = tk.PhotoImage(file=indirizzo2.var)
				label6.var = tk.Label(root, image=img.var)		
				label6.var.config(font=('helvetica', 10))

				canvas1.create_window(300, 400, window=label6.var)
				# ~ label6.var.destroy()
				
			def immagine2():
				label7.var.destroy()
				# ~ indirizzo1="C:\\Users\\Paul9\\Desktop\\provagithub\\work-space-paolo\\2versioni-randomqrcode\\qrcodefolder\\qrfolder2-infotrasportatore\\qrcode9129985083outboards.TIFF"
				# ~ if CA.var=="c":
					# ~ img2.var = tk.PhotoImage(file=indirizzo2.var)
				if CA.var=="f":			
					img2.var = tk.PhotoImage(file=indirizzo1.var)
				if CA.var=="s":
					img2.var = tk.PhotoImage(file=indirizzo2.var)
				if CA.var=="c":
					img2.var = tk.PhotoImage(file=indirizzo3.var)

				label7.var = tk.Label(root, image=img2.var)
				label7.var.config(font=('helvetica', 10))

				canvas1.create_window(0,400, window=label7.var)
			
			
			def a():
				a.var=0
			a()
			
			def b():
				b.var=0
			b()
			turn=0
			# ~ CA.var="s"		#per ora pc gioca sempresasso			
			def label12():
				label12.var=""
			label12()
			def label13():
				label13.var=""
			label13()
			def label16():
				label16.var=""
			label16()
			# ~ def a():
				# ~ a.var=""
				
			# ~ def b():
				# ~ b.var=""
			# ~ b()
			
			label16.var = tk.Label(root, text="")
			label16.var.config(font=('helvetica', 10))
			canvas1.create_window(300, 15, window=label16.var)
		
			
			
			
			
			label12.var = tk.Label(root, text="")
			label12.var.config(font=('helvetica', 10))
			
			canvas1.create_window(300, 15, window=label12.var)
			
			def label10():
				label10.var=""
			label10()
			
			label10.var = tk.Label(root, text="")
			label10.var.config(font=('helvetica', 10))
			canvas1.create_window(300, 15, window=label10.var)
			
		
			
		
			label13.var = tk.Label(root, text="")
			label13.var.config(font=('helvetica', 10))
			canvas1.create_window(300, 15, window=label13.var)
		
			def contatoreturni():
				contatoreturni.var=0
				
			contatoreturni()
		
		
		
		
			def punteggio():
							label12.var = tk.Label(root, text="punteggio:"+str(a.var))
							label12.var.config(font=('helvetica', 10))
							canvas1.create_window(300, 15, window=label12.var)
							# ~ a=a+2
							label13.var = tk.Label(root, text="punteggio:"+str(b.var))
							label13.var.config(font=('helvetica', 10))
							canvas1.create_window(300, 15, window=label13.var)
			
				
				# ~ contatoreturni.var=contatoreturni.var+1
				
				# ~ print("turn ", turn)
				
				# ~ print(b)		
			import random
			
			
			def label11():
				label11.var=""
			label11()
			label11.var= tk.Label(root, text="")
			label11.var.config(font=('helvetica', 10))

			canvas1.create_window(300, 20, window=label11.var)
			
			
			def scrivivinci():
				
				
				
				label11.var.destroy()
				label11.var= tk.Label(root, text="il GIOCATORE vince ")
				label11.var.config(font=('helvetica', 10))

				canvas1.create_window(300, 20, window=label11.var)
				
			def scriviperdi():
				
				label11.var.destroy()
				
				label11.var= tk.Label(root, text="il GIOCATORE perde ")
				label11.var.config(font=('helvetica', 10))

				canvas1.create_window(300, 20, window=label11.var)	
			
			
		
			
			def gioco():
				
				# ~ if x1.var=="f" or x1.var=="s" or x1.var=="c":
					
				
					
					if	CA.var=="s" and x1.var=="f":
						# ~ cancellalabel11()
						label6.var.destroy()
						label7.var.destroy()
						print("GIOCATORE perde "+"rund ",contatoreturni.var)	
						
						a.var=a.var+2
						
						# ~ label12.var = tk.Label(root, text="punteggio:"+str(a.var))
						# ~ label12.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(300, 35, window=label12.var)
							# ~ a=a+2
						# ~ label13.var = tk.Label(root, text="punteggio:"+str(b.var))
						# ~ label13.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(200, 35, window=label13.var)
								
						scriviperdi()	
								
									
						
					
						# ~ print(a.var)
						# ~ print(b.var)
						# ~ punteggio()
						print("")
						immagine()
						immagine2()
						
					elif	CA.var=="f" and x1.var=="s":
						
						# ~ label11.destroy()
						# ~ cancellalabel11()
						label6.var.destroy()
						label7.var.destroy()
						print("GIOCATORE vince "+"rund ",contatoreturni.var)	
						# ~ label11.var= tk.Label(root, text="GIOCATORE vince")
						# ~ label11.var.config(font=('helvetica', 10))

						# ~ canvas1.create_window(300, 20, window=label11.var)
						b.var=b.var+2
						# ~ punteggio()
						# ~ print(a.var)#
					
						# ~ print(b.var)
						print("")
						immagine()
						immagine2()
						# ~ label12.var = tk.Label(root, text="punteggio:"+str(a.var))
						# ~ label12.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(200, 35, window=label12.var)
							# ~ a=a+2
						# ~ label13.var = tk.Label(root, text="punteggio:"+str(b.var))
						# ~ label13.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(300, 35, window=label13.var)
						scrivivinci()		
					
					elif	CA.var=="c" and x1.var=="s":
						# ~ cancellalabel11()
						label6.var.destroy()
						label7.var.destroy()
						print("il GIOCATORE perde "+"rund ",contatoreturni.var)	
						# ~ label11.var= tk.Label(root, text="il GIOCATORE perde")
						# ~ label11.var.config(font=('helvetica', 10))

						# ~ canvas1.create_window(300, 20, window=label11.var)
						a.var=a.var+2
						print(a.var)
						print(b.var)
						# ~ punteggio()
						print("")
						immagine()
						immagine2()
						# ~ label12.var = tk.Label(root, text="punteggio:"+str(a.var))
						# ~ label12.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(200, 40, window=label12.var)
							# ~ a=a+2
						# ~ label13.var = tk.Label(root, text="punteggio:"+str(b.var))
						# ~ label13.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(300, 40, window=label13.var)
						
						scriviperdi()
								
					elif	CA.var=="s" and x1.var=="c":
						# ~ cancellalabel11()
						label6.var.destroy()
						label7.var.destroy()
						print("GIOCATORE vince "+"rund ",contatoreturni.var)	
						# ~ label11.var= tk.Label(root, text="GIOCATORE vince")
						# ~ label11.var.config(font=('helvetica', 10))
						b.var=b.var+2
						# ~ canvas1.create_window(300, 20, window=label11.var)
						# ~ punteggio()
						print(a.var)
						print(b.var)
						print("")
						immagine()
						immagine2()
						# ~ label12.var = tk.Label(root, text="punteggio:"+str(a.var))
						# ~ label12.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(200, 40, window=label12.var)
							# ~ a=a+2
						# ~ label13.var = tk.Label(root, text="punteggio:"+str(b.var))
						# ~ label13.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(300, 40, window=label13.var)
						scrivivinci()
								
					elif	CA.var=="c" and x1.var=="f":
						# ~ cancellalabel11()
						label6.var.destroy()
						label7.var.destroy()
						print("GIOCATORE vince "+"rund ",contatoreturni.var)	
						# ~ label11.var= tk.Label(root, text="GIOCATORE vince")
						# ~ label11.var.config(font=('helvetica', 10))

						# ~ canvas1.create_window(300, 20, window=label11.var)
						b.var=b.var+2
						# ~ print(a.var)
						# ~ print(b.var)
						print("")
						# ~ punteggio()
						immagine()
						immagine2()
						# ~ label12.var = tk.Label(root, text="punteggio:"+str(a.var))
						# ~ label12.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(200, 40, window=label12.var)
							# ~ a=a+2
						# ~ label13.var = tk.Label(root, text="punteggio:"+str(b.var))
						# ~ label13.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(300, 40, window=label13.var)
						scrivivinci()
								
					elif	CA.var=="f" and x1.var=="c":
						# ~ cancellalabel11()
						label6.var.destroy()
						label7.var.destroy()
						print("GIOCATORE perde "+"rund ",contatoreturni.var)	
						# ~ label11.var= tk.Label(root, text="GIOCATORE  perde")
						# ~ label11.var.config(font=('helvetica', 10))

						# ~ canvas1.create_window(300, 20, window=label11.var)
						a.var=a.var+2#a e il computer 
						print(a.var)
						print(b.var)
						# ~ punteggio()
						print("")
						immagine()
						immagine2()
						# ~ label12.var = tk.Label(root, text="punteggio:"+str(a.var))
						# ~ label12.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(200, 40, window=label12.var)
							# ~ a=a+2
						# ~ label13.var = tk.Label(root, text="punteggio:"+str(b.var))
						# ~ label13.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(300, 40, window=label13.var)
						scriviperdi()
								
					elif 	CA.var== x1.var:
						# ~ cancellalabel11()
						label11.var.destroy()
						label11.var= tk.Label(root, text="pari")
						label11.var.config(font=('helvetica', 10))

						canvas1.create_window(300, 20, window=label11.var)
						
						
						label6.var.destroy()
						label7.var.destroy()
						print("pari")	
						a.var=a.var+1
						b.var=b.var+1
						# ~ print(a)
						# ~ print(b)
						# ~ punteggio()
						print("")
						immagine()
						immagine2()
					
			# ~ if turn>=10:
				# ~ print("turno",turno)
				# ~ if a>b:
					# ~ print("cm is the winner")	
				# ~ elif a==b:
					# ~ print("draw")
				# ~ elif a<b:	
					# ~ print("gamer is the winner")
					
					
			def cartaforbice():
				# ~ label11.destroy()
				
				
				
				label16.var.destroy()
				label10.var.destroy()

				import random
				abc=["c","f","s"]
				CA.var=random.choice(abc)	
				
				x1.var=entry1.get()		
				if x1.var=="c" or x1.var=="f" or x1.var=="s":
					
				
					
						
					if contatoreturni.var<10:
						contatoreturni.var=contatoreturni.var+1
						label11.var.destroy()
						label16.var.destroy()
						label10.var.destroy()
						label12.var.destroy()
						
						gioco()

						label10.var= tk.Label(root, text="turno "+str(contatoreturni.var))
						label10.var.config(font=('helvetica', 10))

						canvas1.create_window(200, 20, window=label10.var)
						# ~ canvas1.create_window(20, 20, window=label16.var)
						
						# ~ label12.var = tk.Label(root, text="punteggio:"+str(a.var))
						# ~ label12.var.config(font=('helvetica', 10))
						# ~ canvas1.create_window(200, 40, window=label12.var)
									
							
						
					
						label16.var = tk.Label(root, text=x1.var)
						label16.var.config(font=('helvetica', 10))
						
						canvas1.create_window(20, 20, window=label16.var)
						
						label12.var = tk.Label(root, text="punteggio:"+str(a.var))
						label12.var.config(font=('helvetica', 10))
						canvas1.create_window(200, 40, window=label12.var)
								
						label13.var = tk.Label(root, text="punteggio:"+str(b.var))
						label13.var.config(font=('helvetica', 10))
						canvas1.create_window(300,40, window=label13.var)
										
						
						
						
						
					else:
						label11.var.destroy()
						label7.var.destroy()
						label6.var.destroy()
						
						if a.var>b.var:						#il punteggio finale stabilisce chi vince
						
							label16.var = tk.Label(root, text="GAMEOVER,computer wins")
							label16.var.config(font=('helvetica', 10))
							
							canvas1.create_window(20, 20, window=label16.var)
							
						elif a.var==b.var:
								
							label16.var = tk.Label(root, text="PAREGGIO")
							label16.var.config(font=('helvetica', 10))
							
							canvas1.create_window(20, 20, window=label16.var)
							
						
						
						else:
							label16.var = tk.Label(root, text="GAMEOVER, player wins")
							label16.var.config(font=('helvetica', 10))
						
							canvas1.create_window(20, 20, window=label16.var)
							
							
				else:
						
						
						label16.var = tk.Label(root, text="")
						label16.var.config(font=('helvetica', 10))
						
						canvas1.create_window(20, 20, window=label16.var)
						
						label12.var = tk.Label(root, text="")
						label12.var.config(font=('helvetica', 10))
						canvas1.create_window(200, 40, window=label12.var)
								
						label13.var = tk.Label(root, text="")
						label13.var.config(font=('helvetica', 10))
						canvas1.create_window(300,40, window=label13.var)
										
						
						label11.var.destroy()
						label7.var.destroy()
						label6.var.destroy()
						label12.var.destroy()
						label13.var.destroy()
						label12.var = tk.Label(root, text="")
						label12.var.config(font=('helvetica', 10))
						canvas1.create_window(300, 40, window=label12.var)
								
						label13.var = tk.Label(root, text="")
						label13.var.config(font=('helvetica', 10))
						canvas1.create_window(200,40, window=label13.var)
						label12.var.destroy()
						label13.var.destroy()
								
					
			# ~ if contatoreturni.var<=10:	#max 10 turni
			button2 = tk.Button(text='cartaforbice', command=cartaforbice, bg='brown', fg='white', font=('helvetica', 9, 'bold'))	#PULSANTE CHE GENERA UNA SCRITTA DA INSERIRE NEL QR
			canvas1.create_window(0, 0, window=button2)		
					
					
					
					
					
					
					
					
			
			
			
			
			def clear():
				label7.destroy()
			
		# ~ clear()	
			
			
			
			
			
			
			root.mainloop()
# ~ import tkinter as tk
image1()
# ~ image1()
# ~ root.mainloop()
# ~ indirizzo2.var="C:\\Users\\Paul9\\Desktop\\provagithub\\work-space-paolo\\2versioni-randomqrcode\\qrcodefolder\\qrfolder2-infotrasportatore\\rock.png"
# ~ indirizzo3.var="C:\\Users\\Paul9\\Desktop\\provagithub\\work-space-paolo\\2versioni-randomqrcode\\qrcodefolder\\qrfolder2-infotrasportatore\\carta.png"



# ~ import tkinter as tk

# ~ root= tk.Tk()
# ~ aliditalia


# ~ image2()
# ~ canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
# ~ canvas1.pack()
# ~ if CA.var=="c":
# ~ indirizzoab1="C:\\Users\\Paul9\\Desktop\\provagithub\\work-space-paolo\\2versioni-randomqrcode\\qrcodefolder\\qrfolder2-infotrasportatore\\forbici.png"

# ~ img22 = tk.PhotoImage(file=indirizzoab1)

# ~ label7 = tk.Label(root, image=img22)
# ~ label7.config(font=('helvetica', 10))

# ~ canvas1.create_window(0,400, window=label7)



# ~ root.mainloop()
