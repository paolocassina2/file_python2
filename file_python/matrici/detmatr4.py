import numpy as np#funziona
###CARTELLA==matrici
def determinante_treXtre():
	a = np.array([[g, h, j],[k, l, m],[n, o,p]])
	# ~ print(a)               # Output: [1, 2, 3]
	# ~ print(type(a))         # Output: <class 'numpy.ndarray'>

	print(a)
	# ~ print("k",a[1][1])
	# ~ for i in range(len(a)):
	# ~ m1=[a1[1]]	
		# ~ print(a[:,i])
	# ~ m1=[a[1][1],a[1][2],a[2][1],a[2][2]]
	# ~ print(m1)
	# ~ m2=[a[1][0],a[2][0],a[1][2],a[2][2]]
	# ~ print(m2)
	# ~ m3=[a[1][0],a[2][0],a[1][1],a[2][1]]
	# ~ print(m3)
	m1=a[1:,1:]
	# ~ print(m1)

	m2 = np.array([[a[1][0],a[2][0]],[a[1][2],a[2][2]]])
	# ~ m2=a[1:,1:]
	# ~ print(m2)
	m3=a[1:,:-1]
	# ~ print(m3)
	lista=[m1,m2,m3]
	contatore=0
	somma=0
	# ~ print(np.linalg.det(m1))
	# ~ print(np.linalg.det(m2))
	# ~ print(np.linalg.det(m3))
	for x,y in zip(range(len(a)),lista) :
		contatore=contatore+1
		# ~ print(np.linalg.det(y))
		if contatore%2!=0:
			somma=somma+1*(a[0][x])*np.linalg.det(y)
		else:
			somma=somma-1*(a[0][x])*np.linalg.det(y)
	determinante=somma
	return determinante
	
def jdskf():	
	while True:
		g, h, j,k, l, m,n, o,p=int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n")),int(input("n"))
		
		print("determinante	",determinante_treXtre())
		print()
		
		
g, h, j,k, l, m,n, o,p=1,2,3,45,66,7,8,9,6		
a = np.array([[g, h, j],[k, l, m],[n, o,p]])
print(a)
cc=[]
dd=[]
ee=[]

for i in range(0,3):
		n2=list(a[:,i])
		n2.pop(0)
		if i >0:
			cc.append(n2)
		if i<2:
			dd.append(n2)
		if i!=1:
			ee.append(n2)
		# ~ print (m2)
			# ~ cc=[cc+m2]
	# ~ print(determinante)
# ~ print(round(determinante,2))
	# ~ print(contatore)
print(cc)
print(dd)
print(ee)

m1=np.array(cc)
	# ~ print(m1)

m2 = np.array(dd)
	# ~ m2=a[1:,1:]
m3= np.array(ee)
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
