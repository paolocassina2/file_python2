
a=2306
b=3440
c=18

d=[a,b,c]
# ~ massimo=0
def massimotra2():
	if a >b:
		massimo=a
	else:
		massimo=b
	print(massimo)
def massimotra3(a,b,c):
	if a >b and a>c:
		massimo=a
		return "massimo "+str(massimo)
	elif b>a and b>c:
		massimo=b
		return "massimo "+ str(massimo)
	elif c>a and c>b:
		massimo=c
		return "massimo "+ str(massimo)
	
print(massimotra3(2,3,4))
	# ~ f x >a and x>b and x>c:
		# ~ print(max)
		# ~ break
	# ~ if x>massimo:
		# ~ print("ciao")

###CARTELLA==
###CARTELLA==matematica