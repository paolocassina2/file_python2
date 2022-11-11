
file1="C:\\Users\\Attilio\\Desktop\\60000_parole_italiane.txt"
with open(file1) as f:
    contents = f.readlines()
    
for x in contents:
	parola=x.strip()
	
	# ~ print(parola)
	# ~ print(len(parola))
	# ~ if len(parola)==5 and  parola[len(parola)-1]=="a" and parola[0]=="c":
		# ~ print(parola)
	if len(parola)==5 and  parola[0]=="v" and parola[len(parola)-1]=="a":
		print(parola)
