import numpy as np
from itertools import permutations
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
def definisci_quadrati1_2_3():
	
	
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
						
contatore1=0
contatore2=0
contatore3=0
contatore4=0
contatore5=0
contatore6=0
contatore7=0
contatore8=0
contatore9=0

soluz="dfjk"
import random
# ~ for a1 in listapermutazioni1:
a.var=random.choice(listapermutazioni1)
	# ~ a.var=a1
	# ~ for a1 in listapermutazioni1:
		# ~ if soluz=="ok":
			# ~ break
for b1 in listapermutazioni1:
			if soluz=="ok":
				break
			# ~ for c1 in listapermutazioni1:
				# ~ if soluz=="ok":
					# ~ break					# ~ if soluzione=="ok":
									# ~ break
								
			# ~ a.var=a1
			b.var=b1
			# ~ c.var=c1
			sudoku.var = np.array([a.var,b.var])
			rettangolo1=[a.var[0],b.var[0],a.var[1],b.var[1],a.var[2],b.var[2]]
			rettangolo2=[a.var[3],b.var[3],a.var[4],b.var[4],a.var[5],b.var[5]]
			rettangolo3=[a.var[6],b.var[6],a.var[7],b.var[7],a.var[8],b.var[8]]
			# ~ print(d.var)
			for i in range(len(a.var)):
				if soluz=="ok":
					break	
				colonna1=[a.var[i],b.var[i]]
				# ~ print(d.var[i])
								
									# ~ if contatore<=len(d1):
				if len(set(colonna1))==len(colonna1):	
					contatore1=contatore1+1
					if contatore1>=9 and len(set(rettangolo1))==len(rettangolo1) and len(set(rettangolo2))==len(rettangolo2) and len(set(rettangolo3))==len(rettangolo3):
						# ~ if len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):

							# ~ print(sudoku.var)
											# ~ if contatore==len(b.var):
							soluz="ok"			# ~ print(contatore)
					
												# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

													# ~ print(sudoku.var)
					
											# ~ else:
												# ~ contatore=0
											
													# ~ soluzione="ok"
											# ~ print(sudoku.var)
						
			else:
					contatore1=0
soluz="kjk"
for c1 in listapermutazioni1:
	# ~ print("cioa")
	if soluz=="ok":
		break
	# ~ for b1 in listapermutazioni1:
		# ~ if soluz=="ok":
			# ~ break
		# ~ for c1 in listapermutazioni1:
			# ~ if soluz=="ok":
				# ~ break					# ~ if soluzione=="ok":
	if c1[0]!=a.var and c1[0]!=b.var:						# ~ break
							
		# ~ a.var=a1
		c.var=c1
		# ~ c.var=c1
		sudoku.var = np.array([a.var,b.var,c.var])
		# ~ print(sudoku.var)
		# ~ rettangolo1=[a.var[0],b.var[0],a.var[1],b.var[1],a.var[2],b.var[2]]
		# ~ rettangolo2=[a.var[3],b.var[3],a.var[4],b.var[4],a.var[5],b.var[5]]
		# ~ rettangolo3=[a.var[6],b.var[6],a.var[7],b.var[7],a.var[8],b.var[8]]
		definisci_quadrati1_2_3()
		# ~ print(q1.var)

		# ~ print(d.var)
		for i in range(len(a.var)):
			if soluz=="ok":
				break	
			colonna2=[a.var[i],b.var[i],c.var[i]]
			# ~ print(d.var[i])
							
								# ~ if contatore<=len(d1):
			if len(set(colonna2))==len(colonna2):	
				contatore2=contatore2+1
				# ~ print(contatore2)
				if contatore2>=9:
					if len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):

						# ~ print(sudoku.var)
										# ~ if contatore==len(b.var):
						soluz="ok"			# ~ print(contatore)
				
											# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

												# ~ print(sudoku.var)
				
										# ~ else:
											# ~ contatore=0
										
												# ~ soluzione="ok"
										# ~ print(sudoku.var)
					
		else:
				contatore2=0
