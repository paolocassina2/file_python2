
#COSA FUNZIONA 
# .-->se path c:\\ e inserisco cd.. rimane in c:\\

#se un file contiene diverse cartelle di destinazione, il programma lo sposta
 #nell 'ultima cartella di destinazione che legge all'interno di esso solo se il nome della cartella si trova nell'ultima riga che legge, altrimenti non lo sposta
#
#se il nome della cartella di destinazione contenuto nel file  non corrisponde al nome di una cartella esistente , il file non viene spostato, rimane nello stesso posto
#CONTROLLO FINALE_ controlla se i file sono stati spostati correttamente nella cartella di destinazione
#sceglie cartella in base alla prima scritta CARTELLA==NOMECARTELLA che trova scorrendo dall'alto in basso il testo contenuto nel file. Le righe successive non le legge nemmeno
#conta quanti file leggibili contenenti testo e la scritta cartellaecc(vediquisopra) sono stati spostati correttamente
#stampa in rosso i file che NON sono stati spostati correttamente
#stampa in verde i file che sono stati spostati correttamente
################################################################
################################################################

#cosa non funziona:
#gestire eccezione quando non ci sono file da spostare
 
import os
def path():
	# ~ "C:\\Users\\Attilio\\Desktop\\Nuova cartella"
	path.var="C:\\Users\\Attilio\\"
path()



# ~ print(os.listdir(path))
# ~ print(os.path.isdir(path))
# ~ print(path)
# ~ print()
	# ~ print()
def naviga_tra_i_file():
		def x22():
			x22.var=""
		x22()
		def comando_cd():
			# ~ if path.var!=C:\\
			x1=""	
			c=0	
			x22.var=""#per tornare indietro
			for x in path.var[::-1]:
				if x=="\\":
					c=c+1
					if c>=2:
						break
				x22.var=x22.var+x
			c=0
			# ~ print(x2[::-1])		
			s3 =path.var.replace(x22.var[::-1]		,"")#per cancellare l ultimo pezzo di path in modo da tornare indietro

			# ~ print(s3)
			path.var=s3
			
		print(path.var)
		while True:
					# ~ print()
					# ~ print()
					# ~ try:
					
					
					print()
			
					inp =input("scrivi NOME CARTELLA oppure 'break' per scegliere il path OPPURE scrivi cd.. per tornare indietro nel path	")
					# ~ print(path.var)
					if inp!="cd.." and inp!="break" and inp!="":		

						path.var=path.var+inp+"\\"
						
					elif inp=="cd..":
							if path.var!="C:\\":
								
								comando_cd()
							else:
								path.var="C:\\"
							# ~ print(path.var)	
					elif inp=="break":
							break
							
					# ~ elif inp=="":
							# ~ continue
					try:
						ok="ok"
						# ~ print(os.listdir(path.var))
						os.listdir(path.var)
						# ~ print(path.var)
					except:
						ok="no"
						comando_cd()
						print(inp," non esiste")#se inserisco una cartella che non esiste , non avanza nel path,rimane dov era
						# ~ path.var=path.var
						# ~ print("abcdefgh")
						# ~ pass
					print(path.var)
					# ~ print(ok)
					# ~ if ok=="ok":			
								
					print(os.listdir(path.var))	
					
				
				# ~ print()
				# ~ print()
naviga_tra_i_file()
# ~ while True:
	# ~ inp =inputi
	# ~ if inp=="cd..":
		# ~ comando_cd()
	# ~ print(path.var)
	# ~ comando_cd()

# ~ txt = "I like bananas"

# ~ x = txt.replace("bananas", "apples")

# ~ print(x)
# ~ ciao()

# ~ comando_cd()
			# ~ x1=x1+x
	# ~ else:
		# ~ x1=x1+x
			# ~ break
