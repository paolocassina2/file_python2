# Function which returns subset or r length from n
from itertools import combinations
  
def rSubset(arr, r):
  
    # return list of all subsets of length r
    # to deal with duplicate subsets use 
    # set(list(combinations(arr, r)))
    return list(combinations(arr, r))
  
# Driver Function

# ~ [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

 #anagramma1[0]==4 and anagramma1[1]==6 and anagramma1[2]==2 and anagramma1[3]==3 and anagramma1[5]==5:
# ~ lista1=[ anagramma1[0]==4 and anagramma1[1]==6 and anagramma1[2]==2 and anagramma1[3]==3 and anagramma1[5]==5:
# ~ lista1=[ anagramma1[0]==4 and anagramma1[1]==6 and anagramma1[2]==2 and anagramma1[3]==3 and anagramma1[5]==5:
lista1=[4,6,2,3,"x",5]
# ~ for x1,x2 in zip(lista1,range(lista1)):
	# ~ print(x2)
c1=-1
lista_ind_1=[]
for x1 in lista1:
	c1+=1
	if x1!="x":
		lista_ind_1.append(c1)
print(lista_ind_1)
if __name__ == "__main__":
    arr = [1, 2, 3, 4,5,6]
    r = 2
    print (rSubset(arr, r))

def ciao():
	if anagramma[3]==2:
			# ~ print(anagramma)
					# ~ ebreak
					
			# ~ while True:
			for j2 in list(p):		
				# ~ while True:
				anagramma1=j2
				if anagramma1[0]==4 and anagramma1[1]==6 and anagramma1[2]==2 and anagramma1[3]==3 and anagramma1[5]==5:
					# ~ print(anagramma1)
						# ~ break


			# ~ while True:		
					for j3 in list(p):
						anagramma2=j3	
						if anagramma2[0]==6 and anagramma2[2]==5 and anagramma2[3]==4 and anagramma2[4]==2 and anagramma2[5]==3:
									
								
							# ~ print(anagramma2)
							# ~ break
						
				
			# ~ while True:		
							for j4 in list(p):
								anagramma3=j4	
								if anagramma3[1]==3 and anagramma3[2]==4:
											
										
									# ~ print(anagramma3)
									# ~ break
							# ~ while True:		
									for j5 in list(p):		
										anagramma4=j5
										if anagramma4[5]==2 :
													
												
											# ~ print(anagramma4)
											# ~ break		
				# ~ while True:				
				# ~ while True:		
											for j6 in list(p):
												anagramma5=j6	
												# ~ if anagramma4[1]==6 and anagramma4[4]==8 and anagramma4[5]==2  and anagramma4[7]==1 :
												if anagramma5[0]==3 and anagramma5[1]==2 and anagramma5[2]==6 and anagramma5[3]==5 and anagramma5[4]==4 and anagramma5[5]==1:		
														
													print(anagramma5)
														# ~ break			
