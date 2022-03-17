#calcola minimo comune multiplpb
#n=18

divprimi1=[]
divprimi2=[[]]
co=0
primi=[]

for x in range(7,200):
	for i in range(1,x+1):
		#print(i)	
		if x%i==0:
			co=co+1
	#print(co)
	if co==2:
		primi.append(x)
	co=0
		#print(n," primo")
	#print(primi)	
def caio():
	n1=1	
	n2=1
	print("calcola mcm")
	def MCM(n1,n2):
				#print("calcola mcm")
				div1=[]
				div2=[]
				div3=[]
				a=int(n1)
				b=int(n2)
				while a>1:
					if a%2==0:
						a=a/2
						div1.append(2)
					elif a%3==0:
							a=a/3
							div1.append(3)
					elif a%5==0:
							a=a/5	
							div1.append(5)	
					elif a%7==0:
							a=a/7	
							div1.append(7)	
					elif a%11==0:
							a=a/11	
							div1.append(11)	
					for h in primi:
						if a%h==0:
							a=a/h
							divprimi1.append(h)
							nprimo1=h
							break
				while b>1:
					if b%2==0:
						b=b/2
						div2.append(2)
					elif b%3==0:
							b=b/3
							div2.append(3)
					elif b%5==0:
							b=b/5	
							div2.append(5)
					elif b%7==0:
							b=b/7	
							div2.append(7)
					elif b%11==0:
							b=b/11	
							div2.append(11)
					for h in primi:
						if b%h==0:
							b=b/h
							nprimo2=h
							divprimi2.append(h)
							break
				c2=0
				c3=0
				c4=0
				c5=0
				
				
				#mcm=2**due*3**(tre)
				#print(mcm)
				
				due1=div1.count(2)
				due2=div2.count(2)
				lista=[due1,due2]
				due=max(lista)
					
				tre1=div1.count(3)
				tre2=div2.count(3)
				lista1=[tre1,tre2]
				tre=max(lista1)	
					
				cinque1=div1.count(5)
				cinque2=div2.count(5)
				lista2=[cinque1,cinque2]
				cinque=max(lista2)
				
				sette1=div1.count(7)
				sette2=div2.count(7)
				lista3=[sette1,sette2]
				sette=max(lista3)
				
				undici1=div1.count(11)
				undici2=div2.count(11)
				lista4=[undici1,undici2]
				undici=max(lista4)
				
				contaprimi1=divprimi1.count(nprimo1)
				contaprimi2=divprimi2.count(nprimo2)
				listaprimi=[contaprimi1,contapromi2]
				primi=max(listaprimi)
				
				
				
				divisori={"2":due, "3":tre	,"5":cinque,"7":sette}
				mcm=1
				for k, y in zip(divisori.keys(), divisori.values()):
					mcm=mcm*int(k)**int(y)
				# ~ mcm=mcm*int(nprimo1)**primi
					
				#print("mcm",end="")
				return "  " +str(mcm)+"\n"
			
		#	if str(n1).isnumeric()==False:
			#	n1=input("n1   ")
	#	if str(n2).isnumeric()==False:
		#		n2=input("n2   ")		
			
	#	if str(n1).isnumeric()==True and st
# ~ while True:
	# ~ n1=input("n1	")
	# ~ n2=input("n2	")
	# ~ print("mcm	",MCM(n1,n2))		

# ~ Details = {"Destination": "China", 
		   # ~ "Nstionality": "Italian", "Age": []}
# ~ Details["Age"] += [20, "Twenty"]
# ~ print(Details)
div1=[]
div2=[]
div3=[]
div4=[]

diz1={"2":[],"3":[],"5":[]}
for x in primi:
	diz1[str(x)]=[]
# ~ b=58

# ~ Details = {}
# ~ Details["Age"] = []
# ~ Details.update({"Age": [18, 20, 25, 29, 30]})
# ~ print(Details)
# ~ Details = {"Destination": "China", 
           # ~ "Nstionality": "Italian", "Age": []}
# ~ Details["Age"] += [20, "Twenty"]print(diz1)
# ~ l=[]

# ~ for vv in primi:

a=17
# ~ Details.update({"Age": [18, 20, 25, 29, 30]})
# ~ diz1[str(a)].append("Twenty")
# ~ diz1[str(a)] += [].append(a)
# ~ b=int(n2)

while a>1:
	if a%2==0:
		
		a=a/2
		diz1[str(2)].append("x")
		# ~ diz1[str(a)] += ["x"]
		# ~ diz1=di
	elif a%3==0:
		diz1[str(3)].append("x")
		a=a/3
		
		# ~ diz1[str(a)] += ["x"]
	
	elif a%5==0:
		a=a/5	
		# ~ div3.append(5)
		diz1[str(5)].append("x")					#chiave ü il divisore, 
		# ~ diz1[str(a)] += ["x"]
	for x in primi:
		if a%x==0:
			a=a/x
			diz1[str(x)].append("x")
			# ~ print(x)
	
			# ~ diz1[str(x)] += ["x"]
			# ~ break
	# ~ divprimi2.append(vv)
					# ~ diz1[str(x)] += div4
					# ~ div4.append(x)
					# ~ diz1[str(x)]=len(div4)
			# ~ Details["Age"] += [20, "Twenty"]
					

				
	# ~ diz1["2"]=len(div1)
	# ~ diz1["3"]=len(div2)

	# ~ diz1["5"]=len(div3)


	# ~ Details = {"Destination": "China", 
			   # ~ "Nstionality": "Italian", "Age": []}
	# ~ Details["Age"] += [20, "Twenty"]
	# ~ div4.append(x)
	# ~ for x in primi	
			
		# ~ for h in primi:
			# ~ if a%h==0:
				# ~ div4.append(h)
				# ~ break

# ~ divprimi2.append(vv)
# ~ dizprimi2[str(nprimo2)]+=divprimi2
		# ~ break
print(diz1)
	# ~ for h in primi:#
# ~ d={"2":"kdjkfdffdfdffffg","2":"kdjfkl"}
# ~ print(d)
# ~ print(d["2"])

						# ~ if a%h==0:
							# ~ a=a/h
							# ~ divprimi1.append(h)
							# ~ nprimo1=h
							# ~ break							
# ~ contaprimi1=divprimi1.count(nprimo1)

# ~ contaprimi2=divprimi2.count(nprimo2)
# ~ listaprimi=[contaprimi1,contaprimi2]
# ~ primi=max(listaprimi)
				
# ~ nprimo1=19
# ~ nprimo2=17

# ~ divisori={"2":due, "3":tre	,"5":cinque,"7":sette}
# ~ mcm=1
# ~ for k, y in zip(divisori.keys(), divisori.values()):
	# ~ mcm=mcm*int(k)**int(y)
