from random_word import RandomWords
r = RandomWords()
def x1():
	x1.var="steam"
x1()

#cosi stampa le parole cercate che hanno generato anagrammi
#METTE IN UN DIZIONARIO LE PAROLE CHE GENERANO ANAGRAMMI ASSOCIATE AGLI ANAGRAMMI CHE HANNO GENERATO(sembra che il dizioanrio giä per definiziione rimuova i duplicati)
listaparole=[]
a=0
# ~ print("dimmi una parola inglese e io ti dirò quali sono gli anagrammi possibili  ")
import enchant
my_dict = enchant.Dict("en_US")	
from tkinter import *
from tkinter import *

# ~ enchant.print()
# ~ print(my_dict[)
	
lista=["2","aaaa"]
def CONTROLLAPAROLA():
	CONTROLLAPAROLA.var=""
CONTROLLAPAROLA()
def INPUT():
	INPUT.var=""
INPUT()


def lista_anagrammi_rivista1():
	lista_anagrammi_rivista1.var=[] 
lista_anagrammi_rivista1()
def funzione_anagramma():
		a=x1.var
		print("parola ", a)
		ab=list(a)
		#
		values=[]

		import itertools

		for s in a:
			values.append(s)

		per = itertools.permutations(values)
		
		listaconfronto=[]
	
		nuovalista=[]
		for val in per:
		
			comb=list(val)
			parola1 = ''.join(map(str, comb)) 
			
			nuovalista.append(parola1)#
	

		import enchant
		my_dict = enchant.Dict("en_US")				#CONTROLLO CHE PAROLA SITROVI NEL DIZIONARIO

		
		listaparolepossibilianagrammi=[]
		listacomb_nnaccettabili=[]
	
		for abcdef in nuovalista:
			jj=my_dict.check(abcdef)
		
			if (jj==True):
				if abcdef!=INPUT.var:	
			
					print(abcdef)
					listaparolepossibilianagrammi.append(abcdef)
			else:
				listacomb_nnaccettabili.append(abcdef)
		lista_anagrammi_rivista1.var=[] 
	
			

		for i in listaparolepossibilianagrammi: 
			if i not in lista_anagrammi_rivista1.var: 
			   lista_anagrammi_rivista1.var.append(i) 
		lista_anagrammi_rivista1.var.remove(x1.var)				#LA PAROLA DELL'INPUT NON DEVE FAR PARTE DELLA LISTA DEGLI ANAGRAMMI-->QUINDI LA RIMUOVO
		print("anagrammi_possibili ", listaparolepossibilianagrammi)
		print ("lista_combinazioni_accettabili_senza_duplicati: " + str(lista_anagrammi_rivista1.var)) 
		print("anagrammi_non_accettabili(devono esseere parole inglesi e presenti nel dizionario ", listacomb_nnaccettabili)
	
def conta():
	conta.var=0
