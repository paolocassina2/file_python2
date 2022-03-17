#factorial(p-1) %% p==-1 ~ "prime number",
#factorial(p-1) %% p ==(p-1) ~ "PRIME NUMBER",		sintassi di R LANGUAGE

def checkprime():
	n=6
	fatt_numero_prima=1
	for i in range(1,n):
		fatt_numero_prima=fatt_numero_prima*i
		# ~ print(i)
		
	
	# ~ print(fatt_numero_prima)
	if fatt_numero_prima%n==-1:
		return str(n)+" numero primo"
		# ~ print("numero primo",n)

	elif fatt_numero_prima%n==(n-1):
		return str(n)+" numero primo"
		# ~ print("numero primo",n)
	else:
		return str(n)+" NON numero primo"	
	
		# ~ print("ciao")
		
# ~ print(checkprime())

for j in range(1,100):
	n=j
	fatt_numero_prima=1
	for i in range(1,n):
		fatt_numero_prima=fatt_numero_prima*i
		# ~ print(i)
		
	
	# ~ print(fatt_numero_prima)
	if fatt_numero_prima%n==-1:
		print (str(n)+" numero primo")
		# ~ print("numero primo",n)

	elif fatt_numero_prima%n==(n-1):
		print (str(n)+" numero primo")
		# ~ print("numero primo",n)
	# ~ else:
		# ~ return str(n)+" NON numero primo"	
				# ~ return str(n)+" NON numero primo"	

# ~ RETPRIMENUMBERS()

###CARTELLA==matematica