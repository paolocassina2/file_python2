#PULSANTE RESTART FUNZIONA
#VERSIONE -->UMANO CONTRO UMANO
###############################################
#CARTELLA==game
  
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


vinci.var="b"
vinci2.var="b"
import numpy as np
def condizioni_vittoria():
	aaa=res.var[0:3]
	bbb=res.var[3:6]
	ccc=res.var[6:9]
	caso.var=0
	a = np.array([aaa,bbb,ccc])
	
	# ~ if vinci.var=="b" and vinci2.var=="b":
	for x in range(len(a)):
			caso.var=caso.var+1
			abc1=set(a[x])
			print(abc1)
			if  "-" not in abc1:
				if len(abc1)==1:
					if "*" in abc1:
						print("vittoria g1,orizzionataòe")
						vinci.var="a"
						print("caso.varciao",caso.var)
						break
					else:
						print("vittoria g2,orizzontale")
						vinci2.var="a"
						print("caso.varciao",caso.var)
						break
	# ~ if vinci2.var=
	#scorro per capire se ho vinto in verticale solo se non ho già vinto in orizzontale
	#primi 3 casi, linee orizzontali,
	#casi 4,5,6, linee verticali
	#caso 7,8 linee diagonali
	if vinci.var=="b" and vinci2.var=="b":
		for z in range(len(a)):
				caso.var=caso.var+1
				# ~ b=list(a[:,x])
				# ~ print(b)
				print()
				abc=set(list(a[:,z]))
				if  "-" not in abc:
					if len(abc)==1:#se il set è lungo uno significa che gli elementi sono tutti uguali
						if "*" in abc :
							vinci.var="a"
							print("vittoria g1_verticale")
							print("caso.varciao",caso.var)
							break
						else:
							print("vittoria g2_verticale")
							print("caso.varciao",caso.var)
							vinci2.var="a"
							break
		# ~ caso.var=caso.var
	
	diag1=[aaa[0],bbb[1],ccc[2]]
	diag2=[aaa[2],bbb[1],ccc[0]]
	if  "-" not in diag1:
		if len(set(diag1))==1:
			if "*" in diag1:
				print("vittoria g1,diagonale1")
				caso.var=7
				vinci.var="a"
			else:
				print("vittoria g2,diagonale1")
				caso.var=7
				vinci2.var="a"
	if  "-" not in diag2:
		if len(set(diag2))==1:
			if "*" in diag2:
				print("vittoria g1,diagonale2")
				vinci.var="a"
				caso.var=8
			else:
				print("vittoria g2,diagonale2")
				vinci2.var="a"
				caso.var=8
	# ~ print("caso.var",caso.var)
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
					if int(posizione.var)==0:
						z.var=canvas1.var.create_oval(250, 80, 350, 180, outline="#f11",fill="#1f1", width=2)
					elif int(posizione.var)==1:
						z1.var=canvas1.var.create_oval(450, 80, 550, 180, outline="#f11",fill="#1f1", width=2)
					elif int(posizione.var)==2:
						z2.var=canvas1.var.create_oval(650,80, 750, 180, outline="#f11",fill="#1f1", width=2)

					elif int(posizione.var)==3:
						z3.var=canvas1.var.create_oval(250, 250, 350, 350, outline="#f11",fill="#1f1", width=2)

					elif int(posizione.var)==4:
						z4.var=canvas1.var.create_oval(450, 250, 550, 350, outline="#f11",fill="#1f1", width=2)

					elif int(posizione.var)==5:
						z5.var=canvas1.var.create_oval(650, 250, 750, 350, outline="#f11",fill="#1f1", width=2)

					elif int(posizione.var)==6:
						z6.var=canvas1.var.create_oval(250, 450, 350, 550, outline="#f11",fill="#1f1", width=2)

					elif int(posizione.var)==7:
						z7.var=canvas1.var.create_oval(450, 450, 550, 550, outline="#f11",fill="#1f1", width=2)

					elif int(posizione.var)==8:
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

	def conta():
		conta.var=0
	conta()
	# ~ def a():
		# ~ a.var=0
	# ~ a()

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
		print("game restarted")
		cancella_linee()
		cancella_quadrati()
		cancella_ovale()
		# ~ def pareggio():
		pareggio.var="abc"
