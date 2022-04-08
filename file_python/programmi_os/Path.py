
#COSA FUNZIONA 
# .-->se path c:\\ e inserisco cd.. rimane in c:\\
#se inserisco per esempio desktop e mi trovo già in desktop il path rimane in desktop
#se inserisco una cartella corrispondente a una contenuta nel path, il path non si modifica: per esempio C:users/aaa/desktop , se inserisco aaa il path rimane  C:users/aaa/desktop

###CARTELLA==programmi_os
def path():
		# ~ "C:\\Users\\Attilio\\Desktop\\Nuova cartella"
		path.var="C:/Users/Attilio/desktop/"
path()
print("il programma legge solo all'interno dei file di tipo .txt o .py")
print("i file di un  altro tipo non rientrano nella conta dei file spostati , non spostati e nel totale dei file")
print("NON CREARE CARTELLE IL CUI NOME CONTIENE UNO SPAZIO e non creare piü cartelle aventi lo stesso identico nome ") 
print(path.var)
def x22():
	x22.var="ciao"
x22()
	
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
# ~ print()
import os
def naviga_tra_i_file():
	
	def comando_cd():
			# ~ if path.var!=C:\\
		# ~ x1=""	
		c=0	
		x22.var=""#per tornare indietro
		for x in path.var[::-1]:
			if x=="/":
				c=c+1
				if c>=2:
					break
			x22.var=x22.var+x
		print("X22",x22.var[::-1])
		# ~ x23=""
		# ~ for x in x22.var[::-1]:
			# ~ x23+=x
			# ~ if x==str("\\"):
				# ~ continue
		# ~ print(x23)
		c=0
		# ~ print(x2[::-1])		
		s3 =path.var.replace(x22.var[::-1]		,"")#per cancellare l ultimo pezzo di path in modo da tornare indietro

		# ~ print(s3)
		path.var=s3
	# ~ ciao=""	
		# ~ print(path.var)
	
	while True:
				# ~ print()
				# ~ print()
				# ~ try:
		
				
				
		# ~ x23=""
				from colored import fg
				print()
		
				inp =input("scrivi NOME CARTELLA oppure 'break' per interrompere il programma OPPURE scrivi 'cd..' per tornare indietro nel path	OPPURE 'ordina' per mettere ordine nella cartella  ")
				# ~ print(path.var)
				# ~ if inp==x24:
					# ~ print("casa")
				# ~ if inp==x23:
					# ~ continue
				pathlista=[]
				j1=""
				path1=""
				for j in path.var:
					path1=path1+j
					# ~ print(j)
					if j=="/":
						path1=path1+" "
				# ~ listaspazi=path1.split
				# ~ print(path1.split())
				for x in path1.split():
					# ~ print()
					pathlista.append(x.replace("/",""))
				print("pathlista",pathlista)
					# ~ else:
					# ~ if j=="/":
						# ~ pathlista.append(j1)
						# ~ j=""
					# ~ print(j1)
				# ~ print(pathlista)
						# ~ print(j)
					# ~ for y in j:
						# ~ if y!="/":
						# ~ print(y)
							# ~ j1=j1+y
						# ~ else:
							# ~ pass	
					# ~ pathlista.append(j1)
					# ~ j1=""
				# ~ print(pathlista)
					# ~ if j!="/":
						# ~ j1=j1+j
					# ~ else:
						# ~ continue
					# ~ pathlista.append(j1)
					# ~ j1=""
				# ~ print(pathlista)
					# ~ print(j1)
					
				# ~ pathlista=[x for x in path.var if x is not "/"]
				# ~ pathlista=path.var.split()
				# ~ print(pathlista)
				if inp!="cd.." and inp!="break" and inp!="" and inp!="ordina"  and inp not in pathlista and inp!="C:/" and inp!="c:/":		

					path.var=path.var+inp+"/"
					
				elif inp=="cd..":
						if path.var!="C:/":
							
							comando_cd()
						else:
							path.var="C:/"
				elif inp=="ordina":
					# ~ st2=input("vuoi ordinare ? inserire yes or no	")
					# ~ if st2=="yes":
					ordina()
					# ~ else:
						# ~ pass
						
					# ~ break
						# ~ print(path.var)	
				elif inp=="break":
						break
				# ~ elif inp==ordina()		
				# ~ elif inp=="":
						# ~ continue
				# ~ if x24!=inp:
				try:
					ok="ok"
					# ~ print(os.listdir(path.var))
					os.listdir(path.var)
					# ~ print(path.var)
				except:
						ok="no"
						# ~ if x24!=inp:
						comando_cd()
						print(inp," non esiste")
				else:
						pass#se inserisco una cartella che non esiste , non avanza nel path,rimane dov era
				# ~ path.var=path.var
				# ~ print("abcdefgh")
				# ~ pass
				color4 = fg('white')
				print(color4+path.var)
				# ~ print(ok)
				# ~ if ok=="ok":			
							
				print(os.listdir(path.var))	
				# ~ else:
				
					# ~ pass
					# ~ comando_cd()
					# ~ comando_cd()
					# ~ continue
					# ~ else:
				print(path.var)	
			
# ~ inserisci=input("inserisci 'ordina' per mettere in ordine i files o 'break' per interromepere il programma   	")
# ~ print()
# ~ if inserisci=="ordina":
	# ~ ordina()

# ~ else:
	# ~ pass
# ~ print("jk.var ",jk.var)		
	# ~ return jk.var
# ~ print()		
naviga_tra_i_file()
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
