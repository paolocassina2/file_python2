
# ~ def ciao():
aa=["#","j","j"]
bb=["#","x","#"]
cc=["#","x","#"]


# ~ print(b,c,d)
a=[aa,bb,cc]
colonna=[]
riga=[]
hh=[]
# ~ c1,c2,c3=[],[],[]
# ~ r1,r2,r3=[],[],[]
# ~ for x in a:
ff=[]
# ~ for x in range(3):
for j in range(0,3):
	# ~ ff=[]
	# ~ hh=[]
	c=0
	c1=0
	c2=0
	c3=0
	for z in range(0,3):
		# ~ ff.append(a[j][z])
		# ~ hh.append(a[z][j])
		if a[j][z]=="*": 
		
			c=c+1
			# ~ c1=c1+1
		elif a[j][z]=="#" :
			c1=c1+1
			# ~ c3=c3+1
		elif a[z][j]=="*":
			c2=c2+1 
			# ~ print(c2)
		elif a[z][j]=="#":
			c3=c3+1
			# ~ print(c3)
	if c==len(a[j]):
		print("soluz ",a[j])
		break
	if c1==len(a[j]):
		print("soluz ",a[j])
		break
	
	if c2==len(a[j]):
		print("soluz ",a[j])	
		break
	if c3==len(a[j]):
		print("soluz ",a[j])
		break
	# ~ colonna.append(ff)	
	# ~ riga.append(hh)
	
	# ~ ff=[]
	# ~ hh=[]
print(colonna)
print(riga)
def ciao():
	for x,y in zip(colonna,riga):
		c=0
		for j in x:
			if j=="*":
				c=c+1
		if c==len(x):
			print("soluzione",x)
			break
			
		# ~ nd([a[j][z])
		# ~ c2.append(a[j][x])
		# ~ c3.append(a[j][x])
# ~ def ciao():
# ~ for zz in range(3):
		
		# ~ r2.append(a[x][j])
		# ~ r3.append(a[x][j])
	# ~ l1=[]
	# ~ l2=[]
		# ~ print(x[j])
	# ~ print(l1)
		# ~ l1=[]

# ~ lista_vittoria=[set(r1),set(r2),set(r3),set(c1),set(c2),set(c3)]
# ~ caso=0
# ~ for x in lista_vittoria:
	# ~ caso+=1
	# ~ if len(x)==1:
		# ~ if "*" in x:
			# ~ vinci.var="a"
		# ~ else:
			# ~ vinci2.var="a"
		
		# ~ break
	# ~ for z in range(0,len(a)):
			# ~ colonna.append(a[j][z])
			# ~ print(a[z])
		# ~ for x in range(0,3):
		# ~ print()
	# ~ for x in a[b]:
	# ~ for y in range(len(a[x])):
		# ~ print(a[0][y])
		# ~ colonna.append(a[b])
		# ~ print(a[x][y])
	# ~ colonna.append(a[x])
	# ~ print(riga)
	# ~ print(colonna)
	# ~ riga=[]
	# ~ colonna=[]
	# ~ print(a)
	# ~ print(a)
def ciao():
	if  "-" not in diag2:
		if len(set(diag2))==1:
			if "*" in diag2:
				print("vittoria g1,diagonale2")
				vinci.var="a"
			else:
				print("vittoria g2,diagonale2")
				vinci2.var="a"
		# ~ print(set(list(a[:,2])))
		# ~ print(type(a[:,2]))
			# ~ for y in range(3):
				# ~ print(res.var[0][x])
		# ~ for x in res.var:
			# ~ c=c+1
			# ~ if c%2==0:
			# ~ print(x)
		# ~ for y in x:
			# ~ print(y)

				# ~ for x in 
				
