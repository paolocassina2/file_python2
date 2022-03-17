import numpy as np
def r1():
	r1.var=121
r1()
def r2():
	r2.var=121
r2()
def r3():
	r3.var=121
r3()
def a():
	a.var=""
a()
def b():
	b.var=""
b()
def sudoku():
	sudoku.var=""
sudoku()
a.var=[1,2,3,4,5,6,7,8,9]
b.var=[1,2,3,4,5,6,7,8,9]

def definisci_rettangoli1_2_3():
	#rettangoli ab ,de,gh
	# ~ sudoku.var = np.array([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])					
	# ~ print(sudoku)
	# ~ a.var=list(random.choice(listapermutazioni1))
	# ~ b.var=list(random.choice(listapermutazioni1))
	# ~ c.var=list(random.choice(listapermutazioni1))
	# ~ d.var=list("232")
	# ~ e.var=list("2323")
	# ~ f.var=list("23")
	
	sudoku.var = np.array([a.var,b.var])
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
	print(r1.var)
	print(r2.var)
	print(r3.var)
definisci_rettangoli1_2_3()
