
import os
import shutil
path="C:\\Users\\Attilio\\Desktop\\file_python\\"
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
#uguale
#dato un pezzo di stringa cerca nomi file che contengono quella strigna e li sposta nella cartella con un nome simile(perchü anch essa continene la stringa)
stringa1=input("str		")#inserire pezzo di nome in comune tra files e cartelle
stringa=stringa1.lower()
for x in listafiles:
	minuscolo=x.lower()
	if stringa in minuscolo:
		
		# ~ print(x)
		for cartella1 in listafolders:
			cartella=cartella1.lower()
			if stringa in cartella:
				# ~ print(cartella)
	# ~ if "matr" in cartella:
		# ~ print(cartella)
		# ~ print(cartella)
		
			# ~ if "matr" in x:
				# ~ print(x)
			# ~ if cartella in x:
				# ~ print(x) 
			
				# ~ print(x)
				pathfile="C:\\Users\\Attilio\\Desktop\\file_python\\"+str(x)

				pathdestinazione="C:\\Users\\Attilio\\Desktop\\file_python\\"+str(cartella)+"\\"+str(x)
				# ~ print(pathfile)
				# ~ print(pathdestinazione)
				# ~ if str(cartella) in str(x):
				# ~ print(str(x))
				
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
