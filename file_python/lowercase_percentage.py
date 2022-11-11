# ~ ciao="A".is.low()
print() 
ciao="aCAr"
c=0
d=0
for x in ciao:
	c=c+1
	x.islower()
	if x.islower()==True:
		d=d+1

print("percentuale minuscole ",d/c*100," percento")
