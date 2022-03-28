###CARTELLA==game




#8 casi di tracciamento linee che indicano la vittoria. sono gli stessi sia che vinca il pc che vinca il computer













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

def caso():
	caso.var=8
caso()

def condizioni_vittoria():
				#8 casi di vittoria e tracciamento righe indipendentemente che vinca il pc o il giocatore(3 linee orizziontali, 3 verticali e 2 diagonali)
				if caso.var==1:# ~ if res.var[0]=="*" and res.var[1]=="*"  and res.var[2]=="*" :				#casi orizzontali
							# ~ print("tris")
							# ~ vinci.var="a"
							# ~ canvas.create_line(15, 25, 200, 25)
					canvas1.var.create_line(250, 150, 800, 150,width=2,fill="red")
							# ~ if c=33
							# ~ vinci2.var="b"
							# ~ break
				elif caso.var==2:

				# ~ elif res.var[3]=="*" and res.var[4]=="*"  and res.var[5]=="*" :
					# ~ print("tris")
					# ~ vinci.var="a"
					canvas1.var.create_line(250, 300, 800, 300,width=2,fill="red")
					# ~ vinci2.var="b"
					#	break
					# ~ break
				# ~ elif res.var[6]=="*" and res.var[7]=="*"  and res.var[8]=="*" :
				elif caso.var==3:
					# ~ print("tris")
					# ~ vinci.var="a"
					canvas1.var.create_line(250, 500, 800, 500,width=2,fill="red")
				# ~ vinci2.var="b"
					# ~ break
			# ~ ######################################
# ~ def ciao():	
				elif caso.var==4:
				# ~ elif res.var[0]=="*" and res.var[3]=="*"  and res.var[6]=="*" :		#casi verticali
					canvas1.var.create_line(300, 100, 300, 700,width=2,fill="red")
						# ~ print("tris")
						# ~ vinci.var="a"
						# ~ vinci2.var="b"
						# ~ break
				elif caso.var==5:
				# ~ elif res.var[1]=="*" and res.var[4]=="*"  and res.var[7]=="*" :
						# ~ print("tris")
						# ~ vinci.var="a"
						# ~ vinci2.var="b"
						canvas1.var.create_line(500, 100, 500, 700,width=2,fill="red")
						# ~ break
				elif caso.var==6:
				# ~ elif res.var[2]=="*" and res.var[5]=="*"  and res.var[8]=="*" :
					
						print("tris")
						vinci.var="a"
						canvas1.var.create_line(700, 100, 700, 700,width=2,fill="red")
						# ~ break
						# ~ break
						vinci2.var="b"
				# ~ #####vinci2.var="b"#########################################
				elif caso.var==7:
				# ~ elif res.var[0]=="*" and res.var[4]=="*"  and res.var[8]=="*" :		#casi diagonali
						print("tris")
						vinci.var="a"
						canvas1.var.create_line(200, 600, 650,150,width=2,fill="red")
						vinci2.var="b"
						# ~ break
				elif caso.var==8:
				# ~ elif res.var[2]=="*" and res.var[4]=="*"  and res.var[6]=="*" :
						print("tris")
						vinci.var="a"
						canvas1.var.create_line(240, 50, 800,590,width=2,fill="red")
						vinci2.var="b"
						# ~ break
				######################################
				elif caso.var==833:
				# ~ if res.var[0]=="#" and res.var[1]=="#"  and res.var[2]=="#" :				#computer
					print("tris")
					vinci2.var="a"
					vinci.var="b"
					# ~ canvas1.var.create_line(200, 100, 800, 100,width=2,fill="red")
					# ~ break
				elif caso.var==9:
				# ~ elif res.var[3]=="#" and res.var[4]=="#"  and res.var[5]=="#" :
						print("tris")
						vinci2.var="a"
						vinci.var="b"
						# ~ canvas1.var.create_line(200, 200, 800,200,width=2,fill="red")
						# ~ break
				# ~ elif res.var[6]=="#" and res.var[7]=="#"  and res.var[8]=="#" :
						print("tris")
					
						# ~ canvas1.var.create_line(200, 500, 800,500,width=2,fill="red")
						vinci2.var="a"
						vinci.var="b"
						# ~ break
				# ~ ######################################
				# ~ elif res.var[0]=="#" and res.var[3]=="#"  and res.var[6]=="#" :		#casi verticali
						print("tris")
						vinci2.var="a"
						vinci.var="b"
						# ~ canvas1.var.create_line(300, 50, 300, 600,width=2,fill="red")
						# ~ break
				# ~ elif res.var[1]=="#" and res.var[4]=="#"  and res.var[7]=="#" :
						vinci2.var="a"
						

						vinci.var="b"
						print("tris")

						# ~ break
						# ~ break
				# ~ elif res.var[2]=="#" and res.var[5]=="#"  and res.var[8]=="#" :
						vinci2.var="a"
						# ~ canvas1.var.create_line(700, 50, 700, 700,width=2,fill="red")
						vinci.var="b"
						print("tris")
						# ~ break
						# ~ break
				# ~ ##############################################
				elif res.var[0]=="#" and res.var[4]=="#"  and res.var[8]=="#" :		#casi diagonali
						vinci2.var="a"
						# ~ canvas1.var.create_line(50, 50, 800,800,width=2,fill="red")
						vinci.var="b"
						print("tris")
						# ~ break
				# ~ elif res.var[2]=="#" and res.var[4]=="#"  and res.var[6]=="#" :
						vinci2.var="a"
						# ~ canvas1.var.create_line(50, 800, 800,50,width=2,fill="red")
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
						

from tkinter import *
def entrybox():
	# ~ def entry1():
		# ~ entry1.var=""

	

	

	import tkinter as tk
	root = Tk()
	canvas1.var = tk.Canvas(root, width = 1500, height =800,  relief = 'raised')


	# ~ canvas1.var.bind("<Key>", key)
	# ~ canvas1.var.bind("<Button-1>", callback)
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
	# ~ while True:
	
		# ~ caso.var=input("inp")
	# ~ ìcondizioni_vittoria()
	condizioni_vittoria()
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
entrybox()					

