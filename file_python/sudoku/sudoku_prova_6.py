
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
def ciao():
	print("ciao2""")
	Alist = ['Mon','Tue','Wed',"Tue"]
	print("The given list : ",Alist)

	# Compare length for unique elements
	if(len(set(Alist)) == len(Alist)):

	   print("All elements are unique.")
	else:
	   print("All dfdfelements are not unique.")
	
ciao()
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
			# ~ continue
	# ~ while True:
		
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
	
	

	# ~ while True:		
		
		# ~ anagramma3=sample(list1,9)	
		# ~ if anagramma3[1]==6 and anagramma3[4]==8 and anagramma3[5]==2  and anagramma3[7]==1 :
					
				
			# ~ print(anagramma2)
			# ~ break
	# ~ while True:		
				
			# ~ anagramma4=sample(list1,9)	
			# ~ if anagramma4[1]==6 and anagramma4[4]==8 and anagramma4[5]==2  and anagramma4[7]==1 :
						
					
				# ~ print(anagramma2)
				# ~ break		
	# ~ while True:		
		
		# ~ anagramma4=sample(list1,9)	
		# ~ if anagramma4[1]==1 and anagramma4[4]==4 and  anagramma4[5]==9:
					
				
			# ~ print(anagramma2)
			# ~ break
	# ~ if anagramma[0]!=anagramma1[0]		
	# ~ print()
	# ~ def ciao():
	
	# ~ while True:
		# ~ anagramma4=sample(list1,9)	
		# ~ if anagramma4[1]==1 and anagramma4[4]==4 and anagramma4[5]==9:

			# ~ e=["x",1,"x","x",4,9,"X","x","x"]
				
					
				# ~ print(anagramma2)
				# ~ break
	# ~ def ciaodfd():
	
	
	#quadrati
	primoquadrato = [anagramma[0],anagramma1[0],anagramma2[0]
	,anagramma[1],anagramma1[1],anagramma2[1],
	anagramma[2],anagramma1[2],anagramma2[2]]
		
	secondoquadrato = [anagramma[3],anagramma1[3],anagramma2[3]
	,anagramma[4],anagramma1[4],anagramma2[4],
	anagramma[5],anagramma1[5],anagramma2[5]]
	
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
	
	
	# ~ Alist = ['Mon','Tue','Wed',"Tue"]
	# ~ print("The given list : ",Alist)

	# Compare length for unique elements
	if(len(set(primacolonna)) == len(primacolonna) and len(set(secondacolonna)) == len(secondacolonna)and len(set(terzacolonna)) == len(terzacolonna)and len(set(quartacolonna)) == len(quartacolonna) and len(set(quintacolonna)) == len(quintacolonna) ) and len(set(sestacolonna)) == len(sestacolonna) and len(set(settimacolonna)) == len(settimacolonna) and len(set(ottavacolonna)) == len(ottavacolonna) and len(set(nonacolonna)) == len(nonacolonna) and len(set(primoquadrato)) == len(primoquadrato) and len(set(secondoquadrato)) == len(secondoquadrato) and len(set(terzoquadrato)) == len(terzoquadrato):
		
	   print("All elements are unique.")
	   
	   
	   print(anagramma)
	   print(anagramma1)
	   print(anagramma2)
	   break
	# ~ else:
	   # ~ print("All dfdfelements are not unique.")
		#############
	#############	#############	#############	#############	#############	#############
	# ~ primacolonna = [anagramma[0],anagramma1[0],anagramma2[0],anagramma3[0]]
	# ~ secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1],anagramma3[1]]
	# ~ terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2],anagramma3[2]]
	# ~ quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3],anagramma3[3]]
	# ~ quintacolonna=[anagramma[4],anagramma1[4],anagramma2[4],anagramma3[4]]
	# ~ sestacolonna=[anagramma[5],anagramma1[5],anagramma2[5],anagramma3[5]]
	# ~ settimacolonna=[anagramma[6],anagramma1[6],anagramma2[6],anagramma3[6]]
	# ~ ottavacolonna=[anagramma[7],anagramma1[7],anagramma2[7],anagramma3[7]]
	# ~ nonacolonna=[anagramma[8],anagramma1[8],anagramma2[8],anagramma3[8]]
	#############	#############	#############	#############	#############	#############
	# ~ primacolonna = [anagramma[0],anagramma1[0],anagramma2[0],anagramma3[0],anagramma4[0]]
	# ~ secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1],anagramma3[1],anagramma4[1]]
	# ~ terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2],anagramma3[2],anagramma4[2]]
	# ~ quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3],anagramma3[3],anagramma4[3]]
	# ~ quintacolonna=[anagramma[4],anagramma1[4],anagramma2[4],anagramma3[4],anagramma4[4]]
	# ~ sestacolonna=[anagramma[5],anagramma1[5],anagramma2[5],anagramma3[5],anagramma4[5]]
	# ~ settimacolonna=[anagramma[6],anagramma1[6],anagramma2[6],anagramma3[6],anagramma4[6]]
	# ~ ottavacolonna=[anagramma[7],anagramma1[7],anagramma2[7],anagramma3[7],anagramma4[7]]
	# ~ nonacolonna=[anagramma[8],anagramma1[8],anagramma2[8],anagramma3[8],anagramma4[8]]
	
	
	# using naive method 
	# to check all unique list elements
	#aggiungo controllo quadrati (primo,secondo e terzo)
	
					
			
			
				
				
	# printing result
	
		# ~ print(anagramma3)
		# ~ print(anagramma4)
		# ~ risultato.append(anagramma)
		# ~ ,anagramma1,anagramma2,anagramma3)
		# ~ risultato.append(anagramma)
		# ~ risultato.append(anagramma1)
		# ~ risultato.append(anagramma2)
		# ~ risultato.append(anagramma3)
		# ~ print(anagramma4)
		# ~ print(risultato)
			
		
	# ~ else : 
		# ~ print(flag,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8)
		# ~ print()
		# ~ print(nonacolonna)
		# ~ print ("List contains does not contains all unique elements")

		# ~ if anagramma[x]==numeri[x]:
		# ~ anagramma=sample(list1,9)
		
			# ~ print(anagramma)
			# ~ break
		# ~ break
		# ~ print(k)		
			# ~ print("j",j)
			# ~ print("k",k)
			# ~ print()
			# ~ pri(numeri[j]
			# ~ print(sample(list1,9))		
