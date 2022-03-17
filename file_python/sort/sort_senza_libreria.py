a="    dkjfkljfdk"
print(a.upper())
print(a.capitalize())
print(a.strip())
# ~ print("a"<"b")

# ~ print(max,min)
# ~ print(-444444444444444<min)
# ~ ll="f   f h  j s"
# ~ l=ll.strip()
# ~ l=["b"
l=[3,1,555,77,8,9]
def mass(l):
	l1=[]

	
	import math
	massimo=-math.inf
	minimo=math.inf


	massimo=0
	for i in range(len(l)):
		for y in l:
			# ~ for x in l:
				# ~ for t  in l:
			if 	y>massimo:
					massimo=y
		l1.append(massimo)
		l.remove(massimo)


		massimo=-math.inf
		minimo=math.inf
	return l1
	# ~ print(l1)
	# ~ return l
	# ~ print(l)
	# ~ print(l1)
# ~ l=[3,11,555344,77,8555,9]
# ~ print(mass())
print(mass(l))
l=[3,1,555,77,8,9]

def minimo(l):
	l1=[]

	
	import math
	
	massimo=-math.inf
	minimo=math.inf


	massimo=0
	for i in range(len(l)):
		for y in l:
			# ~ for x in l:
				# ~ for t  in l:
			if 	y>massimo:
					massimo=y
		l1.append(massimo)
		l.remove(massimo)


		massimo=-math.inf
		minimo=math.inf
	return l1[::-1]
print(minimo(l))
