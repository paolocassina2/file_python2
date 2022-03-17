###CARTELLA==matematica
n=5
s=0
res=""
for i in range(1,n+1):
	print(i)
	
	# ~ print(s)
	# ~ print(i)
	s=s+i
	if i <n:
			res=res+str(i)+"+"
	else:
		res=res+str(i)
	# ~ else :
		# ~ res=res+"="
res=res+" = "+str(s)
print(res)
# ~ a=[3,4,5]
# ~ print(sum(a))
#python program to read a number n and compute n+nn+nnn
n=input("	n")
s=0
J=""
for uuu in range(4):
	J=J+uuu*str(n)+" "
	# ~ print(j)
	# ~ J=J+" "
print(J)
abc=J.split()
print(abc)
s=0
for x in abc:
	s=s+int(x)
print(s)
	# ~ j=int(uuu*str(n))
	# ~ j1=float(j)
	# ~ print(int(j))
	# ~ print(type(j))
	# ~ j1=int(j)
	# ~ s=s+j
# ~ print(s)