soluz="dffdfg"		
for d1 in listapermutazioni1:
	# ~ print("cioa")
	if soluz=="ok":
		break
	# ~ for b1 in listapermutazioni1:
		# ~ if soluz=="ok":
			# ~ break
		# ~ for c1 in listapermutazioni1:
			# ~ if soluz=="ok":
				# ~ break					# ~ if soluzione=="ok":
								# ~ break
							
		# ~ a.var=a1
	d.var=d1
	# ~ c.var=c1
	sudoku.var = np.array([a.var,b.var,c.var,d.var])
	# ~ print(sudoku.var)
	# ~ print(sudoku.var)
	# ~ rettangolo1=[a.var[0],b.var[0],a.var[1],b.var[1],a.var[2],b.var[2]]
	# ~ rettangolo2=[a.var[3],b.var[3],a.var[4],b.var[4],a.var[5],b.var[5]]
	# ~ rettangolo3=[a.var[6],b.var[6],a.var[7],b.var[7],a.var[8],b.var[8]]
	# ~ definisci_quadrati4_5_6()
	# ~ print(q1.var)
# ~ def ciao():
	# ~ print(d.var)
	for j in range(len(a.var)):
		if soluz=="ok":
			break	
		colonna3=[a.var[j],b.var[j],c.var[j],d.var[j]]
		# ~ print(d.var[i])
						
							# ~ if contatore<=len(d1):
		if len(set(colonna3))==len(colonna3):	
			contatore3=contatore3+1
			# ~ print(contatore2)
			if contatore3>=9:
				# ~ if len(set(q4.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):

					# ~ print(sudoku.var)
									# ~ if contatore==len(b.var):
					soluz="ok"			# ~ print(contatore)
			
										# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

											# ~ print(sudoku.var)
			
									# ~ else:
										# ~ contatore=0
									
											# ~ soluzione="ok"
									# ~ print(sudoku.var)
				
	else:
			contatore3=0
soluz="dffdfg"	
for e1 in listapermutazioni1:
	# ~ print("cioa")
	if soluz=="ok":
		break
	# ~ for b1 in listapermutazioni1:
		# ~ if soluz=="ok":
			# ~ break
		# ~ for c1 in listapermutazioni1:
			# ~ if soluz=="ok":
				# ~ break					# ~ if soluzione=="ok":
								# ~ break
							
		# ~ a.var=a1
	e.var=e1
	# ~ c.var=c1
	sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var])
	# ~ print(sudoku.var)
	# ~ print(sudoku.var)
	# ~ rettangolo1=[a.var[0],b.var[0],a.var[1],b.var[1],a.var[2],b.var[2]]
	# ~ rettangolo2=[a.var[3],b.var[3],a.var[4],b.var[4],a.var[5],b.var[5]]
	# ~ rettangolo3=[a.var[6],b.var[6],a.var[7],b.var[7],a.var[8],b.var[8]]
	# ~ definisci_quadrati4_5_6()
	# ~ print(q1.var)
# ~ def ciao():
	# ~ print(d.var)
	for j1 in range(len(a.var)):
		if soluz=="ok":
			break	
		colonna4=[a.var[j1],b.var[j1],c.var[j1],d.var[j1],e.var[j1]]
		# ~ print(d.var[i])
		rettangolo4=[d.var[0],e.var[0],d.var[1],e.var[1],d.var[2],e.var[2]]
		rettangolo5=[d.var[3],e.var[3],d.var[4],e.var[4],d.var[5],e.var[5]]
		rettangolo6=[d.var[6],e.var[6],d.var[7],e.var[7],d.var[8],e.var[8]]				
							# ~ if contatore<=len(d1):
		if len(set(colonna4))==len(colonna4):	
			contatore4=contatore4+1
			# ~ print(contatore2)
			if contatore4>=9:
				if len(set(rettangolo4))==len(rettangolo4) and len(set(rettangolo5))==len(rettangolo5) and len(set(rettangolo6))==len(rettangolo6):

				# ~ if len(set(q4.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):

					print(sudoku.var)
					# ~ print(sudoku.var)
									# ~ if contatore==len(b.var):
					soluz="ok"			# ~ print(contatore)
			
										# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

											# ~ print(sudoku.var)
			
									# ~ else:
										# ~ contatore=0
									
											# ~ soluzione="ok"
									# ~ print(sudoku.var)
				
	else:
			contatore4=0

