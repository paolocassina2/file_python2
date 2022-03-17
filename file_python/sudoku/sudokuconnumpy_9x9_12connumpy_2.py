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
for x in listapermutazioni:
	listapermutazioni1.append(list(x))
# ~ print(listapermutazioni1)
# ~ print(listapermutazioni)
# ~ print(a1)
# ~ print(listapermutazioni1)

# ~ sudoku
soluz1="fdkj"
def q1():
	q1.var=""
q1()
def q2():
	q2.var=""
q2()

def q3():
	q3.var=""
q3()
def q4():
	q4.var=""
q4()
def q5():
	q5.var=""
q5()
def q6():
	q6.var=""
q6()
def q7():
	q7.var=""
q7()
def q8():
	q8.var=""
q8()
def q9():
	q9.var=""
q9()

def caso():
	caso.var=""
caso()
def sudoku():
	sudoku.var=[]
sudoku()
import random
import numpy as np
def definisci_quadrati():
	# ~ sudoku.var = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])					
	# ~ print(sudoku)
	a=random.choice(listapermutazioni1)
	b=random.choice(listapermutazioni1)
	c=random.choice(listapermutazioni1)
	sudoku.var = np.array([a,b,c])
	caso.var=1
	a=[]
	q1_1=[]
	q2_2=[]
	q3_3=[]
	q4_4=[]
	q5_5=[]
	q6_6=[]
	q7_7=[]
	q8_8=[]
	q9_9=[]
	
	for i in range(9):
		# ~ print(sudoku[:,i][0:2],end="   ")
		if i<3:
			if caso.var==1:
				q1_1.append(list(sudoku.var[:,i][0:3]))	
			if caso.var==2:
				q4_4.append(list(sudoku.var[:,i][3:6]))
			if caso.var==3:
				q7_7.append(list(sudoku.var[:,i][6:9]))
		elif 3<=i<6:
			if caso.var==1:
				q2_2.append(list(sudoku.var[:,i][0:3])	)
			if caso.var==2:

				q5_5.append(list(sudoku.var[:,i][3:6]))
			if caso.var==3:
				q8_8.append(list(sudoku.var[:,i][6:9]))
		else:
			if caso.var==1:
				q3_3.append(list(sudoku.var[:,i][0:3])	)
			if caso.var==2:
				q6_6.append(list(sudoku.var[:,i][3:6]))
			if caso.var==3:
				q9_9.append(list(sudoku.var[:,i][6:9]))
	print(q1_1)
	print(q2_2)
	print(q1_1)
# ~ print(q4_4)
# ~ print(q7_7)

# ~ print()
# ~ print()
# ~ print(q2_2)
# ~ print(q3_3)

# ~ print(q5_5)
# ~ print(q6_6)

# ~ print(q8_8)


# ~ print()
# ~ print()
# ~ print(q3_3)
# ~ print(q6_6)
# ~ print(q9_9)
	
	# ~ print("q4",q4)
	if caso.var==1:
		q1.var=[]
		q2.var=[]
		q3.var=[]
	if caso.var==2:
		q4.var=[]	
		q5.var=[]
		q6.var=[]
	if caso.var==3:
		q7.var=[]
		q8.var=[]
		q9.var=[]
	
	
	if caso.var==1:				# ~ if conta==4:
		for a1,b1,c1 in zip(q1_1,q2_2,q3_3):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			for a1 in a:
				q1.var.append(a1)
			for b1 in b:
				q2.var.append(b1)
			for c1 in c:
				q3.var.append(c1)
			# ~ for d1 in d:
				# ~ q4.var.append(d1)
			# ~ for e1 in e:
				# ~ q5.var.append(e1)
			# ~ for f1 in f:
				# ~ q6.var.append(f1)
	
	
	
	if caso.var==2:				# ~ if conta==4:
		for a1,b1,c1,d1,e1,f1 in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			for a1 in a:
				q1.var.append(a1)
			for b1 in b:
				q2.var.append(b1)
			for c1 in c:
				q3.var.append(c1)
			for d1 in d:
				q4.var.append(d1)
			for e1 in e:
				q5.var.append(e1)
			for f1 in f:
				q6.var.append(f1)
			# ~ for g1 in g:
				# ~ q7.var.append(g1)
			# ~ for h1 in h:
				# ~ q8.var.append(h1)
			# ~ for j1 in j:
				# ~ q9.var.append(j1)	
	
	
	
	
	
	if caso.var==3:				# ~ if conta==4:
		for a1,b1,c1,d1,e1,f1,g1,h1,j1 in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			for a1 in a:
				q1.var.append(a1)
			for b1 in b:
				q2.var.append(b1)
			for c1 in c:
				q3.var.append(c1)
			for d1 in d:
				q4.var.append(d1)
			for e1 in e:
				q5.var.append(e1)
			for f1 in f:
				q6.var.append(f1)
			for g1 in g:
				q7.var.append(g1)
			for h1 in h:
				q8.var.append(h1)
			for j1 in j:
				q9.var.append(j1)	
	print("q1",q1.var)	
	print("q2",q2.var)
	print("q3",q3.var)
