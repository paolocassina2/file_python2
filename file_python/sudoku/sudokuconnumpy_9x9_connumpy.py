import numpy as np
print("generatore di sudoku 6*6")
#https://www.programiz.com/python-programming/matrix
from itertools import permutations
		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
a1 = list(permutations(range(1, 5)))
b1 = list(permutations(range(1, 5)))
c1 = list(permutations(range(1, 5)))
d1 = list(permutations(range(1, 5)))
e1 = list(permutations(range(1, 7)))
f1 = list(permutations(range(1, 7)))
# ~ print(a1,"fd")
from itertools import permutations
listapermutazioni1=[]		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
listapermutazioni = list(permutations(range(1, 5)))
for x in listapermutazioni:
	listapermutazioni1.append(list(x))
# ~ print(listapermutazioni1)
# ~ print(listapermutazioni)
# ~ print(a1)
print(listapermutazioni1)

soluz1="fdkj"


# ~ if soluz1!="ok":
# ~ conta=0
for ab in listapermutazioni1:
	conta=0
	if soluz1=="ok":
		break
	# ~ a1=listapermutazioni1[abc]
	for ab1 in listapermutazioni1:
		if soluz1=="ok":
			break
		for ab2 in listapermutazioni1:
			if soluz1=="ok":
				break
			for ab3 in listapermutazioni1:
				if soluz1=="ok":
					break
		# ~ b1=listapermutazioni1[ab1]
		# ~ for ab2 in listapermutazioni1:
			# ~ c1=listapermutazioni1[ab2]
		# ~ d1=listapermutazioni1[340]
		# ~ e1=listapermutazioni1[340]
		# ~ f1=listapermutazioni1[340]
				sudoku = np.array([ab, 
									ab1,ab2,ab3]
					
										)
				# ~ print(sudoku)
				# ~ print()
# ~ def difu():
				q1_1=[]
				q2_2=[]
				q3_3=[]
				q4_4=[]
				for i in range(4):
					# ~ print(sudoku[:,i][0:2],end="   ")
					if i<2:
						q1_1.append(list(sudoku[:,i][0:2]))	
						q3_3.append(list(sudoku[:,i][2:4]))
					else:
						q2_2.append(list(sudoku[:,i][0:2])	)
						q4_4.append(list(sudoku[:,i][2:4]))
				# ~ print("q1",q1)
				# ~ print("q2",q2)
				# ~ print("q3",q3)
				# ~ print("q4",q4)
				q1=[]
				q2=[]
				q3=[]
				q4=[]						# ~ if conta==4:
						
				for a,b,c,d in zip(q1_1,q2_2,q3_3,q4_4):
					for a1 in a:
						q1.append(a1)
					for b1 in b:
						q2.append(b1)
					for c1 in c:
						q3.append(c1)
					for d1 in d:
						q4.append(d1)
				# ~ print("q1",q1)	
				# ~ print("q2",q2)
				# ~ print("q3",q3)
				# ~ print("q4",q4)
				# ~ for i in range(len(ab3)):
					# ~ print(sudoku[:,[i]]	)
					# ~ if len(set((sudoku[:,i]))) == len((sudoku[:,i])):
				if len(set((sudoku[:,0]))) == len((sudoku[:,0]))  and len(set((sudoku[:,1]))) == len((sudoku[:,1])) and len(set((sudoku[:,2]))) == len((sudoku[:,2])) and 	len(set((sudoku[:,3]))) == len((sudoku[:,3])) and len(set(q1))==len(q1) and len(set(q2))==len(q2) and len(set(q3))==len(q3) and len(set(q4))==len(q4):
					 # ~ and len(set((sudoku[:,4]))) == len((sudoku[:,4])) and 	if len(set((sudoku[:,1]))) == len((sudoku[:,1])):

				# ~ conta=conta+1
					soluzione1=ab
					soluzione2=ab1
					soluzione3=ab2
					soluzione4=ab3
					# ~ print(sudoku)
					if conta==9:
						break
					soluz1="ok"
					# ~ print("conta",conta)
				# ~ break

				# ~ soluz1="ok"
							# ~ break
					# ~ print(conta)	
print(soluzione1,"iia")
print(soluzione2)
print(soluzione3)
print(soluzione4)
def ciao():					
	for ab2 in listapermutazioni1:
		
			# ~ b1=listapermutazioni1[ab1]
			# ~ for ab2 in listapermutazioni1:
				# ~ c1=listapermutazioni1[ab2]
			# ~ d1=listapermutazioni1[340]
			# ~ e1=listapermutazioni1[340]
			# ~ f1=listapermutazioni1[340]
			sudoku = np.array([soluzione1, 
								soluzione2,ab2]
				
									)
			conta=0
			for i in range(9):
				# ~ print(sudoku[:,[i]]	)
				if len(set((sudoku[:,i]))) == len((sudoku[:,i])):
					conta=conta+1
					
				# ~ print()
					if conta==9:
						soluz1="ok"
						break
	print(sudoku)
	print("conta",conta)
	# ~ A=[["a","b","c","d"],["e","F","g","h"],,["e","F","g","h"],,["e","F","g","h"]]
