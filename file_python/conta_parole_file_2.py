file1="C:\\Users\\Attilio\\Desktop\\660000_parole_italiane.txt"
with open(file1) as f:
	contents = f.readlines()

lettere="abcdefghijklmnopqrstuvwxyz"
mydict={}
# ~ conta=0
lista=["albero","asino","acca","canto","cane","roccia"]

for x in lettere:
	mydict[x]=0
# ~ print(mydict)


# ~ for x in lista:
for j1 in lettere:
	conta=0
	for x1 in contents:
		x=x1.strip()
		if j1==x[0]:
			conta=conta+1
		# ~ else:
			# ~ pass
	# ~ if j1==x[0]:
	if conta!=0:
		print(j1,conta)
	mydict[j1]=conta
import operator
# ~ ciao=list(mydict.items())
# ~ print(ciao.sort())
print(mydict)
lista=list(zip(mydict.keys(),mydict.values()))
print(lista.sort())

# ~ print(mydict.sort())
# ~ sorted_x = sorted(mydict.items(), key=operator.itemgetter(0))
# ~ print(sorted_x)
# ~ {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}	
# ~ print(mydict)
# ~ lista=zip(mydict)
# ~ print(list(lista))
			# ~ conta=0	
			
			
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
