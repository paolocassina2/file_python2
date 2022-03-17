import string
lettere=string.ascii_lowercase
# ~ print(len(lettere),"dfdf")
# ~ print(type(lettere))
# ~ print(lettere)
#ora passo tipo cifratura come variabile
# ~ cifratura=1#
#doubleencryption

#messaggiosegrto  >>-     zosk zu yge nkrru
def codifica1():
	codifica1.var=""
codifica1()

def codifica2():
	codifica2.var=""
codifica2()
#in realtä invece di scorrere il testo ü meglio scorrere le lettere
def messaggio_cifrato():
	testo2=input("inserire messaggio		")
	testo=testo2.lower()	
	metatesto=len(testo)/2
	
	testo3=""
	testo4=""
	for x in range(len(testo)):
		if x <metatesto:
			testo3=testo3+testo[x]
		else:
			testo4=testo4+testo[x]
	# ~ metatesto=testo[len(testo)]
	print("t3",testo3)
	print("t4",testo4)
	# ~ print(metatesto)
	cifratura1=int(input("inserire chiave1		"))
	cifratura2=int(input("inserire chiave1		"))
	# ~ print("CHIAVE	",cifratura)	
		
		# ~ diz_decodifica={}
	def diz_codifica():
		diz_codifica.var={}
	diz_codifica()
	def codice1(testo,cifratura1):
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
			if lettere.index(x)+cifratura1<len(lettere):
				diz_codifica.var[x]=lettere[lettere.index(x)+cifratura1]
			else:
				conto_rovescia=conto_rovescia+1
				diz_codifica.var[x]=lettere[conto_rovescia]
			
		for j in testo:
			if j!=" ":
				codifica1.var=codifica1.var+diz_codifica.var[j]
			else:
				codifica1.var=codifica1.var+" "
		return codifica1.var
		
	def codice2(testo,cifratura2):
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
			if lettere.index(x)+cifratura2<len(lettere):
				diz_codifica.var[x]=lettere[lettere.index(x)+cifratura2]
			else:
				conto_rovescia=conto_rovescia+1
				diz_codifica.var[x]=lettere[conto_rovescia]
			
		for j in testo:
			if j!=" ":
				codifica2.var=codifica2.var+diz_codifica.var[j]
			else:
				codifica2.var=codifica2.var+" "
		return codifica2.var
		# ~ return(codifica)
		# ~ print(len(testo1))
		# ~ print(len(codifica))
	# ~ print("codifica		",codifica)
		# ~ for y in diz_codifica.keys():
		# ~ codifica=codifica+diz_codifica[y]
	# ~ print(codifica)
	print("messaggio:	----> ",codice1(testo3,cifratura1))
	print("messaggio:	----> ",codice2(testo4,cifratura2))
	
	print("mess_in_codice_doppia_cifratura",codifica1.var+codifica2.var)
messaggio_cifrato()
# ~ print("diz_codifica",diz_codifica.var)	
# ~ print(diz_codifica.var)
def decodificare():
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
