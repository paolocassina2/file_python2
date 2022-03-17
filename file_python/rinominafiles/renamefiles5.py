import os
#rinomina un singolo file 
from os import listdir
from os.path import isfile, join
path="C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# ~ newfile_name=""
# ~ print(onlyfiles)
for x in onlyfiles:
	if "ciao" in x:
		print(x)
		new_file_name="hello"+"txt"
		os.rename(path+"\\"+str(x), path+"\\"+str(new_file_name))
