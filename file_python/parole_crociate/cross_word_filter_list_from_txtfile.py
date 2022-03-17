###CARTELLA==parole_crociate
#same algorithm but it iterates through a text file containg words
from english_words import english_words_set
# ~ print('reset' in english_words_set)
# ~ for i in range(10):
	# ~ print(list(english_words_set[i]))
parola="r***t"
def ciao(parola):	
	parola=input("insert known letter otherwhise insert * ")
	print("lenparola",len(parola))
	c=0
	afile=("C:\\Users\\Attilio\\Desktop\\file_python\\parole_crociate\\words_alpha.txt")
	# ~ d2= open
	# ~ f = open(afile, "r")

	print("parola sconosciuta ",parola)
	print("possibili soluzioni")
	f = open(afile, "r")

	cc=-1
	l=[]
	l1=[]
	for jj in parola:
		cc+=1
		if jj!="*":
			l.append(cc)
			l1.append(jj)
			
	# ~ aaa=f.read()
	# ~ print(aaa)	
	ciao="ciao111"
	for j in f:
		# ~ print(j)
		j1=j.strip()
		
		# ~ print(len(j1))
		# ~ print(j1)
		# ~ j1 =f.readline()
		# ~ print(j1)
	# ~ for x in range(len(d1)):
	# ~ for j in d2:
		conta=0		
		
	# ~ def ciao():
			# ~ if len(j)>=8:
				# ~ if j[0]=="g":
		if len(j1)==len(parola):
			# ~ print(j1)
			# ~ print(j)
			for x ,y in zip(l,l1):
				if j1[x]==y:
					conta+=1
					if conta==len(l):
							print(j1)
								
									
					# ~ print(j)
					
					# ~ ciao="ciao"
					# ~ break
		# ~ if ciao=="ciao":
			# ~ break
									# ~ break
											# ~ return j
								# ~ print(j)
					# ~ else:
						# ~ continue
			# ~ while True:
				# ~ print(solve_crossW(parola))
ciao(parola)
