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
# ~ l11="        b d y z g   " 
# ~ "Please split this string".split()
# ~ ciao1=["dfdf","n","b"]e
# ~ ciao=[2,1,11111,22,"dfdf","n","b"]
# ~ print("ciao	",sorted(ciao))	
# ~ a=[x for x in s2: int(x)]
# ~ print(a)
# ~ print(l2)
# ~ print(l2.strip())#rimuove gli spazi iniziali
# ~ print(l3)
#ordina una stringa o lista i cui eleemnti sono sia numeri che lettere : ordina prima i numeri e poi ordina le lettere
def ordina():
	l2="    1 3333  4      5 b d y z g  11111111   6   888    99 " 	
	# ~ l=l2.split()


	l3=l2.split()
	# ~ print("l3		",l3)
	lista=[]
	s=""
	for aaaa in range(len(l2)):
		for x in l3:
			# ~ print(x)
			if x.isnumeric()==True:
				s=s+x+" "
				l3.remove(x)
		
	# ~ print(s)
	s2=s.split()
	# ~ print("s2",s2)
			# ~ print(x)
			# ~ lista.append(int(x))
			# ~ l3.remove(x)
	# ~ print("ciao",lista)
	# ~ print(l3)
	l4=[]
	for x in s2:
		intero=int(x)
		l4.append(intero)
	print("l4",l4)	#numeri
	print("l3",l3)	#stringhe
	def sort_lista_stringhe_cresc(l3):
	
		l8=[]
		for x in range(len(l3)):
		
			import math
			massimo="a"
			minimo="z"
			for x in l3:
				# ~ print(x)
				if x>massimo:
					massimo=x
			l8.append(massimo)
			l3.remove(massimo)	
			massimo="a"
			minimo="z"
		return l8[::-1]
		# ~ print(l1)
		# ~ return l
		# ~ print(l)
		# ~ print(l1)
	# ~ l=[3,11,555344,77,8555,9]
	# ~ print(mass())
	# ~ sort_lista_stringhe_cresc(l3)


	def ordina_numeri(l4):
		l1=[]

		
		import math
		
		massimo=-math.inf
		minimo=math.inf


		# ~ massimo=0
		for i in range(len(l4)):
			for y in l4:
				# ~ for x in l:
					# ~ for t  in l:
				if 	y>massimo:
						massimo=y
			l1.append(massimo)
			l4.remove(massimo)


			massimo=-math.inf
			minimo=math.inf
		return l1[::-1]
	print(ordina_numeri(l4)+sort_lista_stringhe_cresc(l3))
	
	# ~ print( l1 + l8)
ordina()
