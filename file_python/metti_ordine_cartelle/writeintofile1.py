

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
	print("press enter to skip")
	INPUT1=input("inserisci il nome della cartella nel file....altrmimenti scrivi leggifile per vedere contenuto del file	")
	
	if z=="writeintofile1.py":
		continue	
		
		

			#per evitare che il programma sposti i programmi come questo
								
		# ~ with open(pathfile+str(x)) as f:
					
			# ~ lines = f.readlines()	
			# ~ print(lines)		
								# ~ print(lines)
							# ~ cartella_destinazione=""	
								#for y in lines:
	if INPUT1!="" and INPUT1!="leggifile":
			try:
				f = open(z, "a")
				f.write("\n###CARTELLA=="+INPUT1)
				f.close()
			except:
				continue  
	elif INPUT1=="":  #press enter to skip
		continue
	elif INPUT1=="leggifile":	
		try:
			with open(path+str(z)) as f:
						
				lines = f.readlines()
				for j in lines:
					print(j)	
		except:
			continue
	
	print()						# ~ print(lines)
						# ~ cartella_destinazione=""	
								# ~ for y in lines:
	
	      
	

###CARTELLA==
