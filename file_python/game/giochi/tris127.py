#disegnare ovali,  --->OK
#sistemare parte di logica del gioco (vedi anche variabili vinci)	---> OK ADESSO FUNZIONA ANCHE PAREGGIO : SE IL GIOCATORE HA GIÄ VINTO IL COMPUTER NON GIOCA
#richiamare funzione condizione di vittoria-->OK 
#correggere le rette nella funzione condizione di vittoria. che vengono tracciate quando o il computer o il giocatore vincono



#prendere gli otto casi del programma tracciarighe tris e inserirli nelle condizioni di vittoria e in questa funzione aggiungere anche la variabile caso: 

###############################################
#parti da aggiungere. permettere al giocatore di cominciare una nuova partita non appena finisce una partita






















def x():
		x.var=-1
x()

def inserisci():
		inserisci.var=	-1
inserisci()	
def canvas1():
	canvas1.var=""
canvas1()

def a():
	a.var=0
a()
def vinci():
	vinci.var=""
vinci()
def vinci2():
	vinci2.var=""
vinci2()

vinci.var="b"
vinci2.var="b"
def label18():
	label18.var=""
label18()
def label_res():
	label_res.var=""
label_res()


def label78():
	label78.var=""
label78()

def label6():
	label6.var=""
label6()
def label7():
	label7.var=""
label7()
def label8():
	label8.var=""
label8()
def label9():
	label9.var=""
label9()
#VERSIONE UMANO CONTRO PC-->INIZIA L umano-->bisogna gestire errori->quando umano sceglie un numero giä scelto
words = "- - - - - - - - -"
def pareggio():
	pareggio.var="ciao"
pareggio()


def res():
	res.var=""
res()
res.var = words.split()
# ~ for i in range(3):
		# ~ print ("\t".join(res.var[(i*3):(i*3+3)]))

def label():
	label.var=""
label()

def label1():
	label1.var=""

label1()
import random

# ~ conta1=-1




