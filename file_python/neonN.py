
###CARTELLA==serie
#9 -->quadrato 81--->  8+1=9
c1=0
for i in range(0,100):
	quadrato=i*i
	c=0
	for j in str(quadrato):
		c=c+int(j)
	if c==i:
		print(c," is a neon number")


#####################
# ~ Python program to solve quadratic equation.
#The pronic number is a product of two consecutive integers of the form: n(n+1).
# ~ for i in range(300):
	# ~ print(i*(i+1))






###############################
ciao="ciiaaaoooo"
ciao1=set(ciao)
print(ciao1)
for contaset in ciao1:
	x=0
	for xy in ciao:
		if xy==contaset:
			x=x+1
	
	print(contaset,"occurred ",x, " times")
#x**2-4 = 0				
#2x2 + 3x + c = 0	
def solve_quadratic_eq():
	#ax2 + bx + c = 0
	a=1
	b=0
	c=-4
	# ~ print("sol1 ",
	# ~ print("sol2 ",((-b-(((b**2)-(4*a*c))**1/2))/(2*a)))
	x1=((-b+(((b**2)-(4*a*c))**1/2))/(2*a))
	print(a*(x1**2)+b*x+c)

solve_quadratic_eq()	
	# ~ return
# ~ print(x)
