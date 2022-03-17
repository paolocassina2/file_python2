import numpy as np
from itertools import permutations
import time
# ~ import clock
from datetime import datetime

now = datetime.now()
ora_in=now.strftime("%H:%M:%S")
print("ora_inizio ",ora_in)
# ~ ora_inizio import time
ora_inizio = time.time()
# ~ print("ora inizio", ora_inizio)
cc=0
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
l8=[]
l9=[]
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
s6=[]
s7=[]
s8=[]
s9=[]

for i in range(0,9):
	cc=cc+1
	aa=input("a"+str(cc)+" 	")
	
	if aa=="":
		l1.append("x")
	else:
		l1.append(aa)	
	# ~ aa=input("a"+str(cc)+" 	")
print()
cc=0
for i in range(0,9):
	cc=cc+1
	bb=input("b"+str(cc)+" 	")
	# ~ l2.append(bb)
		# ~ l1.append(aa)
	if bb=="":
		l2.append("x")
	else:
		l2.append(bb)
cc=0
print()
for i in range(0,9):	
	cc=cc+1	
	cc_1=input("c"+str(cc)+" 	")
	# ~ l3.append(cc_1)
	if cc_1=="":
		l3.append("x")
	else:
		l3.append(cc_1)
cc=0
print()
for i in range(0,9):	
	cc=cc+1
	dd=input("d"+str(cc)+" 		")
	# ~ l4.append(dd)
	if dd=="":
		l4.append("x")
	else:
		l4.append(dd)
cc=0	
print()
for i in range(0,9):
	cc=cc+1
	ee=input("e"+str(cc)+" 		")
	# ~ l5.append(ee)
	if ee=="":
		l5.append("x")
	else:
		l5.append(ee)
print()
cc=0
print()
for i in range(0,9):
	cc=cc+1
	ff=input("f"+str(cc)+" 		")
	
	if ff=="":
		l6.append("x")
	else:
		l6.append(ff)
cc=0
print()
for i in range(0,9):
	cc=cc+1
	gg=input("g"+str(cc)+" 		")
	# ~ l7.append(gg)
	if gg=="":
		l7.append("x")
	else:
		l7.append(gg)
cc=0
print()
for i in range(0,9):	
	cc=cc+1
	hh=input("h"+str(cc)+" 		")
	# ~ l8.append(hh)
	if hh=="":
		l8.append("x")
	else:
		l8.append(hh)
cc=0
print()
for i in range(0,9):
	cc=cc+1
	kk=input("k"+str(cc)+" 		")
	# ~ l9.append(kk)
	if kk=="":
		l9.append("x")
	else:
		l9.append(kk)
# ~ a=input()
print("l1",l1)
print("l2",l2)
print("l3",l3)
print("l4",l4)
print("l5",l5)
print("l6",l6)
print("l7",l7)
print("l8",l8)
print("l9",l9)
print(len(l1))
print(len(l2))
print(len(l3))
print(len(l4))
print(len(l5))
print(len(l6))
print(len(l7))
print(len(l8))
print(len(l9))

print()
#####################risolve uno specifico sudoku

# ~ print(s1)
		

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

print("risoluzione di sudoku 9*9")
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
# ~ ciao=random.choice(listapermutazioni
# ~ d

# ~ print(type(sud
def controllo_colonne():
	ciao1=[1,4,7,3,311,355,355,3]
	ciao2=[2,5,8,2,3,4,5555,655]
	ciao3=[2,6,81,23,5,6555,7,8]
	ciao4=[4,623,8178,289893,534,65355,343,99]
	# ~ ciao5=[3932,654,891,2893,5,6555,7,8]
	# ~ ciao6=[3113923,656,8981,28993,5,6555,7,8]
	# ~ ciao7=[329323,667,8891,289983,5,6555,7,8]
	# ~ ciao8=[3329923,678,889891,289893,5,6555,7,8]
	print(len(ciao1))
	print(len(ciao2))
	print(len(ciao3))
	
	sudoku.var = np.array([ciao1,ciao2,ciao3,ciao4])
	print(sudoku.var)
	
	
	# ~ print(type(sudoku.var[:,1]))
	# ~ sudouoku.var[:,1]
	# ~ print("size",sudoku.var[:,0].size)
	# ~ print("size_set",len(set(list(sudoku.var[:,0]))))
	# ~ print()
	# ~ lista1=set(sudoku.var)
	if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size:
			
	# ~ if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:
		print("xiao")
		# ~ print("xiao")
		# ~ print("xiao")
