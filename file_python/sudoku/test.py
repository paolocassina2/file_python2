import numpy as np
from itertools import permutations
import time
lista_ind1=[]
lista_ind2=[]
lista_ind3=[]
lista_ind4=[]
lista_ind5=[]
lista_ind6=[]
lista_ind7=[]
lista_ind8=[]
lista_ind9=[]

			
lista_val1=[]
lista_val2=[]
lista_val3=[]
lista_val4=[]
lista_val5=[]
lista_val6=[]
lista_val7=[]
lista_val8=[]
lista_val9=[]


# ~ import clock
from datetime import datetime
# ~ from itertools import permutations
listapermutazioni1=[]		
# ~ def ciao():#generatore di sudoku(manca controllo quadrati)
listapermutazioni = list(permutations(range(1, 10)))
for x in listapermutazioni:
	listapermutazioni1.append(list(x))
now = datetime.now()
ora_in=now.strftime("%H:%M:%S")
print("ora_inizio ",ora_in)
# ~ ora_inizio import time
ora_inizio = time.time()
# ~ print("ora inizio", ora_inizio)
cc=0
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
l8=[]
l9=[]
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
s6=[]
s7=[]
s8=[]
s9=[]

for i in range(0,9):
	cc=cc+1
	aa=input("a"+str(cc)+" 	")
	
	if aa=="":
		l1.append("x")
	else:
		l1.append(int(aa))	
	# ~ aa=input("a"+str(cc)+" 	")
print()
cc=0
for i in range(0,9):
	cc=cc+1
	bb=input("b"+str(cc)+" 	")
	# ~ l2.append(bb)
		# ~ l1.append(aa)
	if bb=="":
		l2.append("x")
	else:
		l2.append(int(bb))
cc=0
print()
for i in range(0,9):	
	cc=cc+1	
	cc_1=input("c"+str(cc)+" 	")
	# ~ l3.append(cc_1)
	if cc_1=="":
		l3.append("x")
	else:
		l3.append(int(cc_1))
cc=0
print()
for i in range(0,9):	
	cc=cc+1
	dd=input("d"+str(cc)+" 		")
	# ~ l4.append(dd)
	if dd=="":
		l4.append("x")
	else:
		l4.append(int(dd))
cc=0	
print()
for i in range(0,9):
	cc=cc+1
	ee=input("e"+str(cc)+" 		")
	# ~ l5.append(ee)
	if ee=="":
		l5.append("x")
	else:
		l5.append(int(ee))
print()
cc=0
print()
for i in range(0,9):
	cc=cc+1
	ff=input("f"+str(cc)+" 		")
	
	if ff=="":
		l6.append("x")
	else:
		l6.append(int(ff))
cc=0
print()
for i in range(0,9):
	cc=cc+1
	gg=input("g"+str(cc)+" 		")
	# ~ l7.append(gg)
	if gg=="":
		l7.append("x")
	else:
		l7.append(int(gg))
cc=0
print()
for i in range(0,9):	
	cc=cc+1
	hh=input("h"+str(cc)+" 		")
	# ~ l8.append(hh)
	if hh=="":
		l8.append("x")
	else:
		l8.append(int(hh))
cc=0
print()
for i in range(0,9):
	cc=cc+1
	kk=input("k"+str(cc)+" 		")
	# ~ l9.append(kk)
	if kk=="":
		l9.append("x")
	else:
		l9.append(int(kk))

for x,y,z,u,j,knk,nkn,jjk,kkj in zip(l1,l2,l3,l4,l5,l6,l7,l8,l9):
	# ~ print(type(x))
	# ~ print(type(y))
	# ~ print(type(z))
	# ~ print(type(u))
	# ~ print(type(j))
	# ~ print(type(knk))
	# ~ print(type(nkn))
	# ~ print(type(jjk))
	# ~ print(type(kkj))
	if x!="x":

		lista_ind1.append(l1.index(x))
		lista_val1.append(x)
	if y!="x":
		lista_ind2.append(l2.index(y))
		lista_val2.append(y)
	if z!="x":
		lista_ind3.append(l3.index(z))
		lista_val3.append(z)
	if u!="x":
		lista_ind4.append(l4.index(u))
		lista_val4.append(u)
	if j!="x":
		lista_ind5.append(l5.index(j))
		lista_val5.append(j)
	if knk!="x":
		lista_ind6.append(l6.index(knk))
		lista_val6.append(knk)
	if nkn!="x":
		lista_ind7.append(l7.index(nkn))
		lista_val7.append(nkn)
	if jjk!="x":
		lista_ind8.append(l8.index(jjk))
		lista_val8.append(jjk)
		
	if kkj!="x":
		lista_ind9.append(l9.index(kkj))
		lista_val9.append(kkj)


