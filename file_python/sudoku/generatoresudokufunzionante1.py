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
# ~ print(a1,"fd")p
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
def a():
	a.var=121
a()

def b():
	b.var=121
b()
def c():
	c.var=121
c()
def d():
	d.var=121
d()
def e():
	e.var=121
e()	
def f():
	f.var=121
f()
def g():
	g.var=121
g()
def h():
	hvar=121
h()
def k():
	k.var=121
k()


def r1():
	r1.var=121
r1()
def r2():
	r2.var=121
r2()
def r3():
	r3.var=121
r3()

def r4():
	r1.var=121
r1()
def r5():
	r2.var=121
r2()
def r6():
	r3.var=121
r3()

def definisci_rettangoli1_2_3():
	#rettangoli ab ,cd,fg
	# ~ sudoku.var = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])					
	# ~ print(sudoku)
	# ~ a.var=list(random.choice(listapermutazioni1))
	# ~ b.var=list(random.choice(listapermutazioni1))
	# ~ c.var=list(random.choice(listapermutazioni1))
	# ~ d.var=list("232")
	# ~ e.var=list("2323")
	# ~ f.var=list("23")
	
	# ~ sudoku.var = np.array([a.var,b.var])
	# ~ print(a)
	# ~ print(b)
	# ~ print(c)
	# ~ sudoku.var = np.array([a,b,c])
	# ~ caso.var=1
	# ~ a=[]
	r1_1=[]
	r2_2=[]
	r3_3=[]
	# ~ q4_4=[]
	# ~ q5_5=[]
	# ~ q6_6=[]
	# ~ q7_7=[]
	# ~ q8_8=[]
	# ~ q9_9=[]
	
	for i in range(9):
		# ~ print(sudoku[:,i][0:2],end="   ")
		if i<3:
			# ~ if caso.var==1:
			r1_1.append(list(sudoku.var[:,i][0:2]))	
			# ~ if caso.var==2:
				# ~ q4_4.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q7_7.append(list(sudoku.var[:,i][6:9]))
		elif 3<=i<6:
			# ~ if caso.var==1:
			r2_2.append(list(sudoku.var[:,i][0:2])	)
			# ~ if caso.var==2:

				# ~ q5_5.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q8_8.append(list(sudoku.var[:,i][6:9]))
		else:
			# ~ if caso.var==1:
			r3_3.append(list(sudoku.var[:,i][0:2])	)
			# ~ if caso.var==2:
				# ~ q6_6.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q9_9.append(list(sudoku.var[:,i][6:9]))
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
	# ~ print(q4_5)
	
	
	# ~ print("q4ddd",q4_4)
	# ~ print("q5ddd",q5_5)
	# ~ print("q6ddd",q6_6)
	# ~ if caso.var==1:
	r1.var=[]
	r2.var=[]
	r3.var=[]
	# ~ if caso.var==2:
	# ~ q4.var=[]	
	# ~ q5.var=[]
	# ~ q6.var=[]
	# ~ if caso.var==3:
		# ~ q7.var=[]
		# ~ q8.var=[]
		# ~ q9.var=[]
		
	
	# ~ if caso.var==1:				# ~ if conta==4:
	for a1,b1,c1 in zip(r1_1,r2_2,r3_3):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			for a2 in a1:
				r1.var.append(a2)
			for b2 in b1:
				r2.var.append(b2)
			for c2 in c1:
				r3.var.append(c2)
	# ~ print(r1.var)
	# ~ print(r2.var)
	# ~ print(r3.var)
