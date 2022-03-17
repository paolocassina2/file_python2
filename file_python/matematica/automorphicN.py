#A number is called Automorphic or Cyclic number if and only if its square ends in the same digits as the number itself.
###CARTELLA==matematica
# ~ q1="1234568936"
# ~ print(
# ~ for j in q1:
	#A number is called Automorphic or Cyclic number if and only if its square ends in the same digits as the number itself.

#Automorphic or Cyclic Number Examples: 52 = 25, 62 = 36, 762 = 5776, 3762 = 141376

#List of Automorphic Numbers: 0, 1, 5, 6, 25, 76, 376, 625, 9376, 90625, 109376, 890625, 2890625, 7109376, 12890625, 87109376
#last_cifra_quad=0
#last_cifra_num=0
print("automorphic numbers")
for i in range(1,100000000):
	quadrato=i*i
	# ~ if i>9:
# ~ n=43434466
	n1=str(i)
	
	q1=str(quadrato)
	# ~ print(q1)
	ultime_cifre=q1[(len(q1)-len(n1)):(len(q1))]
	if n1 in ultime_cifre:
		print(n1,q1)
			
	# ~ else:
		# ~ quadrato=i*i
		# ~ if str(i) in str(quadrato):
			# ~ print(i,quadrato)
	# ~ for i in range(n1):
		# ~ print(ix)
		# ~ print(q1[i])
	# ~ quadratostr(x)	
	# ~ def ciao():
		# ~ for x in range(11,1000):
			# ~ q=x*x

		# ~ q1=str(q)
		# ~ for j in q1:
		# ~ x1=str(x)	
		# ~ if x>9:
		# ~ last_cifra_quad=q1[len(q1)-1]
		# ~ else:
			# ~ last_cifra_quad=q1
		# ~ if q>9:
		# ~ last_cifra_num=x1[len(x1)-1]
		# ~ else:
			# ~ last_cifra_num=x1
		# ~ if x1 in q1 and last_cifra_num==last_cifra_quad:
			# ~ print(x1,q1)