def condizioni_vittoria():
				if res.var[0]=="*" and res.var[1]=="*"  and res.var[2]=="*" :				#casi orizzontali
							print("tris")
							vinci.var="a"
							# ~ canvas.create_line(15, 25, 200, 25)
							canvas1.var.create_line(200, 150, 700, 150,width=2,fill="red")
							# ~ if c=33
							vinci2.var="b"
							# ~ break
				elif res.var[3]=="*" and res.var[4]=="*"  and res.var[5]=="*" :
					print("tris")
					vinci.var="a"
					canvas1.var.create_line(200, 300, 700, 300,width=2,fill="red")
					vinci2.var="b"
					#	break
					# ~ break
				elif res.var[6]=="*" and res.var[7]=="*"  and res.var[8]=="*" :
					print("tris")
					vinci.var="a"
					canvas1.var.create_line(200, 500, 700, 500,width=2,fill="red")
					vinci2.var="b"
					# ~ break
			# ~ ######################################
				elif res.var[0]=="*" and res.var[3]=="*"  and res.var[6]=="*" :		#casi verticali
						print("tris")
						vinci.var="a"
						vinci2.var="b"
						# ~ break
				elif res.var[1]=="*" and res.var[4]=="*"  and res.var[7]=="*" :
						print("tris")
						vinci.var="a"
						vinci2.var="b"
						# ~ break
				elif res.var[2]=="*" and res.var[5]=="*"  and res.var[8]=="*" :
					
						print("tris")
						vinci.var="a"
						canvas1.var.create_line(700, 50, 700, 700,width=2,fill="red")
						# ~ break
						# ~ break
						vinci2.var="b"
				# ~ #####vinci2.var="b"#########################################
				elif res.var[0]=="*" and res.var[4]=="*"  and res.var[8]=="*" :		#casi diagonali
						print("tris")
						vinci.var="a"
						canvas1.var.create_line(200, 800, 800,50,width=2,fill="red")
						vinci2.var="b"
						# ~ break
				elif res.var[2]=="*" and res.var[4]=="*"  and res.var[6]=="*" :
						print("tris")
						vinci.var="a"
						canvas1.var.create_line(50, 800, 800,50,width=2,fill="red")
						vinci2.var="b"
						# ~ break
				######################################
				if res.var[0]=="#" and res.var[1]=="#"  and res.var[2]=="#" :				#computer
					print("tris")
					vinci2.var="a"
					vinci.var="b"
					canvas1.var.create_line(200, 100, 800, 100,width=2,fill="red")
					# ~ break
				elif res.var[3]=="#" and res.var[4]=="#"  and res.var[5]=="#" :
						print("tris")
						vinci2.var="a"
						vinci.var="b"
						canvas1.var.create_line(200, 200, 800,200,width=2,fill="red")
						# ~ break
				elif res.var[6]=="#" and res.var[7]=="#"  and res.var[8]=="#" :
						print("tris")
					
						canvas1.var.create_line(200, 500, 800,500,width=2,fill="red")
						vinci2.var="a"
						vinci.var="b"
						# ~ break
				# ~ ######################################
				elif res.var[0]=="#" and res.var[3]=="#"  and res.var[6]=="#" :		#casi verticali
						print("tris")
						vinci2.var="a"
						vinci.var="b"
						canvas1.var.create_line(300, 50, 300, 600,width=2,fill="red")
						# ~ break
				elif res.var[1]=="#" and res.var[4]=="#"  and res.var[7]=="#" :
						vinci2.var="a"
						

						vinci.var="b"
						print("tris")

						# ~ break
						# ~ break
				elif res.var[2]=="#" and res.var[5]=="#"  and res.var[8]=="#" :
						vinci2.var="a"
						canvas1.var.create_line(700, 50, 700, 700,width=2,fill="red")
						vinci.var="b"
						print("tris")
						# ~ break
						# ~ break
				# ~ ##############################################
				elif res.var[0]=="#" and res.var[4]=="#"  and res.var[8]=="#" :		#casi diagonali
						vinci2.var="a"
						canvas1.var.create_line(50, 50, 800,800,width=2,fill="red")
						vinci.var="b"
						print("tris")
						# ~ break
				elif res.var[2]=="#" and res.var[4]=="#"  and res.var[6]=="#" :
						vinci2.var="a"
						canvas1.var.create_line(50, 800, 800,50,width=2,fill="red")
						vinci.var="b"
						print("tris")
						# ~ break
				
				print("vinci2",vinci2.var)
				print("vinci",vinci.var)

# ~ def condizioni_pareggio():
				if a.var>=5 :
					if vinci2.var=="b" and vinci.var=="b":
						pareggio.var="pareggio"
						# ~ print("pareggio")
						


def listascelte_possibili():
		listascelte_possibili.var=[0,1,2,3,4,5,6,7,8]				#si chiama cosi in realtä sono le scelte possibili per tutti e due, non sono il pc
listascelte_possibili()
		
from tkinter import *		
def posizione():
	posizione.var="ciao"
posizione()	




