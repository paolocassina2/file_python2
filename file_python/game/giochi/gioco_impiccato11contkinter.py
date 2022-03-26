#SISTEMARE TENTATIVI-->si devono ridurre solo se lettera inserita non è giusta
def x1():
		x1.var=""
x1()


def canvas():
		canvas.var=""
canvas()
# ~ if vero!=33 
def indovinalettera():
	indovinalettera.var=""
	
indovinalettera()

def label1():
	label1.var=""
label1()

def label2():
	label2.var=""
label2()
def label3():
	label3.var=""
label3()

def abcdefg():
	abcdefg.var=0
abcdefg()
def contadisegno1():
		
		contadisegno1.var=0
contadisegno1()
def canvas1():
	canvas1.var=""
	
canvas1()

def listastringa1():
	listastringa1.var=""
listastringa1()
# ~ giocoimp_()
def disegna_disegno():
	if contadisegno1.var<=11:	
		if contadisegno1.var==1:
			canvas1.var.create_line(200, 400, 400,400)
			# ~ time.sleep(1000)
			# ~ time.sleep(100)
		elif contadisegno1.var==2:
			canvas1.var.create_line(300, 400, 300, 200)
		# ~ time.sleep(1000)
		# ~ time.sleep(100)
		elif contadisegno1.var==3:
			canvas1.var.create_line(300, 200, 400, 200)
		# ~ time.sleep(100)
		elif contadisegno1.var==4:
			canvas1.var.create_line(400, 200, 400, 250)		
		elif contadisegno1.var==5:
			canvas1.var.create_oval(380, 250, 430,280, width=2)
		elif contadisegno1.var==6:
			canvas1.var.create_oval(390, 270, 410,280, width=2)
		elif contadisegno1.var==7:
			canvas1.var.create_line(400, 280, 400, 310,width=2)
		elif contadisegno1.var==8:
			canvas1.var.create_line(400, 290, 410, 300,width=2)
		elif contadisegno1.var==9:
			canvas1.var.create_line(400, 290, 390, 300,width=2)
		elif contadisegno1.var==10:
			canvas1.var.create_line(400, 310, 410, 320,width=2)
		elif contadisegno1.var==11:
			canvas1.var.create_line(400, 310, 390, 320,width=2)
			abcdefg.var=1
			print("hai perso")
		# ~ canvas1.var.create_text(80, 70, text ="" , font = ('Helvetica', 20, 'bold'), justify = 'center', fill='blue')
		# ~ canvas1.var.destroy()
		# ~ canvas1.var.create_text(80, 70, text =str(stringa3.var) , font = ('Helvetica', 20, 'bold'), justify = 'center', fill='blue')
		# ~ print("stringa3.var",stringa3.var)
		
		# ~ label1.var = tk.Label(root, text="")
		# ~ label1.var.config(font=('helvetica', 14))
		# ~ canvas1.var.create_window(400, 70, window=label1.var
		
def a():
	a.var=""
a()
def parola_random():
	parola_random.var=""
parola_random()		
from random_word import RandomWords		# ~ elif contadisegno1.var==12:
parola_random.var=RandomWords()
# ~ def aa():
	# ~ aa.var=""
# ~ aa()
aa=parola_random.var.get_random_word()
a.var=aa.lower()
print(a.var)
# ~ print(stringa3.var)	
	
lista_di_a=list(a.var)
def stringa3():
	stringa3.var=""
stringa3()

def stringa():
	stringa.var=""
stringa()
indice=-1




indice1=-1	
	##parte per indovinare parola	

		
# ~ print(stringa)		
indice2=-1	

# ~ stringa=a.replace("*","d")	



	
while indice1<(len(a.var)-1):
	indice1=indice1+1
	# ~ print(a[indice1])
	# ~ print(a)
	# ~ if a[indice1]==indovinalettera:
	if indice1!=0 and indice1!=len(a.var)-1:
		stringa.var=stringa.var+str("*")
	
	
	
	else:
		stringa.var=stringa.var+str(a.var[indice1])


listastringa1.var=list(stringa.var)






		# ~ canvas1.var.create_line(400, 310, 390, 320,width=2)
