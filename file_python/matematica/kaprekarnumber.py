##CARTELLA==matematica
#142,857 is a Kaprekar number[5]
# ~ 142,857 is a Kaprekar number[5]f
abc=""
# ~ for i in range(400000):
n= 142857	#check if kaprekar number
for j in str(n):
	abc=abc+j	
# ~ print(abc)
# ~ for jj in ab
ciao1=[x for x in abc]
ciao=sorted(ciao1)
# ~ ciao1=abc.split()
# ~ print(ciao1)
# ~ ciao=ciao1.sort()
# ~ print(ciao)
mm=n*3
ciaociao1=[x for x in str(mm)]
ciaociao2=sorted(ciaociao1)
if ciaociao2==ciao:
	print(n,"is kaprekar number")
ciao1=[]
ciao=[]
ciaociao1=[]
ciaociao2=[]
mm=1
abc=""

def ciao():
	
	for i in range(200000):

		for j in str(i):
			abc=abc+j
		ciao1=abc.split()
		ciao=ciao1.sort()
		for  x in range(0,8):
			m=i*x
			m1=str(m)
		# ~ m2=m1.sort()
			m2=m1.split()
			m3=m2.sort()
				# ~ if m
			if m3==ciao:
				print("kaprekar n",i)
		abc=""
