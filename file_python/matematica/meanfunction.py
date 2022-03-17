
def mean(a,b,c):
	return((a+b+c))/3
	
# ~ print(mean(2,4,6))


def mean():
	s=0
	c=0
	print("insert numbers")
	print("press enter to exit")
	while True:
		# ~ if x!="":
		x=input("x  ")
		if x!="" and x.isnumeric():
			# ~ c>=1:
			c=c+1
			
			s=s+int(x)
		if c>=1:
			media=s/c
		if x=="" and c>=1:
			return ("media ",media)
			break
print(mean())
# ~ print()
# ~ print()

def calcola_media_in_un_intervallo():
	
	a=input("primo _numero_range  ")
	# ~ print(a.isnumeric())
	# ~ print("calcola media in un intervallo")
	while a.isnumeric()==False:
		a=input("primo _numero_range  ")
	print()
		
	b=input("secondo _numero_range  ")
	while b.isnumeric()==False:
		b=input("secondo _numero_range  ")
	if a>b:
		a,b=b,a
	print("a",a)
	print("b",b)
	
# ~ def difi():
	def mean_of_range(a,b):
		s=0
		c=0
		# ~ return(int(b)-int(a))
		for i in range(int(a),int(b)+1):
			s=s+i
			c=c+1
			# ~ print(i)
		# ~ for x in range(0,(b-a)+1):
		media=s/c
		print("somma ",s)
		print("n", c)
		print("media numeri da ",int(a) ," a ",int(b),":",end="		")	
		
		return media
		
	print(mean_of_range(a,b))
calcola_media_in_un_intervallo()

###CARTELLA==matematica