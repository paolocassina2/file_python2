import numpy as np
from itertools import permutations
import time
# ~ import clock
from datetime import datetime

now = datetime.now()
ora_in=now.strftime("%H:%M:%S")
print("ora_inizio ",ora_in)
# ~ ora_inizio import time
ora_inizio = time.time()
# ~ print("ora inizio", ora_inizio)
def input_sudoku():
	print("input_sudoku")
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
	for i in range(0,9):
		cc=cc+1
		aa=input("a"+str(cc)+" 	")
		
		if aa=="":
			l1.append("x")
		else:
			l1.append(aa)	
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
			l2.append(bb)
	cc=0
	print()
	for i in range(0,9):	
		cc=cc+1	
		cc_1=input("c"+str(cc)+" 	")
		# ~ l3.append(cc_1)
		if cc_1=="":
			l3.append("x")
		else:
			l3.append(cc_1)
	cc=0
	print()
	for i in range(0,9):	
		cc=cc+1
		dd=input("d"+str(cc)+" 		")
		# ~ l4.append(dd)
		if dd=="":
			l4.append("x")
		else:
			l4.append(dd)
	cc=0	
	print()
	for i in range(0,9):
		cc=cc+1
		ee=input("e"+str(cc)+" 		")
		# ~ l5.append(ee)
		if ee=="":
			l5.append("x")
		else:
			l5.append(ee)
	print()
	cc=0
	print()
	for i in range(0,9):
		cc=cc+1
		ff=input("f"+str(cc)+" 		")
		
		if ff=="":
			l6.append("x")
		else:
			l6.append(ff)
	cc=0
	print()
	for i in range(0,9):
		cc=cc+1
		gg=input("g"+str(cc)+" 		")
		# ~ l7.append(gg)
		if gg=="":
			l7.append("x")
		else:
			l7.append(gg)
	cc=0
	print()
	for i in range(0,9):	
		cc=cc+1
		hh=input("h"+str(cc)+" 		")
		# ~ l8.append(hh)
		if hh=="":
			l8.append("x")
		else:
			l8.append(hh)
	print()
	for i in range(0,9):
		cc=cc+1
		kk=input("k"+str(cc)+" 		")
		# ~ l9.append(kk)
		if kk=="":
			l9.append("x")
		else:
			l9.append(kk)
	# ~ a=input()
	print("l1",l1)
	print("l2",l2)
	print("l3",l3)
	print("l4",l4)
	print("l5",l5)
	print("l6",l6)
	print("l7",l7)
	print("l8",l8)
	print("l9",l9)
	print(len(l1))
	print(len(l2))
	print(len(l3))
	print(len(l4))
	print(len(l5))
	print(len(l6))
	print(len(l7))
	print(len(l8))
	print(len(l9))

	print()
input_sudoku()
# ~ if contatore6>=9:
								# ~ if len(set(rettangolo4))==len(rettangolo4) and len(set(rettangolo5))==len(rettangolo5) and len(set(rettangolo6))==len(rettangolo6):

								

									# ~ print(sudoku.var)
									# ~ print()		# ~ if contatore==len(b.var):
									# ~ soluz="ok"			# ~ print(contatore)
							
														# ~ if d1[0]!=c1[0]!=a.var[0]!=b.var[0] and d1[1]!=c1[1]!=a.var[1]!=b.var[1]  and d1[2]!=c1[2]!=a.var[2]!=b.var[2] and d1[3]!=c1[3]!=a.var[3]!=b.var[3] and d1[4]!=c1[4]!=a.var[4]!=b.var[4] and d1[5]!=c1[5]!=a.var[5]!=b.var[5] and d1[6]!=c1[6]!=a.var[6]!=b.var[6] and d1[7]!=c1[7]!=a.var[7]!=b.var[7] and d1[8]!=c1[8]!=a.var[8]!=b.var[8]:

															# ~ print(sudoku.var)
							
													# ~ else:
															# ~ contatore=0
														
																# ~ soluzione="ok"
														# ~ print(sudoku.var)
								
					# ~ else:
						# ~ contatore8=0
		# ~ else:
		# ~ contavolte=0		
			
def ciao():
		
							# ~ soluz="ok"
							# ~ break		
							for c1 in listapermutazioni1:
								c.var=c1
								sudoku.var = np.array([a.var,b.var,c.var])
								definisci_quadrati1_2_3()
							
								# ~ print(sudoku.var)
								for x in range(len(a.var)):
				# ~ if soluz=="ok":
					# ~ break	
									colonna2=[a.var[x],b.var[x],c.var[x]]
									# ~ print(d.var[i])
													
														# ~ if contatore<=len(d1):
									# ~ if len(set(colonna1))==len(colonna1):	
										# ~ contatore2=contatore2+1
										# ~ print(contatore2)
												# ~ print(sudoku.var)
												# ~ soluz="ok"
												# ~ break
												# ~ 
							# ~ else:
								# ~ contatore2=0				