soluz="dffdfg"	
for f1 in listapermutazioni1:
	# ~ print("cioa")
	if soluz=="ok":
		break
	# ~ for b1 in listapermutazioni1:
		# ~ if soluz=="ok":
			# ~ break
		# ~ for c1 in listapermutazioni1:
			# ~ if soluz=="ok":
				# ~ break	
								# ~ if soluzione=="ok":
	# ~ f_1=f1							# ~ break
	if f1[0]!=a.var and f1[0]!=b.var[0] and f1[0]!=c.var[0] and f1[0]!=d.var[0] and f1[0]!=e.var[0] and  f1[1]!=a.var[1] and f1[1]!=b.var[1] and f1[1]!=c.var[1] and f1[1]!=d.var[1]and f1[1]!=e.var[1] and f1[2]!=a.var[2] and f1[2]!=b.var[2] and f1[2]!=c.var[2] and f1[2]!=d.var[2] and f1[2]!=e.var[2] and f1[3]!=a.var[3] and f1[3]!=b.var[3] and f1[3]!=c.var[3] and f1[3]!=d.var[3] and f1[3]!=e.var[3] and f1[4]!=a.var[4] and f1[4]!=b.var[4] and f1[4]!=c.var[4] and f1[4]!=d.var[4] and f1[4]!=e.var[4] and f1[5]!=a.var[5] and f1[5]!=b.var[5] and f1[5]!=c.var[5] and f1[5]!=d.var[5] and f1[5]!=e.var[5] and f1[6]!=a.var[6] and f1[6]!=b.var[6] and f1[6]!=c.var[6] and f1[6]!=d.var[6] and f1[6]!=e.var[6] and f1[7]!=a.var[7] and f1[7]!=b.var[7] and f1[7]!=c.var[7] and f1[7]!=d.var[7] and f1[7]!=e.var[7] and f1[8]!=a.var[8] and f1[8]!=b.var[8] and f1[8]!=c.var[8] and f1[8]!=d.var[8] and f1[8]!=e.var[8]:
	#si potrebbe sostituire con un ciclo for 				
		#questa condizione comunque velocizza il tempo di risoluzione del sudoku			
		# ~ a.var=a1
		f.var=f1
	# ~ c.var=c1
		sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var])
		# ~ print(sudoku.var)
		# ~ print(sudoku.var)
		# ~ rettangolo1=[a.var[0],b.var[0],a.var[1],b.var[1],a.var[2],b.var[2]]
		# ~ rettangolo2=[a.var[3],b.var[3],a.var[4],b.var[4],a.var[5],b.var[5]]
		# ~ rettangolo3=[a.var[6],b.var[6],a.var[7],b.var[7],a.var[8],b.var[8]]
		# ~ definisci_quadrati4_5_6()
		# ~ print(q1.var)
	# ~ def ciao():
		# ~ print(d.var)
		for j2 in range(len(a.var)):
			if soluz=="ok":
				break	
			colonna5=[a.var[j2],b.var[j2],c.var[j2],d.var[j2],e.var[j2],f.var[j2]]
			# ~ print(d.var[i])
			# ~ definisci_rettangoli4_5_6()
			definisci_quadrati4_5_6()
			# ~ rettangolo4=[d.var[0],e.var[0],d.var[1],e.var[1],d.var[2],e.var[2]]
			# ~ rettangolo5=[d.var[3],e.var[3],d.var[4],e.var[4],d.var[5],e.var[5]]
			# ~ rettangolo6=[d.var[6],e.var[6],d.var[7],e.var[7],d.var[8],e.var[8]]				
								# ~ if contatore<=len(d1):
			if len(set(colonna5))==len(colonna5):	
				contatore5=contatore5+1
				# ~ print(contatore2)
				if contatore5>=9:
					# ~ if len(set(rettangolo4))==len(rettangolo4) and len(set(rettangolo5))==len(rettangolo5) and len(set(rettangolo6))==len(rettangolo6):

					if len(set(q4.var))==len(q4.var) and len(set(q5.var))==len(q5.var) and len(set(q6.var))==len(q6.var):

						print(sudoku.var)
						print()		# ~ if contatore==len(b.var):
						soluz="ok"			# ~ print(contatore)
				
											# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

												# ~ print(sudoku.var)
				
										# ~ else:
											# ~ contatore=0
										
												# ~ soluzione="ok"
										# ~ print(sudoku.var)
					
		else:
				contatore5=0