# ~ controllo_colonne()
def sudokufoto():	#vedifoto
	for x in listapermutazioni1:
		# ~ print(x)
		if x[0]==2 and x[2]==9 and x[5]==7 and x[8]==6:
			s1.append(x)
		if x[3]==9 and x[4]==3 and x[6]==5:
			s2.append(x)
		if x[1]==4 and x[7]==1 and x[8]==9:
			s3.append(x)
		if x[2]==3 and x[5]==1 and x[7]==6:
			s4.append(x)
		# ~ if x[1]==1 and x[3]==8 and x[5]==5 and x[6]==2:
			# ~ s5.append(x)
lista_ind1=[]
lista_ind2=[]
lista_ind3=[]
lista_ind4=[]
lista_ind5=[]
lista_ind6=[]
lista_ind7=[]
lista_ind8=[]
lista_ind9=[]

			
lista_val1=[]
lista_val2=[]
lista_val3=[]
lista_val4=[]
lista_val5=[]
lista_val6=[]
lista_val7=[]
lista_val8=[]
lista_val9=[]

for x,y,z,u,j,knk,nkn,jjk,kkj in zip(l1,l2,l3,l4,l5,l6,l7,l8,l9):
	if x!="x":
		i1=l1.index(x)
		lista_ind1.append(i1)
		lista_val1.append(int(x))
	if y!="x":
		lista_ind2.append(l2.index(y))
		lista_val2.append(int(y))
	if z!="x":
		lista_ind3.append(l3.index(z))
		lista_val3.append(int(z))
	if u!="x":
		lista_ind4.append(l4.index(u))
		lista_val4.append(int(u))
	if j!="x":
		lista_ind5.append(l5.index(j))
		lista_val5.append(int(j))
	if knk!="x":
		lista_ind6.append(l6.index(knk))
		lista_val6.append(int(knk))
	if nkn!="x":
		lista_ind7.append(l7.index(nkn))
		lista_val7.append(int(nkn))
	if jjk!="x":
		lista_ind8.append(l8.index(jjk))
		lista_val8.append(int(jjk))
		
	if kkj!="x":
		lista_ind9.append(l9.index(kkj))
		lista_val9.append(int(kkj))


print(lista_ind1)
print(lista_val1)	

# ~ print(lista_ind2)
# ~ print(lista_val2)	

# ~ print(lista_ind3)
# ~ print(lista_val3)	

# ~ print(lista_ind4)
# ~ print(lista_val4)	

# ~ print(lista_ind5)
# ~ print(lista_val5)	
# ~ print(lista_ind6)
# ~ print(lista_val6)	

# ~ print(lista_ind7)
# ~ print(lista_val7)	

# ~ print(lista_ind8)
# ~ print(lista_val8)	

# ~ print(lista_ind9)
# ~ print(lista_val9)	
	
# ~ if x[0]==7 and x[4]==4 and x[8]==8:
	# ~ s6.append(x)
	
# ~ if x[2]==5 and x[4]==7:
	# ~ s7.append(x)
	
# ~ if x[4]==6 and x[5]==3 and x[6]==8:
	# ~ s8.append(x)
# ~ if x[0]==9 and x[1]==2 and x[3]==5 and x[6]==4 and x[7]==3:
	# ~ s9.append(x)	