# ~ definisci_rettangoli1_2_3()
def definisci_rettangoli4_5_6():
	#rettangoli ab ,de,gh
	# ~ sudoku.var = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])					
	# ~ print(sudoku)
	# ~ a.var=list(random.choice(listapermutazioni1))
	# ~ b.var=list(random.choice(listapermutazioni1))
	# ~ c.var=list(random.choice(listapermutazioni1))
	# ~ d.var=list("232")
	# ~ e.var=list("2323")
	# ~ f.var=list("23")
	
	# ~ sudoku.var = np.array([a.var,b.var])
	# ~ print(a)
	# ~ print(b)
	# ~ print(c)
	# ~ sudoku.var = np.array([a,b,c])
	# ~ caso.var=1
	# ~ a=[]
	r4_4=[]
	r5_5=[]
	r6_6=[]
	# ~ q4_4=[]
	# ~ q5_5=[]
	# ~ q6_6=[]
	# ~ q7_7=[]
	# ~ q8_8=[]
	# ~ q9_9=[]
	
	for i in range(9):
		# ~ print(sudoku[:,i][0:2],end="   ")
		if i<3:
			# ~ if caso.var==1:
			r4_4.append(list(sudoku.var[:,i][0:2]))	
			# ~ if caso.var==2:
				# ~ q4_4.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q7_7.append(list(sudoku.var[:,i][6:9]))
		elif 3<=i<6:
			# ~ if caso.var==1:
			r5_5.append(list(sudoku.var[:,i][0:2])	)
			# ~ if caso.var==2:

				# ~ q5_5.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q8_8.append(list(sudoku.var[:,i][6:9]))
		else:
			# ~ if caso.var==1:
			r6_6.append(list(sudoku.var[:,i][0:2])	)
			# ~ if caso.var==2:
				# ~ q6_6.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q9_9.append(list(sudoku.var[:,i][6:9]))
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
	# ~ print(q4_5)
	
	
	# ~ print("q4ddd",q4_4)
	# ~ print("q5ddd",q5_5)
	# ~ print("q6ddd",q6_6)
	# ~ if caso.var==1:
	r4.var=[]
	r5.var=[]
	r6.var=[]
	# ~ if caso.var==2:
	# ~ q4.var=[]	
	# ~ q5.var=[]
	# ~ q6.var=[]
	# ~ if caso.var==3:
		# ~ q7.var=[]
		# ~ q8.var=[]
		# ~ q9.var=[]
		
	
	# ~ if caso.var==1:				# ~ if conta==4:
	for a1,b1,c1 in zip(r4_4,r5_5,r6_6):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			for a2 in a1:
				r4.var.append(a2)
			for b2 in b1:
				r5.var.append(b2)
			for c2 in c1:
				r6.var.append(c2)
	# ~ print(r4.var)
	# ~ print(r5.var)
	# ~ print(r6.var)
# ~ definisci_rettangoli1_2_3()
			# ~ for d1 in d:
def definisci_quadrati1_2_3():
	# ~ sudoku.var = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])					
	# ~ print(sudoku)
	# ~ a.var=list(random.choice(listapermutazioni1))
	# ~ b.var=list(random.choice(listapermutazioni1))
	# ~ c.var=list(random.choice(listapermutazioni1))
	# ~ d.var=list("232")
	# ~ e.var=list("2323")
	# ~ f.var=list("23")
	
	sudoku.var = np.array([a.var,b.var,c.var])
	# ~ print(a)
	# ~ print(b)
	# ~ print(c)
	# ~ sudoku.var = np.array([a,b,c])
	# ~ caso.var=1
	# ~ a=[]
	q1_1=[]
	q2_2=[]
	q3_3=[]
	# ~ q4_4=[]
	# ~ q5_5=[]
	# ~ q6_6=[]
	# ~ q7_7=[]
	# ~ q8_8=[]
	# ~ q9_9=[]
	
	for i in range(9):
		# ~ print(sudoku[:,i][0:2],end="   ")
		if i<3:
			# ~ if caso.var==1:
			q1_1.append(list(sudoku.var[:,i][0:3]))	
			# ~ if caso.var==2:
				# ~ q4_4.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q7_7.append(list(sudoku.var[:,i][6:9]))
		elif 3<=i<6:
			# ~ if caso.var==1:
			q2_2.append(list(sudoku.var[:,i][0:3])	)
			# ~ if caso.var==2:

				# ~ q5_5.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q8_8.append(list(sudoku.var[:,i][6:9]))
		else:
			# ~ if caso.var==1:
			q3_3.append(list(sudoku.var[:,i][0:3])	)
			# ~ if caso.var==2:
				# ~ q6_6.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q9_9.append(list(sudoku.var[:,i][6:9]))
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
	# ~ print(q4_5)
	
	
	# ~ print("q4ddd",q4_4)
	# ~ print("q5ddd",q5_5)
	# ~ print("q6ddd",q6_6)
	# ~ if caso.var==1:
	q1.var=[]
	q2.var=[]
	q3.var=[]
	# ~ if caso.var==2:
	q4.var=[]	
	q5.var=[]
	q6.var=[]
	# ~ if caso.var==3:
		# ~ q7.var=[]
		# ~ q8.var=[]
		# ~ q9.var=[]
		
	
	# ~ if caso.var==1:				# ~ if conta==4:
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

	# ~ print(sudoku.var)
	# ~ print()
	
	# ~ print(q1.var)
	# ~ print(q2.var)
	# ~ print(q3.var)
	