soluz="dffdfg"	
for g1 in listapermutazioni1:
	# ~ print("cioa")
	if soluz=="ok":
		break
	# ~ for b1 in listapermutazioni1:
		# ~ if soluz=="ok":
			# ~ break
		# ~ for c1 in listapermutazioni1:
			# ~ if soluz=="ok":
				# ~ break					# ~ if soluzione=="ok":
								# ~ break
							
		# ~ a.var=a1
	g.var=g1
	# ~ c.var=c1
	sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var])
	# ~ print(sudoku.var)
	# ~ print(sudoku.var)
	# ~ rettangolo1=[a.var[0],b.var[0],a.var[1],b.var[1],a.var[2],b.var[2]]
	# ~ rettangolo2=[a.var[3],b.var[3],a.var[4],b.var[4],a.var[5],b.var[5]]
	# ~ rettangolo3=[a.var[6],b.var[6],a.var[7],b.var[7],a.var[8],b.var[8]]
	# ~ definisci_quadrati4_5_6()
	# ~ print(q1.var)
# ~ def ciao():
	# ~ print(d.var)
	for j3 in range(len(a.var)):
		if soluz=="ok":
			break	
		colonna5=[a.var[j3],b.var[j3],c.var[j3],d.var[j3],e.var[j3],f.var[j3],g.var[j3]]
		# ~ print(d.var[i])
		# ~ definisci_rettangoli4_5_6()
		# ~ definisci_quadrati4_5_6()
		# ~ rettangolo4=[d.var[0],e.var[0],d.var[1],e.var[1],d.var[2],e.var[2]]
		# ~ rettangolo5=[d.var[3],e.var[3],d.var[4],e.var[4],d.var[5],e.var[5]]
		# ~ rettangolo6=[d.var[6],e.var[6],d.var[7],e.var[7],d.var[8],e.var[8]]				
							# ~ if contatore<=len(d1):
		if len(set(colonna5))==len(colonna5):	
			contatore6=contatore6+1
			# ~ print(contatore2)
			if contatore6>=9:
				# ~ if len(set(rettangolo4))==len(rettangolo4) and len(set(rettangolo5))==len(rettangolo5) and len(set(rettangolo6))==len(rettangolo6):

				# ~ if len(set(q4.var))==len(q4.var) and len(set(q5.var))==len(q5.var) and len(set(q6.var))==len(q6.var):

				print(sudoku.var)
				print()
				print()
									# ~ if contatore==len(b.var):
				soluz="ok"			# ~ print(contatore)
			
										# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

											# ~ print(sudoku.var)
			
									# ~ else:
										# ~ contatore=0
									
											# ~ soluzione="ok"
									# ~ print(sudoku.var)
				
	else:
			contatore6=0
			
			