# ~ def sudokugenerico():
conta_val_1=0
nn2=0
nn3=0
nn4=0
nn5=0
nn6=0
nn7=0
nn8=0
nn9=0
for yj in listapermutazioni1:			#mancano tutti i casi per ogni riga
			# ~ print(yj)
	for x1,j1,x2,j2,x3,j3,x4,j4,x5,j5,x6,j6,x7,j7,x8,j8,x9,j9 in zip(lista_ind1, lista_val1, lista_ind2, lista_val2,  lista_ind3, lista_val3,  lista_ind4, lista_val4,lista_ind5, lista_val5,lista_ind6, lista_val6,lista_ind7, lista_val7,lista_ind8, lista_val8,lista_ind9, lista_val9):
	#	print(x)
		#print(j)
		
		if yj[x1]==j1:
			conta_val_1=conta_val_1+1
			#print("c",conta)
		#	
		#	print(yj[x])
			if conta_val_1==len(lista_ind1):
				s1.append(yj)
#######################################################
		if yj[x2]==j2:
			nn2=nn2+1
			#print("c",conta)
		#	
		#	print(yj[x])
			if nn2==len(lista_ind2):
				s2.append(yj)
#######################################################		
		if yj[x3]==j3:
			# ~ conta_val_3=conta_val_3+1
			#print("c",conta)
			nn3=nn3+1
		#	print(yj[x])
			if nn3==len(lista_ind3):
				s3.append(yj)
	
#######################################################		
		if yj[x4]==j4:
			nn4=nn4+1
			#print("c",conta)
		#	
		#	print(yj[x])
			if nn4==len(lista_ind4):
				s4.append(yj)
				
#######################################################					
				
		if yj[x5]==j5:
			nn5=nn5+1
			#print("c",conta)
		#	
		#	print(yj[x])
			if nn5==len(lista_ind5):
				s5.append(yj)
						
#####################################################
		if yj[x6]==j6:
			nn6=nn6+1
			#print("c",conta)
		#	
		#	print(yj[x])
			if nn6==len(lista_ind6):
				s6.append(yj)
						
#####################################################						
		if yj[x7]==j7:
			nn7=nn7+1
			#print("c",conta)
		#	
		#	print(yj[x])
			if nn7==len(lista_ind7):
				s7.append(yj)
####################################################								
		if yj[x8]==j8:
			nn8=nn8+1
			#print("c",conta)
		#	
		#	print(yj[x])
			if nn8==len(lista_ind8):
				s8.append(yj)
										
#######################################################
		if yj[x9]==j9:
			nn9=nn9+1
			#print("c",conta)
		#	
		#	print(yj[x])
			if nn9==len(lista_ind9):
				s9.append(yj)
								


				
	else:
		conta_val_1=0		
		nn2=0
		nn3=0
		nn4=0
		nn5=0
		nn6=0
		nn7=0
		nn8=0
		nn9=0
print("******************")
print("s1",s1[3])
print("s2",s2[3])
print("s3",s3[3])
print("s4",s4[3])
print("s5",s5[3])
print("s6",s6[3])
print("s7",s7[3])
print("s8",s8[3])

print("s9",s9[3])
print("******************")
if len(lista_ind1)==0:
	s1=listapermutazioni1
if len(lista_ind2)==0:
	s2=listapermutazioni1
if len(lista_ind3)==0:
	s3=listapermutazioni1
if len(lista_ind4)==0:
	s4=listapermutazioni1
if len(lista_ind5)==0:
	s5=listapermutazioni1
if len(lista_ind6)==0:
	s6=listapermutazioni1
if len(lista_ind7)==0:
	s7=listapermutazioni1
if len(lista_ind8)==0:
	s8=listapermutazioni1
if len(lista_ind9)==0:
	s9=listapermutazioni1
				
# ~ print("s1",s1)

	# ~ for x in listapermutazioni1:
			# ~ print(x)
			# ~ if x[3]==4 and x[6]==1 and x[8]==3:
				# ~ s1.append(x)
		# ~ if x[0]==2 and x[4]==3 and x[6]==6:
			# ~ s2.append(x)
		# ~ if x[0]==1 and x[4]==6 and x[6]==5:
			# ~ s3.append(x)
		# ~ if x[0]==9 and x[5]==6:
			# ~ s4.append(x)
		
		# ~ if x[1]==2 and x[5]==7 and x[7]==4:
			# ~ s5.append(x)
		# ~ if x[3]==9 and x[6]== 8:
			# ~ s6.append(x)
		
		# ~ if x[1]==8 and x[2]==4  and x[8]==5 :
			# ~ s7.append(x)	
		# ~ if x[1]== 1 and x[2]== 3 and x[4]==8 and x[8]== 6:
			# ~ s8.append(x)
		# ~ if x[0]==6:
			# ~ s9.append(x)
