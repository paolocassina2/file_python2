a=[4,"x","x","x",2,6]

# ~ b=[4,"x","x","x",2,6]
b=["x","x",6,5,"x",4]
c=[6,1,2,4,"x",3]
d=["x","x","x","x",6,"x"]
e=[2,6,"x","x",4,"x"]
f=["x",4,5,6,3,"x"]
# ~ print(a,b,c,d,e,f)
conta1=-1
lista_num1=[]
lista_pos1=[]
for x in a:
	conta1+=1
	if x!="x":
		lista_num1.append(x)
	else:
		lista_pos1.append(conta1)
soluz1=[]
# ~ lista_perm1=[[x for x in range(1,6)]-lista_num1]
# ~ print(lista_perm1)
lista_numeri_mancanti1=[1,2,3,4,5,6]
for x in lista_num1:
	lista_numeri_mancanti1.remove(x)
from itertools import permutations 
perm = permutations(lista_numeri_mancanti1, len(lista_num1)) 
for x in perm:
	for j,k,z in zip(a,x,lista_pos1):
		if x=="x":
			a[z]=k
		else:
			a[z]=j
		
	print(a)
		
	
	
	# ~ for j in lista_pos1:
		# ~ soluz1[j]=
# ~ print(lista_perm1)
# ~ print(lista_pos1)
# ~ print(perm)
# ~ print(lista_num1)

	# ~ permutazioni1.remove(x)
# ~ print(permutazioni1)
# ~ print(lista_pos1)
# ~ for n in lista_num1:
	# ~ lista_perm1.remove(n)
# ~ print(lista_perm1)
# ~ from itertools import permutations 
	  
	# Get all permutations of length 2 
	# and length 2 
# ~ perm = permutations([1, 2, 3,4,5,6], 6) 
	  
	# Print the obtained permutations 
# ~ for i in list(perm): 
		# ~ print (i) 
from itertools import permutations 
	  
	# Get all permutations of length 2 
	# and length 2 
# ~ perm = permutations(permutazioni1, len(permutazioni1))
# ~ perm1=[list(x) for x in perm ]
# ~ print("gf",perm1)
# ~ print(perm) ù
# ~ soluz1=[]

	# ~ print(x)
	# ~ for j in a:
	# ~ for j in perm1:
		# ~ if x=="x":
				# ~ soluz1.append(x)
		# ~ else:
				# ~ soluz1.append(j)
	# ~ print(soluz1)
	# ~ soluz1=[]
# ~ for x,j in zip(perm,a):
	# ~ if j=="x":
		# ~ perm[lista_pos1]=lista_num1
# ~ print(perm)
	
# ~ for i,j,k in zip(list(perm),lista_num1,lista_pos1): 
	# ~ for x in # ~ lista=[
	# ~ lista=[i]
def ciao():

 # ~ permutations of given length 
	from itertools import permutations 
	  
	# Get all permutations of length 2 
	# and length 2 
	perm = permutations([1, 2, 3,4,5,6], 6) 
	  
	# Print the obtained permutations 
	for i in list(perm): 
		print (i) 
	# ~ a=[x for x in range(6)]
	# ~ b=[x for x in range(6)]
	# ~ c=[x for x in range(6)]
# ~ d=[x for x in range(6)]
# ~ e=[x for x in range(6)]
# ~ f=[x for x in range(6)]
