###CARTELLA==operazioni_stringhe

stringa="aa222"
# ~ c={stringa.count(set([x for x in stringa]))}
stringa_set=set([x for x in stringa])
conta_occ={}
for x in stringa_set:
	print(x)
	conta_occ[x]=stringa.count(x)
	# ~ conta_occ={x:stringa.count(x)}
print(conta_occ)
for x1,x2 in zip(conta_occ.keys(),conta_occ.values()):
	if x2==max(conta_occ.values()):
		print("most frequent character",x1,"frequency ",x2)
	# ~ print(x1,x2)

# ~ print(c)
