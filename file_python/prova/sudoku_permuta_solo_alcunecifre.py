###CARTELLA==prova
from itertools import permutations
###CARTELLA==prova
# Get all permutations of length 2
# and length 2
import itertools

#if a[0]==5 and a [3]==7:
diz={0:5,3:7}#chiavi, indici, valori sono le cifre

# ~ vowel.insert(3, 'o')
lista=[1,2,3,4,5,6,7,8,9]
for y in diz.values():
	# ~ if y in lista:
		lista.remove(y)		#se ci sono giä delle cifre iniziali, invece che permutare 9 cifre, permuto un numero di cifre pari a  9-n cifre iniziali
print(lista)

# ~ lista.insert(0,5)
# ~ print(lista)
# ~ lista1=[]
# ~ def ciao():
for  a in itertools.permutations(lista):
		ab=list(a)
		for j,z in zip(diz.keys(),diz.values()):
			# ~ lista.insert(j,z)

			ab.insert(j,z)
			# ~ list(a).insert(j,z)
		a=ab
		print(a)
		# ~ print(ab)
		# ~ print(lista)
# ~ while True:
# ~ if a[2]==5 and a [7]==3:
# ~ if a[2]==5 and a [7]==3:
# ~ def ciao():
	# ~ for  a in itertools.permutations([1,2,3,4,5,6,7,8,9]):
		
			# ~ print(a)
	# ~ def ciao():
			for b in itertools.permutations([1,2,3,4,5,6,7,8,9]):
				if b[2]==1 and b [3]==5 and b[6]==6:
					s1=list(set([a[0],b[0]]))
					s2=list(set([a[1],b[1]]))
