#eigenvalues
import numpy as np
from sympy.solvers import solve
from sympy import Symbol
x=Symbol("x")
from sympy import Eq
λ= Symbol("λ")#sarebbe lambda
λ1= Symbol("λ1")
λ2= Symbol("λ2")
v1= Symbol("v1")
v2= Symbol("v2")
# ~ v1=0
# ~ v2=0
import random
n1,n2,n3,n4=random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9)
# ~ a=[n1,n2,n3,n4]
a=[2,1,1,2]
# ~ print(a)

for i in range(len(a)):
	if i==0 or i==3:
		a[i]=a[i]-λ
determinante=a[0]*a[3]-a[1]*a[2]
# ~ print(determinante)

# ~ jkj=determinante==0
# ~ print(jkj)
eigenvalues=solve(a[0]*a[3]-a[1]*a[2],λ)
# ~ print("eigenvalues",eigenvalues)
λ1=eigenvalues[0]
λ2=eigenvalues[1]
from numpy import matrix
ab=matrix([2,1,1,2])
# ~ ab2=matrix([v1,v2])
# ~ print(ab[",:1"])

# ~ sol=solve(eq1,λ1)
# ~ print(sol)
# ~ print(type(ab2))
print(λ2)
# ~ sol=solve(eq1,eq2,v1)
# ~ print(eq1)
list2=[[v1],
        [v2],
        ]
#vector as column
#equazionegiusta>----------matrice*vettore=lambda*vettore
# ~ print(vector2)
# ~ print(type(vector2))

list2=[[v1],
         [v2],
         ]

# ~ print(eq1)
# ~ print(eq2)
# ~ import randome
# ~ while True:
	# ~ v1=random.randint(1,9)
	# ~ v2=random.randint(1,9)
vector = np.array(list2)
eq1=vector*ab
	# ~ print(prod1)
eq2=λ2*vector
# ~ eq2=prod1/λ2
# ~ print(solve(eq1,eq2.),vector,v1)

	# ~ print(eq1.all())
	# ~ if eq1.any()==eq2.any():
print(eq1)
print(eq2)
	# ~ if eq1==eq2:
		# ~ print(eq1)
	# ~ print(eq2)
# ~ print(v1)
# ~ print(v2)
# ~ soluz=solve(prod1,eq2,v1,v2)
# ~ print(soluz)
# ~ print(eq2)
# ~ print(Solve(eq1,eq2))
# ~ sol=solve(eq1,eq2)

###CARTELLA==matematica