def giocoimp_():
	

	punteggio=0
	conta=0
	# ~ abcdefg.var=25

	indovinalettera.var=x1.var	#uguale ad input
	if indovinalettera.var==a.var:
			print("tentativo inserimento parola")
			print("la parola ",a.var," e corretta")

			abcdefg.var=2
			
	contavolte=0	
		
	flag=0
	if abcdefg.var!=2:
		for x in lista_di_a:
				# ~ continue
				
			
				if str(x)==str(indovinalettera.var):
					# ~ punteggio=punteggio+1
					# ~ print("ciao")
					# ~ while str(x)==str(indovinalettera):
					lista_indici=[index for index, value in enumerate(lista_di_a) if value == indovinalettera.var]	#RESTITUISCE TUTTI INDICI
					# ~ listadiindici.append(indici)
					for i in lista_indici:
						listastringa1.var[i]=indovinalettera.var
					
						
					contavolte=contavolte+1
					# ~ if contavolte>=1:
				
						# ~ print("numero tentativi: ",tentativirimasti)	
					
			
					stringa3.var="".join(listastringa1.var)
					flag=1
					print()
		# ~ if str(x)==str(indovinalettera.var):	
		if flag==1:			
			print("hai indovinato",contavolte, " lettera/e","      ",indovinalettera.var)	
			print()
		if flag==0:
			contadisegno1.var=contadisegno1.var+1
			print("non hai indovinato")
			disegna_disegno()
			print()
			
		
		print("contadisegno1.var ",contadisegno1.var)
		

			
	

	

	# ~ print(stringa3.var)
	print(a.var)
	if stringa3.var==a.var:
		abcdefg.var=3
		print("hai vinto!")
		# ~ abcdefg.var=3
		print("la parola era ",a.var)
		# ~ canvas1.create_text(120, 70, text = 'hai vinto!', font = ('Helvetica', 20, 'bold'), justify = 'center', fill='blue'
	
	# ~ print("stringa3.var ",stringa3.var)

		# ~ abcdef=88
		# ~ break

		# ~ canvas1.var.create_text(100, 70, text = 'Welcome', font = ('Helvetica', 40, 'bold'), justify = 'center', fill='blue')
def entrybox():
	

	import tkinter as tk




