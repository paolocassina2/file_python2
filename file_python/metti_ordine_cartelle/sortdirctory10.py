def directory():
	directory.var=None
directory()		

#FUNZIONA:ADESSO LI SPOSTA SENZA COPIARLI
### nei file posso scrivere CARTELLA==nomecartella	adesso il programma entra nel file e legge la parte dopo CARTELLLA==	quindi estrae il nome della cartella dove spostare i file. in piu se non esiste, prima di spostare i file la crea e poi li sposta
def creacartella():			
# importing os module
	import os
	  
	# Directory
	directory.var = "GeeksforGeeks"
import os	  
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
path="C:/Users/Attilio/desktop/file_python/"
# ~ os.startfile(path)
# ~ os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# ~ os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

# ~ direcory=[f for f in path.iterdir() if f.is_dir()]
# ~ shutil.move("C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input\\hellotxt", "C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input\\hello\\hellotxt")
# ~ os.walk(directory)
#CARTELLA==fibonacci


# ~ print(os.path.isdir(path1))
# ~ print(os.listdir(path)) # returns list
# ~ print
listafiles=[]
listafolders=[]
# ~ def ciao():
for x  in os.listdir(path):#guarda dentro questa cartella e se ci sono cartelle dimmi come si chiamano
		path1=path+str(x)	#path per accedere a file e cartelle
		if (os.path.isdir(path+str(x)))==True:
			listafolders.append(x)
				# ~ print(x)
		else:
			listafiles.append(x)
# ~ print(listafolders)	
	# ~ print(listafiles)# ~ print(x)
#uguale
# ~ FILESRIMANENTI=[]
#VUOI SPOSTARE QUESTO FILE IN UNA CARTELLA=? si sceglie nome cartella solo allinizio
#dato un pezzo di stringa cerca nomi file che contengono quella strigna e li sposta nella cartella con un nome simile(perchü anch essa continene la stringa)
# ~ while True:
	# ~ stringa1=input("str		")#inserire pezzo di nome in comune tra files e cartelle
# ~ print(listafiles)	
	# ~ stringa2=
	# ~ stringa=stringa1.lower()
nomefile_corrente=os.path.basename(__file__)
# ~ print(listafolders)
# ~ print("nomequestofile_su_cui_sto_scrivendo		",nomefile_corrente)
lista_file_da_spostare=[]
lista_cartelle=[]
# ~ LISTA=[]
for x in listafiles:#COSI FUNZIONA!!!!!!!!PRIMA LEGGO TUTTI I FILE DI UNA CARTELLA E CREO UNA LISTA di tipo zip CHE CONTIENE FILE leggibili E nomi CARTELLE di destinazione DEI FILE LEGGIBILI(nomi cartelle estratte dai file)
					#poi successivamente scorro la lista che contiene i file e le cartelle di destinazione e sposto ciascun file nella sua cartella
			# ~ print(x)
			# ~ print("nome file	",x)
			# ~ cartella_destinazione=input("nome cartella destinazione	(press enter to skip)"	)
			# ~ minuscolo=x.lower()
		
			# ~ if cartella_destinazione!="":
				# ~ vuoi_spostare=input(" vuoi spostare questo file %s,  nella cartella %s (enter yes or y if u want) press enter if u dont want?"%(minuscolo,cartella_destinazione))
				# ~ if vuoi_spostare=="yes" or "y":
				# ~ print(dove)
					pathfile="C:/Users/Attilio/desktop/file_python/"
			# ~ print(pathfile)
			# ~ pathfile1=r'C:/Users/Attilio/Desktop/prova_programma/'
			# ~ if  "sort" not in x:
				# ~ print(x)
						
								# ~ print(pathfile)
								# ~ print(pathdestinazione)
								# ~ if str(cartella) in str(x):
	#def ciao():						# ~ print(str(x))
			
				# ~ def ciao():
					try:	
						
						if "sortdir" not in x:	#per evitare che il programma sposti i programmi come questo
							print(x)		
							with open(pathfile+str(x)) as f:
							
								lines = f.readlines()			
								# ~ print(lines)
							# ~ cartella_destinazione=""	
								for y in lines:
										# ~ for y in lines:
								# ~ print(y)
									if '#CARTELLA==' in y:
										z=y.replace('CARTELLA==', '')
										for jj in z:
											if jj=="#":
												j=z.replace(jj, '')
										# ~ j=z.split()
										# ~ print(y.replace('CARTELLA==', ''))
												NOMECARTELLA=j.strip()
												
									# ~ if 
									
										print("abc	",x,"			",NOMECARTELLA)				
										# ~ break
								
										lista_file_da_spostare.append(x)
										lista_cartelle.append(NOMECARTELLA)
				

							# ~ try:
							# ~ pathdestinazione=pathfile+NOMECARTELLA
							# ~ print(pathdestinazione)	
							# ~

							
					except:
					
								# ~ print("ecc2")
								continue
									
LISTA=zip(lista_file_da_spostare,lista_cartelle)	
lista1=list(LISTA)
print(lista1)	
import os		
import shutil#x[0]-->file  e x[1]-->cartella

# ~ def ciao():
import time
for x in lista1:
	# ~ time=time.time():
	# ~ if time>=time+3000:
		# ~ print(x[0])
		# ~ print(len("matrice"))
		# ~ print(len(x[1]))
		# ~ pathfile1=r'C:/Users/Attilio/Desktop/prova_programma/'
		pathfile="C:/Users/Attilio/desktop/file_python/"+x[0]
		destination="C:/Users/Attilio/desktop/file_python/"+x[1]+"/"+x[0]
		# ~ print(pathfile+str(x[1])+'/'+str(x[0]))
		# ~ destination=
		try:
			import time
			ora=time.time()
			import os
			import shutil
			shutil.move(pathfile, destination)
			# ~ import time
			
			# ~ destiona"C:/Users/Attilio/desktop/file_python/"+x[1]+"/"+x[0]
			if x in os.listdir("C:/Users/Attilio/desktop/file_python/"+x[1]):#stampa che e stato spostatao solo se effettivamente si trova nella cartella di destinazione
				print("il file "+str(x[0])+" è stato spostato nella directory "+str(x[1]))
				print(os.listdir("C:/Users/Attilio/desktop/file_python/"+x[1]))
			# ~ for x  in os.listdir("il file "+str(x[0])+" è stato spostato nella directory "+str(x[1])
			else:
				print("il file "+str(x[0])+" non e stato spostato")
		except:
			print("eccezione")
			pass	
			
	
						
						
													
def ciao():									
										# ~ if NOMECARTELLA in listafolders:#cr
				# ~ print("ciaociao")
		cartella_destinazione=NOMECARTELLA
		cartella_destinazione=cartella_destinazione
		try:
			
			print(NOMECARTELLA,"c  e gia")
			if NOMECARTELLA=="timer":
				print("il file "+x+"e stato spostato in "+NOMECARTELLA)
				
				for xY in listafolders:
					if NOMECARTELLA in xY:
						pathdestinazione="C:/Users/Attilio/Desktop/"+str(NOMECARTELLA)+"/"+str(x)
						shutil.move(pathfile, pathdestinazione)
		except:
			print("eccezione")
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
def ciao():
	for x in listafiles:
		# ~ print(x)
		pathfile="C:\\Users\\Attilio\\Desktop\\file_python\\"+str(x)
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
