b=[]
###CARTELLA==prova
def enum(b):
		# ~ b=[]
	length=int(input("insert len"))
	for x in range(length):	
		a=input("input")
		b.append(a)
	print(b)
	c=-1
	lista_c=[]

	# ~ for x in a:
	for y in b:
		c+=1
		
		lista_c.append(c)
	# ~ print(lista_c)
	return(dict(zip(lista_c,b)))
	# ~ print()
# ~ ab=zip(a,lista_c)
# ~ print(dict(ab))
# ~ print(dict(zip(a,leista_c)))
print(enum(b))


abc=["A","n","r"]
c=dict(enumerate(abc))
print(c)
