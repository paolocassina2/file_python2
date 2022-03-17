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

		
contatore=0
soluz="dfjk"
for a1 in listapermutazioni1:
	if soluz=="ok":
		break
	for b1 in listapermutazioni1:
		if soluz=="ok":
			break					# ~ if soluzione=="ok":
								# ~ break
							
		a.var=a1
		b.var=b1
		sudoku.var = np.array([a.var,b.var])
		rettangolo1=[a.var[0],b.var[0],a.var[1],b.var[1],a.var[2],b.var[2]]
		rettangolo2=[a.var[3],b.var[3],a.var[4],b.var[4],a.var[5],b.var[5]]
		rettangolo3=[a.var[6],b.var[6],a.var[7],b.var[7],a.var[8],b.var[8]]
		# ~ print(d.var)
		for i in range(len(a.var)):
			# ~ if soluz=="ok":
				# ~ break	
			colonna=[a.var[i],b.var[i]]
			# ~ print(d.var[i])
							
								# ~ if contatore<=len(d1):
			if len(set(colonna))==len(colonna):	
				contatore=contatore+1
										# ~ if contatore==len(b.var):
										# ~ print(contatore)
				
											# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

												# ~ print(sudoku.var)
				if contatore>=9 and len(set(rettangolo1))==len(rettangolo1) and len(set(rettangolo2))==len(rettangolo2) and len(set(rettangolo3))==len(rettangolo3):
						print(sudoku.var)
					# ~ soluz="ok"
					# ~ break						# ~ break
										# ~ else:
											# ~ contatore=0
										
												# ~ soluzione="ok"
										# ~ print(sudoku.var)
					
		else:
				contatore=0

###CARTELLA==prova