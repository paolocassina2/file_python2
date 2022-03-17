import os
mypath="C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input"
# ~ os.system("C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input\\CentoDiQuestiGiorni.mp3")
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# ~ print(onlyfiles)
import random
# ~ ewhile True:
#choose random music
nomefile=random.choice(onlyfiles)
lista_musica=set()
while True:
	nomefile=random.choice(onlyfiles)
	if "mp3" in nomefile:
		# ~ print(nomefile)
		lista_musica.add(nomefile)
		# ~ print(lista_musica)
		# ~ s.update(nomefile)
		if len(lista_musica)>=2:
			break
# ~ print(lista_musica)
import random
		# ~ break
filescelto=random.choice(list(lista_musica))	
print(filescelto)

os.system(mypath+"\\"+filescelto)
