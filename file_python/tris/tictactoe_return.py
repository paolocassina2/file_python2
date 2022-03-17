# ~ A=[0,0,0]
# ~ B=[]
# ~ for i in range(3):
a=[0,0,0]
b=[0,0,0]
c=[0,0,0]	
# ~ print(B)
# ~ s1=1

B=[]
B.append(a)

B.append(b)	

B.append(c)
# ~ s2=1
victory=False
turno=-1
# ~ s1=8
#manca il pareggio e se il giocatore gioca nel posto sbagliato il turno aumenta(correggere)	
		
# ~ s2=8
# ~ B[0][2]="*"
# ~ B[1][2]="#"

def condizionivittoria():
	for i in range(0,3):
		if B[0][i]==B[1][i]==B[2][i]=="#" or B[0][i]==B[1][i]==B[2][i]=="*":
			if B[2][i]=="#":
				
				print("victory giocatore 1")
			else:
				print("victory giocatore 2")
			victory=True
			
		if B[i][0]==B[i][1]==B[i][2]=="#" or B[i][0]==B[i][1]==B[i][2]=="*":
			
			if B[i][2]=="#":
				
				print("victory giocatore 1")
			else:
				print("victory giocatore 2")
			victory=True
	if B[0][0]==B[1][1]==B[2][2]=="#" or B[0][0]==B[1][1]==B[2][2]=="*":		
			print("victory giocatore 2")
			if B[2][i]=="#":
				
				print("victory giocatore 1")
			else:
				print("victory giocatore 2")
			victory=True	
	elif B[0][2]==B[1][1]==B[2][0]=="#" or B[0][0]==B[1][1]==B[2][2]=="*":		
			print("victory giocatore 2")
			if B[2][i]=="#":
				
				print("victory giocatore 1")
			else:
				print("victory giocatore 2")	
# ~ lista_pos=["00","01","02","10","11","12","20","21","22"]
while victory==False:
	turno=turno+1
	s1=int(input("n1"))
	s2=int(input("n2"))
	if turno%2==0:
		if 	B[s1][s2]==0:
			B[s1][s2]="#"
		
	else:
		if B[s1][s2]==0:
			B[s1][s2]="*"
		# ~ else:
	condizionivittoria()
			# ~ turno=turno-1

	# ~ for j in range(B)
		# ~ for x in range(j)
		# ~ if [0] 
	# ~ if B[s1][s2]=="#" or B[s1][s2]=="*" :
		# ~ while B[s1][s2]=="#" or B[s1][s2]=="*":
		# ~ if B[s1][s2]==0:
			
			
			# ~ B[s1][s2]="#"
			# ~ j=str(s1+s2)
			# ~ lista_pos.remove(j)	
			# ~ if B[s1][s2]!="#" and B[s1][s2]!="*":
				# ~ B[s1][s2]=="#"
	
	
	print(B)

###CARTELLA==tris