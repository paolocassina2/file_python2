import string
lettere=string.ascii_lowercase
# ~ print(type(lettere))
# ~ print(lettere)

testo="ciao mi chiamo francesco"
conta1=-1
lista_spazi=[]
for x in testo:
	conta1=conta1+1
	if x==" ":
		lista_spazi.append(conta1)
		# ~ print(conta1)
		
print(lista_spazi)



testo1= testo.replace(" ", "")
# ~ print(testo1)
# ~ "a in lettere"
# ~ >>> s.strip()


	# ~ print(lettere.index("e"))
conta=0
lista_nomi=[]
# ~ print(lista_var)
diz={}
# ~ print(type(diz))
# ~ print()
# ~ CountryCodeDict["Spain"]= 34

# ~ print(diz)
for x in testo1:
	print()
	conta=conta+1
	diz[x]=lettere[lettere.index(x)+1]#quando codifico  aggiungo lettera successiva-->+1. quando decodifico -1
	# ~ diz=diz+[str(x):"ciao"]
# ~ print(diz)
codifica=""
for x in testo1:
	codifica=codifica+diz[x]
# ~ print(codifica)
codifica1=""

c_s=-1
def rimetti_spazi():
	for xz in codifica:
		c_s=c_s+1
		for zz in lista_spazi:
			if c_s==zz:
				codifica1=codifica1+" "
		codifica1=codifica1+xz
# ~ print(codifica)

###############################
conta1=0
diz1={}

#DECODIFICO
for jj in codifica:
	# ~ print()
	conta1=conta1+1
	diz1[jj]=lettere[lettere.index(jj)-1]#quando codifico  aggiungo lettera successiva-->+1. quando decodifico -1
	# ~ diz=diz+[str(x):"ciao"]
print(diz1)
decodifica=""
for x in codifica:
	decodifica=decodifica+diz1[x]
print(decodifica)
# ~ for xu in codifica:
# ~ for x in testo1:
	# ~ decodifica=decodifica+diz[xu]
	
# ~ print(decodifica)
# ~ print(decodifica)
# ~ codifica1=""

		
		# ~ if c_s
# ~ codifica1=""
# ~ for j in codifica:
	# ~ for y in lista_spazi:
		# ~ codificaj=
	
	# ~ nome_var="lettera"+str(conta)
		# ~ var=globals()[nome_var] = 
		# ~ lista_nomi.append(nome_var)
		# ~ diz[nome_var].append(var)
		
	# ~ print(diz)
	# ~ variable("lettera1")
	# ~
	# ~ print(lista_var)
	# ~ print(diz)
	# ~ print(lista_nomi)
	# ~ r=0
	# ~ for j in lista_nomi:
	# ~ r=r+1
	# ~ var=globals()[j] = 33+r
	# ~ print(lettera2)
	# ~ for x in lista_var:
	# ~ print(var)
	# ~ testo_codificato=testo.replace(x, lettere[lettere.index(x)+1])



	# ~ print(testo_codificato)