#################################################
	root= tk.Tk()
	
	canvas1.var = tk.Canvas(root, width = 1500, height =800,  relief = 'raised')
	canvas1.var.pack()
	# ~ x2= entry2.get()
	
	# ~ canvas1.create_text(600, 155, text = 'Welcome', font = ('Helvetica', 72, 'bold'), justify = 'center', fill='blue')


	
			#posizione entrybox(input)

	# ~ def getSquareRoot ():			#creo qr, cerco file +recente in quella cartlla, e prendoproprio quello
	
				# ~ label6.pack()
	
	entry1 = tk.Entry (root) 								#SPAZIOinput
	canvas1.var.create_window(370, 100, window=entry1)	
	# ~ a=str(stringa3.var)

		
	# ~ label1.var = tk.Label(root, text="aa")
	# ~ label1.var.config(font=('helvetica', 14))
	# ~ canvas1.var.create_window(400, 70, window=label1.var)
	
	# ~ label1.var = tk.Label(root, text=stringa3.var)
	# ~ label1.var.config(font=('helvetica', 14))
	# ~ canvas1.var.create_window(400, 70, window=label1.var)
		
	# ~ indovinalettera.var= entry1.get()
	
	# ~ scrivi = entry1.get()
	
	# ~ label1.var = tk.Label(root, text="")
	# ~ label1.var.config(font=('helvetica', 14))
	# ~ canvas1.var.create_window(80, 70, window=label1.var)
	# ~ label2.var = tk.Label(root, text="")
	# ~ label2.var.config(font=('helvetica', 14))
	# ~ canvas1.var.create_window(80, 70, window=label2.var)
	
	label1.var = tk.Label(root, text="")
	label1.var.config(font=('helvetica', 14))
	canvas1.var.create_window(150, 70, window=label1.var)
	
	label3.var = tk.Label(root, text="")
	label3.var.config(font=('helvetica', 14))
	canvas1.var.create_window(150, 70, window=label3.var)
	
	def scrivi_parola():
		
		scrivi_parola.var=stringa3.var
	scrivi_parola()
	# ~ print("scrivi_parola.var ",scrivi_parola.var)
	# ~ print("stringa3.var ",stringa3.var)
	# ~ if indovinalettera.var==a.var:
	def contapulsante():
		contapulsante.var=0
	contapulsante()
	if contapulsante.var<1:
		label3.var = tk.Label(root, text=stringa.var)
		label3.var.config(font=('helvetica', 14))
		canvas1.var.create_window(150, 70, window=label3.var)
	
	# ~ else:
		# ~ label3.destroy()
	def scrivilabel():
		if contadisegno1.var<11 and abcdefg.var!=2 and abcdefg.var!=3:	#IL PULSANTE FUNZIONA SOLO SE NON HAI PERSO O SE NON HAI ANCORA VINTO
			contapulsante.var=contapulsante.var+1
			x1.var = entry1.get()			#VARIABILE CHE RICEVE INPUT
			giocoimp_()
			if contapulsante.var==1:
				label3.var.destroy()
			
			label1.var.destroy()
			label1.var = tk.Label(root, text=x1.var)
			label1.var.config(font=('helvetica', 14))
			canvas1.var.create_window(80, 80, window=label1.var)
		
		# ~ label2.var.destroy()
			label2.var = tk.Label(root, text=stringa3.var)
			label2.var.config(font=('helvetica', 14))
			canvas1.var.create_window(80, 110, window=label2.var)
			if contadisegno1.var==11:
		# ~ canvas1.var.create_text(0, 0, text = 'hai perso!', font = ('Helvetica', 20, 'bold'), justify = 'center', fill='blue')
				label3.var = tk.Label(root, text="hai perso")
				label3.var.config(font=('helvetica', 14))
				canvas1.var.create_window(150, 70, window=label3.var)
			if indovinalettera.var==a.var:
				label3.var = tk.Label(root, text="hai vinto")
				label3.var.config(font=('helvetica', 14))
				canvas1.var.create_window(150, 70, window=label3.var)
			if abcdefg.var==3:
				label3.var = tk.Label(root, text="hai vinto")
				label3.var.config(font=('helvetica', 14))
				canvas1.var.create_window(150, 70, window=label3.var)
	
	button1 = tk.Button(text='scegli_lettera', command=scrivilabel, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
	canvas1.var.create_window(50,50, window=button1)	
	
	
		
		

	
	
	root.mainloop()
# clear the canvas 
entrybox()
# ~ giocoimp_()
	
# ~ time.sleep(1000)    
# ~ canvas1.create_line(200, 100, 300, 100)
# ~ time.sleep(1000)       
# ~ canvas1.create_line(300, 100, 300, 150)
# ~ canvas1.create_oval(280, 150, 330,180, width=2)
# ~ canvas1.create_oval(290, 170, 310,180, width=2)
# ~ canvas1.create_line(300, 180, 300, 210,width=2)
# ~ canvas1.create_line(300, 190, 310, 200,width=2)
# ~ canvas1.create_line(300, 190, 290, 200,width=2)
# ~ canvas1.create_line(300, 210, 310, 220,width=2)
# ~ canvas1.create_line(300, 210, 290, 220,width=2)




# ~ root.mainloop()




# ~ uno()
# ~ time.sleep(2)
# ~ due()
# ~ time.sleep(2)
# ~ tre()
# ~ time.sleep(2)



			
		
		# ~ break
			
	# ~ if contadisegno1.var==11:
		
	# ~ conta=9
# ~ l=[1,4,5,1,1,3,88,5]		
# ~ print("restituiscituttiindici",[index for index, value in enumerate(l) if value == 5])
# ~ print(listadiindici)
# ~ print(stringa)
# ~ print(stringa)		
	# ~ print(listadiindici)
		# ~ stringa.replace("a",indovinalettera)	
		# ~ rivelaparola=str(a[0])+str(a[a.index(i)])+str(a[len(a)-1])
# ~ rivelaparola
		# ~ print(rivelaparola)

