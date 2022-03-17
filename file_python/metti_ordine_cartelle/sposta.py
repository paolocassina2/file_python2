import os 
  
# importing shutil module 
import shutil 
def ciao(): 
	# Source path 
	pathfile="C:/Users/Attilio/Desktop/file_python/timer.pwy"
	  
	# Destination path 
	pathdestination="C:/Users/Attilio/Desktop/file_python/timer/timer.pwy"
	# Move the content of 
	# source to destination 
	dest = shutil.move(pathfile, pathdestination) 
	  
	# List files and directories 
	# in "C:/Users / Rajnish / Desktop / GeeksforGeeks" 
	# ~ print("After moving file:") 
	# ~ print(os.listdir(pathfile)) 
	  
	# Print path of newly 
	# created file 
	print("Destination path:",pathdestination) 		

pathfile="C:/Users/Attilio/Desktop/file_python/"

# ~ pathfile1="C:/Users/Attilio/Desktop/file_python/"	
with open(pathfile) as f:
					
		lines = f.readlines()			
		# ~ print(lines)
		for y in lines:
			if "#CARTELLA" in y:
				z=y.replace('CARTELLA==', '')
				for jj in z:
					if jj=="#":
						j=z.replace(jj, '')
				# ~ j=z.split()
				# ~ print(y.replace('CARTELLA==', ''))
				NOMECARTELLA=j.strip()
				print(len(NOMECARTELLA),"LEN")
				print(NOMECARTELLA)
				pathfile1="C:/Users/Attilio/Desktop/file_python/"+NOMECARTELLA+"/timer_minuti_secondi2.pyw"
				print(pathfile1)


def ciao():
	import glob
	import os
	import shutil

	src_folder = r"E:\pynative\reports"
	dst_folder = r"E:\pynative\account\\"

	# move file whose name starts with string 'emp'
	pattern = src_folder + "\emp*"
	for file in glob.iglob(pattern, recursive=True):
		# extract file name form file path
		file_name = os.path.basename(file)
		shutil.move(file, dst_folder + file_name)
		print('Moved:', file)
import os	
		
get_files = os.listdir(patfhile)

