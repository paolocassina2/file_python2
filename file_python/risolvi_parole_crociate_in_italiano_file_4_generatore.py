
def ciao():
	
	while True:
	
		file1="C:\\Users\\Attilio\\Desktop\\60000_parole_italiane.txt"
		file2="C:\\Users\\Attilio\\Desktop\\660000_parole_italiane.txt"
		with open(file1) as f:
			contents = f.readlines()
		with open(file2) as f:
			contents2 = f.readlines()
		# ~ c1=0
		# ~ for x in contents2:
			# ~ c1=c1+1
		
		l1=contents+contents2	#unisco le parole di due file diversi creando un elenco di parole senza duplicati
		set_l1=set(l1)
		lista_l1=list(set_l1)
		
		print("len",len(set_l1))
		# ~ for x in range(10):
			# ~ print(list(set_l1)[x])
		# ~ print(set_l1)
		# ~ print(type(contents))	
		# ~ print(c1,"c1")
		print("risolutore di parole crociate")
		p=input("scrivi lettera nota altrimenti *				")
		print()
		# ~ p="***l******"
		lista=[]
		indice=[]
		contatore=-1
		for xz in p:
			contatore+=1
			if xz!="*":
				
				lista.append(xz)   
				indice.append(contatore)
		print(lista)
		print(indice)



		# ~ def af():
		lista_soluzioni=[]
		for x in lista_l1:
			
				c=0
				parola=x.strip()
				if len(parola)==len(p):
				# ~ for zz in parola:
					for zz,jj in zip(indice,lista):
						if parola[zz]==jj:
							c=c+1
					if c==len(lista):
						lista_soluzioni.append(parola)
		lista_soluzioni.sort()
		print("n.soluzioni trovate ", len(lista_soluzioni))
		# ~ print(lista_soluzioni)
		for x in lista_soluzioni:
			print(x)
						# ~ print(parola)
						
import random
	# ~ while True:
	
file1="C:\\Users\\Attilio\\Desktop\\60000_parole_italiane.txt"
file2="C:\\Users\\Attilio\\Desktop\\660000_parole_italiane.txt"
with open(file1) as f:
	contents = f.readlines()
	
parola_prima=random.choice(contents)


# ~ posizione_lettera_in_comune=random.randint(0,len(parola_prima)-1)
# ~ parola_prima[posizione_lettera_in_comune]
# ~ print("cc",posizione_lettera_in_comune)

lettera_in_comune=random.choice(parola_prima)
print(lettera_in_comune)

posizione_lettera_in_comune=random.randint(3,8)
lista_parola=[]
for x in contents:
		if posizione_lettera_in_comune<len(x):
			if x[posizione_lettera_in_comune]==lettera_in_comune:
				print(x)
				lista_parola.append(x)
				break
				
for x in range(5):
	lettera_in_comune=random.choice(parola_prima)
	print(lettera_in_comune)

	posizione_lettera_in_comune=random.randint(3,8)
	lista_parola=[]
	for x in contents:
			if posizione_lettera_in_comune<len(x):
				if x[posizione_lettera_in_comune]==lettera_in_comune:
					print(x)
				lista_parola.append(x)
				break

# ~ print(lettera_in
# ~ posizione_lettera_in_comune(
# ~ posizion_incastro=random.randint(
print(parola_prima)
def trova_parola_incastro():
	# ~ parola1=input("parola")
	import random
	
	len_parola2=random.randint(1,10)
	# ~ lettere="abcdefghijklmnopqrstuvwxyz"
	# ~ lista_lett=list(lettere)
	# ~ print(lista_lett)

# ~ def ciao():
	# ~ lettera_in_comune=random.choice(lista_let)
	print("contare da 0")
	# ~ posizione_lettera_in_comune=random.randint(1,len(parola2))
	
def ciao():
	p=""
	for x in range(len_parola2):
		if x==posizione_lettera_in_comune:
			p=p+lettera_in_comune
			
		else:
			p=p+"*"	 
		
	print(p)
	
	# ~ for x in range(len_parola2):
		# ~ if x==posizione_lettera_in_comune:
			# ~ p+=parola1[x]
		# ~ else:
			# ~ p+="*"
	# ~ print(p)
# ~ trova_parola_incastro()
# ~ def ciao():	
	file1="C:\\Users\\Attilio\\Desktop\\60000_parole_italiane.txt"
	file2="C:\\Users\\Attilio\\Desktop\\660000_parole_italiane.txt"
	with open(file1) as f:
		contents = f.readlines()
	with open(file2) as f:
		contents2 = f.readlines()
	# ~ c1=0
	# ~ for x in contents2:
		# ~ c1=c1+1
	
	l1=contents+contents2	#unisco le parole di due file diversi creando un elenco di parole senza duplicati
	set_l1=set(l1)
	lista_l1=list(set_l1)
	
	print("len",len(set_l1))
	# ~ for x in range(10):
		# ~ print(list(set_l1)[x])
	# ~ print(set_l1)
	# ~ print(type(contents))	
	# ~ print(c1,"c1")
	# ~ print("risolutore di parole crociate")
	# ~ p=input("scrivi lettera nota altrimenti *				")
	# ~ print()
	# ~ p="***l******"
	lista=[]
	indice=[]
	contatore=-1
	for xz in p:
		contatore+=1
		if xz!="*":
			
			lista.append(xz)   
			indice.append(contatore)
	print(lista)
	print(indice)



	# ~ def af():
	lista_soluzioni=[]
	for x in lista_l1:
		
			c=0
			parola=x.strip()
			if len(parola)==len(p):
			# ~ for zz in parola:
				for zz,jj in zip(indice,lista):
					if parola[zz]==jj:
						c=c+1
				if c==len(lista):
					lista_soluzioni.append(parola)
	lista_soluzioni.sort()
	print("n.soluzioni trovate ", len(lista_soluzioni))
	# ~ print(lista_soluzioni)
	for x in lista_soluzioni:
		print(x)
trova_parola_incastro()
				# ~ for jj in zz:
				# ~ if jj
		# ~ print(parola)
		# ~ print(len(parola))
		# ~ if len(parola)==5 and  parola[len(parola)-1]=="a" and parola[0]=="c":
			# ~ print(parola)
		# ~ if len(parola)==5 and  parola[0]=="v" and parola[len(parola)-1]=="a":
		# ~ print(parola)

	
# ~ ciao()