# ~ pareggio()
		vinci.var="b"
		vinci2.var="b"	
		conta.var=0
		posizione.var=-10
		# ~ a.var=0		#azzero i turni
		
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
		
		# ~ label6.var = tk.Label(root, text="")
		# ~ label6.var.config(font=('helvetica', 14))
		# ~ canvas1.var.create_window(500, 50, window=label6.var)	
		
		
		label6.var.destroy()
		
		label8.var = tk.Label(root, text="")
		label8.var.config(font=('helvetica', 14))
		canvas1.var.create_window(800, 130, window=label8.var)	
		
		label8.var.destroy()
		label8.var = tk.Label(root, text="turno "+str(conta.var))
		label8.var.config(font=('helvetica', 14))
		canvas1.var.create_window(800, 130, window=label8.var)	
		# ~ label.
		
		
		
		
		
		
		
	# ~ canvas1.var.bind("<Key>", key)
	# ~ canvas1.var.bind("<Button-1>", callback)
	# ~ canvas1.var.pack()

		
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
	# ~ def contaclick():
		# ~ contaclick.var=0
	# ~ contaclick()
	# ~ a.var=0
	def callback(event):
		# ~ contaclick.var+=1
		# ~ print(contaclick.var,"cccc")
		# ~ if contaclick.var>=2:
		# ~ print ("clicked at", event.x, event.y)
		if vinci2.var=="b" and vinci.var=="b":
			# ~ canvas1.var.focus_set()
			print("clicked at", event.x, event.y)
			# ~ if vinci2.var=="b" or vinci.var=="b":
			if (event.x >253 and event.x<400) and (event.y>100 and event.y<200):
			
					if vinci2.var=="b":
						posizione.var=0
						# ~ a.var=a.var+1
				
						
			elif(event.x>400 and event.x<600) and (event.y>100 and event.y<200):
				# ~ if res.var[1]=="-":
					# ~ posizione=1
					if vinci2.var=="b":
						posizione.var=1
						# ~ a.var=a.var+1
					
				
			elif(event.x>600 and event.x<800) and (event.y>100 and event.y<200):
					
					if vinci2.var=="b":
						posizione.var=2
						# ~ a.var=a.var+1
				
			
			####################################################################################	
			elif (event.x >253 and event.x<400) and (event.y>200 and event.y<400):
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
			elif (event.x >253 and event.x<400) and (event.y>400 and event.y<590):		
				if vinci2.var=="b":
					posizione.var=6
					# ~ a.var=a.var+1
				
			
			elif(event.x>400 and event.x<600) and (event.y>400 and event.y<590):
				if vinci2.var=="b":
					posizione.var=7
					# ~ a.var=a.var+1

			elif(event.x>600 and event.x<800) and (event.y>400 and event.y<590):
				if vinci2.var=="b":
					posizione.var=8
			
				# ~ callback()			
			# ~ callback()			
		# ~ if (event.x >0 and event.x<400) and (event.y>0 and event.y<200):
			# ~ print("ciao")
			
			if posizione.var in listascelte_possibili.var:
				conta.var=conta.var+1
				print("conta.var ",conta.var)
					
				if conta.var%2!=0:
					
					res.var[posizione.var]="*"
					disegna_rettangolo()
				else:
					res.var[posizione.var]="#"
					disegna_ovale()
				# ~ a.var+=1
				# ~ print("a.var",a.var)
				label8.var = tk.Label(root, text="")
				label8.var.config(font=('helvetica', 14))
				canvas1.var.create_window(800, 130, window=label8.var)
				label8.var.destroy()
				label8.var = tk.Label(root, text="turno "+str(conta.var))
				label8.var.config(font=('helvetica', 14))
				canvas1.var.create_window(800, 130, window=label8.var)	
				listascelte_possibili.var.remove(posizione.var)
				print(listascelte_possibili.var)
				condizioni_vittoria()
				# ~ a.var=conta.var+1
				
			
				# ~ print(res.var)
				# ~ label_res.var.destroy()			
				
				# ~ condizioni_pareggio()
			#
					
					# ~ condizioni_pareggio()
				# ~ if vinci2.var=="b" and vinci.var=="b":
				
				# ~ label6.var = tk.Label(root, text="il giocatore ha vinto")
				# ~ label6.var.config(font=('helvetica', 14))
				# ~ canvas1.var.create_window(500, 50, window=label6.var)		
				# ~ label6.destroy()
				if vinci.var=="a":
											
					traccia_riga()
					label6.var = tk.Label(root, text="il giocatore1 ha vinto")
					label6.var.config(font=('helvetica', 14))
					canvas1.var.create_window(500, 50, window=label6.var)
					# ~ vinci.var="b"
					# ~ vinci2.var="b"
				elif vinci2.var=="a":
					label6.var = tk.Label(root, text="il giocatore2 ha vinto")
					label6.var.config(font=('helvetica', 14))
					canvas1.var.create_window(500, 50, window=label6.var)
					traccia_riga()
					# ~ vinci.var="b"
					# ~ vinci2.var="b"							
					
				elif conta.var>=9 and vinci.var=="b" and vinci2.var=="b": 
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

				# ~ label_res.var.destroy()
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
	label6.var = tk.Label(root, text="")
	label6.var.config(font=('helvetica', 14))
	canvas1.var.create_window(500, 50, window=label6.var)
	label6.var.destroy()	

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

