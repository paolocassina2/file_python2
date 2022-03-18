###CARTELLA==parole_crociate
from english_words import english_words_set
print('reset' in english_words_set)
# ~ for i in range(10):
	# ~ print(list(english_words_set[i]))
parola="l********e"	

#funyiona solo con le parole ceh si trovano nel set english_words_set. comunque e possibile integrare la lista con nuove parole passando un file testo come argomento
def solve_crossW(parola):#solve CROSSWORDS BY ITERATING AND FILTERING LIST OF WORDS
	parola=input("insert known letters, and * instead of unknown letters	")	
	d1=list(english_words_set)
	d2=sorted(d1)
	# ~ print(len(english_words_set))
	# ~ print(d2)
	print("parola sconosciuta: ",parola)							
	print("possible solutions:")
	cc=-1
	l=[]
	l1=[]
	for jj in parola:
		cc+=1
		if jj!="*":
			l.append(cc)
			l1.append(jj)
	# ~ for x in range(len(d1)):
	for j in d2:
			conta=0		
		# ~ if len(j)>=8:
			# ~ if j[0]=="g":
			if len(j)==len(parola):
					for x ,y in zip(l,l1):
						if j[x]==y:
							conta+=1
							if conta==len(l):
								# ~ print(l)
							
								
								print(j)

								# ~ break
								# ~ return j
					# ~ print(j)
		# ~ else:
			# ~ continue
while True:
	print(solve_crossW(parola))
