#PULSANTE RESTART FUNZIONA
#label _res_funziona
###############################################

#parti da sistemare_-->consentire a utente di premere pulsante ancora prima di giocare senza che si generi un errore
				#--->migliorare area dove si clicca in modo che si possa cliccare solo nei quadrati , 
def caso():
	caso.var="abc"
caso()



def jj():
	jj.var=""
jj()
def jj1():
	jj1.var=""
jj1()
def jj2():
	jj2.var=""
jj2()
def jj3():
	jj3.var=""
jj3()

def jj4():
	jj4.var=""
jj4()
def jj5():
	jj5.var=""
jj5()
def jj6():
	jj6.var=""
jj6()
def jj7():
	jj7.var=""
jj7()



def traccia_riga():
				#8 casi di vittoria e tracciamento righe indipendentemente che vinca il pc o il giocatore(3 linee orizziontali, 3 verticali e 2 diagonali)
				if caso.var==1:# ~ if res.var[0]=="*" and res.var[1]=="*"  and res.var[2]=="*" :				#casi orizzontali
						
					jj.var=canvas1.var.create_line(250, 150, 800, 150,width=2,fill="red")
						
				elif caso.var==2:

			
					jj1.var=canvas1.var.create_line(250, 300, 800, 300,width=2,fill="red")
					
				elif caso.var==3:
			
					jj2.var=canvas1.var.create_line(250, 500, 800, 500,width=2,fill="red")
				# ~ vinci2.var="b"
					# ~ break
			# ~ ######################################
# ~ def ciao():	
				elif caso.var==4:
				# ~ elif res.var[0]=="*" and res.var[3]=="*"  and res.var[6]=="*" :		#casi verticali
					jj3.var=canvas1.var.create_line(300, 100, 300, 700,width=2,fill="red")

						# ~ break
				elif caso.var==5:
				
					jj4.var=	canvas1.var.create_line(500, 100, 500, 700,width=2,fill="red")
						# ~ break
				elif caso.var==6:
				# ~ elif res.var[2]=="*" and res.var[5]=="*"  and res.var[8]=="*" :
					
						# ~ print("tris")
						# ~ vinci.var="a"
					jj5.var=	canvas1.var.create_line(700, 100, 700, 700,width=2,fill="red")
					
						# ~ vinci2.var="b"
				# ~ #####vinci2.var="b"#########################################
				elif caso.var==7:
			
					jj6.var=	canvas1.var.create_line(240, 50, 800,590,width=2,fill="red")	
					
				elif caso.var==8:
			
						jj7.var=canvas1.var.create_line(200, 600, 650,150,width=2,fill="red")
					
					
				######################################
				


















def x():
		x.var=-1
x()

def inserisci():
		inserisci.var=	-1
inserisci()	
def canvas1():
	canvas1.var=""
canvas1()

def r():
	r.var=""
r()

def r1():
	r1.var=""
r1()
def r2():
	r2.var=""
r2()

def r3():
	r3.var=""
r3()

def r4():
	r4.var=""
r4()

def r5():
	r5.var=""
r5()

def r6():
	r6.var=""
r6()

def r7():
	r7.var=""
r7()

def r8():
	r8.var=""
r8()
def r9():
	r9.var=""
r9()































def z():
	z.var=""
z()

def z1():
	z1.var=""
z1()
def z2():
	z2.var=""
z2()
def z3():
	z3.var=""
z3()
def z4():
	z4.var=""
z4()
def z5():
	z5.var=""
z5()
def z6():
	z6.var=""
z6()
def z7():
	z7.var=""
z7()


def z8():
	z8.var=""
z8()


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

def words():
	words.var=""
words()
#VERSIONE UMANO CONTRO PC-->INIZIA L umano-->bisogna gestire errori->quando umano sceglie un numero giä scelto
words.var = "- - - - - - - - -"
def pareggio():
	pareggio.var="abc"
pareggio()


def res():
	res.var=""
