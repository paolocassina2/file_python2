#naviga tra le cartelle senza comando cd: basta inserire il nome della cartella
#per tornare indietro nel path bisogna scrivere cd..
#potrei usarlo per inserire con un input il path della cartella nel programma sortdirectories9.py ecc
import os
def path():
	
	path.var=r'C:/Users/Attilio/'
path()
# ~ print(os.listdir(path))
# ~ print(os.path.isdir(path))
# ~ print(path)
# ~ print()
# ~ print()
def comando_cd():
	x1=""	
	c=0	
	x2=""#per tornare indietro
	for x in path.var[::-1]:
		if x=="/":
			c=c+1
			if c>=2:
				break
		x2=x2+x
	c=0
	# ~ print(x2[::-1])		
	s3 =path.var.replace(x2[::-1]		,"")#per cancellare l ultimo pezzo di path in modo da tornare indietro

	# ~ print(s3)
	path.var=s3
	

while True:
			# ~ print()
			# ~ print()
			# ~ try:
			print(path.var)
			print(os.listdir(path.var))
			print()
			inp =input("scrivi NOME CARTELLA oppure 'break' per scegliere il path e chiudere cmd		")
			if inp!="cd.." and inp!="break":
				path.var=path.var+inp+"/"
				# ~ print(path.var)
			elif inp=="cd..":
				comando_cd()
			
			elif inp=="break":
				break	
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
