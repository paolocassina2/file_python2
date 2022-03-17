import string
#stampa tutti i itipi di cifraturaù
#modifica cifratura ogni 5 caratteri
lettere=string.ascii_lowercase
def diz_codifica():
		diz_codifica.var={}
diz_codifica()
def codifica1():
	codifica1.var=""
codifica1()
n=0
n1=0
cifratura1=0
n2=5
print(lettere)
testo="ciaociaociaociaociaociaociaociaociao"
stringa=""
# ~ print(testo[0:4])
# ~ print(testo[4:8])
lista=[]
for j in range(9):
		codifica1.var=""
		n=n+1
		print("numero",n)
		
		print()

		conto_rovescia=-1
		lista_spazi=[]
		diz_codifica.var={}
		conta1=-1
		conta=0
		cifratura1=cifratura1+1			
		for x in lettere:
					# ~ conta=conta+1
					# ~ if conta%5==0:
						# ~ cifratura1=cifratura1+1
					
					
					# ~ CountryCodeDict["Spain"]= 34
					# ~ print(lettere)
					# ~ codifica=""
					# ~ print(lettere.index("g"))
							# ~ print(conta1)
						# ~ lista_spazi=[]
						# ~ diz_codifica.var={}
					# ~ print(x)
					if lettere.index(x)+cifratura1<len(lettere):
						diz_codifica.var[x]=lettere[lettere.index(x)+cifratura1]
					else:
						conto_rovescia=conto_rovescia+1
						diz_codifica.var[x]=lettere[conto_rovescia]
		
		lista.append(diz_codifica.var)
		def ciao():
			n1=n1+4
			n2=n2+4
			print("n1","n2",n1,n2)
			print(testo[n1:n2])
			for j in testo[n:n2]:
					# ~ for y in diz_codifica.var
						if j!=" ":
							codifica1.var=codifica1.var+diz_codifica.var[j]
						else:
							codifica1.var=codifica1.var+" "
			stringa=stringa+codifica1.var
			codifica1.var=""
					# ~ print(codifica1.var)			
		# ~ stringa=stringa+codifica1.var
		
		# ~ print(n1)
		# ~ print(n2)
			# ~ return codifica1.var
		print(diz_codifica.var)
		
		# ~ conto_rovescia=conto_rovescia+1
		# ~ print()
		diz_codifica.var={}
# ~ print(stringa)
# ~ print(len(codifica1.var))

# ~ print(lista)
# ~ codifi

conta=-1
	
	# ~ print(n1,n2)
	# ~ cifratura1=cifratura1+1
	
for x in lista:
	n1=n1+4
	n2=n2+4
	for j in testo[n1:n2]:
			print(testo[n1:n2])
			# ~ a=lista[conta]
			# ~ conta=conta+1
			# ~ if conta%5==0:
				
			# ~ print(j)
			# ~ print(j)
			if j!=" ":
				codifica1.var=codifica1.var+str(x[j])
				# ~ print(x[j])
			else:
				codifica1.var=codifica1.var+" "		
				
print(codifica1.var)	# ~ for y in diz_codifica.var
print(len(codifica1.var))		# ~ if j!=
			# ~ codifica1.var=codifica1.var+x[j]
		# ~ else:
			# ~ codifica1.var=codifica1.var+" "
		# ~ print(diz_codifica.var)
	# ~ print(stringa)
	# ~ print(len(stringa))
# ~ print(stringa)
# ~ print(codifica1.var)
# ~ print(len(codifica1.var))