res()
res.var = words.var.split()
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
				if res.var[0]=="*" and res.var[1]=="*"  and res.var[2]=="*" :	
					caso.var=1#casi orizzontali
					print("tris")
					vinci.var="a"
					# ~ canvas.create_line(15, 25, 200, 25)
					# ~ canvas1.var.create_line(200, 150, 700, 150,width=2,fill="red")
					# ~ if c=33
					# ~ vinci2.var="b"
							# ~ break
				elif res.var[3]=="*" and res.var[4]=="*"  and res.var[5]=="*" :
					caso.var=2
					print("tris")
					vinci.var="a"
					# ~ canvas1.var.create_line(200, 300, 700, 300,width=2,fill="red")
					# ~ vinci2.var="b"
					#	break
					# ~ break
				elif res.var[6]=="*" and res.var[7]=="*"  and res.var[8]=="*" :
					caso.var=3
					print("tris")
					vinci.var="a"
					# ~ canvas1.var.create_line(200, 500, 700, 500,width=2,fill="red")
					vinci2.var="b"
					# ~ break
			# ~ ######################################
				elif res.var[0]=="*" and res.var[3]=="*"  and res.var[6]=="*" :		#casi verticali
						caso.var=4
						print("tris")
						vinci.var="a"
						vinci2.var="b"
						# ~ break
				elif res.var[1]=="*" and res.var[4]=="*"  and res.var[7]=="*" :
						caso.var=5
						print("tris")
						vinci.var="a"
						vinci2.var="b"
						# ~ break
				elif res.var[2]=="*" and res.var[5]=="*"  and res.var[8]=="*" :
						caso.var=6
						print("tris")
						vinci.var="a"
						# ~ canvas1.var.create_line(700, 50, 700, 700,width=2,fill="red")
						# ~ break
						# ~ break
						vinci2.var="b"
				# ~ #####vinci2.var="b"#########################################
				elif res.var[0]=="*" and res.var[4]=="*"  and res.var[8]=="*" :	
						caso.var=7	#casi diagonali
						print("tris")
						vinci.var="a"
						# ~ canvas1.var.create_line(200, 800, 800,50,width=2,fill="red")
						vinci2.var="b"
						# ~ break
				elif res.var[2]=="*" and res.var[4]=="*"  and res.var[6]=="*" :
						caso.var=8
						print("tris")
						vinci.var="a"
						# ~ canvas1.var.create_line(50, 800, 800,50,width=2,fill="red")
						vinci2.var="b"
						# ~ break
				######################################
				if res.var[0]=="#" and res.var[1]=="#"  and res.var[2]=="#" :	
					caso.var=1			#computer
					print("tris")
					vinci2.var="a"
					vinci.var="b"
					# ~ canvas1.var.create_line(200, 100, 800, 100,width=2,fill="red")
					# ~ break
				elif res.var[3]=="#" and res.var[4]=="#"  and res.var[5]=="#" :
						caso.var=2
						print("tris")
						vinci2.var="a"
						vinci.var="b"
						# ~ canvas1.var.create_line(200, 200, 800,200,width=2,fill="red")
						# ~ break
				elif res.var[6]=="#" and res.var[7]=="#"  and res.var[8]=="#" :
						caso.var=3
						print("tris")
					
						# ~ canvas1.var.create_line(200, 500, 800,500,width=2,fill="red")
						vinci2.var="a"
						vinci.var="b"
						# ~ break
				# ~ ######################################
				elif res.var[0]=="#" and res.var[3]=="#"  and res.var[6]=="#" :	
						caso.var=4	#casi verticali
						print("tris")
						vinci2.var="a"
						vinci.var="b"
						# ~ canvas1.var.create_line(300, 50, 300, 600,width=2,fill="red")
						# ~ break
				elif res.var[1]=="#" and res.var[4]=="#"  and res.var[7]=="#" :
						caso.var=5
						vinci2.var="a"
						

						vinci.var="b"
						print("tris")

						# ~ break
						# ~ break
				elif res.var[2]=="#" and res.var[5]=="#"  and res.var[8]=="#" :
						caso.var=6
						vinci2.var="a"
						# ~ canvas1.var.create_line(700, 50, 700, 700,width=2,fill="red")
						vinci.var="b"
						print("tris")
						# ~ break
						# ~ break
				# ~ ##############################################
				elif res.var[0]=="#" and res.var[4]=="#"  and res.var[8]=="#" :	
						caso.var=7	#casi diagonali
						vinci2.var="a"
						# ~ canvas1.var.create_line(50, 50, 800,800,width=2,fill="red")
						vinci.var="b"
						print("tris")
						# ~ break
				elif res.var[2]=="#" and res.var[4]=="#"  and res.var[6]=="#" :
						caso.var=8
						vinci2.var="a"
						# ~ canvas1.var.create_line(50, 800, 800,50,width=2,fill="red")
						vinci.var="b"
						print("tris")
						# ~ break
				
				print("vinci2",vinci2.var)
				print("vinci",vinci.var)