# ~ definisci_quadrati1_2_3()	
	
	# ~ if caso.var==2:				# ~ if conta==4:
		# ~ for a1,b1,c1,d1,e1,f1 in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			# ~ for a1 in a:
				# ~ q1.var.append(a1)
			# ~ for b1 in b:
				# ~ q2.var.append(b1)
			# ~ for c1 in c:
				# ~ q3.var.append(c1)
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
	
	
	
	
	
	# ~ if caso.var==3:				# ~ if conta==4:
		# ~ for a1,b1,c1,d1,e1,f1,g1,h1,j1 in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			# ~ for a1 in a:
				# ~ q1.var.append(a1)
			# ~ for b1 in b:
				# ~ q2.var.append(b1)
			# ~ for c1 in c:
				# ~ q3.var.append(c1)
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
				
def definisci_quadrati4_5_6():
	# ~ sudoku.var = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])					
	# ~ print(sudoku)
	# ~ d.var=random.choice(listapermutazioni1)
	# ~ e.var=random.choice(listapermutazioni1)
	# ~ f.var=random.choice(listapermutazioni1)
	# ~ print(d.var)
	# ~ print(e.var)
	# ~ print(f.var)
	# ~ print(d)
	
	# ~ sudoku.var = np.array([a,b,c])
	# ~ caso.var=1
	# ~ a=[]
	# ~ sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var])
	q4_4=[]
	q5_5=[]
	q6_6=[]
	
	
	for i in range(9):
		# ~ print(sudoku[:,i][0:2],end="   ")
		if i<3:
			# ~ if caso.var==1:
			# ~ q1_1.append(list(sudoku.var[:,i][0:3]))	
			# ~ if caso.var==2:
			q4_4.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q7_7.append(list(sudoku.var[:,i][6:9]))
		elif 3<=i<6:
			# ~ if caso.var==1:
			# ~ q2_2.append(list(sudoku.var[:,i][0:3])	)
			# ~ if caso.var==2:

			q5_5.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q8_8.append(list(sudoku.var[:,i][6:9]))
		else:
			# ~ caso.var==1:
			# ~ q3_3.append(list(sudoku.var[:,i][0:3])	)
			# ~ if caso.var==2:
			q6_6.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q9_9.append(list(sudoku.var[:,i][6:9]))
	
	# ~ if caso.var==1:
	q4.var=[]
	q5.var=[]
	q6.var=[]

	# ~ print(q4_4)
	# ~ print(q5_5)
	# ~ print(q6_6)
	
	for a1,b1,c1 in zip(q4_4,q5_5,q6_6):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			for abc in a1:
				q4.var.append(abc)
			for abc1 in b1:
				q5.var.append(abc1)
			for abc2 in c1:
				q6.var.append(abc2)
				
