###CARTELLA=lista
a=[3,4,5,6]
b=[5,6,7,3]
# ~ for x in zip(a,b):
# ~ c=0
lista=[]
for x in a:
	for x in b:
		if x in a and x in b:
				# ~ c=c+1
				# ~ if c==1:
					# ~ print(x)
			lista.append(x)
print(	"intersection")		
print(list(set(lista)))
