#perr creare sudoku generico
#parte mancante
#creo liste iniziali con valori noti e x
#faccio scorrere liste  ecreo liste valori e liste indici con la condizione diverso da x
#x sarebbero i valori ignoti
###########################
#altre modificje possibili: scanner sudoku
#											input numeri sudoku
lista1=[]
lista2=[]
a=[]
b=[]
p1=[]
a1=[]
import itertools
permutazioni=itertools.permutations([1,2,3,4,5,6,7,8,9])
for x in permutazioni:
	p1.append(list(x))
#print(p1)
import random
n1=n2=n3=0,0,0
while True:
	n1=random.randint(1,9)
	n2=random.randint(1,9)
	n3=random.randint(1,9)
	if n1!=n2 and n1!=n3 and n2!=n3:

		
		print(n1)
		print(n2)
		print(n3)
		break
if n1!=n2 and n1!=n3 and n2!=n3:

	for v in itertools.	combinations_with_replacement(["x","x","x","x","x","x",n1,n2,n3], 9):
			a1.append(v)

a=random.choice(a1)
#a=random.choice(randomS)
#print(a)
ciao=["x","x","x","x","x","x",n1,n2,n3]
for x in ciao:
	if x!="x":
		lista1.append(ciao.index(x))
		lista2.append(x)
#lista1=[0,2,3,5]#indici	
#lista2=[2,5,8,55]#valori
s1=[]
#listacom=[[2,5,1,4,9,7,8],[2,334,5,8,447,55,8],[2,4,5,8,66,55,8]]
print(lista1)
print(lista2)
conta=0
for yj in p1:
	#	print(xy)
		for x,j in zip(lista1, lista2):
		#	print(x)
			#print(j)
			
			if yj[x]==j:
				conta=conta+1
				#print("c",conta)
			#	
			#	print(yj[x])
				if conta==len(lista1):
					s1.append(yj)
		else:
			conta=0		
print(s1)
		