def definisci_quadrati7_8_9():
	# ~ sudoku.var = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])					
	# ~ print(sudoku)
	# ~ d.var=random.choice(listapermutazioni1)
	# ~ e.var=random.choice(listapermutazioni1)
	# ~ f.var=random.choice(listapermutazioni1)
	# ~ print(d.var)
	# ~ print(e.var)
	# ~ print(f.var)
	# ~ print(d)
	
	# ~ sudoku.var = np.array([a,b,c])
	# ~ caso.var=1
	# ~ a=[]
	# ~ sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var])
	q7_7=[]
	q8_8=[]
	q9_9=[]
	
	
	for i in range(9):
		# ~ print(sudoku[:,i][0:2],end="   ")
		if i<3:
			# ~ if caso.var==1:
			# ~ q1_1.append(list(sudoku.var[:,i][0:3]))	
			# ~ if caso.var==2:
			q7_7.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
				# ~ q7_7.append(list(sudoku.var[:,i][6:9]))
		elif 3<=i<6:
			# ~ if caso.var==1:
			# ~ q2_2.append(list(sudoku.var[:,i][0:3])	)
			# ~ if caso.var==2:

			# ~ q5_5.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
			q8_8.append(list(sudoku.var[:,i][6:9]))
		else:
			# ~ caso.var==1:
			# ~ q3_3.append(list(sudoku.var[:,i][0:3])	)
			# ~ if caso.var==2:
			# ~ q6_6.append(list(sudoku.var[:,i][3:6]))
			# ~ if caso.var==3:
			q9_9.append(list(sudoku.var[:,i][6:9]))
	
	# ~ if caso.var==1:
	q7.var=[]
	q8.var=[]
	q9.var=[]

	# ~ print(q4_4)
	# ~ print(q5_5)
	# ~ print(q6_6)
	
	for a1,b1,c1 in zip(q7_7,q8_8,q9_9):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			for abc in a1:
				q4.var.append(abc)
			for abc1 in b1:
				q5.var.append(abc1)
			for abc2 in c1:
				q6.var.append(abc2)				
	# ~ print(q4.var)
	# ~ print(q5.var)
	# ~ print(q6.var)
	
# ~ definisci_quadrati4_5_6()
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
	
	
	
	
	
	# ~ if caso.var==3:				# ~ if conta==4:
		# ~ for a1,b1,c1,d1,e1,f1,g1,h1,j1 in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			
		# ~ for a,b,c,d,e,f,g,h,j in zip(q1_1,q2_2,q3_3,q4_4,q5_5,q6_6,q7_7,q8_8,q9_9):
			# ~ for a1 in a:
				# ~ q1.var.append(a1)
			# ~ for b1 in b:
				# ~ q2.var.append(b1)
			# ~ for c1 in c:
				# ~ q3.var.append(c1)
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
# ~ def ciao():
soluzione=""
import random
# ~ for ab in listapermutazioni1:
# ~ for a1 in reversed(listapermutazioni1):
	# ~ a.var=a1
	# ~ if soluzione=="ok":
		# ~ break
	# ~ print(a.var)
# ~ a=listapermutazioni1[129]
# ~ print(a)
# ~ while True:
contatore=0

while True:
		a.var=random.choice(listapermutazioni1)
		

		if soluzione=="ok":
				break
		
		
		
		b.var=random.choice(listapermutazioni1)# ~ c.var=random.choice(listapermutazioni1)
		sudoku.var = np.array([a.var,b.var])	
		rettangolo1=[a.var[0],b.var[0],a.var[1],b.var[1],a.var[2],b.var[2]]
		rettangolo2=[a.var[3],b.var[3],a.var[4],b.var[4],a.var[5],b.var[5]]
		rettangolo3=[a.var[6],b.var[6],a.var[7],b.var[7],a.var[8],b.var[8]]
		if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
			if len(set(rettangolo1))==len(rettangolo1) and len(set(rettangolo2))==len(rettangolo2) and len(set(rettangolo3))==len(rettangolo3):
			# ~ if len(set(r1.var))==len(r1.var) and len(set(r2.var))==len(r2.var) and len(set(r3.var))==len(r3.var):
				# ~ print(sudoku.var)
				# ~ break
			# ~ print()




# ~ def ciao():	
				for c1 in listapermutazioni1:
					c.var=c1
					if soluzione=="ok":
						break
					
									
					sudoku.var = np.array([a.var,b.var,c.var])
					definisci_quadrati1_2_3()
					if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
						if len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):	
	
							# ~ soluzione="ok"
							# ~ print(sudoku.var)
							# ~ break
							
							for d1 in listapermutazioni1:
								d.var=d1
								if soluzione=="ok":
									break
								
								sudoku.var = np.array([a.var,b.var,c.var,d.var])
								# ~ definisci_quadrati1_2_3()
								if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
									# ~ if len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):	
				
										# ~ soluzione="ok"
										# ~ print(sudoku.var)
										for e1 in listapermutazioni1:
											e.var=e1
											if soluzione=="ok":
												break
											rettangolo4=[d.var[0],e.var[0],d.var[1],e.var[1],d.var[2],e.var[2]]
											rettangolo5=[d.var[3],e.var[3],d.var[4],e.var[4],d.var[5],e.var[5]]
											rettangolo6=[d.var[6],e.var[6],d.var[7],e.var[7],d.var[8],e.var[8]]
											sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var])
											# ~ definisci_quadrati1_2_3()
											if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
												# ~ if len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):	
												if len(set(rettangolo4))==len(rettangolo4) and len(set(rettangolo5))==len(rettangolo5) and len(set(rettangolo6))==len(rettangolo6):
		
													# ~ soluzione="ok"
													# ~ print(sudoku.var)
										# ~ break
