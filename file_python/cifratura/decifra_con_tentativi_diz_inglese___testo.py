import string
import italian_dictionary
# initializing string 


#FUNYIONA CON UNA PAROLA ALLA VOLTA		#va a tentativi con diverse chiavi di cifratura (es--> chiave 1 sceglie lettera precedente(per es se la lettera e b sceglie "a"),2 seceglie due lettere precedenti(se e d sceglie b) e cosi via
#restituisce la  possibile soluyione con la relativa chiave
##########################################################################

	
# ~ import enchant
# ~ d = enchant.Dict("en_US")
# ~ d.check("Hello")
# ~ True

# ~ print(d.check("Hellddfdfo"))
# ~ print(dictionary[0:3])
# ~ print(type(dictionary))
# ~ print(type(dictionary.meaning("indentation")))
# ~ print("there")

# Use this to get only the meaning 
# ~ definition = italian_dictionary.get_definition('cane', limit=3, all_data=False) 

	#Use this to get all datas of a word (all_data default is True)

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

#N B restituisce una chiave diversa rispetto al sito

#in realtä invece di scorrere il testo ü meglio scorrere le lettere
codifica2=input("inserire mess segreto    ")
# ~ print("diz_codifica",diz_codifica.var)	
# ~ print(diz_codifica.var)
def indice():
		indice.var=0
indice()

def decodifica():
	decodifica.var=""
decodifica()


# ~ test_string = "Geeksforgeeks is best Computer Science Portal"
 
# printing original string
# ~ print ("The original string is : " +  test_string)

# using split()
# to extract words from string
listaparole = codifica2.split()
 
# printing result
print ("The list of words is : " +  str(listaparole))

def decodificare():
		
		
		
		cifratura=indice.var
		def funz_decodifica():
			# ~ def codifica(testo):
			# ~ testo1= testo.replace(" ", "")
			# ~ print(testo1)
			# ~ conta1=-1
			# ~ lista_spazi=[]
			diz_decodifica={}
			decodifica.var=""
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
			# ~ print("diz_deco	",diz_decodifica)	
				# ~ else:
					# ~ conto_rovescia=conto_rovescia+1
					# ~ diz_decodifica[x]=lettere[conto_rovescia]
			# ~ print(diz_decodifica)
			for jj in codifica1.var:	
				# ~ print(jj)	
				if jj!=" ":
				# ~ try:
					decodifica.var=decodifica.var+diz_decodifica[jj]
					# ~ print(decodifica)
				else:
					decodifica.var=decodifica.var+" "
					
			# ~ print(decodifica)
				# ~ except:
					# ~ print(jj)	
			return decodifica.var
			# ~ for j in testo1:
				# ~ decodifica=decodifica+diz_codifica[j]
			# ~ print(decodifica)
		funz_decodifica()
		# ~ print("messaggio nascosto	decodificato-->		",funz_decodifica())
		# ~ print(decodifica())
				# ~ lista_spazi.append(conta1)		
		# ~ print(lista_spazi)
	# ~ for indice.var in range(0,len(lettere)):
		
import enchant	
# ~ decodificare()
possibili_soluzioni={}
possibili_soluzioni_inglese={}


lista_soluzioni=[]
lista_soluzioni1=[]
for xzj in listaparole:
	codifica1.var=xzj		#se ü una parola del diyioniario allora ü una possibile soluyionie
	for indice.var in range(0,len(lettere)):
			# ~ print(indice.var)
			decodificare()
			try:			
				datas = italian_dictionary.get_definition(decodifica.var)
				# ~ datas1=list(datas)
				lista_soluzioni.append(decodifica.var)
				possibili_soluzioni[indice.var]=lista_soluzioni
				# ~ print(datas)
			except:
				pass
				
				
		
			d = enchant.Dict("en_US")
			if d.check(decodifica.var)==True:
			
				lista_soluzioni1.append(decodifica.var)
				possibili_soluzioni_inglese[indice.var]=lista_soluzioni1

		# ~ print(d.check("Hellddfdfo"))
print("possibile soluzione (chiave:valore)	",possibili_soluzioni)
print("possibile soluzione__inglese (chiave:valore)	",possibili_soluzioni_inglese)
		# ~ print(datas1)
			# ~ print(testo_codificato)
	# ~ datas = italian_dictionary.get_definition('cane')
	# ~ print(datas)
