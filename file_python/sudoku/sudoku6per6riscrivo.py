
a=[1,"x","x","x","x","x"]
b=["x",2,"x","x","x","x"]
c=["x","x",3,"x","x","x"]

d=["x","x","x",2,"x","x"]
e=["x",1,"x","x","x","x"]
f=["x",1,"x","x","x","x"]

from itertools import permutations 
  
  
a = [1,2,3,4,5,6]
  
# no length entered so default length
# taken as 4(the length of string GeEK)
p = permutations(a) 
p1 = permutations(a) 
p2 = permutations(a) 
p3 = permutations(a) 
p4 = permutations(a) 
p5 = permutations(a) 

# ~ for j1 in list(p):	
	# ~ print(j1,"j1")
	# ~ for j2 in list(p1):	
		# ~ print(j2,"j2")
		# ~ for j3 in list(p):	
			# ~ for j4 in list(p):	
				# ~ for j5 in list(p):	
					# ~ for j6 in list(p):	
						# ~ for j1 in list(p):	
							# ~ for j1 in list(p):	
	# ~ print(j1)
	# ~ for j2 in list(p):	
		# ~ print(j2)
							# ~ print(j2)
							# ~ print(j3)
							# ~ print(j4)
							# ~ print(j5)
							
				# ~ print(p2)
				# ~ print(p3)
# Print the obtained permutations 
# ~ for j in list(p): 
    # ~ print(j) 	

for j1 in list(p):		
			# ~ while True:
		anagramma=j1

				# ~ for x,j in listaindici, listavalori:
		# ~ if anagramma[3]==2:
			# ~ print(anagramma)
					# ~ ebreak
					
			# ~ while True:
		for j2 in list(p1):		
				# ~ while True:
				anagramma1=j2
				# ~ if anagramma1[0]==4 and anagramma1[1]==6 and anagramma1[2]==2 and anagramma1[3]==3 and anagramma1[5]==5:
					# ~ print(anagramma1)
						# ~ break


			# ~ while True:		
				for j3 in list(p2):
					anagramma2=j3	
				# ~ if anagramma2[0]==6 and anagramma2[2]==5 and anagramma2[3]==4 and anagramma2[4]==2 and anagramma2[5]==3:
									
								
							# ~ print(anagramma2)
							# ~ break
						
					
				# ~ while True:		
					for j4 in list(p3):
						anagramma3=j4	
									# ~ if anagramma3[1]==3 and anagramma3[2]==4:
												
											
										# ~ print(anagramma3)
										# ~ break
								# ~ while True:		
						for j5 in list(p4):		
							anagramma4=j5
										# ~ if anagramma4[5]==2 :
													
												
											# ~ print(anagramma4)
											# ~ break		
				# ~ while True:				
				# ~ while True:		
							for j6 in list(p5):
								anagramma5=j6	
												# ~ if anagramma4[1]==6 and anagramma4[4]==8 and anagramma4[5]==2  and anagramma4[7]==1 :
												# ~ if anagramma5[0]==3 and anagramma5[1]==2 and anagramma5[2]==6 and anagramma5[3]==5 and anagramma5[4]==4 and anagramma5[5]==1:		
														
													# ~ print(anagramma5)
														# ~ break			
				# ~ print()							
			# ~ #colonne
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
																
								if len(set(primacolonna))==6 and len(set(secondacolonna))==6 and len(set(terzacolonna))==6 and len(set(quartaacolonna))==6 and len(set(quintaacolonna))==6 and len(set(sestacolonna))==6:
																	# ~ print("ciaoà")
									print(primacolonna)
									print(secondacolonna)
									print(terzacolonna)
									print(quartacolonna)
									print(quintacolonna)
									print(sestacolonna)
									break