# ~ def ciao():e
	# ~ while True:							
													for f1 in listapermutazioni1:
														f.var=f1
														if soluzione=="ok":
															break
														# ~ rettangolo1=[d.var[0],e.var[0],d.var[1],e.var[1],d.var[2],e.var[2]]
														# ~ rettangolo2=[d.var[3],e.var[3],d.var[4],e.var[4],d.var[5],e.var[5]]
														# ~ rettangolo3=[d.var[6],e.var[6],d.var[7],e.var[7],d.var[8],e.var[8]]
														sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var])
														definisci_quadrati4_5_6()
														# ~ definisci_quadrati1_2_3()
														if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
															if len(set(q4.var))==len(q4.var) and len(set(q5.var))==len(q5.var) and len(set(q6.var))==len(q6.var):	
															# ~ if len(set(rettangolo1))==len(rettangolo1) and len(set(rettangolo2))==len(rettangolo2) and len(set(rettangolo3))==len(rettangolo3) :
																# ~ soluzione="ok"
																# ~ print(sudoku.var)
																# ~ break
																for g1 in listapermutazioni1:
																	g.var=g1
																	if soluzione=="ok":
																		break
																	# ~ rettangolo1=[d.var[0],e.var[0],d.var[1],e.var[1],d.var[2],e.var[2]]
																	# ~ rettangolo2=[d.var[3],e.var[3],d.var[4],e.var[4],d.var[5],e.var[5]]
																	# ~ rettangolo3=[d.var[6],e.var[6],d.var[7],e.var[7],d.var[8],e.var[8]]
																	sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var])
																	# ~ definisci_quadrati4_5_6()
																	# ~ definisci_quadrati1_2_3()
																	if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):			
																		# ~ soluzione="ok"
																		# ~ print(sudoku.var)
																		# ~ break
																		for h1 in listapermutazioni1:
																			h.var=h1
																			if soluzione=="ok":
																				break
																			rettangolo7=[g.var[0],h.var[0],g.var[1],h.var[1],g.var[2],h.var[2]]
																			rettangolo8=[g.var[3],h.var[3],g.var[4],h.var[4],g.var[5],h.var[5]]
																			rettangolo9=[g.var[6],h.var[6],g.var[7],h.var[7],g.var[8],h.var[8]]
																			sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var,h.var])
																			# ~ definisci_quadrati4_5_6()
																			# ~ definisci_quadrati1_2_3()
																			if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):			
																				if len(set(rettangolo7))==len(rettangolo7) and len(set(rettangolo8))==len(rettangolo8) and len(set(rettangolo9))==len(rettangolo9):

																					# ~ soluzione="ok"
																					# ~ print(sudoku.var)
																					# ~ break
																					if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):			
																		# ~ soluzione="ok"
																						# ~ print(sudoku.var)
																						# ~ break
																						for k1 in listapermutazioni1:
																							k.var=k1
																							if soluzione=="ok":
																								break
																							# ~ rettangolo7=[g.var[0],h.var[0],g.var[1],h.var[1],g.var[2],h.var[2]]
																							# ~ rettangolo8=[g.var[3],h.var[3],g.var[4],h.var[4],g.var[5],h.var[5]]
																							# ~ rettangolo9=[g.var[6],h.var[6],g.var[7],h.var[7],g.var[8],h.var[8]]
																							sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var,h.var,k.var])
																							definisci_quadrati7_8_9()
																							# ~ definisci_quadrati4_5_6()
																							# ~ definisci_quadrati1_2_3()
																							if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):			
																								# ~ if len(set(rettangolo7))==len(rettangolo7) and len(set(rettangolo8))==len(rettangolo8) and len(set(rettangolo9))==len(rettangolo9):
																									if len(set(q7.var))==len(q7.var) and len(set(q8.var))==len(q8.var) and len(set(q9.var))==len(q9.var):	
		
																										soluzione="ok"
																										print(sudoku.var)
																										break
									# ~ contatore=0									
						# ~ if c1[0]!=a.var[0]!=b.var[0] and c1[1]!=a.var[1]!=b.var[1]  and c1[2]!=a.var[2]!=b.var[2] and c1[3]!=a.var[3]!=b.var[3] and c1[4]!=a.var[4]!=b.var[4] and c1[5]!=a.var[5]!=b.var[5] and c1[6]!=a.var[6]!=b.var[6] and c1[7]!=a.var[7]!=b.var[7]and c1[8]!=a.var[8]!=b.var[8]:

					# ~ c.var=c1
					# ~ print(c.var)
					# ~ sudoku.var = np.array([a.var,b.var,c.var])
					# ~ definisci_quadrati1_2_3()
				# ~ print(sudoku.var)
				# ~ print()
				
					# ~ contatore=0
					# ~ if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])) and len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):	
						# ~ soluzione="ok"
						# ~ print(sudoku.var)
						# ~ break
