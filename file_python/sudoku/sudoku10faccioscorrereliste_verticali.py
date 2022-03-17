from itertools import permutations
listapermutazioni1=[]		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
listapermutazioni = list(permutations(range(1, 7)))
for x in listapermutazioni:
	listapermutazioni1.append(list(x))
	
import random

lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
lista6=[]
print(len(listapermutazioni1))
# ~ for x in listapermutazioni1:
	# ~ print(x[0])
# ~ print(ciao)
# ~ conta=0
a=[6,5,4,3,2,1]

# ~ print(listapermutazioni1[3])

for x in range(0,len(a)):
		for j in listapermutazioni1:
		# ~ if x==k[0]:
			if a[x]==j[0]:
				if x==0:
					lista1.append(j)
				if x==1:
					lista2.append(j)
				if x==2:
					lista3.append(j)
				if x==3:
					lista4.append(j)
				if x==4:
					lista5.append(j)
				if x==5:
					lista6.append(j)
			# ~ print(j)
				# ~ print(k)
# ~ for x,y,y1,z2,l,k in zip(lista1,lista2,lista3,lista4,lista5,lista6):
import random#in questo progeramma sono sempre giusti in verticale

import numpy as np
while True:
	x1=random.choice(lista1)
	b1=	random.choice(lista2)
	c1=random.choice(lista3)
	d1=random.choice(lista4)
	e1=random.choice(lista5)
	f1=random.choice(lista6)
	b=[x1[1],b1[1],c1[1],d1[1],e1[1],f1[1]]
	c=[x1[2],b1[2],c1[2],d1[2],e1[2],f1[2]]
	d=[x1[3],b1[3],c1[3],d1[3],e1[3],f1[3]]
	e=[x1[4],b1[4],c1[4],d1[4],e1[4],f1[4]]
	f=[x1[5],b1[5],c1[5],d1[5],e1[5],f1[5]]
	A = np.array([a, 
						b,c,d,e,f]
								)
# ~ print(A[:,0][0:4])
	q1=list(A[:,0][0:2])+list(A[:,1][0:2])+list(A[:,2][0:2])
	q2=list(A[:,3][0:2])+list(A[:,4][0:2])+list(A[:,5][0:2])
	q3=list(A[:,0][2:4])+list(A[:,1][2:4])+list(A[:,2][2:4])
	q4=list(A[:,3][2:4])+list(A[:,4][2:4])+list(A[:,5][2:4])
	q5=list(A[:,0][4:6])+list(A[:,1][4:6])+list(A[:,2][4:6])
	q6=list(A[:,3][4:6])+list(A[:,4][4:6])+list(A[:,5][4:6])
	if len(set(b))==len(b) and len(set(c))==len(c) and len(set(d))==len(d) and len(set(e))==len(e) and len(set(f))==len(f) and len(set(q1))==len(q1) and len(set(q2))==len(q2) and len(set(q3))==len(q3) and len(set(q4))==len(q4) and len(set(q5))==len(q5) and len(set(q6))==len(q6):
			print(a)
			print(b)
			print(c)
			print(d)
			print(e)
			print(f)
			
			break

# ~ c=[lista1[i][2],lista2[i][2],lista3[i][2],lista4[i][2],lista5[i][2],lista6[i][2]]	
# ~ b=[lista1[i][1],lista2[i][1],lista3[i][1],lista4[i][1],lista5[i][1],lista6[i][1]]
# ~ c=[lista1[i][2],lista2[i][2],lista3[i][2],lista4[i][2],lista5[i][2],lista6[i][2]]
# ~ d=[lista1[i][3],lista2[i][3],lista3[i][3],lista4[i][3],lista5[i][3],lista6[i][3]]
# ~ e=[lista1[i][4],lista2[i][4],lista3[i][4],lista4[i][4],lista5[i][4],lista6[i][4]]
# ~ f=[lista1[i][5],lista2[i][5],lista3[i][5],lista4[i][5],lista5[i][5],lista6[i][5]]
# ~ def ciao:
	# ~ for i in range(len(lista1)):	
				# ~ b=[lista1[i][1],lista2[i][1],lista3[i][1],lista4[i][1],lista5[i][1],lista6[i][1]]
				# ~ c=[lista1[i][2],lista2[i][2],lista3[i][2],lista4[i][2],lista5[i][2],lista6[i][2]]	
				# ~ b=[lista1[i][1],lista2[i][1],lista3[i][1],lista4[i][1],lista5[i][1],lista6[i][1]]
				# ~ c=[lista1[i][2],lista2[i][2],lista3[i][2],lista4[i][2],lista5[i][2],lista6[i][2]]
				# ~ d=[lista1[i][3],lista2[i][3],lista3[i][3],lista4[i][3],lista5[i][3],lista6[i][3]]
				# ~ e=[lista1[i][4],lista2[i][4],lista3[i][4],lista4[i][4],lista5[i][4],lista6[i][4]]
				# ~ f=[lista1[i][5],lista2[i][5],lista3[i][5],lista4[i][5],lista5[i][5],lista6[i][5]]
			# ~ for j1,j2,j3,j4,j5,j6 in zip(lista1,lista2,lista3,lista4,lista5,lista6):
				# ~ b.append(j1)
			# ~ print(b)
				
				# ~ print(a)
				# ~ if len(set(a))==len(a) and len(set(b))==len(b) and len(set(c))==len(c):
					# ~ print(a)
					# ~ print(b)
					# ~ print(c)
					# ~ print(d)
					# ~ print(e)
					# ~ print(f)
					# ~ print()
					# ~ break

		# ~ print(len(lista1))
	# ~ print(len(lista2))
	# ~ print(len(lista3))
	# ~ print(len(lista4))
	# ~ print(len(lista5))
	# ~ print(len(lista6))
	# ~ print(lista1)
	# ~ print(lista2)
# ~ print(lista3)
# ~ print(lista4)
# ~ print(lista5)
# ~ print(lista6)
	# ~ if x[0]==ciao[0]:
		# ~ lista1=x
	# ~ if x[1]==ciao[1]:
		# ~ lista2=x
	# ~ if x[2]==ciao[2]:
		# ~ lista3=x
	# ~ if x[3]==ciao[3]:
		# ~ lista4=x
	# ~ if x[4]==ciao[4]:
		# ~ lista5=x
	# ~ if x[5]==ciao[5]:
		# ~ lista6=x
		
# ~ print(ciao)
# ~ print(lista[0])	
# ~ print(lista1)
# ~ print(lista2)
# ~ print(lista3)
# ~ print(lista4)
# ~ print(lista5)
# ~ print(lista6)
# ~ print(lista1)

	# ~ for u,b in zip(ciao,x):
		# ~ if u[0]==b[0]:
			# ~ print(u)
		# ~ print(ciao[i])
# ~ for b in ciao:
	
		# ~ if x[0]==b:
			# ~ pass
	# ~ print(b)
		

			# ~ ok="ok"
	# ~ if ok=="ok":
		# ~ lista.append(y)
# ~ print(lista)
			# ~ print(x)
			# ~ break
	# ~ break
