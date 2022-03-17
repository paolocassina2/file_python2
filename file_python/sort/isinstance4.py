#ORDINA LISTE MISTE





# ~ import math
def lnum1():
	lnum1.var=[]
lnum1()
def lnum():
	lnum.var=[]
lnum()
# ~ massimo=0
# ~ massimo=-math.inf
# ~ minimo=math.inf
# ~ for x in range(len(lnum)):
# ~ lista=[]
# ~ print(max(X[1]))
# ~ ciao=[3,2,1]
# ~ print(max(ciao))
# ~ l=[]

# ~ i=0
# ~ X=[("ugo",85),("aldo",25),("aldo",95),("paolo",65),("paolo",65),("lorenzo",65),("carlo",51),("aldo",95)]
# ~ X2=[]
def order_by_name(X1):
	# ~ X1=k
	X=X1
	# ~ X1=k
	# ~ print("j",j)
	# ~ print("sort by name")
	lista=[]
	lista1=[]
	
	for j in range(len(X)):
		l=[]
		# ~ if i<len(X):
			# ~ i=i+1
		for x in X:
			l.append(x[0])
		# ~ print(l)
		minimo="z"
		for j in l:
			if j<minimo:
				minimo=j
		# ~ print(l)
		# ~ minimo=min(l)
		# ~ print(minimo)
		lista.append(minimo)
		
		for x in X:
			
			# ~ print(X[1])
			if x[0]==minimo:
				indice=X.index(x)
				lista1.append((x))
				X.remove(x)
		# ~ print("indice",indice)
		# ~ X.pop(indice)
		# ~ print(X)
		# ~ print(X)
	
	return str(lista1)
	# ~ return(X1)
	
	# ~ return(X)
	# ~ X=lista1
	# ~ return(X)
	# ~ return "j"+str(j)
	# ~ j=X
	# ~ X=j
	# ~ print(X)
	# ~ return j
	# ~ print(lista1)
	# ~ print("X",X)
# ~ order_by_name()

x2=X1=2,3
def order_by_age(X2):
	print(X2)
	# ~ print("sort by age")
	lista=[]
	lista1=[]
	X=X2
	# ~ X=[("ugo",85),("aldo",25),("aldo",95),("paolo",65),("paolo",65),("lorenzo",65),("carlo",51),("aldo",95)]
	for j in range(len(X)):
		l=[]
		# ~ if i<len(X):
			# ~ i=i+1
		for x in X:
			l.append(x[1])
		# ~ print(l)
		# ~ print(l)
		if len(X)>0:
			minimo=min(l)
			# ~ print(minimo)
			lista.append(minimo)
			
			for x in X:
				
				# ~ print(X[1])
				if x[1]==minimo:
					indice=X.index(x)
					lista1.append((x))
					X.remove(x)
					
	# ~ print(lista1)
	return lista1
	# ~ print(lista1)
	# ~ print(X2)e
	# ~ return "l2"+str(lista2)
	# ~ return X2
	# ~ print(X)
	# ~ return "j" +str(j)
	# ~ X=
	# ~ X.pop(indice)
	# ~ print(X)
# ~ order_by_age()
# ~ x=None
j=2
# ~ X1=[("ugo",85),("aldo",25),("aldo",95),("paolo",65),("paolo",65),("lorenzo",65),("carlo",51),("aldo",95)]

j=[]
def sort(j):
	# ~ X1,x2=j,j
	X2=j
	# ~ print(X2)

	# ~ print(X1)
	# ~ x2=j
	
	# ~ X1=k
	# ~ print(
	# ~ X2=k
	# ~ print(order_by_age(X2))
	print("sort by age "+"\n",str(order_by_age(X2)))
	X1=j
	# ~ order_by_name(X1)
	print("\n"+"sort by name"+"\n"+str(order_by_name(X1)))
# ~ sort(j)	
print(str(sort([("ciao",23),("bene",33)])))