# ~ def ciao():						
							# ~ for d1 in listapermutazioni1:
							# ~ if soluzione=="ok":
								# ~ break
							# ~ d.var=d1
						
							# ~ for i in range(len(d1)):
								# ~ colonna=[a.var[i],b.var[i],c.var[i],d.var[i]]
								# ~ print
								# ~ if contatore<=len(d1):
								# ~ if len(set(colonna))==len(colonna):	
										# ~ contatore=contatore+1
										# ~ if contatore==len(b.var):
										# ~ print(contatore)
											# ~ sudoku.var = np.array([a.var,b.var,c.var,d.var])
											# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

												# ~ print(sudoku.var)
										# ~ if contatore>=9:

											# ~ print(sudoku.var)
											# ~ break
										# ~ else:
											# ~ contatore=0
										
												# ~ soluzione="ok"
										# ~ print(sudoku.var)
												# ~ break
								# ~ else:
									# ~ contatore=0
	# ~ if soluzione=="ok":
		# ~ break
							# ~ d.var=d1
							
								# ~ if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
	
									# ~ sudoku.var = np.array([a.var,b.var,c.var,d.var])
									# ~ print(sudoku.var)
									# ~ soluzione="ok"
									# ~ break
	# ~ if soluzione=="ok":
		# ~ break
def ciao():
					for d1 in listapermutazioni1:
					
						if soluzione=="ok":
								break
						# ~ if d1[0]!=a.var[0]!=b.var[0]!=c.var[0]:
						# ~ d.var=random.choice(listapermutazioni1)
							# ~ print(d1)
						# ~ e.var=random.choice(listapermutazioni1)
						# ~ print("a",a)
						
							# ~ sudoku.var = np.array([a.var,b.var,c.var,d.var])
							# ~ print(sudoku.var)
						
def ciao():						# ~ print(sudoku.var)
							
								# ~ print(sudoku.var)
										# ~ break
							while True:
								if soluzione=="ok":
									break
	
								e.var=random.choice(listapermutazioni1)

						# ~ e.var=random.choice(listapermutazioni1)
						# ~ print("a",a)
				
								sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var])
								# ~ print(sudoku.var)
								if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):														
										print(sudoku.var)
										break
					# ~ while True:	
										# ~ for f1 in listapermutazioni1:
													# ~ if f1[0]!=a.var[0]!=b.var[0]!=c.var[0]!=d.var[0]!=e.var[0]:
														# ~ print(f1)
