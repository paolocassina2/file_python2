

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
def caso():
	caso.var=""
caso()

q9.var=[]
def definisci_quadrati():
	# ~ sudoku.var = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])					
	# ~ print(sudoku)
	# ~ a=random.choice(listapermutazioni1)
	# ~ b=random.choice(listapermutazioni1)
	# ~ c=random.choice(listapermutazioni1)
	# ~ print(a)
	# ~ print(b)
	# ~ print(c)
	# ~ sudoku.var = np.array([a,b,c])
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
	# ~ print(q1_1)
	# ~ print(q2_2)
	# ~ print(q3_3)
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
	# ~ if caso.var==1:
	
	q1.var=[]
	q2.var=[]
	q3.var=[]
	# ~ if caso.var==2:
	q4.var=[]	
	q5.var=[]
	q6.var=[]
	# ~ if caso.var==3:
	q7.var=[]
	q8.var=[]
	
	if caso.var==1:				# ~ if conta==4:
		for a1,b1,c1 in zip(q1_1,q2_2,q3_3):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			for a2 in a1:
				q1.var.append(a2)
			for b2 in b1:
				q2.var.append(b2)
			for c2 in c1:
				q3.var.append(c2)
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
			# ~ for d1 in d:
				# ~ q4.var.append(d1)
			# ~ for e1 in e:
				# ~ q5.var.append(e1)
			# ~ for f1 in f:
				# ~ q6.var.append(f1)
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
	# ~ print("q1",q1.var)	
	# ~ print("q2",q2.var)
	# ~ print("q3",q3.var)
# ~ definisci_quadrati()
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
s1=[]
s2=[]
s3=[]
for x in listapermutazioni1:
	if x[0]==5:
		s1.append(x)
	if x[0]==6:
		s2.append(x)
	if x[0]==8:
		s3.append(x)
	
import random
# ~ for ab in listapermutazioni1:

# ~ a=listapermutazioni1[129]
# ~ print(a)
# ~ while True:
for a in s1:
# ~ a=random.choice(listapermutazioni1)
# ~ for a in listapermutazioni1:
	# ~ print(caso.var)
	# ~ a=random.choice(listapermutazioni1)
# ~ print("a",a)
	for b in s2:
		if soluz1=="ok2":
			break
		# ~ b=random.choice(listapermutazioni1)
			# ~ for c in listapermutazioni1:
		# ~ b=random.choice(listapermutazioni1)
				# ~ pass
			# ~ pass
		for c in s3:
			# ~ =random.choice(listapermutazioni1)
	# ~ for c in listapermutazioni1:
		# ~ d=random.choice(listapermutazioni1)
		# ~ e=random.choice(listapermutazioni1)
		# ~ f=random.choice(listapermutazioni1)
			# ~ for c in listapermutazioni1:
		# ~ g=random.choice(listapermutazioni1)
		# ~ h=random.choice(listapermutazioni1)
		# ~ k=random.choice(listapermutazioni1)
	# ~ for ab2 in listapermutazioni1:
				# ~ pass
			if soluz1=="ok2":
				break	
			
			sudoku.var = np.array([a,b,c])
			caso.var=1
			definisci_quadrati()
			# ~ print()
			# ~ print(sudoku.var)
					# ~ print()
			# ~ print(q1.var)
			# ~ print(q2.var)
			# ~ print(q3.var)


					
					
					
				# ~ print(sudoku.var)
				# ~ print()

					# ~ definisci_quadrati()
				# ~ print()
					# ~ print(q1.var)
					# ~ print()
					# ~ print(q2.var)
					# ~ print(q3.var)							
			# ~ if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and 	len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and 	len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5]))and 	len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and 	len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
					# ~ print(sudoku.var)
			# ~ for c in listapermutazioni1:
			
			if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])) and len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):	
				print(sudoku.var)
				soluz1="ok2"
				print()
				break

###CARTELLA==prova