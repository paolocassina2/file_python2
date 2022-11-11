

# ~ for x in range(10,55):

# ~ n=7
for x in range(3,33):
	c=0
	for y in range(1,x+1):
		
		if x%y==0:
			# ~ div=n/y
			c=c+1
	if c<3:
		print(x," prime number")
