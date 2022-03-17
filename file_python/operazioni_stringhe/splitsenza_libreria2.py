a="ab   cd               ef"#esegue split se sono parole della stessa lunghezza
lista=[]
def split_stessa_lunghezza():
	for x,y in zip(range(0,len(a)-1),range(2,len(a)+1)):
			# ~ print(a)
			# ~ print(x,y)
			# ~ if a[x]!=" " and a[y]!=" ":
			if " " not in a[x:y]:
				lista.append(a[x:y])
				# ~ print(a[x:y])
	print(lista)


# ~ split_stessa_lunghezza()
s=""
for yy in range(len(a)):
	for j in range(len(a)):
		if a[xx]==" ":
			s=s+a[yy]
		# ~ print(j)
		# ~ if a[yy]!=" " and a[j]!=" ":
			# ~ if " " not in a[j:yy]:
		print(a[j:yy])
			
###CARTELLA==operazioni_stringhe