# ~ print("dkfkl",A[0][0],A[0][1])
#00	01	02	03 04 05
#10	11	12	13 14 15
#20 21	22	23 24 25
#30	31	32	33 34 35
#40 41 42   43 44 45	
#50  51 52 53  54 55
#

matrix=[]
matrix1=[]
n=0
def caio():
	for x in range(0,9):
		
		for j in range(0,9):
			n=n+1
			matrix.append(n)
		
		matrix1.append(matrix)
		matrix=[]	# ~ print(n,end="	")
		# ~ matrix=[]
			# ~ if n%9==0:
				# ~ print()
	for b in matrix1:
		for c in b:
			print(c,end="	")
	print()
		
# ~ print(listapermutazioni1)
# ~ print(matrix1)
# ~ print(matrix1)
		# ~ matrix.append(j)
	# ~ matrix1.append(matrix1)	
# ~ print(matrix1)
# ~ generatore di sudoku 6*6
# ~ 1  ,     2  ,     3    ,  4    ,   5       6       7       8       9
# ~ 10  ,    11  ,    12  ,    13  ,    14      15      16      17      18
# ~ 19  ,    20  ,    21    ,  22   ,   23      24      25      26      27
# ~ 28   ,   29  ,    30   ,   31   ,   32      33      34      35      36
# ~ 37  ,    38  ,    39  ,   40    ,  41      42      43      44      45
# ~ 46  ,    47  ,    48   ,   49   ,   50      51      52      53      54
# ~ 55   ,   56  ,    57   ,   58   ,   59      60      61      62      63
# ~ 64   ,   65  ,    66   ,   67   ,   68      69      70      71      72
# ~ 73  ,    74  ,    75   ,   76   ,   77      78      79      80      81

import numpy as np


# ~ arr3 = np.append(1,2)
# ~ print(arr3)

# ~ print(arr1)
# ~ print(arr_flat)  # [								
# ~ np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis=0)

# ~ q1=list(A[:,0][0:4])+list(A[:,1][0:4
# ~ ])+list(A[:,2][0:4])
# ~ q2=list(A[:,3][0:2])+list(A[:,4][0:2])+list(A[:,5][0:2])
# ~ print(
# ~ for x in range(1,10):
	# ~ for j in range(1,10):
		# ~ n=n+1
		# ~ print(n)
		# ~ matrix.append(n)
	# ~ matrix1.append(matrix)
		# ~ print()
	
# ~ print(matrix)
# ~ for j in matrix:
	# ~ print(j,end="	")
	# ~ if j%9==0:
		# ~ print()
# ~ for j in range(len(matrix)):
	# ~ print(matrix[j],end="	")
	# ~ if j!=1:
	# ~ if j==8:
		# ~ print()
	# ~ if j==17:
		# ~ print()
	# ~ if j==26:
		# ~ print()
	# ~ if j=0:
		# ~ print()
# ~ a1=[2,   11,   14,   20,    26    ,  32 ]
# ~ b1=[3,   12,   15,   21 ,    27    ,  33 ]
# ~ c1=[4   ,13,  16,   22   , 28    ,  34]
# ~ d1=[5,   14,  17,   23  ,   29   ,   35 ]
# ~ e1=[6,   15,  18,   24  ,   30    ,  36]
# ~ f1=[7,   16,  19,   25   ,  31   ,   37]
# ~ g1=[8,   17,  19,   25   ,  31   ,   37]
# ~ h1=[9,   17,  19,   25   ,  31   ,   37]
# ~ k1=[10,   13,  19,   25   ,  31   ,   37]
# ~ f1=[7,   13,  19,   25   ,  31   ,   37]
# ~ q1=[A[0][0],A[0][1],A[1][0],A[1][1]]

# ~ q2=[A[0][2],A[0][3],A[1][2],A[1][3]]

# ~ q3=[A[2][0],A[2][1],A[3][0],A[3][1]]

# ~ q4=[A[2][2],A[2][3],A[3][2],A[3][3]]
# ~ a1=[2,6,10,14]
# ~ b1=[3,7,11,15]
# ~ c1=[4,8,12,16]
# ~ d1=[5,9,13,17]
