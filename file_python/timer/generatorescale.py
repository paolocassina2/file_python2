


note=["do","re","mi","fa","sol","la","si"]
note_diesis=[]
for x in note:
	note_diesis.append(x+"#")

lista=[]
dizio={}
for x in range(0,len(note_diesis)-1):
	print(note_diesis[x:x+2])
	# ~ if "#" in note_diesis[x] and note_diesis[x+2]:
	lista.append(tuple(x,"tono"))
print(lista)
		# ~ dizio["tono"]=[note_diesis[x:x+2]]
	# ~ dizio[str(note_diesis[x:x+2])]="tono"
print(dizio)
# ~ print(note_diesis)
inter=["tono","tono","semitono","tono","tono","tono","semitono"]
# ~ notebemolli=["do","re","mi","fa","sol","la","si"]
# ~ notediesis=["do","re","mi","fa","sol","la","si"]

# ~ scala1=["si","do+","re+","mi","fa+","sol+","la+"]	#scala di si
# ~ scala2=["sol","la","si","do","re","mi","fa+"]
# ~ nota2=""
# ~ nota1="sol"
