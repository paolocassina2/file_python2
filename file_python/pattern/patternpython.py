#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5
###CARTELLA==pattern
print("PATTERN 1")
for x in range(1,6):

	for y in range(1,6):
		
		print(y,end=" ")
		if y==x:
			 break
			 
	print()		 
print()	
#6 6 6 6 6 6 
#6 6 6 6 6 
#6 6 6 6 
#6 6 6 
#6 6 
#6
print("PATTERN 2")
c=6
n=str(6)
for x in range(c,0,-1):
	# ~ print(x)
	# ~ for j in range(0,x):
		print((n+" ")*x ,end=" ")
		print()
# ~ Enter the number of rows: 6
print()
print("pattern3")
#6 6 6 6 6 6 
#5 5 5 5 5 
#4 4 4 4 
#3 3 3 
#2 2 
#1
#print("PATTERN 2")
c1=6

for x1 in range(c1,0,-1):
	# ~ print(x)
		
		n1=str(x1)
	# ~ for j in range(0,x):
		print((n1+" ")*x1 ,end=" ")
		print()
# ~ Enter the number
