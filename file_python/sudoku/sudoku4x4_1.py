
a=[1,"x","x","x"]
b=["x",2,"x","x"]
c=["x","x",3,"x"]

d=["x","x","x",2]
# ~ e=["x",1,"x","x"]

  

import itertools 
  
listA = [1,2,3,4]
perm = itertools.permutations(listA) 
  
# ~ for i in list(perm): 
    # ~ print(i)
# Print the obtained permutations 
# ~ for j in p: 
    # ~ print(j) 
# ~ ciao=[2,3,5,5]
# ~ print(len(set(ciao)),"ciao")
# ~ def ciao():
# ~ while True:	
for j1 in perm:
	anagramma=list(j1)
	for j2 in perm:
			anagramma1=list(j2)	
		# ~ if len(set(primacolonna))>3 and len(set(secondacolonna ))>3 and len(set (terzacolonna))>3 and len(set (quartacolonna))>3:
			primacolonna = [anagramma[0],anagramma1[0]]
			secondacolonna = [anagramma[1],anagramma1[1]]
			terzacolonna=[anagramma[2],anagramma1[2]]
			quartacolonna=[anagramma[3],anagramma1[3]]
			
			if len(set(primacolonna))==2 and len(set(secondacolonna ))==2 and len(set (terzacolonna))==2 and len(set (quartacolonna))==2:
				# ~ print(primacolonna)
				# ~ print(secondacolonna)
				# ~ print(terzacolonna)
				# ~ print(quartacolonna)
				# ~ break
# ~ def ciao():		
				for j3 in perm:
					anagramma2=list(j3)
					primacolonna = [anagramma[0],anagramma1[0],anagramma2[0]]
					secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1]]
					terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2]]
					quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3]]
	if len(set(primacolonna))==3 and len(set(secondacolonna ))==3 and len(set (terzacolonna))==3 and len(set (quartacolonna))==3:
			print(primacolonna)
			print(secondacolonna)
			print(terzacolonna)
			print(quartacolonna)
		# ~ break
def ciao():			
			for j4 in perm:
				anagramma3=list(j4)
				# ~ print(type(anagramma3))
				# ~ print(anagramma3)
				# ~ print(anagramma)
				# ~ print(anagreamma1)
				# ~ print(anagramma2)
					# ~ print(anagramma3)	print(anagramma)
					# ~ print(anagramma1)
					# ~ print(anagramma2)
					# ~ print(anagramma3)
# ~ def ciao():	
	#colonne
				primacolonna = [anagramma[0],anagramma1[0],anagramma2[0],anagramma3[0]]
				secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1],anagramma3[1]]
				terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2],anagramma3[2]]
				quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3],anagramma3[3]]
				if len(set(primacolonna))>3 and len(set(secondacolonna ))>3 and len(set (terzacolonna))>3 and len(set (quartacolonna))>3:
					print(anagramma)
					print(anagramma1)
					print(anagramma2)
					print(anagramma3)
					
					break
	# ~ primacolonna = [anagramma[0],anagramma1[0],anagramma2[0],anagramma3[0]]
	# ~ secondacolonna = [anagramma[1],anagramma1[1],anagramma2[1],anagramma3[1]]
	# ~ terzacolonna=[anagramma[2],anagramma1[2],anagramma2[2],anagramma3[2]]
	# ~ quartacolonna=[anagramma[3],anagramma1[3],anagramma2[3],anagramma3[3]]
	# ~ quintacolonna=[anagramma[4],anagramma1[4],anagramma2[4],anagramma3[4]]
	# ~ sestacolonna=[anagramma[5],anagramma1[5],anagramma2[5],anagramma3[5]]
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
	
	# ~ flag = 0
	# ~ flag1 = 0
	# ~ flag2 = 0
	# ~ flag3 = 0 
	
	# ~ # using naive method 
	# ~ # to check all unique list elements
	# ~ for i,i1,i2,i3 in zip(range(len(primacolonna)),range(len(secondacolonna)),range(len(terzacolonna)),range(len(quartacolonna))):
			# ~ for checki,checki1,checki2,checki3 in zip(range(len(primacolonna)),range(len(secondacolonna)),range(len(terzacolonna)),range(len(quartacolonna))):
				# ~ if i != checki:
					# ~ if primacolonna[i] == primacolonna[checki]:
						# ~ flag = 1
				# ~ if i1 != checki1:
					# ~ if secondacolonna[i] == secondacolonna[checki1]:
						# ~ flag1 = 1
				# ~ if i2 != checki2:
					# ~ if terzacolonna[i] == terzacolonna[checki2]:
						# ~ flag2 = 1
				# ~ if i3 != checki3:
					# ~ if quartacolonna[i] == quartacolonna[checki3]:
						# ~ flag3 = 1
				
			
	# ~ # printing result
	# ~ if(not flag) and not flag1 and not flag2 and not flag3:
		
		# ~ print(flag,flag1,flag2,flag3)
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
		# ~ break
		
		
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