def ciao():
													# ~ if soluzione=="ok":
															# ~ break
											
													f.var=f1
											
													sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var])
														

													definisci_quadrati4_5_6()
													# ~ print()
													
													if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
														if len(set(q4.var))==len(q4.var) and len(set(q5.var))==len(q5.var) and len(set(q6.var))==len(q6.var):	
															# ~ soluzione="ok"
															print()
															print()
															print("soluzione prime 6 righe")
															print(sudoku.var)
															# ~ break	
														# ~ else:
										# ~ soluzione=""
						
															while True:
																		if soluzione=="ok":
																					break

															
																		g.var=random.choice(listapermutazioni1)
																	
																		sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var])
																				# ~ print(sudoku.var)



																					
																					
																					
																				# ~ print(sudoku.var)
																				# ~ print()

																		# ~ definisci_quadrati4_5_6()
																		# ~ print()
																		# ~ print(",q4",q4.var)
																		# ~ print()
																		# ~ print("q5",q5.var)
																		# ~ print("q6",q6.var)							
																		# ~ if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and 	len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and 	len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5]))and 	len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and 	len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
																		# ~ if len(set(q4.var))==len(q4.var) and len(set(q5.var))==len(q5.var) and len(set(q6.var))==len(q6.var):	
																		if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
																				# ~ print("7righe")
																				# ~ print(sudoku.var)
																				# ~ break
																				while True:
																							if soluzione=="ok":
																								break
																			
																							h.var=random.choice(listapermutazioni1)
																				
																							sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var,h.var])
																									# ~ print(sudoku.var)



																										
																										
																			
																							if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
																									# ~ print("8righe")
																									# ~ print(sudoku.var)
																									# ~ print()
																									# ~ break
																					
																									for k1 in listapermutazioni1:
																											if soluzione=="ok":
																												break
																								
																											k.var=k1
																									
																											sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var,h.var,k.var])
																													# ~ print(sudoku.var)



																														
																														
																														
																													# ~ print(sudoku.var)
																													# ~ print()

																											definisci_quadrati7_8_9()
																											# ~ print()
																											# ~ print(",q4",q4.var)
																											# ~ print()
																											# ~ print("q5",q5.var)
																											# ~ print("q6",q6.var)							
																											# ~ if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and 	len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and 	len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5]))and 	len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and 	len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
																											# ~ if len(set(q4.var))==len(q4.var) and len(set(q5.var))==len(q5.var) and len(set(q6.var))==len(q6.var):	
																											if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5])) and len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7]))and 	len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])):	
																												if len(set(q7.var))==len(q7.var) and len(set(q8.var))==len(q8.var) and len(set(q9.var))==len(q9.var):	
																													soluzione="ok"
																													print()
																													print()
																													print("soluzione prime 9righe")
																													print(sudoku.var)
																													break		
																							
							
	# ~ if soluzione=="ok":
		# ~ break				# ~ print()
					# ~ def ciao():
					# ~ while True:
								# ~ caso.var=1
								# ~ print(caso.var)
								# ~ a=random.choice(listapermutazioni1)
							# ~ b=random.choice(listapermutazioni1)
							# ~ c=random.choice(listapermutazioni1)
							# ~ for c in listapermutazioni1:
							# ~ d=random.choice(listapermutazioni1)
							# ~ e=random.choice(listapermutazioni1)
							# ~ f=random.choice(listapermutazioni1)
						
						# ~ g=random.choice(listapermutazioni1)
						# ~ h=random.choice(listapermutazioni1)
						# ~ k=random.choice(listapermutazioni1)
						# ~ for ab2 in listapermutazioni1:
						# ~ sudoku.var = np.array([a,b,c,])




							
							
							
						# ~ print(sudoku.var)
						# ~ print()

					# ~ definisci_quadrati()
					# ~ print()
					# ~ print(q1.var)
					# ~ print(q2.var)
					# ~ print(q3.var)									
					# ~ if len(set((sudoku.var[:,0]))) == len((sudoku.var[:,0]))  and len(set((sudoku.var[:,1]))) == len((sudoku.var[:,1])) and len(set((sudoku.var[:,2]))) == len((sudoku.var[:,2])) and 	len(set((sudoku.var[:,3]))) == len((sudoku.var[:,3])) and 	len(set((sudoku.var[:,4]))) == len((sudoku.var[:,4])) and 	len(set((sudoku.var[:,5]))) == len((sudoku.var[:,5]))and 	len(set((sudoku.var[:,6]))) == len((sudoku.var[:,6])) and 	len(set((sudoku.var[:,7]))) == len((sudoku.var[:,7])) and len(set((sudoku.var[:,8]))) == len((sudoku.var[:,8])) and len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):	
								# ~ print(sudoku.var)
								# ~ print()
								# ~ break					
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
