
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
		for x in lista_l1:
			
				c=0
				parola=x.strip()
				if len(parola)==len(p):
				# ~ for zz in parola:
					for zz,jj in zip(indice,lista):
						if parola[zz]==jj:
							c=c+1
					if c==len(lista):
						print(parola)
					# ~ for jj in zz:
					# ~ if jj
			# ~ print(parola)
			# ~ print(len(parola))
			# ~ if len(parola)==5 and  parola[len(parola)-1]=="a" and parola[0]=="c":
				# ~ print(parola)
			# ~ if len(parola)==5 and  parola[0]=="v" and parola[len(parola)-1]=="a":
			# ~ print(parola)
	
		
ciao()
