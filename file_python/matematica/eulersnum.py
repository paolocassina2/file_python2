#Python Program to Compute the Value of Euler’s Number e. Use the Formula: e = 1 + 1/1! + 1/2! + …… 1/n!
e=0
n=9
e=1
# ~ fact=4
###CARTELLA==matematica
for i in range(1,n+1):
	
	n=i
	for x in range(1,n):
		# ~ fact=fact*x
		# ~ print(fact)
		n=n*x
	e=e+(1/n)
	# ~ print(n)
	n=0
print(e)

# ~ def ciao():
import math
n=int(input("Enter the number of terms: "))
sum1=1
for i in range(1,n+1):
	sum1=sum1+(1/math.factorial(i))
print("The sum of series is",round(sum1,2))
