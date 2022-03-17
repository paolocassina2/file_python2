import string
lettere=string.ascii_lowercase
# ~ print(len(lettere),"dfdf")
# ~ print(type(lettere))
# ~ print(lettere)
#ora passo tipo cifratura come variabile
cifratura=1#
def codifica1():
	codifica1.var=""
codifica1()
#in realtä invece di scorrere il testo ü meglio scorrere le lettere
testo="ci vediamo a scuola"

diz_decodifica={}
def diz_codifica():
	diz_codifica.var={}
diz_codifica()
def codifica(testo):
	# ~ testo1= testo.replace(" ", "")
	# ~ print(testo1)
	conta1=-1
	lista_spazi=[]
	diz_codifica.var={}
	# ~ CountryCodeDict["Spain"]= 34
	# ~ print(lettere)
	# ~ codifica=""
	# ~ print(lettere.index("g"))
			# ~ print(conta1)
	conto_rovescia=-1
	for x in lettere:
		# ~ print(x)
		if lettere.index(x)+cifratura<len(lettere):
			diz_codifica.var[x]=lettere[lettere.index(x)+cifratura]
		else:
			conto_rovescia=conto_rovescia+1
			diz_codifica.var[x]=lettere[conto_rovescia]
		
	for j in testo:
		if j!=" ":
			codifica1.var=codifica1.var+diz_codifica.var[j]
		else:
			codifica1.var=codifica1.var+" "
	return codifica1.var
	# ~ return(codifica)
	# ~ print(len(testo1))
	# ~ print(len(codifica))
	# ~ print("codifica		",codifica)
		# ~ for y in diz_codifica.keys():
		# ~ codifica=codifica+diz_codifica[y]
	# ~ print(codifica)
print(codifica(testo))
print("diz_codifica",diz_codifica.var)	
# ~ print(diz_codifica.var)

def funz_decodifica():
	# ~ def codifica(testo):
	testo1= testo.replace(" ", "")
	# ~ print(testo1)
	# ~ conta1=-1
	# ~ lista_spazi=[]
	diz_decodifica={}
	decodifica=""
	# ~ CountryCodeDict["Spain"]= 34
	# ~ print(lettere)
	# ~ codifica=""
	# ~ print(lettere.index("g"))
			# ~ print(conta1)
	# ~ conto_rovescia=len(lettere)
	for x in lettere:
		# ~ print(x)
		if lettere.index(x)>=0:
		
				diz_decodifica[x]=lettere[lettere.index(x)-cifratura]
	print("diz_deco	",diz_decodifica)	
		# ~ else:
			# ~ conto_rovescia=conto_rovescia+1
			# ~ diz_decodifica[x]=lettere[conto_rovescia]
	# ~ print(diz_decodifica)
	for jj in codifica1.var:	
		print(jj)	
		if jj!=" ":
		# ~ try:
			decodifica=decodifica+diz_decodifica[jj]
			# ~ print(decodifica)
		else:
			decodifica=decodifica+" "
			
	# ~ print(decodifica)
		# ~ except:
			# ~ print(jj)	
	return decodifica
	# ~ for j in testo1:
		# ~ decodifica=decodifica+diz_codifica[j]
	# ~ print(decodifica)
print("messaggio nascosto	decodificato-->		",funz_decodifica())
# ~ print(decodifica())
	# ~ return codifica1.var
	# ~ testo.replace(x, )
	# ~ print(diz_codifica)
	
	# ~ conta1=conta1+1
	# ~ if x==" ":
		# ~ lista_spazi.append(conta1)		
# ~ print(lista_spazi)


	# ~ var=globals()[j] = 33+r
	# ~ print(lettera2)
	# ~ for x in lista_var:
	# ~ print(var)
	# ~ 



	# ~ print(testo_codificato)
