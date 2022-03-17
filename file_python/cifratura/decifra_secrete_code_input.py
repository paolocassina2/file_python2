import string

#Algorithm of Caesar Cipher
lettere=string.ascii_lowercase
# ~ print(len(lettere),"dfdf")
# ~ print(type(lettere))
# ~ print(lettere)
#ora passo tipo cifratura come variabile
# ~ cifratura=1#
def codifica1():
	codifica1.var=""
codifica1()
#in realtä invece di scorrere il testo ü meglio scorrere le lettere

# ~ print("diz_codifica",diz_codifica.var)	
# ~ print(diz_codifica.var)
def decodificare():
	codifica1.var=input("inserire mess segreto    ")
	cifratura=int(input("inserire chiave		"))
	def funz_decodifica():
		# ~ def codifica(testo):
		# ~ testo1= testo.replace(" ", "")
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

decodificare()
		# ~ var=globals()[j] = 33+r
	# ~ print(lettera2)
	# ~ for x in lista_var:
	# ~ print(var)
	# ~ 



	# ~ print(testo_codificato)
