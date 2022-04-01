#PULSANTE RESTART FUNZIONA
#VERSIONE -->UMANO CONTRO UMANO
###############################################
#CARTELLA==prova

def res():
	res.var=[]
res()
import numpy as np
# ~ aaa=["*","6","*"]
# ~ bbb=["x ","*","7"]
# ~ ccc=["*","5","x"]

res.var=["x","*x","xx","x","-","-","x","-","-"]
# ~ res.var=[x for x in range(1,10)]
# ~ c=0
# ~ for  x in res:
	# ~ if c%3==0:
aaa=res.var[0:3]
bbb=res.var[3:6]
ccc=res.var[6:9]
# ~ print(aaa,bbb,ccc)
# ~ def ciao():
# ~ res.var(a,b,c)
a = np.array([aaa,bbb,ccc])
	# ~ print(a)
	# ~ print(a)
	# ~ matrix([[1, 2],
			# ~ [3, 4]])
for x in range(len(a)):
		b=list(a[:,x])
		# ~ print(b)
		print()
		abc=set(list(a[:,x]))
		if  "-" not in abc:
			if len(abc)==1:#se il set è lungo uno significa che gli elementi sono tutti uguali
				if "*" in abc :
					vinci.var="a"
					print("vittoria g1_verticale")
				else:
					print("vittoria g2_verticale")
					vinci2.var="a"
for x in range(len(a)):
		abc1=set(a[x])
		print(abc1)
		if  "-" not in abc1:
			if len(abc1)==1:
				if "*" in abc1:
					print("vittoria g1,orizzionataòe")
					vinci.var="a"
				else:
					print("vittoria g2,orizzontale")
					vinci2.var="a"
diag1=[aaa[0],bbb[1],ccc[2]]
diag2=[aaa[2],bbb[1],ccc[0]]
if  "-" not in diag1:
	if len(set(diag1))==1:
		if "*" in diag1:
			print("vittoria g1,diagonale1")
			vinci.var="a"
		else:
			print("vittoria g2,diagonale1")
			vinci2.var="a"
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
