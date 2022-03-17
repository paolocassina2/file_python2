import numpy as np#funziona

###CARTELLA==matrici
def determinante_treXtre():
	
# ~ g, h, j,k, l, m,n, o,p=1,2,3,4,5,6,7,8,9
# ~ a = np.array([[g, h, j],[k, l, m],[n, o,p]])		
	cc=[]
	dd=[]
	ee=[]
	# ~ print(a)
	for i in range(0,3):
		n2=list(a[:,i])
		n2.pop(0)
		# ~ n2.T

		if i >0:
			
			cc.append(n2)
		if i<2:
			ee.append(n2)
		if i!=1:
			dd.append(n2)
		# ~ print (m2)
			# ~ cc=[cc+m2]
		# ~ print(determinante)
	# ~ print(round(determinante,2))
		# ~ print(contatore)
	# ~ print(cc)
	# ~ print(dd)
	# ~ print(ee)

	m1=np.array(cc)
	# ~ print(m1)
	m1_1=m1.transpose()
	m2 = np.array(dd)
	m2_2 = m2.transpose()
		# ~ m2=a[1:,1:]
	m3= np.array(ee)
	m3_3=m3.transpose()
	# ~ m1.transpose()
	# ~ print(m1_1)
	# ~ print(m2_2)
	# ~ print(m3_3)

	# ~ print(np.linalg.det(m1))
	 # ~ np.array(dd)
	# ~ print(m1)
	# ~ print(m3)
	lista=[m1_1,m2_2,m3_3]
	contatore=0
	somma=0
	# ~ print(np.linalg.det(m2))
	# ~ print(np.linalg.det(m2))
	# ~ print(np.linalg.det(m3))

	for x,y in zip(range(len(a)),lista) :
			contatore=contatore+1
			# ~ print(np.linalg.det(y))
			if contatore%2!=0:
				somma=somma+1*(a[0][x])*np.linalg.det(y)
			else:
				somma=somma-1*(a[0][x])*np.linalg.det(y)
	determinante=round(somma,2)
	# ~ print(determinante)
	return determinante
	# ~ g, h, j,k, l, m,n, o,p=1,2,3,45,66,7,8,9,6		
	# ~ a = np.array([[g, h, j],[k, l, m],[n, o,p]])
	# ~ print(a)

# ~ print(m2)
	

while True:
			g, h, j,k, l, m,n, o,p=int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n"))
			a = np.array([[g, h, j],[k, l, m],[n, o,p]])
			print("determinante	",determinante_treXtre())
			print()




# ~ m3=np.array([[a[1][0],a[2][0]],[a[1][2],a[2][2]]])
# ~ print
# ~ print(y)
# ~ print(x)
# ~ print(a[0][x])
# ~ print(ee)

# ~ m2=a[1:,1:]
	
# ~ g, h, j,k, l, m,n, o,p=1,2,3,45,66,7,8,9,6		
# ~ a = np.array([[g, h, j],[k, l, m],[n, o,p]])
# ~ print(a)

# ~ print(m3)
# ~ print(np.linalg.det(m1))
# ~ np.array(dd)
# ~ print(m1)
	# ~ print(m2)
# ~ m3=np.array([[a[1][0],a[2][0]],[a[1][2],a[2][2]]])
	# ~ print
	# ~ print(y)
	# ~ print(x)
	# ~ print(a[0][x])
# ~ print(det(m3))
# ~ print(np.linalg.det(m3))