# ~ print(lista_ind1)
# ~ print(lista_val1)	

# ~ a=input()
# ~ print("l1",l1)
# ~ print("l2",l2)
# ~ print("l3",l3)
# ~ print("l4",l4)
# ~ print("l5",l5)
# ~ print("l6",l6)
# ~ print("l7",l7)
# ~ print("l8",l8)
# ~ print("l9",l9)

conta_val_1=0
nn2=0
nn3=0
nn4=0
nn5=0
nn6=0
nn7=0
nn8=0
nn9=0


print("listindice1",lista_ind1)
print("listaval1",lista_val1)

for y in lista_val1:
	print(type(y))
	print("tipoval")
	
for y in lista_ind1:
	print(type(y))
	print("tipoind")
	
#CONTROLLOQUI
for yj in listapermutazioni1:
	# ~ print(conta_val_1)
	# ~ print(nn2)
	
	for x1,j1 in zip(lista_ind1,lista_val1):

				#mancano tutti i casi per ogni riga
			# ~ print(yj)
	# ~ for x1,j1,x2,j2,x3,j3,x4,j4,x5,j5,x6,j6,x7,j7,x8,j8,x9,j9 in zip(lista_ind1, lista_val1, lista_ind2, lista_val2,  lista_ind3, lista_val3,  lista_ind4, lista_val4,lista_ind5, lista_val5,lista_ind6, lista_val6,lista_ind7, lista_val7,lista_ind8, lista_val8,lista_ind9, lista_val9):
	#	print(x)
		#print(j)
		
		if yj[x1]==j1:
			conta_val_1=conta_val_1+1
			# ~ print("c",conta_val_1)
			# ~ print("conta_val_1",conta_val_1)
		#	print(yj[x])
			if conta_val_1==len(lista_ind1):
				s1.append(yj)
	else:
		conta_val_1=0
#######################################################
	for x2,j2 in zip(lista_ind2,lista_val2):	
		if yj[x2]==j2:
			nn2=nn2+1

			if nn2==len(lista_ind2):
				s2.append(yj)
	else:
		nn2=0	
#######################################################		
	for x3,j3 in zip(lista_ind3,lista_val3):
		if yj[x3]==j3:

			nn3=nn3+1
		
			if nn3==len(lista_ind3):
				s3.append(yj)
	else:
		nn3=0	
#######################################################		
	for x4,j4 in zip(lista_ind4,lista_val4):	
		if yj[x4]==j4:
			nn4=nn4+1
	
			if nn4==len(lista_ind4):
				s4.append(yj)
	else:
		nn4=0				
#######################################################					
	for x5,j5 in zip(lista_ind5,lista_val5):			
		if yj[x5]==j5:
			nn5=nn5+1
	
			if nn5==len(lista_ind5):
				s5.append(yj)
	else:
		nn5=0						
#####################################################
	for x6,j6 in zip(lista_ind6,lista_val6):
		if yj[x6]==j6:
			nn6=nn6+1
			if nn6==len(lista_ind6):
				s6.append(yj)
	else:
		nn6=0						
#####################################################						
	for x7,j7 in zip(lista_ind7,lista_val7):
		if yj[x7]==j7:
			nn7=nn7+1
		
			if nn7==len(lista_ind7):
				s7.append(yj)
	else:
		nn7=0	
####################################################								
	for x8,j8 in zip(lista_ind8,lista_val8):
		if yj[x8]==j8:
			nn8=nn8+1

			if nn8==len(lista_ind8):
				s8.append(yj)
	
	else:
		nn8=0											
#######################################################
	for x9,j9 in zip(lista_ind9,lista_val9):
		if yj[x9]==j9:
			nn9=nn9+1
		
			if nn9==len(lista_ind9):
				s9.append(yj)
								


				
	else:
		nn9=0		



print("******************")
# ~ prin


# ~ print("s9",s9[3])
print("******************")
if len(lista_ind1)==0:
	s1=listapermutazioni1
if len(lista_ind2)==0:
	s2=listapermutazioni1
if len(lista_ind3)==0:
	s3=listapermutazioni1
if len(lista_ind4)==0:
	s4=listapermutazioni1
if len(lista_ind5)==0:
	s5=listapermutazioni1
if len(lista_ind6)==0:
	s6=listapermutazioni1
if len(lista_ind7)==0:
	s7=listapermutazioni1
if len(lista_ind8)==0:
	s8=listapermutazioni1
