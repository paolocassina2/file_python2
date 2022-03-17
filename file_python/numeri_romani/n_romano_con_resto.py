n="187"
multiplo_c=int(n)//100
resto=int(n)%100
# ~ print(resto)
# ~ print(multiplo_c)
# ~ print(resto)
n_d=""
resto_d=resto%50
# ~ if resto_d>=0:
u=""
resto_u=resto_d%5
# ~ print(resto_u)
if resto_u==4:
	u="IV"
elif 5<=resto_u<=8:
	u="V"+resto_u%5*"I"
else:
	u=resto_u%5*"I"

	
if 50<=resto<90:
	n_d="L"+resto_d//10*"X"
# ~ print(resto_d)
# ~ print(resto_u)
# ~ cinque=
centinaia=multiplo_c*"C"
# ~ print("fd",resto_u)
# ~ print(n_d)
print(u)
# ~ print(str(centinaia)+str(n_d)+str(u))

###CARTELLA==numeri_romani