import string
lettere=string.ascii_lowercase
# ~ print(len(lettere),"dfdf")
# ~ print(type(lettere))
# ~ print(lettere)
#ora passo tipo cifratura come variabile
# ~ cifratura=1#
#ognivoltacheemultiplodiunnumeroincremnto la chiave

#messaggiosegrto  >>-     zosk zu yge nkrru
def codifica1():
	codifica1.var=""
codifica1()

def codifica2():
	codifica2.var=""
codifica2()
#in realtä invece di scorrere il testo ü meglio scorrere le lettere
def messaggio_cifrato():
	# ~ testo2=input("inserire messaggio		")
	# ~ testo=testo2.lower()	
	# ~ metatesto=len(testo)/2
	testo="ciaociaociaociaociaociaociaociaociaociaociaociaociaociaociaociaociaociaociaociao"
	# ~ testo3=""
	# ~ testo4=""
	# ~ for x in range(len(testo)):
		# ~ if x <metatesto:
			# ~ testo3=testo3+testo[x]
		# ~ else:
			# ~ testo4=testo4+testo[x]
	# ~ metatesto=testo[len(testo)]
	# ~ print("t3",testo3)
	# ~ print("t4",testo4)
	# ~ print(metatesto)
	cifratura1=1
	# ~ cifratura1=int(input("inserire chiave1		"))
	# ~ cifratura2=int(input("inserire chiave1		"))
	# ~ print("CHIAVE	",cifratura)	
	
	
		# ~ diz_decodifica={}
	def diz_codifica():
		diz_codifica.var={}
	diz_codifica()
	def codice1(testo,cifratura1):
		# ~ testo1= testo.replace(" ", "")
		# ~ print(testo1)
		conta1=-1
		conta=0
		lista_spazi=[]
		diz_codifica.var={}
		# ~ CountryCodeDict["Spain"]= 34
		# ~ print(lettere)
		# ~ codifica=""
		# ~ print(lettere.index("g"))
				# ~ print(conta1)
		conto_rovescia=-1
		for x in lettere:
			conta=conta+1
			if conta%5==0:
				cifratura1=cifratura1+1
			
				# ~ lista_spazi=[]
				# ~ diz_codifica.var={}
			# ~ print(x)
			if lettere.index(x)+cifratura1<len(lettere):
				diz_codifica.var[x]=lettere[lettere.index(x)+cifratura1]
			else:
				conto_rovescia=conto_rovescia+1
				diz_codifica.var[x]=lettere[conto_rovescia]
			
		for j in testo:
			# ~ for y in diz_codifica.var
				if j!=" ":
					codifica1.var=codifica1.var+diz_codifica.var[j]
				else:
					codifica1.var=codifica1.var+" "
		return codifica1.var
	conta=0
	n=0
	n2=0
	# ~ for x in testo:
		# ~ conta+=1
	stringa=""
	# ~ for x in range(len(testo)):
		# ~ conta=conta+1
		# ~ if conta%5==0:
		# ~ cifratura1=cifratura1+1
			# ~ n=n+5
			# ~ n2=n2+5
	# ~ for x in (range(round((len(testo))/5.0),0)):
	print(codice1(testo,cifratura1))
		# ~ conta=conta+1
		# ~ if conta%5==0:
			# ~ cifratura1=cifratura1+1
		# ~ stringa=stringa+str(codice1(testo[0:5],cifratura1))
	print(stringa)	
	# ~ print(len(stringa))
			# ~ print(codifica1.var)
		# ~ if conta%5==0:
			# ~ cifratura1=cifratura1+1
			
	# ~ print("codifica",codifica1.var)
	# ~ print(len(testo))
	# ~ print(len(codifica1.var))
	# ~ print("messaggio:	----> ",codice1(testo,cifratura1))
	
	# ~ print("mess_in_codice_doppia_cifratura",codifica1.var+codifica2.var)
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
