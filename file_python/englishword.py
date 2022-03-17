from english_words import english_words_set
print('ghost' in english_words_set)
# ~ for i in range(10):
	# ~ print(list(english_words_set[i]))
parola="**j***t"#r	
d1=list(english_words_set)
d2=sorted(d1)
print(len(english_words_set))
print(d2)

cc=-1
l=[]
l1=[]
for jj in parola:
	cc+=1
	if jj!="*":
		l.append(cc)
		l1.append(jj)
for j in d2:
		conta=0
	# ~ if len(j)>=8:
		# ~ if j[0]=="g":
		if len(j)==len(parola):
				for x ,y in zip(l,l1):
					if j[x]==y:
						conta+=1
						if conta>=len(l):
							print(j)
							break
				# ~ print(j)
		# ~ else:
			# ~ continue