print("len")	
print(len(s1))	
print(len(s2))	
print(len(s3))	
print(len(s4))	
print(len(s5))	
print(len(s6))	
print(len(s7))	
print(len(s8))	
print(len(s9))
#####################
print("*********************")
print(len(listapermutazioni1))	
	
# ~ s4=listapermutazioni1
# ~ s5=listapermutazioni1
# ~ s6=listapermutazioni1
# ~ s7=listapermutazioni1
# ~ s8=listapermutazioni1
# ~ s9=listapermutazioni1			
						


	# ~ if x[0]==8:
		# ~ s3.append(x)			
	# ~ if x[0]==6:
		# ~ s4.append(x)	
	# ~ if x[0]==7:
		# ~ s5.append(x)
	# ~ if x[1]==4:
		# ~ s6.append(x)
	# ~ if x[2]==5:
		# ~ s7.append(x)
	# ~ if x[1]==2:
		# ~ s8.append(x)
	# ~ if x[2]==9:
		# ~ s9.append(x)
		
		
for a1 in s1:
	ora_inizio_loop = time.time()
	a.var=a1
	# ~ a.var=a1
	# ~ for a1 in listapermutazioni1:
	if soluz=="ok":
		break
	for b1 in s2:
		if soluz=="ok":
			break
				# ~ for c1 in listapermutazioni1:
					# ~ if soluz=="ok":
						# ~ break					# ~ if soluzione=="ok":
		if b1[0]!=a.var[0] and b1[1]!=a.var[1] and b1[2]!=a.var[2] and b1[3]!=a.var[3] and b1[4]!=a.var[4] 	and b1[5]!=a.var[5]  and b1[6]!=a.var[6]  and b1[7]!=a.var[7]  and b1[8]!=a.var[8]: 								# ~ and b1[0]!=a.var[0] 								# ~ 								# ~ 								# ~ break
										
				# ~ a.var=a1
				b.var=b1
				# ~ c.var=c1
				sudoku.var = np.array([a.var,b.var])
				rettangolo1=[a.var[0],b.var[0],a.var[1],b.var[1],a.var[2],b.var[2]]
				rettangolo2=[a.var[3],b.var[3],a.var[4],b.var[4],a.var[5],b.var[5]]
				rettangolo3=[a.var[6],b.var[6],a.var[7],b.var[7],a.var[8],b.var[8]]
				if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:#controlla tutte e otto le colonne
					if len(set(rettangolo1))==len(rettangolo1) and len(set(rettangolo2))==len(rettangolo2) and len(set(rettangolo3))==len(rettangolo3):
					
	
						for c1 in s3:
							# ~ print("cioa")
							if soluz=="ok":
								break
											# ~ if soluzione=="ok":
							if c1[0]!=a.var[0] and c1[0]!=b.var[0]and c1[1]!=a.var[1] and c1[1]!=b.var[1] and c1[2]!=a.var[2] and c1[2]!=b.var[2] and c1[3]!=a.var[3] and c1[3]!=b.var[3] and c1[4]!=a.var[4] and c1[4]!=b.var[4]and c1[5]!=a.var[5] and c1[5]!=b.var[5] and c1[6]!=a.var[6] and c1[6]!=b.var[6] and c1[7]!=a.var[7] and c1[7]!=b.var[7] and c1[8]!=a.var[8] and c1[8]!=b.var[8]:									# ~ 								# ~ break
											# ~ break
													
								# ~ a.var=a1
								c.var=c1
								# ~ c.var=c1
								sudoku.var = np.array([a.var,b.var,c.var])
							
								definisci_quadrati1_2_3()
								# ~ print(q1.var)

								# ~ print(d.var)
								if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:#controlla tutte e otto le colonne

									
									if len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):

										
										for d1 in s4:
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
											if d1[0]!=a.var[0] and d1[0]!=b.var[0] and d1[0]!=c.var[0]:
												if d1[1]!=a.var[1] and d1[1]!=b.var[1] and d1[1]!=c.var[1]:
													if d1[2]!=a.var[2] and d1[2]!=b.var[2] and d1[2]!=c.var[2]:	
														if d1[3]!=a.var[3] and d1[3]!=b.var[3] and d1[3]!=c.var[3]:		
															if d1[4]!=a.var[4] and d1[4]!=b.var[4] and d1[4]!=c.var[4]:	
																if d1[5]!=a.var[5] and d1[5]!=b.var[5] and d1[5]!=c.var[5]:
																	if d1[6]!=a.var[6] and d1[6]!=b.var[6] and d1[6]!=c.var[6]:
																		if d1[7]!=a.var[7] and d1[7]!=b.var[7] and d1[7]!=c.var[7]:
																			if d1[8]!=a.var[8] and d1[8]!=b.var[8] and d1[8]!=c.var[8]:
												# ~ a.var=a1
																				d.var=d1
																				# ~ c.var=c1
																				sudoku.var = np.array([a.var,b.var,c.var,d.var])
																				if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:#controlla tutte e otto le colonne
											
	
																					for e1 in s5:
																						# ~ print("cioa")
																						if soluz=="ok":
																							break
																						
																						e.var=e1
																						
																						sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var])
																						rettangolo4=[d.var[0],e.var[0],d.var[1],e.var[1],d.var[2],e.var[2]]
																						rettangolo5=[d.var[3],e.var[3],d.var[4],e.var[4],d.var[5],e.var[5]]
																						rettangolo6=[d.var[6],e.var[6],d.var[7],e.var[7],d.var[8],e.var[8]]	
																						if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:#controlla tutte e otto le colonne

																							
																							if len(set(rettangolo4))==len(rettangolo4) and len(set(rettangolo5))==len(rettangolo5) and len(set(rettangolo6))==len(rettangolo6):

	
		
																								for f1 in s6:
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
																									
																											
																										definisci_quadrati4_5_6()

																										if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:#controlla tutte e otto le colonne
	
																											if len(set(q4.var))==len(q4.var) and len(set(q5.var))==len(q5.var) and len(set(q6.var))==len(q6.var):

																														# ~ print(sudoku.var)
																												# ~ print(sudoku.var)		# ~ if contatore==len(b.var):
																												# ~ soluz="ok"			# ~ print(contatore)
																												for g1 in s7:
			# ~ print("cioa")
																													if soluz=="ok":
																															break
																														
																													g.var=g1
																														
																													sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var])
																														
																													if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:#controlla tutte e otto le colonne
									
																														# ~ soluz="ok"
																														# ~ print(sudoku.var)
				
		

																														for h1 in s8:
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
			# ~ print(d.var)																																																				if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:#controlla tutte e otto le colonne
																															if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:#controlla tutte e otto le colonne
																																if len(set(rettangolo7))==len(rettangolo7) and len(set(rettangolo8))==len(rettangolo8) and len(set(rettangolo9))==len(rettangolo9):
																																	# ~ soluz="ok"
																																	# ~ print(sudoku.var)
		
																																	for k1 in s9:
																																		# ~ contatore8=0
																																		# ~ print("cioa")
																																		if soluz=="ok":
																																			break
																																		
																																		
																																		if k1[0]!=a.var and k1[0]!=b.var and k1[0]!=c.var and k1[0]!=d.var and k1[0]!=e.var and k1[0]!=f.var and k1[0]!=g.var and k1[0]!=h.var and k1[1]!=a.var and k1[1]!=b.var and k1[1]!=c.var and k1[1]!=d.var and k1[1]!=e.var and k1[1]!=f.var and k1[1]!=g.var and k1[1]!=h.var and k1[2]!=a.var and k1[2]!=b.var and k1[2]!=c.var and k1[2]!=d.var and k1[2]!=e.var and k1[2]!=f.var and k1[2]!=g.var and k1[2]!=h.var and k1[3]!=a.var and k1[3]!=b.var and k1[3]!=c.var and k1[3]!=d.var and k1[3]!=e.var and k1[3]!=f.var and k1[3]!=g.var and k1[3]!=h.var and k1[4]!=a.var and k1[4]!=b.var and k1[4]!=c.var and k1[4]!=d.var and k1[4]!=e.var and k1[4]!=f.var and k1[4]!=g.var and k1[4]!=h.var and k1[5]!=a.var and k1[5]!=b.var and k1[5]!=c.var and k1[5]!=d.var and k1[5]!=e.var and k1[5]!=f.var and k1[5]!=g.var and k1[5]!=h.var and k1[6]!=a.var and k1[6]!=b.var and k1[6]!=c.var and k1[6]!=d.var and k1[6]!=e.var and k1[6]!=f.var and k1[6]!=g.var and k1[6]!=h.var and k1[7]!=a.var and k1[7]!=b.var and k1[7]!=c.var and k1[7]!=d.var and k1[7]!=e.var and k1[7]!=f.var and k1[7]!=g.var and k1[7]!=h.var	and k1[8]!=a.var and k1[8]!=b.var and k1[8]!=c.var and k1[8]!=d.var and k1[8]!=e.var and k1[8]!=f.var and k1[8]!=g.var and k1[8]!=h.var:
																																			# ~ print(k1)
																																			k.var=k1		#in questo assegno il valore solo secondo la precedente condizione  (poi successivametne definisco colonne e controllo le colonne e i quadrati)
																																			sudoku.var = np.array([a.var,b.var,c.var,d.var,e.var,f.var,g.var,h.var,k.var])
																																			definisci_quadrati7_8_9()
																																			
																																			
																																			if len(set(list(sudoku.var[:,0])))==sudoku.var[:,0].size and len(set(list(sudoku.var[:,1])))==sudoku.var[:,1].size and len(set(list(sudoku.var[:,2])))==sudoku.var[:,2].size  and len(set(list(sudoku.var[:,3])))==sudoku.var[:,3].size  and len(set(list(sudoku.var[:,4])))==sudoku.var[:,4].size  and len(set(list(sudoku.var[:,5])))==sudoku.var[:,5].size  and len(set(list(sudoku.var[:,6])))==sudoku.var[:,6].size  and len(set(list(sudoku.var[:,7])))==sudoku.var[:,7].size  and len(set(list(sudoku.var[:,8])))==sudoku.var[:,8].size:#controlla tutte e otto le colonne

																																				if len(set(q7.var))==len(q7.var) and len(set(q8.var))==len(q8.var) and len(set(q9.var))==len(q9.var):
																																					soluz="ok"
																																					now1 = datetime.now()
																																					elapsed = time.strftime("%H:%M:%S", time.gmtime(time.time() - ora_inizio))
																																					
																																					print(f"tempo trascorso dall'inizio: {elapsed}"," (hours, minutes seconds)")#dall'inizio del programma
																																					
																																					tempo_loop=time.strftime("%H:%M:%S", time.gmtime(time.time() - ora_inizio_loop))
																																					print(f"tempo trascorso dall'inizio LOOP: {tempo_loop}"," (hours, minutes seconds)")	#tempo trascorso tra ogni loop
																																					
																																					ora_fine = now1.strftime("%H:%M:%S")
																																					# ~ tempo
																																					print("soluzione_trovata alle ore 	", ora_fine)
																																					# ~ print("tempo trascorso: ", float(ora_fine-ora_inizio))
																																					
																																					print(sudoku.var)
	soluz="jdfi"	#se alla fine cambio il valore di soluz soluz!="ok"il ciclo for prosegue

																																					# ~ if contatore7>=9 and len(set(rettangolo7))==len(rettangolo7) and len(set(rettangolo8))==len(rettangolo8) and len(set(rettangolo9))==len(rettangolo9):
							# ~ if len(set(q1.var))==len(q1.var) and len(set(q2.var))==len(q2.var) and len(set(q3.var))==len(q3.var):
	
					#
						# ~ definisci_quadrati7_8_9()
						
		# ~ for i1,i2,i3,i4,i5,i6,i7,i8,	#
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
