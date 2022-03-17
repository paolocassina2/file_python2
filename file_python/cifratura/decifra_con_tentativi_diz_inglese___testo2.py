import string
import italian_dictionary
# initializing string 
import enchant	

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
# ~ def codifica1():
	# ~ codifica1.var=""
# ~ codifica1()

codifica2=input("inserire mess segreto    ")

def indice():
		indice.var=0
indice()

def decodifica():
	decodifica.var=""
decodifica()


listaparole = codifica2.split()
 
# printing result
# ~ print ("The list of words is : " +  str(listaparole))
def cifratura():
	cifratura.var=0
cifratura()
dizio_possibili_sol={}
dizio2={}
def decodificare():
		
		
		
		diz_decodifica={}
		decodifica.var=""
		
		for x in lettere:
			if lettere.index(x)>=0:
			
					diz_decodifica[x]=lettere[lettere.index(x)-cifratura.var]
	
		# ~ print(diz_decodifica)
		for jj1 in listaparole:
			for jj in jj1:
				decodifica.var=decodifica.var+diz_decodifica[jj]
			decodifica.var=decodifica.var+" "
		dizio_possibili_sol[str(cifratura.var)]=decodifica.var
		dizio2[decodifica.var]=str(cifratura.var)
		return decodifica.var
# ~ decodificare()		
# ~ print(dizio_possibili_sol)

lista_soluzioni=[]
for x in range(0,len(lettere)):
	cifratura.var=x
	# ~ wub wr vdb khoor
	
	# ~ print("chiave	",cifratura.var)
	decodificare()
# ~ print(dizio_possibili_sol)
	# ~ print(decodificare())
	# ~ print()

# ~ print(dizio_possibili_sol)
	# ~ def lkdjfkl():
parola=""

# ~ print(lista_possibili_sol)
lista111=[]


	#messaggiosegreto  >>-     zosk zu yge nkrru
for xy in dizio_possibili_sol.values():
		# ~ print(xy)
	listaparole2 = xy.split()
	lista111.append(listaparole2)
parola=""
d = enchant.Dict("en_US")	
# ~ pr(lista111)

	
# ~ for x i	
soluz="jkdj"
soluzioni_meno_probabili=[]
for xxy in dizio_possibili_sol.values():		
	# ~ print(xxy)
	# ~ print(xxy.split())
	# ~ soluz="ok"
	conta=0
	for xy in xxy.split():
		if  d.check(xy)==True:#se le parole decifrate sono contenute nel vocabolario
			
			conta=conta+1
			if conta==len(xxy.split()):
				lista_soluzioni.append(xxy)
				break
			elif conta<=2:
				soluzioni_meno_probabili.append(xxy)
	# ~ print(conta)
	if soluz=="ok":
		break
print("soluzione più probabile	",lista_soluzioni,"	chiave = ",dizio2[lista_soluzioni[0]])
if len(soluzioni_meno_probabili)>1:
	print("soluzione MENO probabile	",soluzioni_meno_probabili)
	# ~ for jj234 in xxy:
		# ~ print(jj234)
			# ~ parola=parola+jj234
			
			# ~ print("parola",parola)

	# ~ if  d.check(parola)==True:
		# ~ lista_soluzioni.append(parola)
	# ~ parola=""
			# ~ print(xxy)
			# ~ if d.check(jj234)==True:
					# ~ print(xxy)	
					# ~ lista_soluzioni.append(xxy)
				# ~ print(xy)
				# ~ lista_soluzioni.append(d)
	# ~ print(lista_soluzioni)
def ciao():			
			
	import enchant	
	# ~ decodificare()
	possibili_soluzioni={}
	possibili_soluzioni_inglese={}


	lista_soluzioni=[]
	lista_soluzioni1=[]
	soluz="dfdf"
	#semplifico con parole solo in inglese
	# ~ for xzj in listaparole:
	codifica1.var=listaparole[1]	
			#se ü una parola del diyioniario allora ü una possibile soluyionie
	for indice.var in range(0,len(lettere)):
			cifratura.var=indice.var# ~ print(indice.var)
			decodificare()
				
					
			
			d = enchant.Dict("en_US")
			if d.check(decodifica.var)==True:
			
				lista_soluzioni1.append(decodifica.var)
				possibili_soluzioni_inglese[indice.var]=lista_soluzioni1

			# ~ print(d.check("Hellddfdfo"))
	# ~ print("possibile soluzione (chiave:valore)	",possibili_soluzioni)
	print("possibile soluzione__inglese (chiave:valore)	",possibili_soluzioni_inglese)
			# ~ print(datas1)
				# ~ print(testo_codificato)
		# ~ datas = italian_dictionary.get_definition('cane')
	# ~ print(datas)
