###CARTELLA==matematica


 #base {\displaystyle b}{\displaystyle b} Harshad number is a positive integer that is divisible by the sum of its base {\displaystyle b}{\displaystyle b} digits. 
 #For example, in the decimal numeral system, 1729 is a Harshad number since 1 + 7 + 2 + 9 = 19, and 1729 = 19 × 91. Also called Niven numbers or, much less commonly, multidigital numbers.

# ~ s=0

# ~ n=str(18)
# ~ n1=int(n)
# ~ if n1%3==0:
	# ~ print("ciao")
# ~ c=[]
s=0
c22=0
c44=0
c66=0
for x in range(10,40000):
		c22=c22+1
		# ~ print("x",x)
		stri=str(x)
		c=[x for x in stri]
		
		# ~ print(c)
		for j in c:
			s=s+int(j)
		if x%s==0:
			c44+=1
			c66+=c22
			print(c22)#differenza tra un harshad number e l' altro
			c22=0
			print(x," is Harshad number")
			# ~ print(x%s)
		s=0
		# ~ stri1=stri.s()
		# ~ print(stri1)
		# ~ print("stri",stri)
		# ~ for x in stri:
			# ~ s=s+int(x)
		# ~ print(type(s))
		# ~ print(s)
		# ~ print (x%s)
		# ~ if x%s==0:
			# ~ print(x)
			# ~ print(x," is Harshad number")
		# ~ e
		# ~ r=x%s
		# ~ if r==0:
			# ~ print(x," is Harshad n")
		# ~ print(x%s)
			# ~ print(x," is Harshad number")
		# ~ s=0
print(c66/c44)#media delle distanze tra i numeri harshad
