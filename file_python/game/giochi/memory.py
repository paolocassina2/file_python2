
a=["*","A","C","C","*","A","x","B","x","B"]

b=["###","###","###","###","###","###","###","###","###","###"]
# ~ for i in a:
	# ~ b.append("###")
# ~ print(a[2])
# ~ for i in range(2):
punteggio=0

while True:
	scegliposiz=int(input("posiz"))
	print("scegli",scegliposiz)
	scegliposiz1=int(input("posiz"))
	print("scegli",scegliposiz1)
	if a[scegliposiz]==a[scegliposiz1]:
		punteggio=punteggio+1
		print(punteggio)
		b[scegliposiz]=a[scegliposiz]
		b[scegliposiz1]=a[scegliposiz1]
	

	if b[0]!="###" and b[1]!="###"  and b[2] !="###" and b[3]!="###"  and b[4] !="###" and b[5]!="###" and  b[6]!="###" and  b[7]!="###"  and b[8] !="###" :
		print("hai vinto")
		print(b)
		break
	# ~ break
	print(b)
