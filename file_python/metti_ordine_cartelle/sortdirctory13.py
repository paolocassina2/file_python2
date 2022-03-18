

#
#codice adesso è funzionante-->manca il controllo finale per asssicurarsi che il file sia effetivamente stato spostato nella cartella di destinazione
import os
def path():
	# ~ "C:\\Users\\Attilio\\Desktop\\Nuova cartella"
	path.var="C:\\Users\\Attilio\\"
path()

def ciao():
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
			x1=""	
			c=0	
			x22.var=""#per tornare indietro
			for x in path.var[::-1]:
				if x=="/":
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
			
					inp =input("scrivi NOME CARTELLA oppure 'break' per scegliere il path		")
					# ~ print(path.var)
					if inp!="cd.." and inp!="break" and inp!="":

						path.var=path.var+inp+"/"
						
					elif inp=="cd..":
							comando_cd()
							print(path.var)	
					elif inp=="break":
							break
							
					# ~ elif inp=="":
							# ~ continue
					try:
					
						os.listdir(path.var)
						# ~ print(path.var)
					except:
						comando_cd()
						print(inp," non esiste")#se inserisco una cartella che non esiste , non avanza nel path,rimane dov era
						# ~ path.var=path.var
						# ~ print("abcdefgh")
						# ~ pass
					print(path.var)
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
ciao()

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

def NOMECARTELLA():
	NOMECARTELLA.var=""
NOMECARTELLA()

def NOMECARTELLA1():
	NOMECARTELLA1.var=""
NOMECARTELLA1()
# ~ def ordina():
import os
def ordina():
	for x in listafiles.var:
	#COSI FUNZIONA!!!!!!!!PRIMA LEGGO TUTTI I FILE DI UNA CARTELLA E CREO UNA LISTA di tipo zip CHE CONTIENE FILE leggibili E nomi CARTELLE di destinazione DEI FILE LEGGIBILI(nomi cartelle estratte dai file)
		
			pathfile=path.var
			NOMECARTELLA1.var=""
			# ~ try:	
			
			if "sortdir" not in x:	#per evitare che il programma sposti i programmi come questo che ordinano i file
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
						# ~ def ciao():
							if '#CARTELLA==' in y:
								z=y.replace('CARTELLA==', '')
								# ~ print(z)
								# ~ for jj in z:
									# ~ if jj=="#":
										# ~ j=z.replace(jj, '')
								NOMECARTELLA.var=z.strip()
								# ~ print(y.replace('CARTELLA==', ''))
								# ~ print(j)
								# ~ NOMECARTELLA.var=j[0].strip()
								# ~ print(j)
								# ~ NOMECARTELLA.var=j
								# ~ NOMECARTELLA.var.replace('#', '')
						# ~ print("NOMeECARTELLA.var",NOMECARTELLA.var)
						
					for jjj in NOMECARTELLA.var:
							if jjj=="#":
								continue
							else:
								NOMECARTELLA1.var=NOMECARTELLA1.var+jjj
						# ~ for x in NOMECARTELLA.var:
							# ~ if x==	
					print(NOMECARTELLA1.var)
					print(len(NOMECARTELLA1.var))
				
					if NOMECARTELLA1.var in listafolders.var:
							
						source=pathfile+"\\"+str(x)
						destination=pathfile+"\\"+NOMECARTELLA1.var+"\\"+str(x)
						# ~ print(NOMECARTELLA1.var,"ce")
						shutil.move(source, destination)

						# ~ shutil.rename(source, destination)
					else:
						print(NOMECARTELLA1.var,"non ce")
						continue
				except:
					print("eccezione1")
					continue
print()
inserisci=input("inserisci 'ordina' per mettere in ordine i files o 'break' per interromepere il programma   	")
if inserisci=="ordina":
	ordina()
else:
	pass								
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