# ~ print(x1)
# ~ print(x1[::-1])
# ~ for x in path:
	# ~ x2=
	# ~ if x=="/":
		# ~ c=c+1
		# ~ if c==2:
			# ~ break
	# ~ x1=x1+x
		# ~ except:
			# ~ path=r'C:/Users/Attilio/'
		# ~ path=path+inp+"/"
		# ~ inp =input("")
		# ~ continue
	# ~ print()




def directory():
	directory.var=None
directory()		

#FUNZIONA:ADESSO LI SPOSTA SENZA COPIARLI
### nei file posso scrivere CARTELLA==nomecartella	adesso il programma entra nel file e legge la parte dopo CARTELLLA==	quindi estrae il nome della cartella dove spostare i file. in piu se non esiste, prima di spostare i file la crea e poi li sposta
  
	# Parent Directory path
# ~ parent_dir  ="C:/Users/Attilio/Desktop/prova_programma"
	  
	# Path
# ~ path = os.path.join(parent_dir, directory.var)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# ~ import os
  
# Directory
# ~ directory.var = NOMECARTELLA
  
# Parent Directory path
# ~ parent_dir = 	"C:\\Users\\Attilio\\Desktop\\file_python"
  
# Path
# ~ path = os.path.join(parent_dir, directory.var)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# ~ os.mkdir(path)
# ~ print("Directory '% s' created" % directory.var)
##SPOSTA IL FILE IN UNA CARTELLA SE NEL FILE E CONTENUTO IL NOME DI QUELLA CARTELLA 		NEL FILE C E SCRITTO CARTELLA==nomecartella     per esempio sse si chima fibonacci 			CARTELLA==fibonacci
import os
import shutil

# ~ os.startfile(path)
# ~ os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# ~ os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

# ~ direcory=[f for f in path.iterdir() if f.is_dir()]
# ~ shutil.move("C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input\\hellotxt", "C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input\\hello\\hellotxt")
# ~ os.walk(directory)



# ~ print(os.path.isdir(path1))
# ~ print(os.listdir(path)) # returns list
# ~ print
def listafiles():
	listafiles.var=[]
listafiles()
# ~ listafolders=[]
# ~ def ciao():
# ~ print("path.var")
# ~ path2=path.var

def listafolders():
	listafolders.var=[]
listafolders()
for x  in os.listdir(path.var):#guarda dentro questa cartella e se ci sono cartelle dimmi come si chiamano
		# ~ path1=path2+str(x)	#path per accedere a file e cartelle
		# ~ if (os.path.isdir(path2+str(x)))==True:
		if os.path.isdir(path.var+"\\"+x):  

			listafolders.var.append(x)
				# ~ print(x)
			# ~ print(x)
		else:
			listafiles.var.append(x)
print("lista_dir",listafolders.var)	
print("listafile",listafiles.var)# ~ print(x)
#uguale
# ~ FILESRIMANENTI=[]
#VUOI SPOSTARE QUESTO FILE IN UNA CARTELLA=? si sceglie nome cartella solo allinizio
#dato un pezzo di stringa cerca nomi file che contengono quella strigna e li sposta nella cartella con un nome simile(perchü anch essa continene la stringa)
# ~ while True:
	# ~ stringa1=input("str		")#inserire pezzo di nome in comune tra files e cartelle
# ~ print(listafiles)	
	# ~ stringa2=
# ~ def ciaociao():
		# ~ stringa=stringa1.lower()
nomefile_corrente=os.path.basename(__file__)
# ~ print(listafolders)
# ~ print("nomequestofile_su_cui_sto_scrivendo		",nomefile_corrente)
lista_file_da_spostare=[]
lista_cartelle=[]
# ~ LISTA=[]
# ~ def icaa():
def lista1():
	lista1.var=[]
lista1()

# ~ def NOMECARTELLA():
	# ~ NOMECARTELLA.var=""
# ~ NOMECARTELLA()


# ~ def ordina():
import os
def l():
	l.var=[3,4]
l()
def l1():
	l1.var=[3,5]
l1()
# ~ def jk():
	
		# ~ jk.var=None
# ~ jk()
# ~ print(jk.var)
def destinazione111():
	destinazione111.var=[]
