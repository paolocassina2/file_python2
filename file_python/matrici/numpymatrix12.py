import numpy as np

#https://www.programiz.com/python-programming/matrix
from itertools import permutations
		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
# ~ a1 = list(permutations(range(1, 7)))
# ~ b1 = list(permutations(range(1, 7)))
# ~ c1 = list(permutations(range(1, 7)))
# ~ d1 = list(permutations(range(1, 7)))
# ~ e1 = list(permutations(range(1, 7)))
# ~ f1 = list(permutations(range(1, 7)))

from itertools import permutations
		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
listapermutazioni = list(permutations(range(1, 5)))
# ~ print(a1)
soluz1="fdkj"
# ~ if soluz1!="ok":
for a in listapermutazioni:
	a1=list(a)
	if soluz1=="ok":
		break
	# ~ print(a1)
	for b in listapermutazioni:
		b1=list(b)
		# ~ print(b1)
		A = np.array([a1, 
						b1]
							)
		if soluz1=="ok":
			break
		if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]):
			# ~ soluz1="ok"
			for c in listapermutazioni:
				if soluz1=="ok":
					break
				c1=list(c)
				A = np.array([a1, 
						b1,c1]
							)
				# ~ print(A)
				if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]):
					# ~ print(A)
					for d in listapermutazioni:
						if soluz1=="ok":
							break
						d1=list(d)
						A = np.array([a1, 
						b1,c1,d1]
							)	
						if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]):
							print(A)
							soluz1="ok"
							break
					# ~ soluz1="ok"
					# ~ break
		
# ~ print("af",A[:,0])
	# ~ if len(set(a1[:,0]))==len(a1[:,0]) and  len(set(b1[:,0]))==len(b1[:,0]):
		# ~ print(A)
		# ~ break
	# ~ A = np.array([a1, 
					# ~ b1,
						# ~ c1,d1])

	# ~ for b in listapermutazioni:
		# ~ b1=list(b)
		# ~ print(b1)
def ciao():
		# ~ print(f1)
	a1=list(a)
	b1=list(b)
	c1=list(c)

	d1=list(d)
	import numpy as np
	# ~ a=[1, 4, 5, 12]
	# ~ b=  [-5, 8, 9, 0]
	# ~ c=[-6, 7, 11, 19]
	# ~ A = np.array(
	A = np.array([a1, 
					b1,
						c1,d1])

	print("A[:,0] =",a1[:,0]) 
	print("A[:,1] =",a1[:,1]) 
	print("A[:,2] =",a1[:,2]) 
	print("A[:,2] =", a1[:,3])

###CARTELLA==matrici