# ~ def ciao():
		# ~ while True:			
		
def ciao():				
			
	while True:		
			# ~ print("anagramma1",anagramma1,"anagramma2",anagramma2)		
			anagramma4=sample(list1,9)	
			if anagramma4[1]==1 and anagramma4[4]==4 and anagramma4[5]==9:

			# ~ e=["x",1,"x","x",4,9,"X","x","x"]
				
					
				# ~ print(anagramma2)
				break
		# ~ def ciaodfd():
			primacolonna = [anagramma[0],anagramma1[0],anagramma2[0],anagramma3[0],anagramma4[0]]
			secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1],anagramma3[1],anagramma4[1]]
			terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2],anagramma3[2],anagramma4[2]]
			quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3],anagramma3[3],anagramma4[3]]
			quintacolonna=[anagramma[4],anagramma1[4],anagramma2[4],anagramma3[4],anagramma4[4]]
			sestacolonna=[anagramma[5],anagramma1[5],anagramma2[5],anagramma3[5],anagramma4[5]]
			settimacolonna=[anagramma[6],anagramma1[6],anagramma2[6],anagramma3[6],anagramma4[6]]
			ottavacolonna=[anagramma[7],anagramma1[7],anagramma2[7],anagramma3[7],anagramma4[7]]
			nonacolonna=[anagramma[8],anagramma1[8],anagramma2[8],anagramma3[8],anagramma4[8]]
			flag = 0
			flag1 = 0
			flag2 = 0
			flag3 = 0 
			flag4 = 0
			flag5 =0
			flag6=0
			flag7=0
			flag8=0
			# using naive method 
			# to check all unique list elements
			for i,i1,i2,i3,i4,i5,i6,i7,i8 in zip(range(len(primacolonna)),range(len(secondacolonna)),range(len(terzacolonna)),range(len(quartacolonna)),range(len(quintacolonna)),range(len(sestacolonna)),range(len(settimacolonna)),range(len(ottavacolonna)),range(len(nonacolonna))):
					for checki,checki1,checki2,checki3,checki4,checki5,checki6,checki7,checki8 in zip(range(len(primacolonna)),range(len(secondacolonna)),range(len(terzacolonna)),range(len(quartacolonna)),range(len(quintacolonna)),range(len(sestacolonna)),range(len(settimacolonna)),range(len(ottavacolonna)),range(len(nonacolonna))):
						if i != checki:
							if primacolonna[i] == primacolonna[checki]:
								flag = 1
						if i1 != checki1:
							if secondacolonna[i] == secondacolonna[checki1]:
								flag1 = 1
						if i2 != checki2:
							if terzacolonna[i] == terzacolonna[checki2]:
								flag2 = 1
						if i3 != checki3:
							if quartacolonna[i] == quartacolonna[checki3]:
								flag3 = 1
						if i4 != checki4:
							if quintacolonna[i] == quintacolonna[checki4]:
								flag4 = 1
						if i5 != checki5:
							if sestacolonna[i] == sestacolonna[checki5]:
								flag5 = 1
								
						if i6 != checki6:
							if settimacolonna[i] == settimacolonna[checki6]:
								flag6 = 1
								
						if i7 != checki7:
							if ottavacolonna[i] == ottavacolonna[checki7]:
								flag7 = 1
						
						if i8 != checki8:
							if nonacolonna[i] == nonacolonna[checki8]:
								flag8 = 1
			# printing result
			if(not flag) and not flag1 and not flag2 and not flag3 and not flag4 and not flag5 and not flag6 and not flag7 and not flag8 and not flagquadrato1 and not flagquadrato2 and not flagquadrato3:
				print("colonne")
				print(flag,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8)
				print("quadrati")
				print(flagquadrato1,flagquadrato2,flagquadrato3)
				# ~ print("flag",flag)
				print()
				print ("List contains all unique elements")
				print(anagramma)
				print(anagramma1)
				print(anagramma2)
				print(anagramma3)
				print(anagramma4)
				break
			else : 
				
				# ~ print(flag,flag1,flag2,flag3,flag4,flag5,flag6,flag7,flag8)
				print()	
	def ciao():
		import random
		# ~ if aaa[0]!="0":

		# the use of sample() function .
		list1 = [1, 2, 3, 4, 5,6,7,8,9] 
		 
		from random import sample
		while True:  
		# Prints list of random items of given length
			if numeri[numeri.index(x)]==x:
				print(sample(list1,9))
		 
	 
		# ~ print(x_int.index())
	# ~ print(sample(list1,9))
 
 
