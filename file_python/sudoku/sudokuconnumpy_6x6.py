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
listapermutazioni = list(permutations(range(1, 7)))
# ~ print(listapermutazioni)
# ~ print(a1)
soluz1="fdkj"
# ~ if soluz1!="ok":

# ~ A=[["a","b","c","d"],["e","F","g","h"],,["e","F","g","h"],,["e","F","g","h"]]
# ~ print("dkfkl",A[0][0],A[0][1])
#00	01	02	03 04 05
#10	11	12	13 14 15
#20 21	22	23 24 25
#30	31	32	33 34 35
#40 41 42   43 44 45	
#50  51 52 53  54 55
#
a1=[2,   8,   14,   20,    26    ,  32 ]
b1=[3,   9,   15,   21 ,    27    ,  33 ]
c1=[4   ,10,  16,   22   , 28    ,  34]
d1=[5,   11,  17,   23  ,   29   ,   35 ]
e1=[6,   12,  18,   24  ,   30    ,  36]
f1=[7,   13,  19,   25   ,  31   ,   37]
# ~ q1=[A[0][0],A[0][1],A[1][0],A[1][1]]

# ~ q2=[A[0][2],A[0][3],A[1][2],A[1][3]]

# ~ q3=[A[2][0],A[2][1],A[3][0],A[3][1]]

# ~ q4=[A[2][2],A[2][3],A[3][2],A[3][3]]
# ~ a1=[2,6,10,14]
# ~ b1=[3,7,11,15]
# ~ c1=[4,8,12,16]
# ~ d1=[5,9,13,17]
A = np.array([a1, 
						b1,c1,d1,e1,f1]
								)
# ~ print(A[:,0][0:4])
q1=list(A[:,0][0:2])+list(A[:,1][0:2])+list(A[:,2][0:2])
q2=list(A[:,3][0:2])+list(A[:,4][0:2])+list(A[:,5][0:2])
q3=list(A[:,0][2:4])+list(A[:,1][2:4])+list(A[:,2][2:4])
q4=list(A[:,3][2:4])+list(A[:,4][2:4])+list(A[:,5][2:4])
q5=list(A[:,0][4:6])+list(A[:,1][4:6])+list(A[:,2][4:6])
q6=list(A[:,3][4:6])+list(A[:,4][4:6])+list(A[:,5][4:6])
# ~ q3=list(A[:,0][2:4])+list(A[:,1][2:4])
# ~ q4=list(A[:,2][2:4])+list(A[:,3][2:4])
# ~ print(type(q1))
# ~ print(q1)
# ~ print(q2)
# ~ print(q3)
# ~ print(q4)
# ~ print(q5)
print(q6)
# ~ print(type(list(A[:,0][0:2]))
# ~ q2=A[:,2][0:2]
# ~ q3=A[:,0][0:2]
# ~ q4=A[:,0][0:2]

# ~ b = a[:][0:2]

# ~ print(q1)
def ciao():
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
			q1=list(A[:,0][0:2])+list(A[:,1][0:2])
			q2=list(A[:,2][0:2])+list(A[:,3][0:2])
			# ~ q3=list(A[:,0][2:4])+list(A[:,1][2:4])
			# ~ q4=list(A[:,2][2:4])+list(A[:,3][2:4])
			# ~ q1=[A[0][0],A[0][1],A[1][0],A[1][1]]

			# ~ q2=[A[0][2],A[0][3],A[1][2],A[1][3]]

			# ~ q3=[A[2][0],A[2][1],A[3][0],A[3][1]]

			# ~ q4=[A[2][2],A[2][3],A[3][2],A[3][3]]
			if soluz1=="ok":
				break
			if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]) and len(set(q1))==len(q1) and len(set(q2))==len(q2):
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
							# ~ q1=[A[0][0],A[0][1],A[1][0],A[1][1]]

							# ~ q2=[A[0][2],A[0][3],A[1][2],A[1][3]]

							# ~ q3=[A[2][0],A[2][1],A[3][0],A[3][1]]

							# ~ q4=[A[2][2],A[2][3],A[3][2],A[3][3]]
							q1=list(A[:,0][0:2])+list(A[:,1][0:2])
							q2=list(A[:,2][0:2])+list(A[:,3][0:2])
							q3=list(A[:,0][2:4])+list(A[:,1][2:4])
							q4=list(A[:,2][2:4])+list(A[:,3][2:4])
							if soluz1=="ok":
								break
							d1=list(d)
							A = np.array([a1, 
							b1,c1,d1]
								)	
							if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]) and len(set(q1))==len(q1) and len(set(q2))==len(q2) and len(set(q3))==len(q3) and len(set(q4))==len(q4) :
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
