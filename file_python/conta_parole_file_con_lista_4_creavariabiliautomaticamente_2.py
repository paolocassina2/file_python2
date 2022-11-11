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

# ~ print(type(contents))
for lettera in lettere:
	# ~ user_input = input("Enter string for variable name: \n")
	
	dizio[lettera]=globals()[lettere] = []
print(dizio)
for x in contents:	#legge file di testo
	
	for j, z in zip(dizio.keys(),dizio.values()):
		if x[0]==j:
			z.append(x)
			dizio[j]=len(z)
# ~ print(dizio)
dizio_len={}
for x in dizio:	#creo un secondo dizionario con le lunghezze delle liste 
	# ~ print(len(dizio[x]))
	dizio_len[x]=len(dizio[x])
#creo un dizionario con le parole

# ~ print(dizio_len)
	# ~ print(x)
# ~ def ciao():	

# ~ print(j,len(z))
	# ~ markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
# ~ markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist=sorted((value, key) for (key,value) in dizio_len.items())	#ordino il dizionario con la lunghezza delle liste in ordine crescente (in base ai valori)
sortdict=dict([(k,v) for v,k in marklist])
print(sortdict)

####################################################################
#ORDINA DIZIONARIO IN MODO DECRESCCENTE
import operator

# ~ print('Original dictionary : ',dizio_len)
# ~ sorted_dizio_len_decresc = sorted(dizio_len.items(), key=operator.itemgetter(1))
# ~ print('Dictionary in ascending order by value : ',sorted_dizio_len_decresc)
sorted_dizio_len_decresc = dict( sorted(dizio_len.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_dizio_len_decresc)

# ~ print(sortdict)	
# ~ print({k: v for k, v in sorted(dizio.items(), key=lambda item: len(item[1]))})
		

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
