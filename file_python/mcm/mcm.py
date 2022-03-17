
# ~ n1=18
# ~ n2=52
print("calcola mcm")
def caio():
	if len(dizio1)==len(dizio2):
		for y,z,k,j in zip  (dizio1.keys(),dizio1.values() ,dizio2.keys(),dizio2.values()):
							# ~ print(z)
							
					if z>j:
									# ~ dizio3[y] += z
						dizio3[y]=z
									# ~ diz3[str(y)] += len(z)
					else:
									# ~ diz3[str(k)] += len(j)
						dizio3[k] = j
						
					if y not in dizio2:
						dizio3[y] = z
					if k not in dizio1:
						dizio3[k] = j
						
		for j,z in zip(dizio3.keys(), dizio3.values()):
			mcm=mcm*int(j)**z
		print(dizio3)
		print(mcm)
def ciasudfi():
	while n1>1:
			# ~ if x<=n:
			for x in range(2,int(n1)+1):
				# ~ x=x+1
				if n1%x==0:
					n1=n1/x	
					l1.append(x)
					
					break
				# ~ print(x)
# ~ print(l1)
# ~ while n>0:

	
	x=0

		# ~ for x in range(1,int(n)+1):
	# ~ if n%x==0:
				# ~ n=n/x
				# ~ l1.append(x)
				# ~ break
		# ~ return n	
		# ~ print(n)
	# ~ print(l1)
def min_com_mult(n1,n2):
	l1=[]
	l2=[]
	while n1>1:
			# ~ if x<=n:
			for x in range(2,int(n1)+1):
				# ~ x=x+1
				if n1%x==0:
					n1=n1/x	
					l1.append(x)
					break
	
					
	while n2>1:
			# ~ if x<=n:
			for y in range(2,int(n2)+1):
				# ~ x=x+1
				if n2%y==0:
					n2=n2/y
					l2.append(y)
					# ~ print(x)
					# ~ print(n)
					break
	# ~ l1_1
	# ~ print(l1)

	# ~ l1_1=[]
	# ~ for x in  l1:
		# ~ l1_1.append(l1.count(x))
	# ~ print(l1_1)
	# ~ print(l2)
	# ~ print(l1+l2)
	# ~ def cioa():
	dizio1={}	
	dizio2={}
	dizio3={}		
	for x1 in l1:
		# ~ print()
		dizio1[str(x1)]=l1.count(x1)
	# ~ print(dizio1)
	for x2 in l2:
		# ~ print()
		dizio2[str(x2)]=l2.count(x2)
	# ~ print(dizio1)
	# ~ print(dizio2)
	# ~ dizio3
	lista_f=[]

	def ajk():

		# ~ a = ['a1', 'a2', 'a3']
		# ~ b = ['b1', 'b2']
		if len(dizio1)>len(dizio2):
			dizionariolungo=dizio1
		else:
			dizionariolungo=dizio2
		for x in range(len(dizionariolungo)):
			if x<len(dizio1):
				print(dizio1[x])
			if x<len(dizio2):
				print(dizio1[x])
				
		print(dizio1)
	# ~ dizio3=dizio1+dizio2
	mcm=1

	# ~ print(dizio1)
	for j ,k in zip  (dizio1.keys(),dizio1.values()):			#dizio 3 per ora è solo una copia di diozio2
		# ~ dizio3
		dizio3[j]=k

	print("d1",dizio1)
	print("d2,",dizio2)
	
		
	for j1 ,k1 in zip  (dizio2.keys(),dizio2.values()):	#se il secondo dizionario ha le stesse chiavi del primo, aggiorno i valori di ciascuna chiave del dizio3 solo se il valore associato a quella chiave è più alto. Se invece quella chiave non c'è in dizio 3 il programma esegue "un append"- in questo modo riesco ad ottenere i fattori comuni con l'esponente più alto e non comuni
		# ~ print(j1)
		if j1 in dizio1:
			print(j1)
			if dizio2[j1]>dizio1[j1]:
				# ~ dizio3.update({j1 : k1})
				dizio3[j1] = k1
		else:		
		# ~ elif j1 not in dizio1:
			# ~ print(j1)
			# ~ if k1>dizio1[j1]:
			dizio3[j1] = k1
			# ~ dizio3.update({j1 : k1})
		# ~ for x,p in  zip(dizio1.keys(),dizio1.values):
			# ~ print(j)
						# ~ elif y in dizio1 and y not in dizio2:
							# ~ dizio3[y]=z
						# ~ elif  k in dizio2 and y not in dizio1:
							# ~ dizio3[k]=j
	print("d3",dizio3)						
	mcm=1
	for j,z in zip(dizio3.keys(), dizio3.values()):
				mcm=mcm*int(j)**z
	# ~ print(dizio3)
	print("mcm: 	",mcm)
	print()
	# ~ print(dizio3)
				# ~ for 				
			# ~ while True:		
			# ~ print(divisione())
		# ~ print(l1)
		# ~ print(l2)
		# ~ print "List comprehension:"

while True:
	n1=int(input("n1 "))
	n2=int(input("n2 "))
	min_com_mult(n1,n2)

		# ~ print (x, y)