definisci_quadrati()
	# ~ print("q4",q4.var)
	# ~ print("q5",q5.var)	
	# ~ print("q6",q6.var)
		
	# ~ print("q7",q7.var)
	# ~ print("q8",q8.var)
	# ~ print("q9",q9.var)
	# ~ print()
# ~ definisci_quadrati()
		# ~ print("q1",q9)	
	# ~ print("q2",q2)
	# ~ print("q3",q3)
	# ~ print("q4",q4)
# ~ definisci_quadrati()
	# ~ print(soluzione1,"iia")
	# ~ print(soluzione2)
	# ~ print(soluzione3)
	# ~ print(soluzione
# ~ def ciao():
# ~ if soluz1!="ok":
# ~ conta=0
# ~ def ciao():

import random
# ~ for ab in listapermutazioni1:

# ~ a=listapermutazioni1[129]
# ~ print(a)
def  caio():
	for b in listapermutazioni:
		caso.var=1
		# ~ print(caso.var)
		a=random.choice(listapermutazioni1)
		c=random.choice(listapermutazioni1)
	# ~ for c in listapermutazioni1:
		c=random.choice(listapermutazioni1)
	# ~ e=random.choice(listapermutazioni1)
	# ~ f=random.choice(listapermutazioni1)

	# ~ g=random.choice(listapermutazioni1)
	# ~ h=random.choice(listapermutazioni1)
	# ~ k=random.choice(listapermutazioni1)
	# ~ for ab2 in listapermutazioni1:
		sudoku.var = np.array([a,b,c])




			
			
			
		# ~ print(sudoku.var)
		# ~ print()

		definisci_quadrati()
		# ~ print()
		print(q1.var)
		print()
		# ~ print(q2.var)
		# ~ print(q3.var)							
		# ~ if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and 	len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and 	len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5]))and 	len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and 	len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
			
		# ~ if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])) and len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):	
				# ~ print(sudoku.var)
				# ~ print()
def ciao():				# ~ break	
	while True:
		caso.var=1
		# ~ print(caso.var)
		# ~ a=random.choice(listapermutazioni1)
		# ~ b=random.choice(listapermutazioni1)
		c=random.choice(listapermutazioni1)
		# ~ for c in listapermutazioni1:
		# ~ d=random.choice(listapermutazioni1)
		# ~ e=random.choice(listapermutazioni1)
		# ~ f=random.choice(listapermutazioni1)
		
		# ~ g=random.choice(listapermutazioni1)
		# ~ h=random.choice(listapermutazioni1)
		# ~ k=random.choice(listapermutazioni1)
		# ~ for ab2 in listapermutazioni1:
		sudoku.var = np.array([a,b,c,])




			
			
			
		# ~ print(sudoku.var)
		# ~ print()

		definisci_quadrati()
		# ~ print()
		# ~ print(q1.var)
		# ~ print(q2.var)
		# ~ print(q3.var)									
		if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and 	len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and 	len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5]))and 	len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and 	len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])) and len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):	
					print(sudoku.var)
					print()
					break					
	# ~ print(sudoku.var)
	# ~ def ciao():
		# ~ if soluz1!="ok":
		# ~ ab1=random.choice(listapermutazioni1)
	# ~ for ab1 in listapermutazioni1:
	# ~ if soluz1=="ok":
			# ~ break
		# ~ if soluz1!="ok":
	# ~ ab2=random.choice(listapermutazioni1)
