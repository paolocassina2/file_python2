
a=[9,5,"x","x","X","x",1,"x","x"]
b=["x",8,6,"x",9,"X",7,"x","x"]
c=["x","x",7,8,"X",1,"X",9,"x"]

d=["x",6,"x","x",8,2,"X",1,"x"]
e=["x",1,"x","x",4,9,"X","x","x"]
f=[2,"x",4,7,"X","x",5,8,"x"]

g=[3,4,"x","x","X","x","X","x",6]
h=[8,"x","x",9,"X","x","X","x",1]
i=["x","x","x",4,2,"x","X","x",9]

# ~ x = 1.23
# ~ x_int = x.is_integer()
# ~ Check if x is an integer


# ~ print(x_int)

# ~ numeri.append(b,c)
# ~ print(numeri)
# ~ for x in numeri:
	# ~ if x is not int:
		# ~ print(x," ciao",type(x))
import random
# ~ if aaa[0]!="0":

# the use of sample() function .
  
from random import sample
  
# Prints list of random items of given length
list1 = [1, 2, 3, 4, 5,6,7,8,9] 
# ~ x = 1.0
listaindici=[]
listavalori=[]
for x in a:
	x_int = isinstance(x, int)
	# ~ Check if x is an integer
	if x_int==True:
		
		print(x_int)
		print(a.index(x))
		listaindici.append(a.index(x))
		listavalori.append(x)
		
print(listaindici)
print("val",listavalori)
# ~ for u in listaindici:
	# ~ if numeri[u]==2:
		# ~ print("ciao")  
	# Prints list of random i

# ~ while True:  
# ~ print(type(anagramma))
# ~ print(anagramma)
	# ~ print(sample(list1,9))
# ~ def abc():
# ~ for j,k in zip(listaindici,listavalori):
	# Prints list of random items of given length
		# ~ if numeri[j]==listavalori[j]:
			# ~ print(j)
def checkuniqueelements():
	test_list = [1, 3,7, 6, 7]
	  
	# printing original list 
	print ("The original list is : " + str(test_list))
	  
	flag = 0
	  
	# using naive method 
	# to check all unique list elements
	for i in range(len(test_list)):
			for i1 in range(len(test_list)):
				if i != i1:
					if test_list[i] == test_list[i1]:
						flag = 1
	  
	  
	# printing result
	if(not flag) :
		print ("List contains all unique elements")
	else : 
		print ("List contains does not contains all unique elements")



# ~ checkuniqueelements()
risultato=[]		
while True:		
	while True:
		anagramma=sample(list1,9)

			# ~ for x,j in listaindici, listavalori:
		if anagramma[0]==9 and anagramma[1]==5 and anagramma[6]==1:
				# ~ print(anagramma)
			break
		
			
	while True:
		anagramma1=sample(list1,9)	# ~ for x,j in listaindici, listavalori:
		if anagramma1[1]==8 and anagramma1[2]==6 and anagramma1[4]==9 and anagramma1[6]==7:
					# ~ print(anagramma1)
				# ~ pass
			break
				# ~ continue	
	while True:		
			
		anagramma2=sample(list1,9)	
		if anagramma2[2]==7 and anagramma2[3]==8 and anagramma2[5]==1 and anagramma2[7]==9:
						
				# ~ continue	
				# ~ print(anagramma2)
			break


	#while True:		
			
		#anagramma3=sample(list1,9)	
		#if anagramma3[1]==6 and anagramma3[4]==8 and anagramma3[5]==2  and anagramma3[7]==1 :
						
					
				# ~ print(anagramma2)
			#break
	while True:
		primoquadrato = [anagramma[0],anagramma1[0],anagramma2[0],anagramma[1],anagramma1[1],anagramma2[1],anagramma[2],anagramma1[2],anagramma2[2]]
			
		secondoquadrato = [anagramma[3],anagramma1[3],anagramma2[3],anagramma[4],anagramma1[4],anagramma2[4],anagramma[5],anagramma1[5],anagramma2[5]]
		
		terzoquadrato = [anagramma[6],anagramma1[6],anagramma2[6]
		,anagramma[7],anagramma1[7],anagramma2[7],
		anagramma[8],anagramma1[8],anagramma2[8]]
		
		
		#colonne
		#questo programma cerca una  soluzione per le prime 5 colonne
		primacolonna = [anagramma[0],anagramma1[0],anagramma2[0]]
		secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1]]
		terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2]]
		quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3]]
		quintacolonna=[anagramma[4],anagramma1[4],anagramma2[4]]
		sestacolonna=[anagramma[5],anagramma1[5],anagramma2[5]]
		settimacolonna=[anagramma[6],anagramma1[6],anagramma2[6]]
		ottavacolonna=[anagramma[7],anagramma1[7],anagramma2[7]]
		nonacolonna=[anagramma[8],anagramma1[8],anagramma2[8]]
	
		#primacolonna = [anagramma[0],anagramma1[0],anagramma2[0],anagramma3[0]]
	#	secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1],anagramma3[1]]
		#terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2],anagramma3[2]]
		#quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3],anagramma3[3]]
		#quintacolonna=[anagramma[4],anagramma1[4],anagramma2[4],anagramma3[4]]
	#	sestacolonna=[anagramma[5],anagramma1[5],anagramma2[5],anagramma3[5]]
	#	settimacolonna=[anagramma[6],anagramma1[6],anagramma2[6],anagramma3[6]]
	#	ottavacolonna=[anagramma[7],anagramma1[7],anagramma2[7],anagramma3[7]]
	#	nonacolonna=[anagramma[8],anagramma1[8],anagramma2[8],anagramma3[8]]
		
		# ~ Alist = ['Mon','Tue','Wed',"Tue"]
		# ~ print("The given list : ",Alist)

		# Compare length for unique elements

		if(len(set(primacolonna)) == len(primacolonna) and len(set(secondacolonna)) == len(secondacolonna)and len(set(terzacolonna)) == len(terzacolonna)and len(set(quartacolonna)) == len(quartacolonna) and len(set(quintacolonna)) == len(quintacolonna) ) and len(set(sestacolonna)) == len(sestacolonna) and len(set(settimacolonna)) == len(settimacolonna) and len(set(ottavacolonna)) == len(ottavacolonna) and len(set(nonacolonna)) == len(nonacolonna) and len(set(primoquadrato)) == len(primoquadrato) and len(set(secondoquadrato)) == len(secondoquadrato) and len(set(terzoquadrato)) == len(terzoquadrato):
    		
			print("All elements are unique.")
				
				
			print(anagramma)
			print(anagramma1)
			print(anagramma2)
			break