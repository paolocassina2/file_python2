import numpy as np
print("generatore di sudoku 6*6")
#https://www.programiz.com/python-programming/matrix
from itertools import permutations
		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
# ~ a1 = list(permutations(range(1, 7)))
# ~ b1 = list(permutations(range(1, 7)))
# ~ c1 = list(permutations(range(1, 7)))
# ~ d1 = list(permutations(range(1, 7)))
# ~ e1 = list(permutations(range(1, 7)))
# ~ f1 = list(permutations(range(1, 7)))

from itertools import permutations
		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
listapermutazioni = list(permutations(range(1, 7)))
# ~ print(listapermutazioni)
# ~ print(a1)
soluz1="fdkj"
# ~ if soluz1!="ok":

# ~ A=[["a","b","c","d"],["e","F","g","h"],,["e","F","g","h"],,["e","F","g","h"]]
# ~ print("dkfkl",A[0][0],A[0][1])
#00	01	02	03 04 05
#10	11	12	13 14 15
#20 21	22	23 24 25
#30	31	32	33 34 35
#40 41 42   43 44 45	
#50  51 52 53  54 55
#
a1=[2,   8,   14,   20,    26    ,  32 ]
b1=[3,   9,   15,   21 ,    27    ,  33 ]
c1=[4   ,10,  16,   22   , 28    ,  34]
d1=[5,   11,  17,   23  ,   29   ,   35 ]
e1=[6,   12,  18,   24  ,   30    ,  36]
f1=[7,   13,  19,   25   ,  31   ,   37]
# ~ q1=[A[0][0],A[0][1],A[1][0],A[1][1]]

# ~ q2=[A[0][2],A[0][3],A[1][2],A[1][3]]

# ~ q3=[A[2][0],A[2][1],A[3][0],A[3][1]]

# ~ q4=[A[2][2],A[2][3],A[3][2],A[3][3]]
# ~ a1=[2,6,10,14]
# ~ b1=[3,7,11,15]
# ~ c1=[4,8,12,16]
# ~ d1=[5,9,13,17]
A = np.array([a1, 
						b1,c1,d1,e1,f1]
								)
# ~ print(A[:,0][0:4])
# ~ q1=list(A[:,0][0:2])+list(A[:,1][0:2])+list(A[:,2][0:2])
# ~ q2=list(A[:,3][0:2])+list(A[:,4][0:2])+list(A[:,5][0:2])
# ~ q3=list(A[:,0][2:4])+list(A[:,1][2:4])+list(A[:,2][2:4])
# ~ q4=list(A[:,3][2:4])+list(A[:,4][2:4])+list(A[:,5][2:4])
# ~ q5=list(A[:,0][4:6])+list(A[:,1][4:6])+list(A[:,2][4:6])
# ~ q6=list(A[:,3][4:6])+list(A[:,4][4:6])+list(A[:,5][4:6])
# ~ q3=list(A[:,0][2:4])+list(A[:,1][2:4])
# ~ q4=list(A[:,2][2:4])+list(A[:,3][2:4])
# ~ print(type(q1))
# ~ print(q1)
# ~ print(q2)
# ~ print(q3)
# ~ print(q4)
# ~ print(q5)
# ~ print(q6)
# ~ print(type(list(A[:,0][0:2]))
# ~ q2=A[:,2][0:2]
# ~ q3=A[:,0][0:2]
# ~ q4=A[:,0][0:2]