destinazione111()
def f2():
	f2.var=[]
f2()
print()
print()
def NOMECARTELLA():
	NOMECARTELLA.var=""
NOMECARTELLA()
def NOMECARTELLA1():
	NOMECARTELLA1.var=""
NOMECARTELLA1()
print("listafolders",listafolders.var)

from colored import fg

# ~ if "ciao" in listafolders.var:
	# ~ print("dfdfkjdlfjoleole")
def conta():
	conta.var=0#conta solo i file che possono essere letti (file txt, file di python ecc ) , . altri che non possono essere letti non sono nemmeno presi in considerazione(per esempio mp3 ecc)
conta()

def conta1():
	conta1.var=0
conta1()
def ordina():


	destinazione1=[]
	# ~ source1=[]
	# ~ def ordina1():
	for x in listafiles.var:
	#COSI FUNZIONA!!!!!!!!PRIMA LEGGO TUTTI I FILE DI UNA CARTELLA E CREO UNA LISTA di tipo zip CHE CONTIENE FILE leggibili E nomi CARTELLE di destinazione DEI FILE LEGGIBILI(nomi cartelle estratte dai file)
			
			pathfile=path.var
			# ~ print(pathfile)
			NOMECARTELLA1.var=""
			# ~ try:	
			
			# ~ if "sortdir" not in x:	#per evitare che il programma sposti i programmi come questo che ordinano i file
				# ~ print(x)	
			try:	#solleva eccezioni per esempio se non riesce a leggere il file
				
				with open(pathfile+"\\"+str(x)) as f:
				
					lines = f.readlines()			
					# ~ print(lines)
			# ~ def ciao():
					# ~ cartella_destinazione=""	
					for y in lines:
						# ~ for y in lines:
						# ~ print(y)
						# ~ pass
						if '#CARTELLA==' in y:
							z=y
							break
				z=y.replace('CARTELLA==', '')
				# ~ print("z",z)
							# ~ NOMECARTELLA.var=z.strip()
		
							# ~ NOMECARTELLA.var.replace('#', '')
						
# ~ print(j)
						
				senza_spazi=z.strip()
				
							# ~ print(NOMECARTELLA)
				
				for jjj in senza_spazi:
						if jjj=="#":
							continue
						else:
							NOMECARTELLA1.var=NOMECARTELLA1.var+jjj
	
				# ~ print(x,"n",NOMECARTELLA1.var,"len",len(NOMECARTELLA1.var))
				# ~ conta=conta+1
					
				if NOMECARTELLA1.var in listafolders.var:
								# ~ l1.var.append(NOMECARTELLA1.var)
						# ~ l.var.append(x)
						# ~ print("nomefile",x)
						# ~ def ciao():
						source=pathfile+str(x)
						destination=pathfile+NOMECARTELLA1.var+"\\"+str(x)
						# ~ print(source)
						destination1=pathfile+NOMECARTELLA1.var
						# ~ print(destination1)
						# ~ print("X",x)
						f2.var.append(x)
						# ~ print(f2.var)
						destinazione111.var.append(destination1)
						# ~ print("f2!!!!!!!!!!!!",f2.var)
						# ~ print,("destinazione1111",destinazione111.var)				
						# ~ jk.var=dict(zip(f2.var,destinazione111.var))	
						lista=list(zip(f2.var,destinazione111.var))			
						# ~ print(jk.var)
						shutil.move(source, destination)			
				else:
					# ~ print(x,"ecc2")
					color = fg('red')
					# ~ print(color+str(xk)+ "NON e stato spostato correttamente")
					print(color +str(x) +" NON e stato spostato correttamente")
					conta1.var=conta1.var+1
					print()
					# ~ print(conta1, " file leggibili su " ,conta , "sono stati spostati corretamente")
			except:
				continue
# ~ print(jk.var)				
	# ~ jk3=sorted(jk.var)
	# ~ print(lista)
	# ~ sorted(jk.var, key=lambda student: jk.var[1])
