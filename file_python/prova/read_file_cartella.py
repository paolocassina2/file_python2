###CARTELLA==prova
#cosi leggendo il file "prende" la prima riga con scritto ###CARTELLA==nomecartella.
#per esempio se c'è scritto ###CARTELLA==prova e poi ###CARTELLA==giacomo prende CARTELLA==prova
#ignora anche tutto il resto del contenuto del file
#funziona , bisogna integrarlo col resto del programma 
import os
def path():
	# ~ "C:\\Users\\Attilio\\Desktop\\Nuova cartella"
	path.var="C:\\Users\\Attilio\\desktop\\Nuova Cartella"
path()



# ~ print(os.listdir(path))
# ~ print(os.path.isdir(path))
# ~ print(path)
# ~ print()
	# ~ print()
# ~ d
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
def jk():
	
		jk.var=None
jk()
# ~ print(jk.var)
def destinazione111():
	destinazione111.var=[]
destinazione111()
def f2():
	f2.var=[]
f2()
print()
print()
# ~ def NOMECARTELLA():
	# ~ NOMECARTELLA.var=""
# ~ NOMECARTELLA()
def NOMECARTELLA1():
	NOMECARTELLA1.var=""
NOMECARTELLA1()
print("listafolders",listafolders.var)


# ~ if "ciao" in listafolders.var:
# ~ print("dfdfkjdlfjoleole")



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
	
				print(x,"n",NOMECARTELLA1.var,"len",len(NOMECARTELLA1.var))

			except:
				# ~ print("ecc",x)
				continue# ~ def ciao():
def ci():					
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
						# ~ print("destinazione1111",destinazione111.var)				
					
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