# ~ for ab2 in listapermutazioni1:
		# ~ if soluz1=="ok":
			# ~ break
		# ~ for ab3 in listapermutazioni1:
			# ~ if soluz1=="ok":
				# ~ break
			# ~ for ab4 in listapermutazioni1:
				# ~ if soluz1=="ok":
					# ~ break
				# ~ for ab5 in listapermutazioni1:
					# ~ if soluz1=="ok":
						# ~ break
					# ~ for ab6 in listapermutazioni1:
						# ~ if soluz1=="ok":
							# ~ break
						# ~ for ab7 in listapermutazioni1:
							# ~ if soluz1=="ok":
								# ~ break
							# ~ for ab8 in listapermutazioni1:
								# ~ if soluz1=="ok":
									# ~ break
	# ~ b1=listapermutazioni1[ab1]
	# ~ for ab2 in listapermutazioni1:
		# ~ c1=listapermutazioni1[ab2]
	# ~ d1=listapermutazioni1[340]
	# ~ e1=listapermutazioni1[340]
	# ~ f1=listapermutazioni1[340]
			# ~ sudoku.var = np.array([ab, 
										# ~ ab1]
						
											# ~ )
			# ~ print(sudoku.var)
				
			# ~ print()
			# ~ definisci_quadrati()
							# ~ print()
			# ~ def difu():	print(
							# ~ definisci_quadrati()						# ~ if conta==4:
			# ~ print(sudoeku.var)						
							
			# ~ print("q1.var",q1.var)	
			# ~ print("q2.var",q2.var)
			# ~ print("q3.var",q3.var)
			# ~ print()
			# ~ print()
							# ~ print("q4",q4)
							# ~ for i in range(len(ab3)):
								# ~ print(sudoku[:,[i]]	)
								# ~ if len(set((sudoku[:,i]))) == len((sudoku[:,i])):
			# ~ if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and 	len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and 	len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5]))and 	len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and 	len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])) and
			# ~ if len(set(q1.var))==len(q1.var): 
			# ~ a
			# ~ nd len(set(q3.var))==len(q3.var):
			 # ~ and len(set(q4))==len(q4)  and len(set(q5))==len(q5)  and len(set(q6))==len(q6):
					# ~ soluz1="ok"
					# ~ print(sudoku.var)
					# ~ break
			# ~ if len(set((sudoku[:,0]))) == len((sudoku[:,0]))  and len(set((sudoku[:,1]))) == len((sudoku[:,1])) and len(set((sudoku[:,2]))) == len((sudoku[:,2])) and 	len(set((sudoku[:,3]))) == len((sudoku[:,3])) and 	len(set((sudoku[:,4]))) == len((sudoku[:,4])) and 	len(set((sudoku[:,5]))) == len((sudoku[:,5]))and 	len(set((sudoku[:,6]))) == len((sudoku[:,6])) and 	len(set((sudoku[:,7]))) == len((sudoku[:,7]))and 	len(set((sudoku[:,8]))) == len((sudoku[:,8])) and  len(set(q1))==len(q1) and len(set(q2))==len(q2) and len(set(q3))==len(q3) and len(set(q4))==len(q4)  and len(set(q5))==len(q5)  and len(set(q6))==len(q6):
								 # ~ and len(set((sudoku[:,4]))) == len((sudoku[:,4])) and 	if len(set((sudoku[:,1]))) == len((sudoku[:,1])):
			# ~ soluz1="ok"
		#		break
	# ~ if soluz1=="ok":
	# ~ #
		# ~ print(sudoku.var)
		# ~ break								# ~ conta=conta+1
										# ~ soluzione1=ab
											# ~ soluzione2=ab1
												# ~ soluzione3=ab2
												# ~ soluzione4=ab3
							# ~ print(sudoku)
												# ~ if conta==9:
													# ~ break
def ciao():												# ~ soluz1="ok"
						# ~ print("conta",conta)					# ~ p
				# ~ break

						# ~ soluz1="ok"
									# ~ break
							# ~ print(conta)	
	# ~ [1,2,3,4,5,6,7,8,9]
	# ~ 4)
				
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
				# ~ if len(set((sudoku[:,i]))) == len((sudoku[:,i])):
					# ~ conta=conta+1
					
				# ~ print()
					if conta==9:
						soluz1="ok"
						break
	# ~ print(sudoku)
	# ~ print("conta",conta)
	# ~ A=[["a","b","c","d"],["e","F","g","h"],,["e","F","g","h"],,["e","F","g","h"]]
		# ~ print("dkfkl",A[0][0],A[0][1])
		#00	01	02	03 04 05
		#10	11	12	13 14 15
	#20 21	22	23 24 25
	#30	31	32	33 34 35
	#40 41 42   43 44 45	
	#50  51 52 53  54 55
	#

	# ~ matrix=[]
	# ~ matrix1=[]
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