# ~ def ciaociao():	
	# ~ jk.var.sort()
# ~ def ciao():
	def takeSecond(elem):
		return elem[1]	
	lista.sort(key=takeSecond)
	# ~ print(lista)			
	# ~ print("jk.var", jk.var)	
	# ~ def ciao():
	if lista!=None:
	# ~ print("ciao",os.listdir(path.var))	
		for xk,xj in lista:
			# ~ print("xk",xk)
			# ~ print("xj",xj)
			if xk in os.listdir(xj)	:
				color = fg('green')
				# ~ print (color + 'Hello World !!!')
				print(color +str(xk)+ " è stato spostato correttamente in ",xj)
				conta.var=conta.var+1
				# ~ conta1=conta1+1
			elif xk in os.listdir(pathfile):
			# ~ if xk in os.listdir(xj)	:
				color = fg('red')
				print(color+str(xk)+ "NON e stato spostato correttamente")
				conta1.var=conta1.var+1
			print()
			

		# ~ for jkj, kkk in zip(jk.var):
				# ~ if				
	# ~ def ciao():
							
							# ~ print("NOMeECARTELLA.var",NOMECARTELLA.var)
	# ~ def ciao():								
							#
						# ~ for x in NOMECARTELLA.var:
							# ~ if x==	
							# ~ print("NOMECARTELLA1.var",nomecartella1.var)
							# ~ print(len(NOMECARTELLA1.var))
	# ~ def ciao():					
							
								# ~ continue
							
				# ~ except:
						# ~ print(x," eccezione , tipo file non leggibile")
					# ~ continue
	# ~ ordina1()	

		# ~ return jk.var
		# ~ print("jk.var	",jk.var)
print()

inserisci=input("inserisci 'ordina' per mettere in ordine i files o 'break' per interromepere il programma   	")
print()
if inserisci=="ordina":
	ordina()
	
else:
	pass
# ~ print("jk.var ",jk.var)		
	# ~ return jk.var
print()		

print("conta")
color = fg('white')
print(color +str(conta.var)  +" files su "+ str(conta.var+conta1.var)+" sono stati spostati correttamente")
# ~ print(conta.var)
# ~ print(conta1.var)
# ~ print(conta1, " file leggibili su " ,conta , "sono stati spostati corretamente")
# ~ import time
# ~ print("attendere 5 secondi")
# ~ time.sleep(5)	
# ~ ordina()
# ~ for xj in jk.var:

	# ~ path2=path.var+str(xj[1])+"\\" +str(xj[0])
	# ~ print(xj)
	
	# ~ destinazione=os.listdir(path2)
	# ~ print(destinazione)
	# ~ path2=""
	# ~ print("destinazione",destinazione)
	# ~ if xj[0] in destinazione:
		# ~ print(str(xj[0]) +"è stato spostato correttamente in "+ str(xj[1]))
# ~ for l						
	# ~ def ciaociao():					
						# ~ for jj in NOMECARTELLA.var:
								
						# ~ if jj=="#":
							# ~ jj.
							# ~ continue
							# ~ NOMECARTELLA.var.replace(jj)
							# ~ jj=j.replace(jj, '')
						# ~ else:
							# ~ NOMECARTELLA1.var=NOMECARTELLA1.var+jj
						# ~ NOMECARTELLA2=NOMECARTELLA1.split()
					# ~ print("NOMEECARTELLA1",NOMECARTELLA1.var)
					# ~ print(len(NOMECARTELLA1.var))
						# ~ print()
					
					# ~ if NOMECARTELLA1.var in  listafolders.var:
						# ~ print(NOMECARTELLA1.var)
						# ~ print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
					# ~ if NOMECARTELLA1.var in listafolders.var:
					# ~ try:
						# ~ source=pathfile+"\\"+str(x)
						# ~ destination=pathfile+"\\"+NOMECARTELLA1.var+"\\"+str(x)
						# ~ shutil.move(source, destination)

							# ~ shutil.move(, )
						# ~ except:
							# ~ pass
					# ~ else:
						# ~ continue
						# ~ if 
			# ~ except:
				# ~ print(x,"eccezione")
				# ~ continue			
							# ~ print("abc	",x,"			",NOMECARTELLA)				
							# ~ break
					
							# ~ lista_file_da_spostare.append(x)
							# ~ lista_cartelle.append(NOMECARTELLA.var)

