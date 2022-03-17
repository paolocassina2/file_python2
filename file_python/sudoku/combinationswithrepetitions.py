import itertools
# ~ x = [1, 2, 3, 4, 5, 6]
# ~ print([p for p in itertools.product(x, repeat=2)])
# ~ [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), 
 # ~ (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), 
 # ~ (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), 
 # ~ (5, 4), (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
import random
# ~ soluz="ok"
# ~ a=[2,61,4,61]
import numpy as np
# ~ print("set ",len(set(a)))
# ~ print("lista ",len(a))
# ~ perm_list = []
from itertools import permutations
		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
a1 = list(permutations(range(1, 7)))
# ~ b1 = list(permutations(range(1, 7)))
# ~ c1 = list(permutations(range(1, 7)))
# ~ d1 = list(permutations(range(1, 7)))
# ~ e1 = list(permutations(range(1, 7)))
# ~ f1 = list(permutations(range(1, 7)))
while True:
	
	a=np.random.permutation([1, 2,3,4,5,6])
	# ~ print(f1)
	# ~ a=np.random.permutation([1, 4, 9, 12, 15])
	b=np.random.permutation([1,2,3,4,5,6])
	c=np.random.permutation([1,2,3,4,5,6])
	d=np.random.permutation([1,2,3,4,5,6])
	e=np.random.permutation([1,2,3,4,5,6])
	f=np.random.permutation([1,2,3,4,5,6])

	# ~ print(a)
	# ~ print (l)
	a2=list(a)

	b2=list(b)
	c2=list(c)
	d2=list(d)
	e2=list(e)
	f2=list(f)
	# ~ print(type(a2))

	lista=[]
	q=[a2,b2,c2,d2,e2,f2]
	# ~ print(q)
	# ~ print(a2)
	# ~ print(b2)
	# ~ print(c2)
	# ~ print(d2)
	# ~ print(e2)
	# ~ print(f2)
	# ~ print()
	# ~ for x in l:
	# ~ for j in a:
		# ~ lista.append(list(j))
	# ~ rows =3
	# ~ columns= 2
	# ~ mylist = [[0 for x in range(columns)] for x in range(rows)]
	# ~ for i in range(rows):
		# ~ for j in range(columns):
			# ~ mylist[i][j] = '%s,%s'%(i,j)
	# ~ print (mylist)
	colonna1=[]
	colonna2=[]
	colonna3=[]
	colonna4=[]
	colonna5=[]
	colonna6=[]
	# ~ conta=0
	for i in range(len(q)):
		# ~ for j in range(len(f[i])):
			# ~ if len(set(f[i]))==len(f[i]):
				# ~ print("ok")
			colonna1.append(q[i][0])
			colonna2.append(q[i][1])
			colonna3.append(q[i][2])
			colonna4.append(q[i][3])
			colonna5.append(q[i][4])
			colonna6.append(q[i][5])
			# ~ conta=conta+1
			# ~ print(colonna1)
	if len(set(colonna1))==len(colonna1) and len(set(colonna2))==len(colonna2) and len(set(colonna3))==len(colonna3) and len(set(colonna4))==len(colonna4) and len(set(colonna5))==len(colonna5) and len(set(colonna6))==len(colonna6):
			print(a2)
			print(b2)
			print(c2)
			print(d2)
			print(e2)
			print(f2)
			
			break
	# ~ c=np.random.permutation([1,2,3,4,5,6])		
	# ~ c2=list(c)
		
	# ~ for i in range(0,4):
		# ~ for j in range(len(f[i])):
			# ~ if len(set(f[i]))==len(f[i]):
				# ~ print("ok")
			# ~ colonna1.append(q[i][0])
			# ~ colonna2.append(q[i][1])
			# ~ colonna3.append(q[i][2])
			# ~ colonna4.append(q[i][3])
			# ~ colonna5.append(q[i][4])
			# ~ colonna6.append(q[i][5])
			# ~ conta=conta+1
			# ~ print(colonna1)
			# ~ if len(set(colonna1))==len(colonna1) and len(set(colonna2))==len(colonna2) and len(set(colonna3))==len(colonna3) and len(set(colonna4))==len(colonna4) and len(set(colonna5))==len(colonna5) and len(set(colonna6))==len(colonna6):
				# ~ print(a2)
				# ~ print(b2)
				# ~ print(c2)
				# ~ break
			# ~ if len(set(colonna1))==len(colonna1) and len(set(colonna2))==len(colonna2):
				 # ~ and len(set(colonna3))==len(colonna3) and len(set(colonna4))==len(colonna4) and len(set(colonna5))==len(colonna5) and len(set(colonna6))==len(colonna6):
			# ~ if set(colonna
					# ~ f[i][0])
					# ~ f[i][0])
				# ~ f[i][0])
			# ~ soluz="ok"
			# ~ print(a2)
			# ~ print(b2)
			# ~ print(c2)
			# ~ print(d2)
			# ~ print(e2)
			# ~ print(f2)
			# ~ break
	