# ~ def condizioni_pareggio():
				
						# ~ print("pareggio")
					# ~ else:
						# ~ pareggio.var="abc"

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
			
				r1.var=canvas1.var.create_rectangle(250, 80, 350, 180,outline="#f11", fill="#1f1", width=2)
			
		elif posizione.var==1:
			
				r2.var=canvas1.var.create_rectangle(450, 80, 550, 180,outline="#f11", fill="#1f1", width=2)
		elif posizione.var==2:
				r3.var=canvas1.var.create_rectangle(650, 80, 750, 180,outline="#f11", fill="#1f1", width=2)	

		elif posizione.var==3:
				r4.var=canvas1.var.create_rectangle(250, 250, 350, 350,outline="#f11", fill="#1f1", width=2)
		elif posizione.var==4:
				r5.var=canvas1.var.create_rectangle(450, 250, 550, 350,outline="#f11", fill="#1f1", width=2)
		
		elif posizione.var==5:
			r6.var=canvas1.var.create_rectangle(450+200, 250, 550+200, 350,outline="#f11", fill="#1f1", width=2)
		elif posizione.var==6:
			r7.var=canvas1.var.create_rectangle(250, 450, 350, 550,outline="#f11", fill="#1f1", width=2)
		elif posizione.var==7:
			r8.var=canvas1.var.create_rectangle(250+200, 450, 350+200, 550,outline="#f11", fill="#1f1", width=2)
			
		elif posizione.var==8:
			r9.var=canvas1.var.create_rectangle(250+200+200, 450, 350+200+200,550,outline="#f11", fill="#1f1", width=2)
		# ~ elif posizione.var==7:
		# ~ elif posizione.var==8:
		
