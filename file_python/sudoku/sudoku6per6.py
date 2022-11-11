
a=[1,"x","x","x","x","x"]
b=["x",2,"x","x","x","x"]
c=["x","x",3,"x","x","x"]

d=["x","x","x",2,"x","x"]
e=["x",1,"x","x","x","x"]
f=["x",1,"x","x","x","x"]

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
list1 = [1, 2, 3, 4,5,6] 
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

# ~ checkuniqueelements()
risultato=[]		
while True:			
	while True:
		anagramma=sample(list1,6)

		# ~ for x,j in listaindici, listavalori:
		if anagramma[3]==2:
			print(anagramma)
			break
			
	# ~ while True:
		
	while True:
		anagramma1=sample(list1,6)	# ~ for x,j in listaindici, listavalori:
		if anagramma1[0]==4 and anagramma1[1]==6 and anagramma1[2]==2 and anagramma1[3]==3 and anagramma1[5]==5:
				print(anagramma1)
				break


	while True:		
		
		anagramma2=sample(list1,6)	
		if anagramma2[0]==6 and anagramma2[2]==5 and anagramma2[3]==4 and anagramma2[4]==2 and anagramma2[5]==3:
					
				
			print(anagramma2)
			break
			
	
	while True:		
		
		anagramma3=sample(list1,6)	
		if anagramma3[1]==3 and anagramma3[2]==4:
					
				
			print(anagramma3)
			break
	while True:		
				
			anagramma4=sample(list1,6)	
			if anagramma4[5]==2 :
						
					
				print(anagramma4)
				break		
	# ~ while True:		
	while True:		
				
			anagramma5=sample(list1,6)	
			# ~ if anagramma4[1]==6 and anagramma4[4]==8 and anagramma4[5]==2  and anagramma4[7]==1 :
			if anagramma5[0]==3 and anagramma5[1]==2 and anagramma5[2]==6 and anagramma5[3]==5 and anagramma5[4]==4 and anagramma5[5]==1:		
					
				print(anagramma5)
				break			
	print()
	#colonne
	primacolonna = [anagramma[0],anagramma1[0],anagramma2[0],anagramma3[0],anagramma4[0],anagramma5[0]]
	secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1],anagramma3[1],anagramma4[1],anagramma5[1]]
	terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2],anagramma3[2],anagramma4[2],anagramma5[2]]
	quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3],anagramma3[3],anagramma4[3],anagramma5[3]]
	
	# ~ primacolonna = [anagramma[0],anagramma1[0],anagramma2[0],anagramma3[0]]
	# ~ secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1],anagramma3[1]]
	# ~ terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2],anagramma3[2]]
	# ~ quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3],anagramma3[3]]
	quintacolonna=[anagramma[4],anagramma1[4],anagramma2[4],anagramma3[4],anagramma4[4],anagramma5[4]]
	sestacolonna=[anagramma[5],anagramma1[5],anagramma2[5],anagramma3[5],anagramma4[5],anagramma5[5]]
	# ~ settimacolonna=[anagramma[6],anagramma1[6],anagramma2[6],anagramma3[6]]
	# ~ ottavacolonna=[anagramma[7],anagramma1[7],anagramma2[7],anagramma3[7]]
	# ~ nonacolonna=[anagramma[8],anagramma1[8],anagramma2[8],anagramma3[8]]
	# ~ primacolonna = [anagramma[0],anagramma1[0],anagramma2[0],anagramma3[0],anagramma4[0]]
	# ~ secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1],anagramma3[1],anagramma4[1]]
	# ~ terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2],anagramma3[2],anagramma4[2]]
	# ~ quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3],anagramma3[3],anagramma4[3]]
	# ~ quintacolonna=[anagramma[4],anagramma1[4],anagramma2[4],anagramma3[4],anagramma4[4]]
	# ~ sestacolonna=[anagramma[5],anagramma1[5],anagramma2[5],anagramma3[5],anagramma4[5]]
	# ~ settimacolonna=[anagramma[6],anagramma1[6],anagramma2[6],anagramma3[6],anagramma4[6]]
	# ~ ottavacolonna=[anagramma[7],anagramma1[7],anagramma2[7],anagramma3[7],anagramma4[7]]
	# ~ nonacolonna=[anagramma[8],anagramma1[8],anagramma2[8],anagramma3[8],anagramma4[8]]
	
	flag = 0
	flag1 = 0
	flag2 = 0
	flag3 = 0 
	flag4 = 0 
	flag5 = 0 
			
	# using naive method 
	# to check all unique list elements
	for i,i1,i2,i3,i4,i5 in zip(range(len(primacolonna)),range(len(secondacolonna)),range(len(terzacolonna)),range(len(quartacolonna)),range(len(quintacolonna)),range(len(sestacolonna))):
			for checki,checki1,checki2,checki3,checki4,checki5 in zip(range(len(primacolonna)),range(len(secondacolonna)),range(len(terzacolonna)),range(len(quartacolonna)),range(len(quintacolonna)),range(len(sestacolonna))):
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
	# printing result
	if(not flag) and (not flag1) and (not flag2) and (not flag3) and (not flag4) and (not flag5):
		
		print(flag,flag1,flag2,flag3)
		# ~ print("flag",flag)
		# ~ print()
		# ~ print ("List contains all unique elements")
		# ~ print(anagramma)
		# ~ print(anagramma1)
		# ~ print(anagramma2)
		# ~ print(anagramma3)
	
		# ~ risultato.append(anagramma)
		# ~ ,anagramma1,anagramma2,anagramma3)
		# ~ risultato.append(anagramma)
		# ~ risultato.append(anagramma1)
		# ~ risultato.append(anagramma2)
		# ~ risultato.append(anagramma3)
		# ~ print(anagramma4)
		# ~ print(risultato)
		break
		
		
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
	
	# ~ print(sample(list1,9))
 
#CARTELLA==sudoku

