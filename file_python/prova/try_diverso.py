a=[2,2,2,1]

b=[5,23,1,2]
c=[43,24,3,3]
d=[21,25,3,4]
# ~ e=[5,2,3,4]

import numpy as np
from itertools import permutations


print("generatore di sudoku 9*9")
#https://www.programiz.com/python-programming/matrix
from itertools import permutations
		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
# ~ a1 = list(permutations(range(1, 5)))
# ~ b1 = list(permutations(range(1, 5)))
# ~ c1 = list(permutations(range(1, 5)))
# ~ d1 = list(permutations(range(1, 5)))
# ~ e1 = list(permutations(range(1, 7)))
# ~ f1 = list(permutations(range(1, 7)))
# ~ print(a1,"fd")
from itertools import permutations
listapermutazioni1=[]		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
listapermutazioni = list(permutations(range(1, 10)))
a=[1,2,3,4,5,6,7,8,9]
conta=0
soluzione="dkfjk"
for x in listapermutazioni:
	listapermutazioni1.append(list(x))
	b=x
	# ~ print(a)
	# ~ print(b)
	
	# ~ set(colonna)==len(colonna)
	if soluzione=="ok":
		break
	for i in range(len(b)):
		colonna=[a[i],b[i]]
		if len(set(colonna))==len(colonna):
			conta=conta+1
			if conta>=9:
				print(a)
				print(b)
				soluzione="ok"
				break
			# ~ print(colonna)
	# ~	 for i in range(len(x)):
		# ~ print(i)
	# ~ for x in range(len(colonna):
		# ~ for i in range(x):
				
			# ~ if len(set(colonna))==len(colonna):
				# ~ conta=conta+1
				# ~ if conta==9:
					# ~ print(a)
					# ~ print(b)
			
