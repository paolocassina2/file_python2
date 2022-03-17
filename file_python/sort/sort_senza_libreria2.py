# ~ a="    dkjfkljfdk"
# ~ print(a.upper())
# ~ print(a.capitalize())
# ~ print(a.strip())
# ~ print("a"<"b")

# ~ print(max,min)
# ~ print(-444444444444444<min)
# ~ ll="f   f h  j s"
# ~ l=ll.strip()
# ~ l=["b"
l11="        b d y z g   " 
# ~ "Please split this string".split()
l2="     1  4    " 	
# ~ print(l2)
# ~ print(l2.strip())#rimuove gli spazi iniziali
l=l2.split()
# ~ print(l3)
def sort_lista_stringhe_decresc(l):
	
	l1=[]
	for x in range(len(l)):
	
		import math
		massimo="a"
		minimo="z"
		for x in l:
			# ~ print(x)
			if x>massimo:
				massimo=x
		l1.append(massimo)
		l.remove(massimo)	
		massimo="a"
		minimo="z"
	return l1
	# ~ print(l1)
	# ~ return l
	# ~ print(l)
	# ~ print(l1)
# ~ l=[3,11,555344,77,8555,9]
# ~ print(mass())
# ~ l=l2.split()
print( sort_lista_stringhe_decresc(l))

l4=l11.split()

def sort_lista_stringhe_cresc(l4):
	
	l8=[]
	for x in range(len(l4)):
	
		import math
		massimo="a"
		minimo="z"
		for x in l4:
			# ~ print(x)
			if x>massimo:
				massimo=x
		l8.append(massimo)
		l4.remove(massimo)	
		massimo="a"
		minimo="z"
	return l8[::-1]
	# ~ print(l1)
	# ~ return l
	# ~ print(l)
	# ~ print(l1)
# ~ l=[3,11,555344,77,8555,9]
# ~ print(mass())
# ~ print( sort_lista_stringhe_cresc(l4))	
lista=[3,1,555,77,8,9]

def minimo(lista):
	l1=[]

	
	import math
	
	massimo=-math.inf
	minimo=math.inf


	# ~ massimo=0
	for i in range(len(lista)):
		for y in lista:
			# ~ for x in l:
				# ~ for t  in l:
			if 	y>massimo:
					massimo=y
		l1.append(massimo)
		lista.remove(massimo)


		massimo=-math.inf
		minimo=math.inf
	return l1[::-1]
# ~ print(minimo(lista))