def disegna_rettangolo():
	if vinci2.var=="b":
		if posizione.var==0:
			
				r1=canvas1.var.create_rectangle(250, 80, 350, 180,outline="#f11", fill="#1f1", width=2)
			
		elif posizione.var==1:
			
				r2=canvas1.var.create_rectangle(450, 80, 550, 180,outline="#f11", fill="#1f1", width=2)
		elif posizione.var==2:
				r3=canvas1.var.create_rectangle(650, 80, 750, 180,outline="#f11", fill="#1f1", width=2)	

		elif posizione.var==3:
				r4=canvas1.var.create_rectangle(250, 250, 350, 350,outline="#f11", fill="#1f1", width=2)
		elif posizione.var==4:
				r5=canvas1.var.create_rectangle(450, 250, 550, 350,outline="#f11", fill="#1f1", width=2)
		
		elif posizione.var==5:
			r6=canvas1.var.create_rectangle(450+200, 250, 550+200, 350,outline="#f11", fill="#1f1", width=2)
		elif posizione.var==6:
			r7=canvas1.var.create_rectangle(250, 450, 350, 550,outline="#f11", fill="#1f1", width=2)
		elif posizione.var==7:
			r8=canvas1.var.create_rectangle(250+200, 450, 350+200, 550,outline="#f11", fill="#1f1", width=2)
			
		elif posizione.var==8:
			r9=canvas1.var.create_rectangle(250+200+200, 450, 350+200+200,550,outline="#f11", fill="#1f1", width=2)
		# ~ elif posizione.var==7:
		# ~ elif posizione.var==8:
		
def disegna_ovale():
			
				
				if vinci.var=="b":		#disegna i cerchi solo se non il giocatore  non ha ancora vinto
					if int(x.var)==0:
						canvas1.var.create_oval(250, 80, 350, 180, outline="#f11",fill="#1f1", width=2)
					elif int(x.var)==1:
						canvas1.var.create_oval(450, 80, 550, 180, outline="#f11",fill="#1f1", width=2)
					elif int(x.var)==2:
						canvas1.var.create_oval(650,80, 750, 180, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==3:
						canvas1.var.create_oval(250, 250, 350, 350, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==4:
						canvas1.var.create_oval(450, 250, 550, 350, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==5:
						canvas1.var.create_oval(650, 250, 750, 350, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==6:
						canvas1.var.create_oval(250, 450, 350, 550, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==7:
						canvas1.var.create_oval(450, 450, 550, 550, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==8:
						canvas1.var.create_oval(650, 450, 750, 550, outline="#f11",fill="#1f1", width=2)
								
def entrybox():
	# ~ def entry1():
		# ~ entry1.var=""

	

	

	import tkinter as tk
	root = Tk()
	canvas1.var = tk.Canvas(root, width = 1500, height =800,  relief = 'raised')

	def key(event):
		print ("pressed", repr(event.char))
	
	def callback(event):
		# ~ print ("clicked at", event.x, event.y)
		if vinci2.var=="b" and vinci.var=="b":
			# ~ canvas1.var.focus_set()
			print("clicked at", event.x, event.y)
			# ~ if vinci2.var=="b" or vinci.var=="b":
			if (event.x >0 and event.x<400) and (event.y>0 and event.y<200):
			
					if vinci2.var=="b":
						posizione.var=0
						a.var=a.var+1
				
						
			elif(event.x>400 and event.x<600) and (event.y>0 and event.y<200):
				# ~ if res.var[1]=="-":
					# ~ posizione=1
					if vinci2.var=="b":
						posizione.var=1
						a.var=a.var+1
					
				
			elif(event.x>600 and event.x<800) and (event.y>0 and event.y<200):
					
					if vinci2.var=="b":
						posizione.var=2
						a.var=a.var+1
				
			
			####################################################################################	
			elif (event.x >0 and event.x<400) and (event.y>200 and event.y<400):
				# ~ if res.var[3]=="-":
				
				
				if vinci2.var=="b":
					posizione.var=3
					a.var=a.var+1
				
				# ~ else:
					# ~ print("ciaociao")
			elif(event.x>400 and event.x<600) and (event.y>200 and event.y<400):
				if vinci2.var=="b":
					posizione.var=4
					a.var=a.var+1
						
			
									
					# ~ else:
						# ~ print("ciaociao")
			elif(event.x>600 and event.x<800) and (event.y>200 and event.y<400):
				# ~ for scegli in sceltepc.var:
						# ~ if scegli==str(0):
				if vinci2.var=="b":
					posizione.var=5
					a.var=a.var+1
						
						
							
						# ~ print("scelta_pc",x.var)
						# ~ print("scelte possibili ",listasceltepc.var)
			###########################################################################################
			elif (event.x >0 and event.x<400) and (event.y>400 and event.y<800):	
				if vinci2.var=="b":
					posizione.var=6
					a.var=a.var+1
				
			
			elif(event.x>400 and event.x<600) and (event.y>400 and event.y<800):
				if vinci2.var=="b":
					posizione.var=7
					a.var=a.var+1

			elif(event.x>600 and event.x<800) and (event.y>400 and event.y<800):
				if vinci2.var=="b":
					posizione.var=8
					a.var=a.var+1	
			# ~ callback()			
			# ~ callback()			
		# ~ if (event.x >0 and event.x<400) and (event.y>0 and event.y<200):
			# ~ print("ciao")
			if posizione.var in listascelte_possibili.var:
					
						
		# ~ if scegli==str(posizione.var):
		# ~ if scegli==str(posizione.var):
		
				# ~ print("djfkljdlfkdl")
				# ~ canvas1.var.create_rectangle(250, 450, 350, 550,outline="#f11", fill="#1f1", width=2)
				res.var[posizione.var]="*"	
					
						
				disegna_rettangolo()
		
				print(res.var)
					
				listascelte_possibili.var.remove(posizione.var)
				print(listascelte_possibili.var)
				condizioni_vittoria()
				# ~ condizioni_pareggio()
				if len(listascelte_possibili.var)>=1:
					if vinci2.var=="b" and vinci.var=="b":
						x.var=random.choice(listascelte_possibili.var)
						
						res.var[x.var]="#"
						listascelte_possibili.var.remove(x.var)
						# ~ d
							
					
				# ~ else:
					# ~ printe("abcdef")
				# ~ vinci.var="a"	
				print("posizione= ",posizione.var)
				print("turno ",a.var)
			# ~ condizioni_vittoria()
				# ~ abc=70
				# ~ conta=0
				# ~ iniz=0
				# ~ fine=3
				# ~ for j in range(len(res.var)):
					# ~ print(j)
					# ~ conta=conta+1
					# ~ if conta%3==0:
						# ~ iniz=iniz+3
						# ~ fine=fine+3
						# ~ abc=abc+30
						# ~ label_res.var = tk.Label(root, text=str(j))
								
						# ~ label_res.var.config(font=('helvetica', 14))
								# ~ if conta%3==0:
								# ~ j=j+20
						# ~ canvas1.var.create_window(1100,abc,window=label_res.var)
					# ~ else:
				label_res.var = tk.Label(root, text=res.var[0:3])
							
				label_res.var.config(font=('helvetica', 14))
						# ~ if conta%3==0:
						# ~ j=j+20
				canvas1.var.create_window(1100,70,window=label_res.var)
				
				
				label_res.var = tk.Label(root, text=res.var[3:6])
							
				label_res.var.config(font=('helvetica', 14))
						# ~ if conta%3==0:
						# ~ j=j+20
				canvas1.var.create_window(1100,110,window=label_res.var)
				
				label_res.var = tk.Label(root, text=res.var[6:9])
							
				label_res.var.config(font=('helvetica', 14))
						# ~ if conta%3==0:
						# ~ j=j+20
				canvas1.var.create_window(1100,140,window=label_res.var)
	# ~ canvas= Canvas(root, width=100, height=100)
				# ~ vinci.var="a"
				
				condizioni_vittoria()
				# ~ condizioni_pareggio()
				# ~ if vinci2.var=="b" and vinci.var=="b":
				disegna_ovale()		
				if vinci.var=="a":
					label6.var = tk.Label(root, text="il giocatore ha vinto")
					label6.var.config(font=('helvetica', 14))
					canvas1.var.create_window(500, 20, window=label6.var)
				elif vinci2.var=="a":
					label6.var = tk.Label(root, text="il computer ha vinto")
					label6.var.config(font=('helvetica', 14))
					canvas1.var.create_window(500, 70, window=label6.var)
					
				elif pareggio.var=="pareggio": 
					label6.var = tk.Label(root, text="PAREGGIO")
					label6.var.config(font=('helvetica', 14))
					canvas1.var.create_window(500, 70, window=label6.var)
	canvas1.var.bind("<Key>", key)
	canvas1.var.bind("<Button-1>", callback)
	canvas1.var.pack()

	# ~ root.mainloop()

	# ~ canvas1.var = tk.Canvas(root, width = 1500, height =800,  relief = 'raised')
	# ~ canvas1.var.bind("<Key>", key)
	# ~ canvas1.var.bind("<Button-1>", callback)
	# ~ canvas1.var.pack()
	# ~ if (event.x >0 and event.x<400) and (event.y>0 and event.y<200):
		# ~ print("ciao")
	# ~ entry1 = tk.Entry (root) 								#SPAZIOinput
	# ~ canvas1.var.create_window(370, 50, window=entry1)

	


	label7.var = tk.Label(root, text="")
	label7.var.config(font=('helvetica', 14))
	canvas1.var.create_window(600, 100, window=label7.var)

	label8.var = tk.Label(root, text="")
	label8.var.config(font=('helvetica', 14))
	canvas1.var.create_window(600, 130, window=label8.var)

	label9.var = tk.Label(root, text="")
	label9.var.config(font=('helvetica', 14))
	canvas1.var.create_window(600, 430, window=label9.var)
	
			
	canvas1.var.create_line(250, 200, 800, 200)
	canvas1.var.create_line(250, 400, 800, 400)
	canvas1.var.create_line(250, 600, 800, 600)
	canvas1.var.create_line(400, 100, 400, 700)
	canvas1.var.create_line(600, 100, 600, 700)
	# ~ posiz=-3
	
	# ~ condizioni_vittoria()
	# ~ if vinci.var=="a":
		# ~ vinci2.var="b"
		
	# ~ if vinci2.var=="a":
		# ~ vinci.var="b"
	# ~ def ciao():
	
	# ~ print(posizione)
	# ~ print(a.var)		
	root.mainloop()
					# ~ print("scelta_pc",x.var)
						# ~ print("scelte possibili ",listasceltepc.var)
entrybox()						# ~ canvas1.var.create_rectangle(710, 410, 810, 500,outline="#f11", fill="#1f1", width=2)
						# ~ if vinci.var=="b":				#se il giocatore non ha vinto
						# ~ if len(listasceltepc.var)>=1:
							# ~ x.var=random.choice(listasceltepc.var)
						# ~ listasceltepc.var.remove(str(x.var))
						# ~ res.var[int(x.var)]="#"
				# ~ if vinci.var=="b":
def ciao():					# ~ a.var==8
			for scegli in listasceltepc.var:
					
					
					
						if scegli==str(posizione):
					
							# ~ canvas1.var.create_rectangle(500, 100, 600, 180,outline="#f11", fill="#1f1", width=2)
							canvas1.var.create_rectangle(650, 250, 750, 350,outline="#f11", fill="#1f1", width=2)
							res.var[int(posizione)]="*"	
						
					

						
							listasceltepc.var.remove(str(posizione))
							
							if vinci.var=="b":
								if len(listasceltepc.var)>=1:
									x.var=random.choice(listasceltepc.var)
									listasceltepc.var.remove(str(x.var))
									res.var[int(x.var)]="#"
							
					# ~ else:
						# ~ print("ciaociao")				
				# ~ if a.var<5 :
			
			# ~ if len(listasceltepc.var)>=1:
				
				# ~ x.var=random.choice(listasceltepc.var)				#se l ultima scelta e del giocatore allora il non deve nemmeno giocare 
			
				# ~ listasceltepc.var.remove(str(x.var))
				# ~ res.var[int(x.var)]="#"	
			
			if a.var==5:
				x.var="abc"



			label18.var = tk.Label(root, text="")
			label18.var.config(font=('helvetica', 14))
			canvas1.var.create_window(150, 90, window=label18.var)
			
			label.var = tk.Label(root, text=str("sceltacomputer:"+str(x.var)+"\n"+"scelta del giocatore: "+str(posizione)))
			label.var.config(font=('helvetica', 14))
			canvas1.var.create_window(150, 140, window=label.var)
	
			
			
			# ~ for xxxx in res.var:
				# ~ if xxxx!="-":
					# ~ pass
			
		
			
			label18.var.destroy()
			label6.var.destroy()
			label7.var.destroy()
			label8.var.destroy()
			label9.var.destroy()

			label9.var = tk.Label(root, text="turno: "+str(a.var)+"\n"+"scelte_possibili"+"\n"+str(listasceltepc.var))
			label9.var.config(font=('helvetica', 14))
			canvas1.var.create_window(800, 50, window=label9.var)


			if vinci.var=="a":
	
				label18.var = tk.Label(root, text="il giocatore vince")
				label18.var.config(font=('helvetica', 14))
				canvas1.var.create_window(400, 20, window=label18.var)
	
	
			elif vinci2.var=="a":
			
				label18.var = tk.Label(root, text="il computer vince")
				label18.var.config(font=('helvetica', 14))
				canvas1.var.create_window(400,20, window=label18.var)
			
			elif a.var>=5:
				if vinci2.var=="b" and vinci.var=="b":
					label18.var = tk.Label(root, text="pareggio")
					label18.var.config(font=('helvetica', 14))
					canvas1.var.create_window(400,20, window=label18.var)
			
						
	# ~ if vinci2.var=="b" and vinci.var=="b" and a.var>=5:
			# ~ print("pareggio")
			# ~ label78.var = tk.Label(root, text=str(res.var))
			# ~ label78.var.config(font=('helvetica', 14))
			# ~ canvas1.var.create_window(900,200, window=label78.var)				
						
						
					# ~ canvas1.var.create_rectangle(710, 410, 810, 500,outline="#f11", fill="#1f1", width=2)
						
			print("res",res.var)
			print("turno ",a.var)
			
		
			
			
			
			
			
			
			
			if a.var>=5:
				if vinci2.var=="b" and vinci.var=="b":
					print("pareggio")	
				
					
						
			if vinci2.var=="b" and vinci.var=="b":

				canvas1.var.bind("<Button-1>", callback)
						# ~ if a.var<5:
				

		
		
	
	
			canvas1.var.pack()
# ~ inserisci.var=3			
				
				
				

		# ~ inserisci.var=entry1.get()

		# ~ print("scelta giocatore", inserisci)
		# ~ sceltegiocatore.append(inserisci)
		
		# ~ griglia()
		# ~ listasceltepc.var.remove(str(inserisci.var))
	# ~ if a.var>=4:
		# ~ if vinci2=="b" and vinci=="b":
			# ~ print("pareggio")	



	


				# ~ print(sceltegiocatore)
				# ~ print(listasceltepc)
				
				# ~ print("in",inserisci.var)
				# ~ print("x.var",x.var)
				

				


	



	# ~ a=str(stringa3.var)
			root.mainloop()




# ~ griglia()
		# ~ break

	# ~ if contadisegno1.var==11:

	# ~ conta=9
# ~ l=[1,4,5,1,1,3,88,5]
# ~ print("res.vartituiscituttiindici",[index for index, value in enumerate(l) if value == 5])
# ~ print(listadiindici)
# ~ print(stringa)
# ~ print(stringa)
	# ~ print(listadiindici)
		# ~ stringa.replace("a",indovinalettera)
		# ~ rivelaparola=str(a[0])+str(a[a.index(i)])+str(a[len(a)-1])
# ~ rivelaparola
		# ~ print(rivelaparola)

