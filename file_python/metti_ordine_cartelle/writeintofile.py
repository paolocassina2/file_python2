

import os
path="C:/Users/Attilio/desktop/file_python/"
listafiles=[]
listafolders=[]
# ~ def ciao():

###scrive nei file ###CARTELLA==qualcosa	-->qualcosa e un input 
for x  in os.listdir(path):#guarda dentro questa cartella e se ci sono cartelle dimmi come si chiamano
		path1=path+str(x)	#path per accedere a file e cartelle
		if (os.path.isdir(path+str(x)))==True:
			listafolders.append(x)
				# ~ print(x)
		else:
			listafiles.append(x)
# ~ print(listafolders)	
for z in listafiles:
	print(z)
	try:
		f = open(z, "a")
		INPUT1=input("inserisci nome cartella nel file	")
		f.write("\n###CARTELLA=="+INPUT1)
		f.close()
		if INPUT1=="":  #press enter to skip
			continue
		if "z==writeintofile.py":
			continue
	except:
		continue        
	

###CARTELLA==
