# ~ a="    dkjfkljfdk"
# ~ print(a.upper())
# ~ print(a.capitalize())
# ~ print(a.strip())
# ~ print("a"<"b")
L=2
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
import math
massimo=-math.inf
def l2():
	l2.var=""
l2()
def l3():
	l3.var=[]
l3()

def s():
	s.var=""
s()

def lnum():
	lnum.var=[]
lnum()
def lstr():
	
	lstr.var=[]
lstr()


def lnum1():
	lnum1.var=[]
lnum1()
def lstr1():
	
	lstr1.var=[]
lstr1()
# ~ minimo=math.inf
def suddividi():
	l3.var=l2.var.split()
	print(l3.var)
	for x in l3.var:
		# ~ print(x)
		if x.isnumeric()==True:
			s.var=s.var+x+" "
			lnum.var.append(int(x))
			# ~ l3.remove(x)
		else:
			lstr.var.append(x)
# ~ print(lstr)
# ~ print(lnum)

# ~ for x in lnum:
	# ~ print(type(x))
# ~ print(lnum)
def ordinanumeri():
	import math
	# ~ import math

	# ~ massimo=0
	# ~ massimo=-math.inf
	minimo=math.inf
	# ~ for x in range(len(lnum)):
	for j in range(len(lnum.var)):
		if len(lnum.var)>=1:
			for y in lnum.var:	# ~ for x in l:
					# ~ for t  in l:
				if 	y<minimo:
					minimo=y
					# ~ print(massimo)
					
			lnum1.var.append(minimo)
			lnum.var.remove(minimo)
				# ~ l4.remove(massimo)	
			minimo=math.inf		
			# ~ print("lnum",lnum)
			# ~ print("lnum1",lnum1)
				# ~ else:
				# ~ continue
def ordina_stringhe():
	# ~ l8=[]
	
	for x in range(len(lstr.var)):
	
		import math
		# ~ massimo="a"
		minimo="z"
		for x in lstr.var:
			# ~ print(x)
			if x<minimo:
				minimo=x
		lstr1.var.append(minimo)
		lstr.var.remove(minimo)	
		# ~ massimo="a"
		minimo="z"
def inserisci():
	for x in range(6):
			L=input("inserisci_n	")
			l2.var=l2.var+L+" "
def ordina(L):
	inserisci()
	
	suddividi()
	ordinanumeri()
	ordina_stringhe()
	print()
	print()
	return "lista ordinata "+"\n"+str(lnum1.var+lstr1.var)
	# ~ return l8[::-1]
	# ~ return l1[::-1]
	# ~ print(ordina_numeri(l4)+sort_lista_stringhe_cresc(l3))

	# ~ print( l1 + l8)
print(ordina(L))
