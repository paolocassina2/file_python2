
import os
import shutil
path="C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input"
# ~ os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# ~ os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

# ~ direcory=[f for f in path.iterdir() if f.is_dir()]
# ~ shutil.move("C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input\\hellotxt", "C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input\\hello\\hellotxt")
# ~ os.walk(directory)



# ~ print(os.path.isdir(path1))
# ~ print(os.listdir(path)) # returns list
# ~ print
listafiles=[]
listafolders=[]

for x  in os.listdir(path):#guarda dentro questa cartella e se ci sono cartelle dimmi come si chiamano
	path1=path+"\\"+str(x)	#path per accedere a file e cartelle
	if (os.path.isdir(path+"\\"+x))==True:
		listafolders.append(x)
			# ~ print(x)
	else:
		listafiles.append(x)
# ~ print(listafolders)	
# ~ print(listafiles)# ~ print(x)
# ~ def ciao():
#sposta tutti i file con nome che assomiglia ad una cartella in quella cartella: per esempio  i files si chiamano caio1 caio2 e la cartella caio. allora sposta caio1 ecaio2 in caio
for cartella in listafolders:

	# ~ print(cartella)
	for x in listafiles:
		pathfile="C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input"+"\\"+str(x)

		pathdestinazione="C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input"+"\\"+str(cartella)+"\\"+str(x)
		if str(cartella) in str(x) :	#e meglio che il nome del file sia sempre più lungo del nome della cartelal in modo da dare i nomi a file e cartelle sempre allo stesso mdoo
			# ~ print(str(x))				per esempio nomi files achille1.py,achille2.py ee e nome cartella -->achille
			shutil.move(pathfile, pathdestinazione)	
			# ~ if listafolders[0] in x:
				# ~ print("ciao")	

def sposta_nella_cartella_prova_se_e_una_prova():
	#per capire se e una prova apre il file e legge se nel file ci e scritto fileprova
	with open("C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input"+"\\tkmusic.py") as f:
		lines = f.readlines()			
	print(lines)

	for x in lines:
		if "fileprova" in x:
			print("e una prova")
	# ~ print(x)
# ~ if "fileprova" in lines:
	# ~ print("ciaociao")
	
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
