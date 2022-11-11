stringa="a4544546666666668"
# ~ c={stringa.count(set([x for x in stringa]))}
stringa_set=set([x for x in stringa])
massimo=-200000000000
for x in stringa_set:
	print(x)
	conta=stringa.count(x)
	if conta>massimo:
		massimo=conta
		max_occurrence=[x,massimo]
	print()
print("max_occurence ",max_occurrence)
# ~ print(c)
