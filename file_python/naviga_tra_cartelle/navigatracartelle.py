#naviga tra le cartelle senza comando cd: basta inserire il nome della cartella
import os
path=r'C:/Users/Attilio/'
# ~ print(os.listdir(path))
# ~ print(os.path.isdir(path))
# ~ print(path)
# ~ print()
# ~ print()
while True:
	# ~ print()
	# ~ print()
	# ~ try:
	print(os.listdir(path))
	# ~ print()
	inp =input("")
	path=path+inp+"/"
	print(path)
	print()
	print()
	# ~ except:
		# ~ path=r'C:/Users/Attilio/'
		# ~ path=path+inp+"/"
		# ~ inp =input("")
		# ~ continue
	# ~ print()

###CARTELLA==metti_ordine_cartelle