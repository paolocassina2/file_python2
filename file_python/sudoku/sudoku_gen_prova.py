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
# ~ s1=[]
# ~ s2=[]
# ~ s3=[]
# ~ s4=[]
# ~ s5=[]
# ~ s6=[]
# ~ s7=[]
# ~ s8=[]
# ~ s9=[]

for i in range(0,9):
	cc=cc+1
	aa=input("a"+str(cc)+" 	")
	
	if aa=="":
		l1.append("x")
	else:
		l1.append(aa)	
	# ~ aa=input("a"+str(cc)+" 	")
print()

def caid():
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

for x in l1:
	if x!="x":
		i1=l1.index(x)
		lista_ind1.append(i1)
		lista_val1.append(x)

# ~ for x,y,z,u,j,knk,nkn,jjk,kkj in zip(l1,l2,l3,l4,l5,l6,l7,l8,l9):
	# ~ if x!="x":
		# ~ i1=l1.index(x)
		# ~ lista_ind1.append(i1)
		# ~ lista_val1.append(x)
	# ~ if y!="x":
		# ~ lista_ind2.append(l2.index(y))
		# ~ lista_val2.append(y)
	# ~ if z!="x":
		# ~ lista_ind3.append(l3.index(z))
		# ~ lista_val3.append(z)
	# ~ if u!="x":
		# ~ lista_ind4.append(l4.index(u))
		# ~ lista_val4.append(u)
	# ~ if j!="x":
		# ~ lista_ind5.append(l5.index(j))
		# ~ lista_val5.append(j)
	# ~ if knk!="x":
		# ~ lista_ind6.append(l6.index(knk))
		# ~ lista_val6.append(knk)
	# ~ if nkn!="x":
		# ~ lista_ind7.append(l7.index(nkn))
		# ~ lista_val7.append(nkn)
	# ~ if jjk!="x":
		# ~ lista_ind8.append(l8.index(jjk))
		# ~ lista_val8.append(jjk)
		
	# ~ if kkj!="x":
		# ~ lista_ind9.append(l9.index(kkj))
		# ~ lista_val9.append(kkj)


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
s1=[]
for yj in listapermutazioni1:			#mancano tutti i casi per ogni riga
	# ~ print(yj)
	for x,j in zip(lista_ind1, lista_val1):
		# ~ print(x)
		# ~ print(j)
		
		if yj[x]==int(j):
			conta_val_1=conta_val_1+1
			# ~ print(conta_val_1)
			#print("c",conta)
		#	
		#	print(yj[x])
			if conta_val_1==len(lista_ind1):
				s1.append(yj)
	else:
		conta_val_1=0		
				
print("len__s1__1",len(s1))
for x in range(4):
	print(s1[x])

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
# ~ print(len(s[]1))	
# ~ print(len(s2))	
# ~ print(len(s3))	
# ~ print(len(s4))	
# ~ print(len(s5))	
# ~ print(len(s6))	
# ~ print(len(s7))	
# ~ print(len(s8))	
# ~ print(len(s9))
#####################
print("*********************")
print(len(listapermutazioni1))	