# ~ def ciaoabc():
				# ~ try:
				# ~ pathdestinazione=pathfile+NOMECARTELLA
				# ~ print(pathdestinazione)	
				# ~

				
		# ~ except:
		
						# ~ print("ecc2")
						# ~ continue
					
	# ~ LISTA=zip(lista_file_da_spostare,lista_cartelle)	
	# ~ lista1.var=list(LISTA)
	# ~ print("lista1.var ",lista1.var)	
	# ~ import os		
	# ~ import shutil#x[0]-->file  e x[1]-->cartella

	# ~ def ciao():
		# ~ import time
		# ~ ciao=
		# ~ print("ciao",ciao)
		# ~ ciao22="C:\\Users\\Attilio\\Desktop\\Nuova cartella"
		# ~ ciao33=os.listdir(path.var)
		# ~ print("ciao33 ",ciao33)	#da modificare ,serve solo per testare programma quest indirizzo
		# ~ for x in lista1.var:
				
				
				# ~ if x[1] in ciao33:
			# ~ time=time.time():
			# ~ if time>=time+3000:
				# ~ print(x[0])
				# ~ print(len("matrice"))
				# ~ print(len(x[1]))
				# ~ pathfile1=r'C:/Users/Attilio/Desktop/prova_programma/'
					# ~ pathfile=path.var+x[0]
					# ~ destination=path.var+x[1]+"/"+x[0]
					# ~ print(pathfile+str(x[1])+'/'+str(x[0]))
					# ~ destination=
					# ~ try:
		# ~ import time
		# ~ ora=time.time()
		# ~ import os
		# ~ import shutil
		# ~ shutil.move(pathfile, destination)
						# ~ import time
						
						# ~ destiona"C:/Users/Attilio/desktop/file_python/"+x[1]+"/"+x[0]
						# ~ if x in os.listdir(path.var+x[1]):#stampa che e stato spostatao solo se effettivamente si trova nella cartella di destinazione
							# ~ print("il file "+str(x[0])+" è stato spostato nella directory "+str(x[1]))
									# ~ print(os.listdir(path.var+x[1]))
								# ~ for x  in os.listdir("il file "+str(x[0])+" è stato spostato nella directory "+str(x[1])
								# ~ else:
									# ~ print("il file "+str(x[0])+" non e stato spostato")
							# ~ except:
								# ~ print("eccezione")
								# ~ pass
						# ~ else:
								# ~ print("cartella ", x[1], "inesistente")
								# ~ continue		
								
			# ~ return lista1
		# ~ print()					
	# ~ def ciaocioacioacioa():
			# ~ print("ciao33",ciao33)
			# ~ if len (lista1.var)>0:		
			# ~ ordinare=input("scrivi 'ordina' per ordinare la cartella, altrimenti premi qualsiasi tasto per uscire dal programma   " )	
			# ~ print("listafol",listafolders.var)
			# ~ if ordinare=="ordina":
					# ~ folder=os.listdir(path.var)
					# ~ print("folder",folder)
					# ~ if NOMECARTELLA in listafolders.var:
						# ~ ordina()
						# ~ print("lista1.var",lista1.var)
						# ~ for xj in lista1.var:#ordina_e poi controlla che i file siano stati spostati corretamente
							# ~ print(os.listdir("C:/Users/Attilio/desktop/file_python"))
							# ~ if xj[1]!="":
								# ~ if xj[0] in os.listdir(path.var+xj[1]):
									# ~ print(xj[0] ," e stato spostato correttamente")
								# ~ else:
									# ~ print(xj[0] ,"non e stato spostato correttamente")	
							# ~ else:
								# ~ print(xj[0], "non e stato spostato")	#file che probabilmente riesce a leggere ma all interno di essi non c e scritto il nome di una cartella (oppure c e scritto CARTELLA=="", quindi non sa dove spostarli
					# ~ else:
						# ~ pass
			# ~ else:
						# ~ pass
				
											
		# ~ else:
			# ~ print("nessun file da spostare")							
																
	# ~ def ciao():									
													# ~ if NOMECARTELLA in listafolders:#cr
							# ~ print("ciaociao")
					# ~ cartella_destinazione=NOMECARTELLA
					# ~ cartella_destinazione=cartella_destinazione
					# ~ try:
						
						# ~ print(NOMECARTELLA,"c  e gia")
						# ~ if NOMECARTELLA=="timer":
							# ~ print("il file "+x+"e stato spostato in "+NOMECARTELLA)
							
							# ~ for xY in listafolders:
								# ~ if NOMECARTELLA in xY:
									# ~ pathdestinazione="C:/Users/Attilio/Desktop/"+str(NOMECARTELLA)+"/"+str(x)
									# ~ shutil.move(pathfile, pathdestinazione)
					# ~ except:
						# ~ print("eccezione")
						# ~ continue			#per semplificare, il programma non crea la cartella nel caso in cui non esiste
				# ~ else:
					# ~ try:
													# ~ creacartella()
													# ~ FILESRIMANENTI.append(x)	
													# ~ listafolders.append(NOMECARTELLA)
													# ~ if NOMECARTELLA in listafolders:#cr
														# ~ print("il file "+x+"e stato spostato in "+NOMECARTELLA)	
														# ~ cartella_destinazione=NOMECARTELLA
														# ~ cartella_destinazione=cartella_destinazione
												
														# ~ pathdestinazione="C:\\Users\\Attilio\\Desktop\\file_python\\"+str(NOMECARTELLA)+"\\"+str(x)
													# ~ shutil.move(pathfile, pathdestinazione)
												# ~ else:
													# ~ continue
											# ~ except:
												# ~ pass
											

								# ~ print("e una prova")
								# ~ try:			
						
							
						# ~ except:
							# ~ print("error , this folder does not exist")
							# ~ continue
					# ~ if stringa in minuscolo:
						# ~ pr