if len(lista_ind9)==0:
	s9=listapermutazioni1
			

# ~ for x1,x2,x3,x4,x5,x6,x7,x8,x9 in zip(l1,l2,l3,l4,l5,l6,l7,l8,l9):
print(l1)


# ~ print(l2)
# ~ print(l3)
# ~ print(l4)
# ~ print(l5)
# ~ print(l6)
# ~ print(l7)
# ~ print(l8)
# ~ print(l9)	
# ~ print("s1",s1)

	# ~ for x in listapermutazioni1:
			# ~ print(x)
			# ~ if x[3]==4 and x[6]==1 and x[8]==3:
				# ~ s1.append(x)
		# ~ if x[0]==2 and x[4]==3 and x[6]==6:
			# ~ s2.append(x)
		# ~ if x[0]==1 and x[4]==6 and x[6]==5:
			# ~ s3.append(x)
		# ~ if x[0]==9 and x[5]==6:
			# ~ s4.append(x)
		
		# ~ if x[1]==2 and x[5]==7 and x[7]==4:
			# ~ s5.append(x)
		# ~ if x[3]==9 and x[6]== 8:
			# ~ s6.append(x)
		
		# ~ if x[1]==8 and x[2]==4  and x[8]==5 :
			# ~ s7.append(x)	
		# ~ if x[1]== 1 and x[2]== 3 and x[4]==8 and x[8]== 6:
			# ~ s8.append(x)
		# ~ if x[0]==6:
			# ~ s9.append(x)
print("len")	
# ~ print(len(s1))	
print(len(s2))	
# ~ print(len(s3))	
# ~ print(len(s4))	
# ~ print(len(s5))	
# ~ print(len(s6))	
# ~ print(len(s7))	
# ~ print(len(s8))	
# ~ print(len(s9))

print("fd",lista_ind1[0])
print("djfkd",lista_val1[0])
# ~ a=[3,4]
# ~ b=[4,5]

# ~ print(a-b)
# ~ for i in range(0,(len(s2)-2)):
c=0
c1=0
c2=0
for j2 in s2:
	# ~ if j2[0]
	# ~ if j2[0]==2:
	if len(lista_ind1)==1:
		# ~ if j2[lista_ind1[0]]==lista_val1[0]:
		
		if j2[lista_ind1[0]]==1:
			
			# ~ s2.remove(j2)
		# ~ if j2[lista_ind1[0]]==lista_val1[0] and j2[lista_ind1[1]]==lista_val1[1]:
			c=c+1
	if j2[lista_ind1[0]]==2:
			
			# ~ s2.remove(j2)
		# ~ if j2[lista_ind1[0]]==lista_val1[0] and j2[lista_ind1[1]]==lista_val1[1]:
			c1=c1+1	
	if j2[lista_ind1[0]]==3:
			
			# ~ s2.remove(j2)
		# ~ if j2[lista_ind1[0]]==lista_val1[0] and j2[lista_ind1[1]]==lista_val1[1]:
			c2=c2+1	
		
print(c)
print(c1)
print(c2)
			# ~ s2.remove(j2)
	# ~ if len(lista_ind1)==3:
		# ~ if :
			# ~ s2.remove(j2)
		# ~ if j2[lista_ind1[0]]==lista_val1[0] and j2[lista_ind1[1]]==lista_val1[1] and j2[lista_ind1[2]]==lista_val1[2]:
			# ~ s2.remove(j2)
		# ~ if j2[lista_ind1[0]]==lista_val1[0]:
			# ~ s2.remove(j2)
	# ~ elif len(lista_ind1)==2:
		# ~ if j2[lista_ind1[0]]==lista_val1[0] and j2[lista_ind1[1]]==lista_val1[1]:
			# ~ s2.remove(j2)
	# ~ else:
		# ~ if j2[lista_ind1[0]]==lista_val1[0] and j2[lista_ind1[1]]==lista_val1[1]:
			# ~ s2.remove(j2)
		# ~ print(j2)
		# ~ del(s2[i])
		# ~ s2.remove(s2[i])
		# ~ s2.pop(i)
		# ~ print(s2[i])
		# ~ s2.remove(j2)
		# ~ print(j2)
	# ~ else:
		# ~ pass
	# ~ if j2[lista_ind1[1]]==lista_val1[1]:
		# ~ s2.remove(j2)
	# ~ else:
		# ~ pass
# ~ else:
	# ~ continue
		# ~ print(j
	# ~ if j[lista_ind1[2]]==lista_val1[2]:
		# ~ s2.remove(j2)	
			
print("len",len(s2))
