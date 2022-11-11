note=["do","re","mi","fa","sol","la","si"]
# ~ notebemolli=["do","re","mi","fa","sol","la","si"]
# ~ notediesis=["do","re","mi","fa","sol","la","si"]

scala1=["si","do+","re+","mi","fa+","sol+","la+"]	#scala di si
scala2=["sol","la","si","do","re","mi","fa+"]
# ~ nota2=""
nota1="sol"
if nota1=="sol":
# ~ insnota=[]
	# ~ nota1=scala2[0]
	c=0
	nota2="re"
	for x in scala2:
		if x==nota2:
			c=c+1
		# ~ if x==nota2:
			# ~ continue
			# ~ break
			print(c)
			break
	if c==4 or  c==5:
		print(str(c)+" giusta")
			

# ~ indice=note.index(nota1)
# ~ lista=[x for x in note[indice:len(note)]]
# ~ lista1=[x for x in note[0:indice]]
# ~ lista2=lista+lista1
# ~ for x in j:
# ~ lista1=[y for y in x: for x in lista]
	# ~ for jj in x:
		
# ~ print(lista2)
# ~ for x in note:

		# ~ print(a)
		# ~ print("intervallo",a)