def disegna_ovale():
			
				
				if vinci.var=="b":		#disegna i cerchi solo se non il giocatore  non ha ancora vinto
					if int(x.var)==0:
						z.var=canvas1.var.create_oval(250, 80, 350, 180, outline="#f11",fill="#1f1", width=2)
					elif int(x.var)==1:
						z1.var=canvas1.var.create_oval(450, 80, 550, 180, outline="#f11",fill="#1f1", width=2)
					elif int(x.var)==2:
						z2.var=canvas1.var.create_oval(650,80, 750, 180, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==3:
						z3.var=canvas1.var.create_oval(250, 250, 350, 350, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==4:
						z4.var=canvas1.var.create_oval(450, 250, 550, 350, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==5:
						z5.var=canvas1.var.create_oval(650, 250, 750, 350, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==6:
						z6.var=canvas1.var.create_oval(250, 450, 350, 550, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==7:
						z7.var=canvas1.var.create_oval(450, 450, 550, 550, outline="#f11",fill="#1f1", width=2)

					elif int(x.var)==8:
						z8.var=canvas1.var.create_oval(650, 450, 750, 550, outline="#f11",fill="#1f1", width=2)

def cancella_ovale():
	canvas1.var.delete(z.var)
	canvas1.var.delete(z1.var)
	canvas1.var.delete(z2.var)
	canvas1.var.delete(z3.var)
	canvas1.var.delete(z4.var)
	canvas1.var.delete(z5.var)
	canvas1.var.delete(z6.var)
	canvas1.var.delete(z7.var)
	canvas1.var.delete(z8.var)						
	# ~ z.var.destroy()
def cancella_linee():
			canvas1.var.delete(jj.var) 
			canvas1.var.delete(jj1.var)#Deletes the lines
			canvas1.var.delete(jj2.var)
			canvas1.var.delete(jj3.var)
			canvas1.var.delete(jj4.var)
			canvas1.var.delete(jj5.var)
			canvas1.var.delete(jj6.var)
			canvas1.var.delete(jj7.var)
		# ~ canvas1.var.delete(jj8.var)
def cancella_quadrati():
		# ~ canvas1.var.delete(r.var) #Deletes the squares
			canvas1.var.delete(r1.var)
			canvas1.var.delete(r2.var)
			canvas1.var.delete(r3.var)
			canvas1.var.delete(r4.var)
			canvas1.var.delete(r5.var)
			canvas1.var.delete(r6.var)
			canvas1.var.delete(r7.var)
			canvas1.var.delete(r8.var)
		
			canvas1.var.delete(r9.var)

	# ~ z1.var.destroy()
	# ~ z2.var.destroy()
	# ~ z3.var.destroy()
	# ~ z4.var.destroy()
	# ~ z5.var.destroy()
	# ~ z6.var.destroy()
	# ~ z7.var.destroy()
	# ~ z8.var.destroy()	# ~ label_res.var.destroy()
		# ~ label6.var.destroy()
		# ~ canvas1.var.delete(z.v
		# ~ canvas1.var.delete(z.var)		


def entrybox():
	# ~ def entry1():
		# ~ entry1.var=""

	
	

	import tkinter as tk
	root = Tk()
	canvas1.var = tk.Canvas(root, width = 1500, height =800,  relief = 'raised')
	
	# ~ label_res.var = tk.Label(root, text=res.var[0:3])
				
	# ~ label_res.var.config(font=('helvetica', 14))
			# ~ if conta%3==0:
			# ~ j=j+20
	# ~ canvas1.var.create_window(1100,70,window=label_res.var)


	# ~ label_res.var = tk.Label(root, text=res.var[3:6])
				
	# ~ label_res.var.config(font=('helvetica', 14))
			# ~ if conta%3==0:
			# ~ j=j+20
	# ~ canvas1.var.create_window(1100,110,window=label_res.var)

	# ~ label_res.var = tk.Label(root, text=res.var[6:9])
				
	# ~ label_res.var.config(font=('helvetica', 14))
			# ~ if conta%3==0:
			# ~ j=j+20
	# ~ canvas1.var.create_window(1100,140,window=label_res.var)	
	
	def drawlabel():
		# ~ res=[x for x in range(1,10)]					#stampa per esempio in questo modo:
					
		def posX():
			posX.var=1000
		posX()
		def posY():
			posY.var=200
		posY()																#			1 2 3
																			#			4 5 6
		# ~ canvas1.pack()													#			7 8 9
		j=0
		
		for x in res.var:
			# ~ if j>:
				# ~ j=200
			j=j+1
			# ~ j=j+1
			if j>1:
				posX.var=posX.var+20
			# ~ print(posX)
			# ~ label6.var = tk.Label(root, text="pareggio")
			# ~ label6.var.config(font=('helvetica', 14))
			# ~ canvas1.var.create_window(500, 50, window=label6.var)		
			# ~ if j==4 or j==6:
			if ((j-1)%3==0):
				posX.var=1000
				posY.var=posY.var+20
			label_res.var = tk.Label(root, text=x)
			label_res.var.config(font=('helvetica', 14))
			canvas1.var.create_window(posX.var, posY.var, window=label_res.var)		
	# ~ label_res.var = tk.Label(root, text=res.var[0:3])
	def newgame():
		import tkinter as tk

		cancella_linee()
		cancella_quadrati()
		cancella_ovale()
		# ~ def pareggio():
		pareggio.var="abc"
# ~ pareggio()
		vinci.var="b"
		vinci2.var="b"	
		
		
		a.var=0		#azzero i turni
		
		words.var = "- - - - - - - - -"
		res.var=""
		res.var = words.var.split()
		# ~ canvas1.var.create_window(1100,140,window=label_res.var)
		listascelte_possibili.var=[0,1,2,3,4,5,6,7,8]
		print("res",res.var)
		print("scelte", listascelte_possibili.var)
		drawlabel()
		# ~ label_res.var.destroy()
		
		# ~ label_res.var = tk.Label(root, text=res.var[0:4])
					
		# ~ label_res.var.config(font=('helvetica', 14))
				# ~ if conta%3==0:
				# ~ j=j+20
		# ~ canvas1.var.create_window(1100,110,window=label_res.var)
		# ~ label_res.var = tk.Label(root, text=res.var[3:6])
					
		# ~ label_res.var.config(font=('helvetica', 14))
				# ~ if conta%3==0:
				# ~ j=j+20
		# ~ canvas1.var.create_window(1100,110,window=label_res.var)
		# ~ label_res.var = tk.Label(root, text=res.var[6:9])
					
		# ~ label_res.var.config(font=('helvetica', 14))
				# ~ if conta%3==0:
				# ~ j=j+20
		# ~ canvas1.var.create_window(1100,110,window=label_res.var)
		# ~ label6.var = tk.Label(root, text="")
		# ~ label6.var.config(font=('helvetica', 14))
		# ~ canvas1.var.create_window(500, 50, window=label6.var)
		
		label6.var.destroy()
		label8.var.destroy()
	
		# ~ label.
		# ~ label8.var = tk.Label(root, text="turno "+str(a.var))
		# ~ label8.var.config(font=('helvetica', 14))
		# ~ canvas1.var.create_window(800, 130, window=label8.var)
			# ~ if vinci2.var=="a":
		# ~ label_res.var e= tk.Label(root, text=res.var[6:9])						
		# ~ label_res.var.config(font=('helvetica', 14))
				# ~ if conta%3=e=0:
				# ~ j=j+20
		# ~ canvas1.var.create_window(1100,70,window=label_res.var)

	# ~ label_res.var.config(font=('helvetica', 14))
			# ~ if conta%3==0:
			# ~ j=j+20
	# ~ canvas1.var.create_window(1100,140,window=label_res.var)
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
						# ~ a.var=a.var+1
				
						
			elif(event.x>400 and event.x<600) and (event.y>0 and event.y<200):
				# ~ if res.var[1]=="-":
					# ~ posizione=1
					if vinci2.var=="b":
						posizione.var=1
						# ~ a.var=a.var+1
					
				
			elif(event.x>600 and event.x<800) and (event.y>0 and event.y<200):
					
					if vinci2.var=="b":
						posizione.var=2
						# ~ a.var=a.var+1
				
			
			####################################################################################	
			elif (event.x >0 and event.x<400) and (event.y>200 and event.y<400):
				# ~ if res.var[3]=="-":
				
				
				if vinci2.var=="b":
					posizione.var=3
					# ~ a.var=a.var+1
				
				# ~ else:
					# ~ print("ciaociao")
			elif(event.x>400 and event.x<600) and (event.y>200 and event.y<400):
				if vinci2.var=="b":
					posizione.var=4
					# ~ a.var=a.var+1
						
			
									
					# ~ else:
						# ~ print("ciaociao")
			elif(event.x>600 and event.x<800) and (event.y>200 and event.y<400):
				# ~ for scegli in sceltepc.var:
						# ~ if scegli==str(0):
				if vinci2.var=="b":
					posizione.var=5
					# ~ a.var=a.var+1
						
						
							
						# ~ print("scelta_pc",x.var)
						# ~ print("scelte possibili ",listasceltepc.var)
			###########################################################################################
			elif (event.x >0 and event.x<400) and (event.y>400 and event.y<800):	
				if vinci2.var=="b":
					posizione.var=6
					# ~ a.var=a.var+1
				
			
			elif(event.x>400 and event.x<600) and (event.y>400 and event.y<800):
				if vinci2.var=="b":
					posizione.var=7
					# ~ a.var=a.var+1

			elif(event.x>600 and event.x<800) and (event.y>400 and event.y<800):
				if vinci2.var=="b":
					posizione.var=8
			
			# ~ callback()			
			# ~ callback()			
		# ~ if (event.x >0 and event.x<400) and (event.y>0 and event.y<200):
			# ~ print("ciao")
			if posizione.var in listascelte_possibili.var:
					
				a.var=a.var+1	
				
				label8.var = tk.Label(root, text="turno "+str(a.var))
				label8.var.config(font=('helvetica', 14))
				canvas1.var.create_window(800, 130, window=label8.var)		
		# ~ if scegli==str(posizione.var):
		# ~ if scegli==str(posizione.var):
		
				# ~ print("djfkljdlfkdl")
				# ~ canvas1.var.create_rectangle(250, 450, 350, 550,outline="#f11", fill="#1f1", width=2)
				res.var[posizione.var]="*"	
					
						
				disegna_rettangolo()
				
				
			
				print(res.var)
				# ~ label_res.var.destroy()			
				listascelte_possibili.var.remove(posizione.var)
				print(listascelte_possibili.var)
				condizioni_vittoria()
				# ~ condizioni_pareggio()
				if len(listascelte_possibili.var)>=1:
					if vinci2.var=="b" and vinci.var=="b":
						x.var=random.choice(listascelte_possibili.var)
						
						res.var[x.var]="#"

						# ~ d
							
						listascelte_possibili.var.remove(x.var)
						# ~ else:
							# ~ printe("abcdef")
						# ~ vinci.var="a"	
						print("posizione= ",posizione.var)
						print("turno ",a.var)
					
							# ~ else:
						label_res.var = tk.Label(root, text="")				
						label_res.var.config(font=('helvetica', 14))		# ~ if conta%3==0:
								# ~ j=j+20
						canvas1.var.create_window(1100,70,window=label_res.var)	

						label_res.var.destroy()

						# ~ canvas= Canvas(root, width=100, height=100)
						# ~ vinci.var="a"

						condizioni_vittoria()
						disegna_ovale()
				
				# ~ condizioni_pareggio()
				# ~ if vinci2.var=="b" and vinci.var=="b":
				
				# ~ label6.var = tk.Label(root, text="il giocatore ha vinto")
				# ~ label6.var.config(font=('helvetica', 14))
				# ~ canvas1.var.create_window(500, 50, window=label6.var)		
				# ~ label6.destroy()
				if vinci.var=="a":
											
					traccia_riga()
					label6.var = tk.Label(root, text="il giocatore ha vinto")
					label6.var.config(font=('helvetica', 14))
					canvas1.var.create_window(500, 50, window=label6.var)
					# ~ vinci.var="b"
					# ~ vinci2.var="b"
				elif vinci2.var=="a":
					label6.var = tk.Label(root, text="il computer ha vinto")
					label6.var.config(font=('helvetica', 14))
					canvas1.var.create_window(500, 50, window=label6.var)
					traccia_riga()
					# ~ vinci.var="b"
					# ~ vinci2.var="b"							
					
				elif a.var>=5 and vinci.var=="b" and vinci2.var=="b": 
					label6.var = tk.Label(root, text="PAREGGIO")
					label6.var.config(font=('helvetica', 14))
					canvas1.var.create_window(500, 50, window=label6.var)
					# ~ vinci.var="b"
					# ~ vinci2.var="b"		

				elif vinci2.var!="a" and vinci.var!="a": 
					
					label6.var = tk.Label(root, text="")
					label6.var.config(font=('helvetica', 14))
					canvas1.var.create_window(500, 50, window=label6.var)
					label6.var.destroy()
				# ~ elif a.var>=5 :
						# ~ if vinci2.var=="b" and vinci.var=="b":	
							# ~ pareggio.var=="pareggio"
					
				
			# ~ pareggio.var="pareggio"
						# ~ cancella_ovale()
# ~ if vinci2.var=="a":

# ~ label6.var.destroy()
# ~ elif pareggio.var=="pareggio": 
# ~ label6.var = tk.Label(root, text="PAREGGIO")
			# ~ label6.var.config(font=('helvetica', 14))
			# ~ canvas1.var.create_window(500, 50, window=label6.var)											

# ~ if vinci.var=="a":

				label_res.var.destroy()
					# ~ label6.var.destroy()e
				drawlabel()	

				
	if pareggio.var=="pareggio":
				label6.var = tk.Label(root, text="pareggio")
				label6.var.config(font=('helvetica', 14))
				canvas1.var.create_window(500, 50, window=label6.var)		

	
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

			# ~ import Tkinter
		# ~ import tkMessageBox

	# ~ top = Tkinter.Tk()
	
	
		
	button1 = tk.Button(text='restart', command=newgame, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
	canvas1.var.create_window(50,50, window=button1)	
		
	# ~ root.mainloop()


	label7.var = tk.Label(root, text="TRIS")
	label7.var.config(font=('helvetica', 14))
	canvas1.var.create_window(600, 10, window=label7.var)


	# ~ label9.var = tk.Label(root, text="")
	# ~ label9.var.config(font=('helvetica', 14))
	# ~ canvas1.var.create_window(600, 430, window=label9.var)
	
			
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

