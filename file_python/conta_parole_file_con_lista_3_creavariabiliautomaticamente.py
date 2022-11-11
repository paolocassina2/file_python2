# ~ def ciao():
file1="C:\\Users\\Attilio\\Desktop\\660000_parole_italiane.txt"
with open(file1) as f:
	contents = f.readlines()
#questo programma crea automaticamente le variabili
lettere="abcdefghijklmnopqrstuvwxyz"
# ~ mydict={}
# ~ conta=0
lista=["banana","albero","asino","acca","anno","bacca","inno"]
dizio={}

for lettera in lettere:
	# ~ user_input = input("Enter string for variable name: \n")
	
	dizio[lettera]=globals()[lettere] = []
print(dizio)
for x in lista:
	
	for j, z in zip(dizio.keys(),dizio.values()):
		if x[0]==j:
			z.append(x)

for j, z in zip(dizio.keys(),dizio.values()):
	if len(z)>0:
		print(j,len(z))
		
		

# ~ print(apple)
# ~ print(type(apple))
# ~ a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
# ~ for x in lettere:
	# ~ mydict[x]=0
# ~ print(mydict)
# ~ lista2=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

# ~ for x in lista:

# ~ print(type(j))
# ~ b .append("r")
# ~ print(b)
# ~ def ciao():


	

				
			# ~ mydict[]
		# ~ else:
			# ~ pass
	# ~ print(conta)
	# ~ conta=0
	# ~ for j1 in lettere:
		# ~ conta=0
		# ~ print(j1)
		# ~ conta=conta+1
		# ~ if x[0]==j1:
			# ~ print(x[0])#
			# ~ conta=conta+1
			# ~ mydict[j1]=conta
		# ~ aggiorna={j1:conta}
		# ~ mydict.update(aggiorna)
		# ~ else:
			# ~ break
		# ~ conta=0
	# ~ print(conta)
		# ~ if 
	# ~ print(conta)	
	# ~ print(x[0])
	# ~ parola=x.strip()
		
	# ~ for j1 in lettere:
	
		# ~ if parola[0]==j1:
			# ~ ok="ok"
	# ~ if ok=="ok":
		# ~ conta+=1
	# ~ print(conta)
	# ~ conta=0
			# ~ print(lista.count())
			# ~ print(parola[0])
			# ~ conta=conta+1
			# ~ mydict[j1] = conta	
		# ~ print(conta)
			# ~ up_dict = {j1:conta}
			# ~ print("Dictionary before updation:",dict)
			# ~ mydict.update(up_dict)
		
		# ~ conta=0
# ~ print(mydict)


# ~ up_dict = {"Python":500}
# ~ print("Dictionary before updation:",dict)
# ~ dict.update(up_dict)
	# ~ conta+=1
				# ~ mydict[j] = conta	


def ciao():
	for x in contents:
			parola=x.strip()
		
			for j in lettere:
				if parola[0]==j:
					conta+=1
					mydict[j] = conta	
			enumerate()
			conta=0
