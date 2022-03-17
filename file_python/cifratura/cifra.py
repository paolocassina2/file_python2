import string
#stampa tutti i itipi di cifratura
lettere=string.ascii_lowercase
def diz_codifica():
		diz_codifica.var={}
diz_codifica()
n=0
cifratura1=-1
for j in range(25):
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
	print(diz_codifica.var)
	# ~ print()
	diz_codifica.var={}
	# ~ print(diz_codifica.var)
print(codifica.var)
