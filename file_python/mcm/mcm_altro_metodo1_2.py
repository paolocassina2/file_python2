a=541
b=38



def mcm(a,b):
	c=0
	a1=a
	b1=b
	lm1=[]
	lm2=[]
	while True:
		c=c+1
		prod1=a1*c			#mcm _ altro metodo_ se il multiplo piu piccolo di tutti e due si trova anche nellß altra lista
		prod2=b1*c				#Poiché 20558 è il numero più piccolo che appare in entrambe le liste di multipli, 20558 è il Minimo Comune Multiplo tra 541 e 38.
		# ~ a1*c
		lm1.append(prod1)			#se trovo prod1 nellßaltra lista significa che si trova in entrambe le liste. Siccome il programma si interrompe quando trova il primo valore che si trova anhe nellaltra lista, significa che quel valore e il piu piccolo
		lm2.append(prod2)
		# ~ b1*c
		a1=a
		b1=b
		# ~ print(prod1)
		# ~ print(prod2)
		# ~ if prod1 in lm2 :
			# ~ print("mcm ",prod1)
			# ~ break
		# ~ print(lm1)
		# ~ def printCommons(lm1, lm2): 
		comms = list() 
		for i in range(len(lm1)): 
			if lm1[i] in lm2: 
				comms.append(lm1[i]) 
		if len(comms)>=1:
			mcm=comms[0]
			return "mcm	" + str(mcm) +"\n"
			# ~ print("mcm",comms[0])	
			break
	# ~ print( comms) 
	# ~ printCommons(lm1,lm2)
while True:
	a=int(input("a	"))
	b=int(input("b	"))
	print(mcm(a,b))
