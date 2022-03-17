def rename_all_file_of_folder_and_openFolderAtTheEnd():
	print("FUNZIONA SOLO CON FILE JPG E PDF. MODIFICA IL NOME DEL FILE SENZA MODIFICARE IL TIPO")
	print("rename_all files in a folder")
	print("i files verranno chiamati nel seguente  modo:")
	print("per esempio se scegli ciao verranno chiamati rispettivamente ciao1, ciao2,ciao3 ecc")
	print()
	choose_name=str(input("come vuoi chiamare i nuovi file?	"))
	import os
	path="C://Users//Attilio//Desktop//iscrizione_valdimellowinter_documenti_vuoti8//"
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
		filenames = os.listdir(dir)
		for files in filenames:
			# ~ for j in files:
			if ".jpg" in files:
				# ~ print("bene")
				tipo= ".jpg"
					# ~ print(j)
			else: 
				tipo=".pdf"
			
			# ~ print(files)
			conta+=1
			# ~ old_file_name = files
			# ~ print(old_file_name)
			print(files)
			new_file_name = choose_name+str(conta)
			print(new_file_name)
			os.rename(path+str(files), path+str(new_file_name)+tipo)
		os.startfile(path)
	listdir(path)

rename_all_file_of_folder_and_openFolderAtTheEnd()






# ~ print("File renamed!")
