primidiecihexadecimal=[0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
"A",
"B",
"C",
"D",
"E",
"F",
10]
a=48
diz= {}
for x in range(len(primidiecihexadecimal)):
	# ~ diz[str(x)]=primidiecihexadecimal[x]
	print(primidiecihexadecimal[x])
	diz[str(x)]=primidiecihexadecimal[x]
print(diz)
listaresto=[]
while a>0:
	a=int(a/16)
	print("a",a)
	resto=a%16	# ~ print(resto)
	listaresto.append(diz[str(resto)])
	print("resto",resto)
# ~ print(lista(resto))
# ~ print(diz["10"])
print(listaresto)

###CARTELLA==
###CARTELLA==numeral_system
###CARTELLA==numeral_system