soluz="dffdfg"	
for h1 in listapermutazioni1:
	if soluz=="ok":
		break
	# ~ for c1 in listapermutazioni1:
		# ~ if soluz=="ok":
			# ~ break					# ~ if soluzione=="ok":
							# ~ break
						
	h.var=h1
	# ~ b.var=b1
	# ~ c.var=c1
	sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var,h.var])
	rettangolo7=[g.var[0],h.var[0],g.var[1],h.var[1],g.var[2],h.var[2]]
	rettangolo8=[g.var[3],h.var[3],g.var[4],h.var[4],g.var[5],h.var[5]]
	rettangolo9=[g.var[6],h.var[6],g.var[7],h.var[7],g.var[8],h.var[8]]
	# ~ print(d.var)
	for j4 in range(len(a.var)):
		if soluz=="ok":
			break	
		colonna6=[a.var[j4],b.var[j4],c.var[j4],d.var[j4],e.var[j4],f.var[j4],g.var[j4],h.var[j4]]

		# ~ print(d.var[i])
						
							# ~ if contatore<=len(d1):
		if len(set(colonna6))==len(colonna6):	
			contatore7=contatore7+1
			if contatore7>=9 and len(set(rettangolo7))==len(rettangolo7) and len(set(rettangolo8))==len(rettangolo8) and len(set(rettangolo9))==len(rettangolo9):
				# ~ if len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):

					print(sudoku.var)
									# ~ if contatore==len(b.var):
					soluz="ok"			# ~ print(contatore)
			
										# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

											# ~ print(sudoku.var)
			
									# ~ else:
										# ~ contatore=0
									
											# ~ soluzione="ok"
									# ~ print(sudoku.var)
				
	else:
			contatore7=0