conta() 
def entrybox1():
	
	
	
	def entrybox():
		def listaparolecercate():
			listaparolecercate.var=[]
		listaparolecercate()	
			
		def label10():
			label10.var=""
		label10()		
		
		# ~ def
		import tkinter as tk

		root= tk.Tk()
		# ~ aliditalia

		canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
		canvas1.pack()

		label1 = tk.Label(root, text='GENERATORE DI ANAGRAMMI\nENTRY BOX')
		label1.config(font=('helvetica', 14))
		canvas1.create_window(200, 25, window=label1)

		label2 = tk.Label(root, text='inserisci una parola:')
		label2.config(font=('helvetica', 10))
		canvas1.create_window(200, 80, window=label2)
		def label4():
			label4.var=""
		label4()
			
				
				# ~ canvas1.create_window(200, 270, window=label9.var)
		# ~ canvas1.create_window(200, 180, window=label9.var)
		entry1 = tk.Entry (root) 
		canvas1.create_window(200, 100, window=entry1)				#posizione entrybox(input)-->INPUT PAROLA
		anagrammipossibili=""
		for z in lista_anagrammi_rivista1.var:
			anagrammipossibili=anagrammipossibili+z
		print("anagrammipossibili ",anagrammipossibili)
		label4.var = tk.Label(root, text= "",font=('helvetica', 10, 'bold'))
		def label11():
			label11.var=""
		label11()
		
		
		def CLEAR4():
			label4.var.destroy()
		def label9():
				label9.var=""
		label9()
		
				
		label9.var = tk.Label(root, text="",font=('verdana', 10, 'bold'))	
		
		
		label11.var = tk.Label(root, text="",font=('verdana', 10, 'bold'),fg=('blue'))
		# ~ canvas1.create_window(200, 180, window=label11.var)	
							
		def listaparolechegeneranoanagrammi():
				listaparolechegeneranoanagrammi.var=[]	
		listaparolechegeneranoanagrammi()
		def dizionario_di_liste_anagrammi():
				dizionario_di_liste_anagrammi.var={}
		dizionario_di_liste_anagrammi()
	
		
		
		# ~ word_freq.update({'before': 23})			#come append ma a dizionario
			# ~ print(word_freq)
		# ~ listaparolecercate=[]		
		
		def calcolaanagramma():
			
			
			
			def CLEAR9():
				label9.var.destroy()
				
				
			def CLEAR11():
				label11.var.destroy()
				
			
	
			# ~ ciao="ciao"
			x1.var = entry1.get()
				
			CAPITAL_LETTER=""
			for i in x1.var:
				maiuscola=i.capitalize()
				CAPITAL_LETTER=CAPITAL_LETTER+maiuscola
			print("x1.var",x1.var)
			print("CAPITAL_LETTER",CAPITAL_LETTER)
			controlla_che_sia_parola_inglese=my_dict.check(x1.var)
			if controlla_che_sia_parola_inglese==True:	
				
				funzione_anagramma()
					
					
			print("parolecercate: ",listaparolecercate.var)
			# ~ funzione_anagramma()
			anagrammipossibili=""
			for z in lista_anagrammi_rivista1.var:
				
				anagrammipossibili=anagrammipossibili+z+"\n"
					
			print("anagrammipossibili",anagrammipossibili)
			label3 = tk.Label(root, text= 'gli anagrammi possibili sono:',font=('helvetica', 10))
			canvas1.create_window(200, 200, window=label3)
			# ~ label4 = tk.Label(root, text= "",font=('helvetica', 10, 'bold'))	
			
			# ~ CLEAR4()	#PRIMA DI RISCRIVERE QUALCOSA CANCELLO LABEL4(per evitare che si sovrapponga)
			# ~ CLEAR9()
		
			if controlla_che_sia_parola_inglese==True:	
					# ~ listaparolechegeneranoanagrammi=[]	
					
					if (len(lista_anagrammi_rivista1.var)>0):	#se genera anagrammi la lista é lunga almeno 1
						# ~ label11.var = tk.Label(root, text="",font=('verdana', 10, 'bold'),fg=('blue'))
						# ~ canvas1.create_window(200, 180, window=label11.var)	
						
						listaparolechegeneranoanagrammi.var.append(x1.var)			
						
						(dizionario_di_liste_anagrammi.var).update({str(x1.var):lista_anagrammi_rivista1.var})
				# ~ dizionario_di_liste_anagrammi.update({str(x1.var):lista_anagrammi_rivista1.var})
						print("dizionario ",dizionario_di_liste_anagrammi.var)
								
						CLEAR4()	#PRIMA DI RISCRIVERE QUALCOSA CANCELLO LABEL4(per evitare che si sovrapponga)
						CLEAR9()
						CLEAR11()
						label4.var = tk.Label(root, text= anagrammipossibili,font=('helvetica', 10, 'bold'))
						canvas1.create_window(200, 270, window=label4.var)
						
						label9.var = tk.Label(root, text="la parola " +str(CAPITAL_LETTER)+ " genera " +str(len(lista_anagrammi_rivista1.var))+" anagramma/i",font=('verdana', 10, 'bold'),fg=('blue'))
						canvas1.create_window(200, 180, window=label9.var)		
						
						
						listaparolecercate.var.append(x1.var)
						label10.var = tk.Label(root, text="parolecercate "+str(listaparolecercate.var),font=('verdana', 10, 'bold'))	
				
						canvas1.create_window(200,60, window=label10.var)	
						
					
					
						print(listaparolechegeneranoanagrammi.var)
						
						
						# ~ for i in listaparolechegeneranoanagrammi.var: 
							# ~ if i not in listaparolechegeneranoanagrammi.var: 		#tolgo i dublicati
							  # ~ listaparolechegeneranoanagrammi.var.append(i) 
						# ~ listaparolechegeneranoanagrammi.var.remove(x1.var)
						label11.var = tk.Label(root, text=str(listaparolechegeneranoanagrammi.var),font=('verdana', 10, 'bold'))	
						canvas1.create_window(400,300, window=label11.var)
				
		
					
					
					else:
						
						# ~ label11.var = tk.Label(root, text="",font=('verdana', 10, 'bold'),fg=('blue'))
						# ~ canvas1.create_window(200, 180, window=label11.var)	
							
						CLEAR4()
						CLEAR9()
						CLEAR11()
						
						label9.var = tk.Label(root, text="la parola " +str(CAPITAL_LETTER)+ " genera " +str(len(lista_anagrammi_rivista1.var))+" anagramma/i",font=('verdana', 10, 'bold'),fg=('blue'))	
						canvas1.create_window(200, 180, window=label9.var)		
					
						label4.var = tk.Label(root, text= "questa parola non genera anagrammi",font=('helvetica', 10, 'bold'))
						canvas1.create_window(200, 270, window=label4.var)
						
						
						listaparolecercate.var.append(x1.var)
						label10.var = tk.Label(root, text="parolecercate "+str(listaparolecercate.var),font=('verdana', 10, 'bold'))	
						canvas1.create_window(200,60, window=label10.var)
			
			
						# ~ for x in listaparolechegeneranoanagrammi.var:
							# ~ label11.var = tk.Label(root, text=str(x),font=('verdana', 10, 'bold'))	
							# ~ canvas1.create_window(400,300, window=label11.var)
					
				
		
			else:
				# ~ label11.var = tk.Label(root, text="",font=('verdana', 10, 'bold'),fg=('blue'))
				# ~ canvas1.create_window(200, 180, window=label11.var)	
							
				CLEAR4()
				CLEAR9()
				CLEAR11()
				label9.var = tk.Label(root, text="la parola " +str(CAPITAL_LETTER),font=('helvetica', 10, 'bold')	)
				canvas1.create_window(200, 180, window=label9.var)	
				print("non è una parola inlgese")
				label4.var = tk.Label(root, text= "non è una parola inglese",font=('helvetica', 10, 'bold'))
				canvas1.create_window(200, 270, window=label4.var)
				
				listaparolecercate.var.append(x1.var)
				label10.var = tk.Label(root, text="parolecercate "+str(listaparolecercate.var),font=('verdana', 10, 'bold'))	
				canvas1.create_window(200,60, window=label10.var)
				
				
				# ~ for x in listaparolechegeneranoanagrammi.var:
							# ~ label11.var = tk.Label(root, text=str(x),font=('verdana', 10, 'bold'))	
							# ~ canvas1.create_window(400,300, window=label11.var)
		
		
	
		
			
				# ~ lista_anagrammi_rivista1.var=[]
					
		button1 = tk.Button(text='genera gli anagrammi possibili', command=calcolaanagramma, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
		canvas1.create_window(200, 130, window=button1)
		
		root.mainloop()
	
	
		# ~ label4.destroy()
	
	entrybox()

	# ~ entrybox()
# clear the canvas 


entrybox1()
# ~ canvas1.delete()
# ~ funzione_anagramma()







# ~ controlla_che_sia_parola_inglese=my_dict.check(x1)

# ~ parolaacaso="mage"
# ~ textwidget_abc()
# ~ widget2()


# ~ while CONTROLLAPAROLA==False:
	# ~ if CONTROLLAPAROLA==False:
		# ~ parolaacaso=input("dimmi un'altra parola ")


# ~ x=r.get_random_words()
# ~ y=r.get_random_words()
# ~ z=r.get_random_words()
# ~ h=r.get_random_words()
# ~ print(type(x))
# ~ print(x)
# ~ print(type(x))
 #on Windows System				#FUNZIONE CHE CANCELLA CMD

listaliste=[]

	

		# ~ parolaacaso=input("dimmi_una_parola_inglese e io ti dirò quali sono gli anagrammi possibili  ")
# ~ while CONTROLLAPAROLA.var==False:
	# ~ if CONTROLLAPAROLA==False:
		# ~ parolaacaso=input("dimmi_una_parola_inglese e io ti dirò quali sono gli anagrammi possibili  ")











		
		# ~ if CONTROLLAPAROLA==True:
			# ~ funzione_anagramma()
			
# ~ elif CONTROLLAPAROLA==False:
	# ~ while CONTROLLAPAROLA==False:
		# ~ if CONTROLLAPAROLA==False:
			# ~ parolaacaso=input("dimmi un'altra parola ")
		# ~ elif CONTROLLAPAROLA==True:
			# ~ funzione_anagramma()
	# ~ if jjjjjjjjj==0:
		# ~ print("nella lista non si trova l'anagramma di", parolaacaso)		
# ~ print("nuovalista",nuovalista)
# ~ nuovalista1=[]	
# ~ j=0
# ~ for xjx in nuovalista:
	# ~ print(xjx)
	
	# ~ z=(str(xjx))			
			# ~ print(parolaacaso," e un anagramma di ",uuu)
			# ~ print("ab",ab)
# ~ print(nuovalista1)
	
# ~ print(nuovalista)
	# ~ print(nuovalista)


# ~ for zzz in nuovalista:	
	# ~ for aaa in zzz:
		# ~ stringabc=str(aaa)
		# ~ nuovalista1.append(stringabc)
		# ~ print("nuovalista1",nuovalista1)	#faccio scorrere tutte le combinazioni di una parola random

	# ~ print(uuu)
		
	# ~ print(z)
		# ~ if zzz==uuu:#
			# ~ j=1
			# ~ print("ciao")
			
			# ~ print(parolaacaso," e un anagramma di ",uuu)
		# ~ print("ab",ab)

# ~ if j==0:
	# ~ print(parolaacaso," non e un anagramma di queste parola nella lista")
# ~ print(ab)
