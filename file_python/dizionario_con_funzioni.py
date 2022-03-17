# ~ def bye():
	
	# ~ return abc
# ~ def abc():
	# ~ abc.var=0
# ~ abc()
# ~ bye()
abc=5
a=0




def ciao(abc):
	while True:
	
		abc=abc+1
		return abc
def ciao1(abc):
	while True:
		abc=abc-1
		return abc
a=0

dizio={"a":ciao(abc),"b":ciao1(abc)}

print("dizio", dizio["b"])
b="a"
import time
while True:
	time.sleep(1)
	if a <=10:
		if b=="a":
			a=a+1
	if a <=1:
		b="a"		
	if a>10:
		b="b"
	if b=="b":
		a=a-1
	print(a)
	# ~ print(dizio["a"])
	# ~ print(ciao(abc))
