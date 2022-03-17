import numpy as np#funziona
a = np.array([[7, 7, 7],[8, 3, 3],[4, 4,8]])
# ~ print(a)               # Output: [1, 2, 3]
# ~ print(type(a))         # Output: <class 'numpy.ndarray'>

###CARTELLA==matrici
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
print(m1)

m2 = np.array([[a[1][0],a[2][0]],[a[1][2],a[2][2]]])
# ~ m2=a[1:,1:]
print(m2)
m3=a[1:,:-1]
print(m3)
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
print(determinante)
# ~ print(round(determinante,2))
	# ~ print(contatore)
	# ~ 
	# ~ print
	# ~ print(y)
	# ~ print(x)
	# ~ print(a[0][x])
# ~ print(det(m3))
# ~ print(np.linalg.det(m3))
