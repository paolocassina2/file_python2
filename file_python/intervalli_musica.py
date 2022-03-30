note=["do","re","mi","fa","sol","la","si"]

intervallo=["tono","tono","semitono","tono","tono","tono"]
c=0
a=0
nota1="re"
nota2="la"
alterazione2=""
alterazione1=""

# ~ if "mi" in nota1:
	# ~ print("ciao")
# ~ for jj in note:
	# ~ if jj in nota1:
		# ~ print(jj,"jj")

indice1=note.index(nota1)
indice2=note.index(nota2)
# ~ for x,z in zip(note[indice1:indice2+1],intervallo[indice1:indice2+1]):
	# ~ print(x,z)
	# ~ if intervallo==[tono]

# ~ print(nota1,nota2)
# ~ print(indice1,indice2)
for x in zip(range(indice1,indice2+1)):
	c=c+1
	print(c)
if c==2 or c==3 or c==6 or c==7:
	if alterazione2=="b":
		print(c, "minore")
	else:	
		print(c,"maggiore")
# ~ def ci():		

print(intervallo[indice1:indice2+1])
# ~ def ciao():
if c==5:
		# ~ if intervallo[indice1:indice2+1]==[	"semitono","tono","tono","semitono"]:
		# ~ if a:
			print(c, "giusta")
		# ~ elif intervallo[indice1+1:indice2+1]==[	"semitono","tono","tono","tono"]:
		# ~ else:	
			# ~ print(c,"eccedente")
			# ~ print(c,"maggiore")
# ~ print(intervallo[indice1+1:indice2+1])
# ~ if alterazione1 and alterazione2=="":
	
	# ~ a=a+1
	# ~ c=c+1
	# ~ if nota1==x:
		# ~ ind=note.index(x)
	# ~ print(ind)
		
		# ~ if c>=ind:
			# ~ a=a+1
		# ~ print(a)
		# ~ if nota2==x:
			# ~ break

		# ~ print(a)
		# ~ print("intervallo",a)
