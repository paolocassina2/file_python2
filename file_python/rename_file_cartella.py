import os
###CARTELLA==programmi_os
path="C:/Users/Attilio/Desktop/cartella22"
# ~ import os.path
# ~ print(os.listdir(path)	)
contatore=0

# ~ while True:
	
sceglinome=input("sceglinomefile	")#fare in modo che non si possano inserire le cifre nell'input
	# ~ for x in sceglinome:
	# ~ if x==1 in sceglinome or in sceglinome or in sceglinome or in sceglinome or in sceglinomeor x==6 or x  ==7 or x==8 or x==9:
		# ~ pass
	# ~ else:
		# ~ break
	
contatore=0

# ~ print(os.listdir(path))
for x  in os.listdir(path):#guarda dentro questa cartella e se ci sono cartelle dimmi come si chiamano
				# ~ path1=path2+str(x)	#path per accedere a file e cartelle
				# ~ if (os.path.isdir(path2+str(x)))==True:
				if not os.path.isdir(path+"\\"+x):  
					
					# ~ print(x)
					# ~ listafolders.var.append(x)
						# ~ print(x)
					# ~ print(x)
				# ~ else:


					text =x

						# find the index of is
					conta=text.count(".")
					
					if conta==1:#rinomino il file solo se è contenuto solo un punto all'interno di esso
						contatore=contatore+1	
						result = text.index('.')
						# ~ print(result)
						vecchionome=text[0:result]
						# ~ print("vecchionome",vecchionome)	
						extention=text[result:len(text)]
						# ~ print(extention)#per fare in modo che non cambi il tipo di file
						nuovonome=sceglinome+str(contatore)+extention
						try:
							if nuovonome !=vecchionome:#lo rinomino solo se in quella cartelal non esistono già file con quel nome
								print("vecchionome:",x,"		nuovonome:",nuovonome)
								os.rename(path+"/"+x, path+"/"+nuovonome)
							else:
								pass
						except:
							pass
							# ~ os.rename(nuovonome,x) 
					else:
						print("file non rinominato ",x)
# Output: 7	
					# ~ listafiles.var.append(x)
# ~ def ciao():
		# ~ path1=path+"/"+x
		# ~ print(path1)
###cartella==programmi_os
		# ~ st=""
		# ~ c=-1
		# ~ print(st.index("."))
		# ~ if x.count(".")==1:
			# ~ print((".").index(st))
			# ~ for j in x:
				
				# ~ st+=""e
			
			# ~ print("ciao")
		# ~ old_name =path+"/"+x
		# ~ print(old_name)
		# ~ contatore+=1
		# ~ new_name = path+"/"+"ciao"+str(contatore)
		# ~ print(new_name)

# ~ if os.path.isfile(x):
	# ~ print("The file already exists")
# ~ else:
		# ~ Rename the file
		# ~ os.rename(old_name, new_name)
