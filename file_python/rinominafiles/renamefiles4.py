
			# ~ old_file_name = files
			# ~ print(old_file_name)
				# ~ print(files)
		
print("aggiungi compilato a nome file")
print("aggiunge compilato solo se non c'è già scritto compilato")
print()
# ~ conta=0
def ciao():
	# ~ choose_name=str(input("come vuoi chiamare i nuovi file?	"))
	

	
	import os
	path="C://Users//Attilio//Desktop//teglio_w-r//"
	# ~ import iterdir
	# ~ path = 'C:\\Users\\Username\\Path\\To\\File'
	# ~ import os
	# ~ path = "C:/Users"
	# ~ import os

	# ~ path = "C:\\Users"
	import os

	# ~ os.rename('a.txt', 'b.kml')
	# ~ os.rename(files, new_file_name)
	tipo=""

	def listdir(dir):
		conta=0
		# ~ conta=0
		filenames = os.listdir(dir)
		for files in filenames:
			conta=conta+1
			# ~ filenames = os.listdir(dir)
# ~ If you note the location of the gate (first 'a') then you can split the string after that point like:

	# ~ Code:
			a_string = files
			# ~ print(a_string)
		# ~ sentence = 'Mary had a little lamb'
			conta_punti=a_string.count('.')
			def rename():
					first_a = a_string.index('.')
					a_split = a_string[first_a:].split('.')
					a_split[0] = a_string[:first_a] + a_split[0]
					a_split = [x.strip() for x in a_split]
					tipo="."+a_split[1]
					# ~ print(tipo)
					
					if a_string[len(a_string)-4:len(a_string)]==tipo:
						nome=(a_string[0:len(a_string)-4])
						# ~ print(nome)
					# ~ x = text.replace(a_string, "k", 1)
					# ~ a_string.remove(tipo)
					# ~ print(tipo)
					if "compilato" not in a_string:
						new_file_name = nome+"_compilato"
							# ~ print(new_file_name)
						os.rename(path+str(files), path+str(new_file_name)+tipo)
						print(a_string,"file	rinominato")
					else:
						print(a_string,"		nessuna modifica al file")		
			# ~ a_string = files
			# ~ print(a_string)
		
				
		
			# ~ try:
				# ~ if conta_punti!=1:
					# ~ ajkl()
			rename()
			# ~ except:
				# ~ pass
				
	listdir(path)
ciao()
				# ~ if conta_punti==1:
					# ~ try:
						# ~ print(tipo)
					# ~ except:
def ajkjk():
						# ~ continue
			def ciuiau():
				
				# ~ a_split[0] = a_string[:first_a] + a_split[0]
				# ~ a_split = [x.strip() for x in a_split]
				def rinomina():
					if conta_punti==1:
						tipo="."+a_split[1]
						print(tipo)
						try:
							rename()
						except:
							pass
					else:
						pass
			# ~ tipo=a_split
			# ~ rename()
		
	# ~ listdir(path)
# ~ ciao()
# ~ def iuiu():

# ~ for j in files:

# ~ print(a_split)
# ~ print(files)
# ~ conta+=1


def rename_all_file_of_folder_and_openFolderAtTheEnd():
	print("FUNZIONA SOLO CON FILE JPG E PDF. MODIFICA IL NOME DEL FILE SENZA MODIFICARE IL TIPO")
	print("rename_all files in a folder")
	print("i files verranno chiamati nel seguente  modo:")
	print("per esempio se scegli ciao verranno chiamati rispettivamente ciao1, ciao2,ciao3 ecc")
	print()

	import os
	path="C://Users//Attilio//Desktop//iscrizione_valdimellowinter_documenti_vuoti8//"
	# ~ import iterdir
	# ~ path = 'C:\\Users\\Username\\Path\\To\\File'
	# ~ import os
	# ~ path = "C:/Users"
	# ~ import os
	# ~ def rename():
	# ~ path = "C:\\Users"
	import os

	# ~ os.rename('a.txt', 'b.kml')
	# ~ os.rename(files, new_file_name)
	tipo=""
	def listdir(dir):
		conta=0
		filenames = os.listdir(dir)
		for files in filenames:



















			
			# ~ if conta_punti==1:
				# ~ try:
					# ~ rename()
				# ~ except:
					# ~ continue
			# ~ else:
				# ~ continue
		# ~ os.startfile(path)
			if conta_punti==1:
				print(files)
	listdir(path)

# ~ rename_all_file_of_folder_and_openFolderAtTheEnd()






# ~ print("File renamed!")
