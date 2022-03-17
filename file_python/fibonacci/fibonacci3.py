#CARTELLA==fibonacci
def fibonacci():
	a, b = 0, 1
	while True:
		
		a, b = b, a + b
		if a <50:
			print(a)
		else:
			break
fibonacci()


c=[2,3,4,5,6,7]
d=c[:]
e=c

print("d",d)

print(d==c)
print(e==c)			#== confronta i valori
print(d is c)			# in questo caso false perchè le ivaribili in entrambi le parti dell operatore NON puntano allo stesso oggetto
print(e is c)		#is    confronta identita
			#The is operator evaluates to true if the variables on either side of the operator point to the same object and false otherwise.

#The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two variables point to the same object in memory
