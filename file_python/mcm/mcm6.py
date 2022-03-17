#calcola minimo comune multiplpb
#n=18

# ~ divprimi1=[]
# ~ divprimi2=[[]]

print("LCM DI DUE NUMERI")
		#print(n," primo")
	#print(primi)	
def caio():
	n1=1	
	n2=1
	print("calcola mcm")
	def MCMewwe(n1,n2):
				#print("calcola mcm")
		
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
# ~ while True:

	div1=[]
	div2=[]
	div3=[]
	div4=[]
	a=n1
	b=n2
	
	# ~ Details = {}
	# ~ Details["Age"] = []
	# ~ Details.update({"Age": [18, 20, 25, 29, 30]})
	# ~ print(Details)
	# ~ Details = {"Destination": "China", 
			   # ~ "Nstionality": "Italian", "Age": []}
	# ~ Details["Age"] += [20, "Twenty"]print(diz1)
	# ~ l=[]

	# ~ for vv in primi:

	# ~ a=17
	# ~ Details.update({"Age": [18, 20, 25, 29, 30]})
	# ~ diz1[str(a)].append("Twenty")
	# ~ diz1[str(a)] += [].append(a)
	# ~ b=int(n2)

# ~ def LCM1(n1,n2):
a=88
b=8	
	# ~ a=n1
	# ~ b=n2
	# ~ if n1>n2:
		# ~ b=n1
		# ~ a=n2
		# ~ a,b=n2,n1
		# ~ n2n1
		# ~ print(n1)
		# ~ print(n2)	
# ~ LCM1(88,30)

primi=[]
n1=2
n2=3
co=0

	


for x in range(7,200):
	for i in range(1,x+1):
		#print(i)	
		if x%i==0:
			co=co+1
	#print(co)
	if co==2:
		primi.append(x)
	co=0	#MINIMO C
		# ~ return str(primi)


# ~ LCM(2,3)	
def LCM(n1,n2):

	a=n1
	b=n2
	if n2 >n1:
		numeromax=n2
	else:
		numeromax=n1
	
	# ~ NUMERI_primi()
	# ~ OMUNE MULTIPLO
	diz1={"2":[],"3":[],"5":[]}
	diz2={"2":[],"3":[],"5":[]}

	diz3={"2":[],"3":[],"5":[]}
	for x in primi:
		diz1[str(x)]=[]
	for x1 in primi:
		diz2[str(x1)]=[]
	# ~ b=58
	for x2 in primi:
		diz3[str(x2)]=[]
	
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

	while b>1:
		if b%2==0:
			
			b=b/2
			diz2[str(2)].append("x")
			# ~ diz2[str(b)] += ["x"]
			# ~ diz2=di
		elif b%3==0:
			diz2[str(3)].append("x")
			b=b/3
			
			# ~ diz2[str(b)] += ["x"]
		
		elif b%5==0:
			b=b/5	
			# ~ div3.append(5)
			diz2[str(5)].append("x")					#chibve ü il divisore, 
			# ~ diz2[str(b)] += ["x"]
		for x in primi:
			if b%x==0:
				b=b/x
				diz2[str(x)].append("x")
				

	for y,z,k,j in zip(  diz1.keys(),diz1.values() ,diz2.keys(),diz2.values()):
		# ~ print(z)
		if len(z)>len(j):
			diz3[str(y)].append(len(z))

			# ~ diz3[str(y)] += len(z)
		else:
			# ~ diz3[str(k)] += len(j)
			diz3[str(k)].append(len(j))
			
	# ~ for x in diz3.keys():
				
			# ~ diz3[str(y)] += len([z])
	# ~ print(diz3)
	lcm=1
	for x,z in zip(diz3.keys(),diz3.values()):
		# ~ print(z[0])
		# ~ if z[0]==int:
		# ~ print(z)
			# ~ print(z)
		lcm=lcm*int(x)**z[0]
		# ~
		
		
	string="LCM di {} e {} è {} ".format(n1,n2,lcm)	#least common multiple

	# ~ string="lcm di {a:.2d} e {b:.2d} è  {lcm:.2d} ".format(a)	#least common multiple
	# ~ return "LCM  "+str(lcm)+"\n"
	return string +"\n"
	# ~ print(mcm)

while True:
	
	try:
	# ~ n1=10
	# ~ n2=35
		n1=int(input("n1  "))
		n2=int(input("n2  "))
		print(LCM(n1,n2))
		
	except:
		pass
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
	# ~ print(diz1)
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
