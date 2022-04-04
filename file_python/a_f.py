###CARTELLA==alfabeto_farfallino
parola="paolo"

vocali=["a","e","i","o","u"]
a_f=""

for y in parola:
	# ~ for x in vocali:
		if y in vocali:
				
			a_f=a_f+y+"F"+y
		else:
			a_f=a_f+y

print(a_f)