# ~ if len(set(colonna3))==len(colonna3):
	# ~ print("c3",colonna3)
	# ~ break
	# ~ if soluz=="ok":
		# ~ break
# ~ print(f)
# ~ x = [ ['0,0', '0,1'], ['1,0', '1,1'], ['2,0', '2,1'] ]
# ~ for i in range(len(x)):
# ~ for j in range(len(x[i])):
			# ~ print(x[i][j])
	
# ~ print(len(a2))
# ~ for x in l:
# ~ print(x)
# ~ print(l)
# ~ data = list('123')
# ~ for p in permutation(data):
# ~ print (p)

# ~ array([1, 7, 4, 3, 0, 9, 2, 5, 8, 6]) # random

a1 = [1,2,3,4]

# no length entered so default length
# taken as 4(the length of string GeEK)
# ~ a1 = list(np.random.permutation(5))
# ~ b1= list(np.random.permutation(5))
# ~ c1= list(np.random.permutation(5))
# ~ d1= list(np.random.permutation(5))
# ~ a1.remove(0)
# ~ b1.remove(0)
# ~ c1.remove(0)
# ~ d1.remove(0)

# ~ a=a1
# ~ b=b1
# ~ c=c1
# ~ d=d1
# Print the obtained permutations 
# ~ print("a",a)
	# ~ print(j) 
# ~ while True:
	# ~ a=list(np.random.permutation([1, 2, 3, 4]))
	# ~ b=list(np.random.permutation([1, 2, 3, 4]))
	# ~ c=list(np.random.permutation([1, 2, 3, 4]))
	# ~ d=list(np.random.permutation([1, 2, 3, 4]))

	# ~ colonna1=[a[i],]
# ~ f=[a,b,c,d]
# ~ for x in range(len(f)):
	# ~ for j in range(len(a)):
		# ~ if len(set(f[x][j]))==len(f[x][j]):
			# ~ print(a)
		# ~ print()
			# ~ print(f[x][j])
			# ~ print("2ciao")
		# ~ print(f[x][j])	
		
# ~ print(f)
# ~ for x in f:
	# ~ for j in x:
		# ~ print(j)
		# ~ if len(set(f[x][j]))==len(f[x][j]):
			# ~ break
			# ~ print(a)
			# ~ print(b)
			# ~ print(c)
				# ~ print(d)
				# ~ soluzione="ok"
		# ~ break
		# ~ if soluzione=="ok":
			# ~ break
# ~ list(np.random.permutation(10))
# ~ list(np.random.permutation(10))
# ~ list(np.random.permutation(10))
# ~ list(np.random.permutation(10))
# ~ list(np.random.permutation(10)
# ~ list(np.random.permutation(10))

# ~ print(lista)



###CARTELLA==sudoku

###CARTELLA==ciaociaociao
###CARTELLA==ciaopaolo