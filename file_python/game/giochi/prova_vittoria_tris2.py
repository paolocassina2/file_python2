
# ~ def ciao():
d=[x for x in range(1,4)]
b=[x for x in range(4,7)]
c=[x for x in range(7,9)]


print(b,c,d)
a=[b,c,d]

c1,c2,c3=[],[],[]
r1,r2,r3=[],[],[]
# ~ for x in a:
# ~ for x in range(3):
for j in range(3):
		c1.append(a[j][0])
		c2.append(a[j][1])
		c3.append(a[j][2])
# ~ def ciao():
# ~ for zz in range(3):
		r1.append(a[0][j])
		r2.append(a[1][j])
		r3.append(a[2][j])
	# ~ l1=[]
	# ~ l2=[]
		# ~ print(x[j])
	# ~ print(l1)
		# ~ l1=[]
	print(c1,c2,c3)

	print(r1,r2,r3)
	lista_vittoria=[set(r1),set(r2),set(r3),set(c1),set(c2),set(c3)]
	caso=0
	for x in lista_vittoria:
		caso+=1
		if len(x)==1:
			if "*" in x:
				vinci.var="a"
			else:
				vinci2.var="a"
			
			break
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
