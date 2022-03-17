#ORDINA LISTE MISTE




#nB CON DUE TUPLE UGUALI NE PRENDE SOLO UNA
import math
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
lista=[]
# ~ print(max(X[1]))
ciao=[3,2,1]
# ~ print(max(ciao))
l=[]

i=0
X=[("ugo",85),("aldo",25),("aldo",95),("paolo",65),("paolo",65),("lorenzo",65),("carlo",51),("aldo",95)]
def order_by_name():
	print("sort by name")
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
	print(lista1)
order_by_name()

X=[("ugo",85),("aldo",25),("aldo",95),("paolo",65),("paolo",65),("lorenzo",65),("carlo",51),("aldo",95)]
def order_by_age():
	print("sort by age")
	lista=[]
	lista1=[]
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
	print(lista1)
	# ~ X.pop(indice)
	# ~ print(X)
order_by_age()
		# ~ l.append(x[1])
	# ~ X.remove(x)
	# ~ lista.append(minimo)
	# ~ print(lista)
	# ~ X.remove(x)
	# ~ print(X)
		# ~ print(minimo)
		# ~ print(l)
	
		#

	# ~ print(x[1])
		# ~ lista.append(minimo)
		# ~ X.remove(x)
	# ~ print(X)

# ~ print(lista)	
	# ~ l=[x,y]
	# ~ lista.append(l)
	# ~ print(x,y)
# ~ print(lista)
# ~ for  x in X[1]:
	# ~ print(max(X[1]))
# ~ for j in range(len(X)):
# ~ for b in X[1]:
	# ~ print(max(X[1]))
		

			# ~ print(minimo)
# ~ print(lista)			
				
		# ~ lnum.var.append(y[1])
	# ~ X.remove(y)
# ~ print(lnum.var)					
	# ~ minimo=math.inf
				# ~ if len(X)>=1:		
				
	# ~ print(lnum.var)
# ~ print(lista)
					# ~ lnum1.var.append(minimo)
				# ~ X.remove(y)
			# ~ minimo=math.inf
	# ~ print(lnum.var)
					# ~ print(massimo)
		
		
def ciao():				
		lnum1.var.append(minimo)
		lnum.var.remove(minimo)
			# ~ l4.remove(massimo)	
		minimo=math.inf		
		# ~ print("lnum",lnum)
		# ~ print("lnum1",lnum1)
			# ~ else:
