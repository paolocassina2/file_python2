import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, borderwidth=5, relief=tk.SUNKEN)
frame.pack()
entry = tk.Entry(frame, borderwidth=15, relief=tk.FLAT)
entry.pack()
root.mainloop()
def ciao():
	


	
	file1="C:\\Users\\Attilio\\Desktop\\60000_parole_italiane.txt"
	with open(file1) as f:
		contents = f.readlines()



	

	p="***l******"
	lista=[]
	indice=[]
	contatore=-1
	for xz in p:
		contatore+=1
		if xz!="*":
			
			lista.append(xz)   
			indice.append(contatore)
	print(lista)
	print(indice)



	# ~ def af():
	for x in contents:
		
			c=0
			parola=x.strip()
			if len(parola)==len(p):
			# ~ for zz in parola:
				for zz,jj in zip(indice,lista):
					if parola[zz]==jj:
						c=c+1
				if c==len(lista):
					print(parola)
				# ~ for jj in zz:
				# ~ if jj
		# ~ print(parola)
		# ~ print(len(parola))
		# ~ if len(parola)==5 and  parola[len(parola)-1]=="a" and parola[0]=="c":
			# ~ print(parola)
		# ~ if len(parola)==5 and  parola[0]=="v" and parola[len(parola)-1]=="a":
			# ~ print(parola)
	
		
ciao()