def ciao():
		if res.var[0]=="*" and res.var[1]=="*"  and res.var[2]=="*" :	
			caso.var=1#casi orizzontali
			print("tris")
			vinci.var="a"
			# ~ canvas.create_line(15, 25, 200, 25)
			# ~ canvas1.var.create_line(200, 150, 700, 150,width=2,fill="red")
			# ~ if c=33
			# ~ vinci2.var="b"
					# ~ break
		elif res.var[3]=="*" and res.var[4]=="*"  and res.var[5]=="*" :
			caso.var=2
			print("tris")
			vinci.var="a"
			# ~ canvas1.var.create_line(200, 300, 700, 300,width=2,fill="red")
			# ~ vinci2.var="b"
			#	break
			# ~ break
		elif res.var[6]=="*" and res.var[7]=="*"  and res.var[8]=="*" :
			caso.var=3
			print("tris")
			# ~ vinci.var="a"
			# ~ canvas1.var.create_line(200, 500, 700, 500,width=2,fill="red")
			# ~ vinci2.var="b"
			# ~ break
		# ~ ######################################
		elif res.var[0]=="*" and res.var[3]=="*"  and res.var[6]=="*" :		#casi verticali
				caso.var=4
				print("tris")
				# ~ vinci.var="a"
				# ~ vinci2.var="b"
				# ~ break
		elif res.var[1]=="*" and res.var[4]=="*"  and res.var[7]=="*" :
				caso.var=5
				print("tris")
				# ~ vinci.var="a"
				# ~ vinci2.var="b"
				# ~ break
		elif res.var[2]=="*" and res.var[5]=="*"  and res.var[8]=="*" :
				caso.var=6
				print("tris")
				# ~ vinci.var="a"
				# ~ canvas1.var.create_line(700, 50, 700, 700,width=2,fill="red")
				# ~ break
				# ~ break
				# ~ vinci2.var="b"
		# ~ #####vinci2.var="b"#########################################
		elif res.var[0]=="*" and res.var[4]=="*"  and res.var[8]=="*" :	
				caso.var=7	#casi diagonali
				print("tris")
				# ~ vinci.var="a"
				# ~ canvas1.var.create_line(200, 800, 800,50,width=2,fill="red")
				# ~ vinci2.var="b"
				# ~ break
		elif res.var[2]=="*" and res.var[4]=="*"  and res.var[6]=="*" :
				caso.var=8
				print("tris")
				# ~ vinci.var="a"
				# ~ canvas1.var.create_line(50, 800, 800,50,width=2,fill="red")
				# ~ vinci2.var="b"
				# ~ break
		######################################
		if res.var[0]=="#" and res.var[1]=="#"  and res.var[2]=="#" :	
			caso.var=1			#computer
			print("tris")
			# ~ vinci2.var="a"
			# ~ vinci.var="b"
			# ~ canvas1.var.create_line(200, 100, 800, 100,width=2,fill="red")
			# ~ break
		elif res.var[3]=="#" and res.var[4]=="#"  and res.var[5]=="#" :
				caso.var=2
				print("tris")
				# ~ vinci2.var="a"
				# ~ vinci.var="b"
				# ~ canvas1.var.create_line(200, 200, 800,200,width=2,fill="red")
				# ~ break
		elif res.var[6]=="#" and res.var[7]=="#"  and res.var[8]=="#" :
				caso.var=3
				print("tris")
			
				# ~ canvas1.var.create_line(200, 500, 800,500,width=2,fill="red")
				# ~ vinci2.var="a"
				# ~ vinci.var="b"
				# ~ break
		# ~ ######################################
		elif res.var[0]=="#" and res.var[3]=="#"  and res.var[6]=="#" :	
				caso.var=4	#casi verticali
				print("tris")
				# ~ vinci2.var="a"
				# ~ vinci.var="b"
				# ~ canvas1.var.create_line(300, 50, 300, 600,width=2,fill="red")
				# ~ break
		elif res.var[1]=="#" and res.var[4]=="#"  and res.var[7]=="#" :
				caso.var=5
				# ~ vinci2.var="a"
				

				# ~ vinci.var="b"
				print("tris")

				# ~ break
				# ~ break
		elif res.var[2]=="#" and res.var[5]=="#"  and res.var[8]=="#" :
				caso.var=6
				# ~ vinci2.var="a"
				# ~ canvas1.var.create_line(700, 50, 700, 700,width=2,fill="red")
				# ~ vinci.var="b"
				print("tris")
				# ~ break
				# ~ break
		# ~ ##############################################
		elif res.var[0]=="#" and res.var[4]=="#"  and res.var[8]=="#" :	
				caso.var=7	#casi diagonali
				# ~ vinci2.var="a"
				# ~ canvas1.var.create_line(50, 50, 800,800,width=2,fill="red")
				# ~ vinci.var="b"
				print("tris")
				# ~ break
		elif res.var[2]=="#" and res.var[4]=="#"  and res.var[6]=="#" :
				caso.var=8
				# ~ vinci2.var="a"
				# ~ canvas1.var.create_line(50, 800, 800,50,width=2,fill="red")
				# ~ vinci.var="b"
				print("tris")
				# ~ break

		# ~ print("vinci2",vinci2.var)
		# ~ print("vinci",vinci.var)

		# ~ def condizioni_pareggio():

				# ~ print("pareggio")
			# ~ else:
				# ~ pareggio.var="abc"