# ~ b = a[:][0:2]
ciao=""
# ~ print(q1)
import random
soluz2=""
contatore=0
# ~ def caio():
listasoluzioni=[]
lista_a=[]
lista_b=[]
lista_c=[]
lista_d=[]
lista_e=[]
lista_f=[]
while contatore<100:#a volte scorre lista permutazioni, a volte la sceglie a caso
		if soluz2=="ok":
			soluz1=""
		for a in listapermutazioni:
			a1=list(a)
			if soluz1=="ok":
					break
				# ~ print(a1)
			# ~ for b in listapermutazioni:
			b=random.choice(listapermutazioni)	
			b1=list(b)
			# ~ print(b1)
			A = np.array([a1, 
							b1]
								)
								
			q1=list(A[:,0][0:2])+list(A[:,1][0:2])+list(A[:,2][0:2])
			q2=list(A[:,3][0:2])+list(A[:,4][0:2])+list(A[:,5][0:2])
			# ~ q1=list(A[:,0][0:2])+list(A[:,1][0:2])
			# ~ q2=list(A[:,2][0:2])+list(A[:,3][0:2])
			# ~ q3=list(A[:,0][2:4])+list(A[:,1][2:4])
			# ~ q4=list(A[:,2][2:4])+list(A[:,3][2:4])
			# ~ q1=[A[0][0],A[0][1],A[1][0],A[1][1]]

			# ~ q2=[A[0][2],A[0][3],A[1][2],A[1][3]]

			# ~ q3=[A[2][0],A[2][1],A[3][0],A[3][1]]

			# ~ q4=[A[2][2],A[2][3],A[3][2],A[3][3]]
			if soluz1=="ok":
				break
			if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]) and len(set(A[:,4]))==len(A[:,4]) and len(set(A[:,5]))==len(A[:,5]) and len(set(q1))==len(q1) and len(set(q2))==len(q2):
				# ~ print("ok!A")
				c=random.choice(listapermutazioni)
				# ~ for c in listapermutazioni:
				if soluz1=="ok":
					break
				c1=list(c)
				A = np.array([a1, 
						b1,c1]
							)
				# ~ print(A)
				if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]) and len(set(A[:,4]))==len(A[:,4]) and len(set(A[:,5]))==len(A[:,5]):
					# ~ print(A)
					for d in listapermutazioni:
						# ~ q1=[A[0][0],A[0][1],A[1][0],A[1][1]]

						# ~ q2=[A[0][2],A[0][3],A[1][2],A[1][3]]

						# ~ q3=[A[2][0],A[2][1],A[3][0],A[3][1]]

						# ~ q4=[A[2][2],A[2][3],A[3][2],A[3][3]]
						d1=list(d)
						A = np.array([a1, 
						b1,c1,d1]
							)	
						q1=list(A[:,0][0:2])+list(A[:,1][0:2])+list(A[:,2][0:2])
						q2=list(A[:,3][0:2])+list(A[:,4][0:2])+list(A[:,5][0:2])
						q3=list(A[:,0][2:4])+list(A[:,1][2:4])+list(A[:,2][2:4])
						q4=list(A[:,3][2:4])+list(A[:,4][2:4])+list(A[:,5][2:4])
						if soluz1=="ok":
							break
						
						
						if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]) and len(set(A[:,4]))==len(A[:,4]) and len(set(A[:,5]))==len(A[:,5]) and len(set(q1))==len(q1) and len(set(q2))==len(q2) and len(set(q3))==len(q3) and len(set(q4))==len(q4) :
							# ~ print(A)
							# ~ soluz1="ok"
							for e in listapermutazioni:
								e1=list(e)
								A = np.array([a1, 
									b1,c1,d1,e1]
										)	
								if soluz1=="ok":
									break
								if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]) and len(set(A[:,4]))==len(A[:,4]) and len(set(A[:,5]))==len(A[:,5])  :
									
									for f in listapermutazioni:
										f1=list(f)
										A = np.array([a1, 
										b1,c1,d1,e1,f1]
											)	
							# ~ breakq1=list(A[:,0][0:2])+list(A[:,1][0:2])+list(A[:,2][0:2])
										q1=list(A[:,0][0:2])+list(A[:,1][0:2])+list(A[:,2][0:2])
										q2=list(A[:,3][0:2])+list(A[:,4][0:2])+list(A[:,5][0:2])
										q3=list(A[:,0][2:4])+list(A[:,1][2:4])+list(A[:,2][2:4])
										q4=list(A[:,3][2:4])+list(A[:,4][2:4])+list(A[:,5][2:4])
										q5=list(A[:,0][4:6])+list(A[:,1][4:6])+list(A[:,2][4:6])
										q6=list(A[:,3][4:6])+list(A[:,4][4:6])+list(A[:,5][4:6])
										if soluz1=="ok":
												break
										if len(set(A[:,0]))==len(A[:,0]) and len(set(A[:,1]))==len(A[:,1]) and len(set(A[:,2]))==len(A[:,2]) and len(set(A[:,3]))==len(A[:,3]) and len(set(A[:,4]))==len(A[:,4]) and len(set(A[:,5]))==len(A[:,5]) and len(set(q1))==len(q1) and len(set(q2))==len(q2) and len(set(q3))==len(q3) and len(set(q4))==len(q4) and len(set(q5))==len(q5)and len(set(q6))==len(q6) :
												print("soluzione")
												print(A)
												A1=[a1,b1,c1,d1,e1,f1]
												soluz1="ok"
												soluz2="ok"
												ciao=""
												contatore=contatore+1
												print("contatore",contatore)
												lista_a.append(a1)
												lista_b.append(b1)
												lista_c.append(c1)
												lista_d.append(d1)
												lista_e.append(e1)
												lista_f.append(f1)
												print()
												print()		
												break
												