# ~ def ciao():
			# ~ for x in listafiles:
				# ~ print(x)
				# ~ pathfile="C:\\Users\\Attilio\\Desktop\\file_python\\"+str(x)
				# ~ if x!=nomefile_corrente:
				# ~ if x=="timer.pyw":
					# ~ try:
						# ~ with open(pathfile) as f:
									
							# ~ lines = f.readlines()			
									# ~ print(lines)
						# ~ cartella_destinazione=""	
					
		# ~ for x in listafolders:
			# ~ print(x)
			# ~ if u in x:
				# ~ print(u ,"ce") 
				
				# ~ break
			# ~ else:
				# ~ print(u ," non c e")
				# ~ check=="c e"
		# ~ ciao="CARTELLA==ciao"
		# ~ if check== "c e":
		# ~ print(
		# ~ print(ciao[10:
			

		# ~ if "fileprova" in lines:
		# ~ print("ciaociao")
	# ~ creacartella()	
		# ~ print("ce")
	# ~ print(path1)
	# ~ pathfile=path1+"\\"+str("hello2.txt")
	# ~ print(pathfile)	
	# ~ pathdestinazione=path1+"\\"+str(listafolders[0])+"\\"+str("hello2.txt")
	# ~ print(pathdestinazione)
			# ~ print(os.path.isdir(path1))
			# ~ print(os.listdir(path))
	# ~ import os
	# pathfile=path1+"\\"+str(x)
	# ~ print(pathfile)	
	# ~ pathdestinazione=path1+"\\"+str(listafolders[0])+"\\"+str(x)~ import shutil

	# ~ os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
	# ~ os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
