#naviga tra le cartelle senza comando cd: basta inserire il nome della cartella
#per tornare indietro nel path bisogna scrivere cd..
#potrei usarlo per inserire con un input il path della cartella nel programma sortdirectories9.py ecc
#questo gestisce tutte le eccezioni --> se per errore inserisco cartella che non esiste, se inserisco ""
#se inserisco con  input una cartella  che non esiste, il progarmma non si interrompe, il path rimane lo stesso e permette di reinserire tramite un imput il nome della cartella .
import os
def path():
	
	path.var=r'C:/Users/Attilio/'
path()
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
		
				inp =input("scrivi NOME CARTELLA oppure 'break' per scegliere il path e chiudere cmd		")
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
def ciao():
				if inp!="cd.." and inp!="break":
				
				
					path.var=path.var+inp+"/"
					try:
						print(os.listdir(path.var))
					except:
						pass
					print(path.var)
				elif inp=="cd..":
					comando_cd()
					print(path.var)	
				# ~ elif inp=="break":
					# ~ break
			# ~ except:
				# ~ path.var=path.var
					# ~ print(path.var)
				# ~ continue		
				# ~ print(path.var)
	
			# ~ print(os.listdir(path.var))
			# ~ print(path.var)
print(path.var)
			# ~ print()
			# ~ print()
# ~ while True:
	# ~ inp =input("")

	# ~ if inp=="cd..":
		# ~ comando_cd()
	# ~ print(path.var)
	# ~ comando_cd()

# ~ txt = "I like bananas"

# ~ x = txt.replace("bananas", "apples")

# ~ print(x)


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

###CARTELLA==naviga_tra_cartelle