soluz="dffdfg"	
contavolte=0
for k1 in listapermutazioni1:
	# ~ contatore8=0
	# ~ print("cioa")
	if soluz=="ok":
		break
	# ~ for b1 in listapermutazioni1:
		# ~ if soluz=="ok":
			# ~ break
		# ~ for c1 in listapermutazioni1:
			# ~ if soluz=="ok":
				# ~ break					# ~ if soluzione=="ok":
	# ~ f_1=f1	
	# ~ for i in range(0,9):
		# ~ if soluz=="ok":
			# ~ break
						# ~ break
	# ~ if k1[i]!=a.var and k1[i]!=b.var and k1[i]!=c.var and k1[i]!=d.var and k1[i]!=e.var and k1[i]!=f.var and k1[i]!=g.var and k1[i]!=h.var:
	if k1[0]!=a.var and k1[0]!=b.var and k1[0]!=c.var and k1[0]!=d.var and k1[0]!=e.var and k1[0]!=f.var and k1[0]!=g.var and k1[0]!=h.var:
		if k1[1]!=a.var and k1[1]!=b.var and k1[1]!=c.var and k1[1]!=d.var and k1[1]!=e.var and k1[1]!=f.var and k1[1]!=g.var and k1[1]!=h.var:
			if k1[2]!=a.var and k1[2]!=b.var and k1[2]!=c.var and k1[2]!=d.var and k1[2]!=e.var and k1[2]!=f.var and k1[2]!=g.var and k1[2]!=h.var:
				if k1[3]!=a.var and k1[3]!=b.var and k1[3]!=c.var and k1[3]!=d.var and k1[3]!=e.var and k1[3]!=f.var and k1[3]!=g.var and k1[3]!=h.var:
					if k1[4]!=a.var and k1[4]!=b.var and k1[4]!=c.var and k1[4]!=d.var and k1[4]!=e.var and k1[4]!=f.var and k1[4]!=g.var and k1[4]!=h.var:			
						if k1[5]!=a.var and k1[5]!=b.var and k1[5]!=c.var and k1[5]!=d.var and k1[5]!=e.var and k1[5]!=f.var and k1[5]!=g.var and k1[5]!=h.var:
							if k1[6]!=a.var and k1[6]!=b.var and k1[6]!=c.var and k1[6]!=d.var and k1[6]!=e.var and k1[6]!=f.var and k1[6]!=g.var and k1[6]!=h.var:
								if k1[7]!=a.var and k1[7]!=b.var and k1[7]!=c.var and k1[7]!=d.var and k1[7]!=e.var and k1[7]!=f.var and k1[7]!=g.var and k1[7]!=h.var:	
									if k1[8]!=a.var and k1[8]!=b.var and k1[8]!=c.var and k1[8]!=d.var and k1[8]!=e.var and k1[8]!=f.var and k1[8]!=g.var and k1[8]!=h.var:

										k.var=k1		#in questo assegno il valore solo secondo la precedente condizione 
										sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var,h.var,k.var])
										definisci_quadrati7_8_9()
										for j9 in range(len(a.var)):
										# ~ if soluz=="ok":
											# ~ break	
											colonna9=[a.var[j9],b.var[j9],c.var[j9],d.var[j9],e.var[j9],f.var[j9],g.var[j9],h.var[j9],k.var[j9]]

											# ~ print(d.var[i])
															
																# ~ if contatore<=len(d1):
											if len(set(colonna9))==len(colonna9):	
												contatore9=contatore9+1
												if contatore9>=9:
													
													# ~ print(contatore9)
													if len(set(q7.var))==len(q7.var) and len(set(q8.var))==len(q8.var) and len(set(q9.var))==len(q9.var):

												# ~ if contatore7>=9 and len(set(rettangolo7))==len(rettangolo7) and len(set(rettangolo8))==len(rettangolo8) and len(set(rettangolo9))==len(rettangolo9):
													# ~ if len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):

														print(sudoku.var)
																		# ~ if contatore==len(b.var):
														soluz="ok"	
										else:
											contatore9=0		#
												# ~ definisci_quadrati7_8_9()	#
					# ~ for j9 in range(len(a.var)):
					# ~ if soluz=="ok":
					# ~ break	
					
					# ~ colonna7=[a.var[j9],b.var[j9],c.var[j9],d.var[j9],e.var[j9],f.var[j9],g.var[j9],h.var[j9],k.var[j9]]
				# ~ print(d.var[i])
					
				# ~ definisci_rettangoli4_5_6()
				
				# ~ rettangolo4=[d.var[0],e.var[0],d.var[1],e.var[1],d.var[2],e.var[2]]
				# ~ rettangolo5=[d.var[3],e.var[3],d.var[4],e.var[4],d.var[5],e.var[5]]
				# ~ rettangolo6=[d.var[6],e.var[6],d.var[7],e.var[7],d.var[8],e.var[8]]				
									# ~ if contatore<=len(d1):
					# ~ if len(set(colonna7))==len(colonna7):	
						# ~ contatore8=contatore8+1
						# ~ if contatore8>=9:
							# ~ soluz="ok"
							# ~ print(sudoku.var)
					# ~ contatore6=contatore6+1
					# ~ print(contatore2)
					# ~ if contatore6>=9:
						# ~ if len(set(rettangolo4))==len(rettangolo4) and len(set(rettangolo5))==len(rettangolo5) and len(set(rettangolo6))==len(rettangolo6):

						

							# ~ print(sudoku.var)
							# ~ print()		# ~ if contatore==len(b.var):
							# ~ soluz="ok"			# ~ print(contatore)
					
												# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

													# ~ print(sudoku.var)
					
											# ~ else:
													# ~ contatore=0
												
														# ~ soluzione="ok"
												# ~ print(sudoku.var)
							
				# ~ else:
					# ~ contatore8=0
	# ~ else:
		# ~ contavolte=0		
			
def ciao():
		
							# ~ soluz="ok"
							# ~ break		
							for c1 in listapermutazioni1:
								c.var=c1
								sudoku.var = np.array([a.var,b.var,c.var])
								definisci_quadrati1_2_3()
							
								# ~ print(sudoku.var)
								for x in range(len(a.var)):
				# ~ if soluz=="ok":
					# ~ break	
									colonna2=[a.var[x],b.var[x],c.var[x]]
									# ~ print(d.var[i])
													
														# ~ if contatore<=len(d1):
									# ~ if len(set(colonna1))==len(colonna1):	
										# ~ contatore2=contatore2+1
										# ~ print(contatore2)
												# ~ print(sudoku.var)
												# ~ soluz="ok"
												# ~ break
												# ~ 
							# ~ else:
								# ~ contatore2=0				

###CARTELLA==prova