matrice1=[]												
for aa,bb,cc,dd,ee,ff in zip(lista_a,lista_b,lista_c,lista_d,lista_e,lista_f):
	matrice=[aa,bb,cc,dd,ee,ff]
	matrice1.append(matrice)
	for x in matrice:
		print(x)
		
	print()
# ~ print ("The original list is : " + str(matrice1))
  
print(type(matrice1))
# ~ [1, 5, 2, 4, 6, 3]
# ~ [6, 3, 4, 5, 2, 1]
# ~ ùùùùùùùùùùùùùù

# ~ [1, 4, 6, 3, 2, 5]
# ~ [5, 3, 2, 6, 4, 1]
# ~ [4, 2, 1, 5, 3, 6]
# ~ [3, 6, 5, 2, 1, 4]
# ~ [2, 5, 4, 1, 6, 3]
# ~ [6, 1, 3, 4, 5, 2]
	# ~ print(matrice)
# ~ print(listasoluzioni)
# ~ print(len(set(listasoluzioni)))
# ~ print(len(list(listasoluzioni)))
# ~ lista1=set(listasoluzioni)
# ~ print(len(lista1))
# ~ addd=[[1, 4, 2, 3, 5, 6],
 # ~ [6, 3 ,5 ,4 ,1 ,2],
 # ~ [5 ,6 ,1 ,2 ,4 ,3],
 # ~ [3 ,2 ,4 ,1 ,6 ,5],
 # ~ [2 ,1 ,6 ,5, 3 ,4],
 # ~ [4 ,5, 3 ,6 ,2 ,1]]
# ~ addd1=[[1, 4, 2, 3, 5, 6],
 # ~ [6, 3 ,5 ,4 ,1 ,2],
 # ~ [5 ,6 ,1 ,2 ,4 ,3],
 # ~ [3 ,2 ,4 ,1 ,6 ,5],
 # ~ [2 ,1 ,6 ,5, 3 ,4],
 # ~ [4 ,5, 3 ,6 ,2 ,1]]
# ~ soluzione
# ~ bddd=[[2, 5 ,1 ,3, 6 ,4],
 # ~ [4 ,6, 3 ,5 ,2, 1],
 # ~ [6, 2, 4 ,1, 5 ,3],
 # ~ [1 ,3, 5 ,2, 4, 6],
 # ~ [3 ,4 ,2, 6, 1 ,5],
 # ~ [5 ,1 ,6 ,4 ,3 ,2]]
# ~ if addd==addd1:
	# ~ print("abla")
 
# ~ soluzione							
								
	# ~ print("af",A[:,0])
			# ~ if len(set(a1[:,0]))==len(a1[:,0]) and  len(set(b1[:,0]))==len(b1[:,0]):
				# ~ print(A)
			# ~ break
		# ~ A = np.array([a1, 
						# ~ b1,
							# ~ c1,d1])

		# ~ for b in listapermutazioni:
			# ~ b1=list(b)
		# ~ print(b1)
def ciao():
		# ~ print(f1)
	a1=list(a)
	b1=list(b)
	c1=list(c)

	d1=list(d)
	import numpy as np
	# ~ a=[1, 4, 5, 12]
	# ~ b=  [-5, 8, 9, 0]
	# ~ c=[-6, 7, 11, 19]
	# ~ A = np.array(
	A = np.array([a1, 
					b1,
						c1,d1])

	print("A[:,0] =",a1[:,0]) 
	print("A[:,1] =",a1[:,1]) 
	print("A[:,2] =",a1[:,2]) 
	print("A[:,2] =", a1[:,3])
