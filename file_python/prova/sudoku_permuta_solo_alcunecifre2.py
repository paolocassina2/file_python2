###CARTELLA==prova
from itertools import permutations
###CARTELLA==prova
# Get all permutations of length 2
# and length 2
import itertools

#if a[0]==5 and a [3]==7:
diz1={3:7,4:8,5:6}
diz2={1:1,2:4,7:8}

diz3={0:2,3:3,8:9}
diz4={0:8,2:5,4:1,6:7}
#if b[2]==1 and b [3]==5 and b[6]==6:#chiavi, indici, valori sono le cifre ---> indici e valori delle cifre iniziali
# ~ diz2
# ~ vowel.insert(3, 'o')
lista1=[1,2,3,4,5,6,7,8,9]
lista2=[1,2,3,4,5,6,7,8,9]
lista3=[1,2,3,4,5,6,7,8,9]
lista4=[1,2,3,4,5,6,7,8,9]
# ~ lista5=[1,2,3,4,5,6,7,8,9]
# ~ lista6=[1,2,3,4,5,6,7,8,9]
for y1 in diz1.values():
	# ~ if y in lista:
		lista1.remove(y1)
for y2 in diz2.values():		
		lista2.remove(y2)
for y3 in diz3.values():		
		lista3.remove(y3)
for y4 in diz4.values():		
		lista4.remove(y4)		
# ~ for y4 in diz4.values():		
		# ~ lista4.remove(y4)
		
# ~ for y5 in diz5.values():		
		# ~ lista5.remove(y5)
# ~ for y6 in diz6.values():		
		# ~ lista6.remove(y6)		#se ci sono giä delle cifre iniziali, invece che permutare 9 cifre, permuto un numero di cifre pari a  9-n cifre iniziali
print(lista1)				#quind ise per esempio ci sono 2 cifre iniziali permuto 7 cifre e non 9
conta=0
# ~ lista.insert(0,5)
# ~ print(lista)
# ~ lista1=[]
# ~ def ciao():
for  a in itertools.permutations(lista1):
		ab1=list(a)
		for j1,z1 in zip(diz1.keys(),diz1.values()):
			# ~ lista.insert(j,z)

			ab1.insert(j1,z1)
			# ~ list(a).insert(j,z)
		a=ab1
		for  b in itertools.permutations(lista2):
			ab2=list(b)
			for j2,z2 in zip(diz2.keys(),diz2.values()):
				# ~ lista.insert(j,z)

				ab2.insert(j2,z2)
			# ~ print(a)
			b=ab2
			# ~ print(a)
			# ~ print(b)
			s1=list(set([a[0],b[0]]))
			s2=list(set([a[1],b[1]]))

			s3=list(set([a[2],b[2]]))
			
			s4=list(set([a[3],b[3]]))
			
			s5=list(set([a[4],b[4]]))
			s6=list(set([a[5],b[5]]))
			# ~ if tipo_sud==9:
			s7=list(set([a[6],b[6]]))
			
			s8=list(set([a[7],b[7]]))
			s9=list(set([a[8],b[8]]))
			
			conta=2
			if len(s1)==conta and len (s2)==conta and len (s3)==conta and len (s4)==conta and len (s5)==conta and len (s6)==conta and len (s7)==conta and len (s8)==conta and len (s9)==conta:

			# ~ if len(s1)==2 and len (s2)==2 and len (s3)==2 and len (s4)==2 and len (s5)==2 and len (s6)==2 and len (s7)==2 and len (s8)==2 and len (s9)==2:
		# ~ print(ab)
				conta=3
				for  c in itertools.permutations(lista3):
					
					ab3=list(c)
					for j3,z3 in zip(diz3.keys(),diz3.values()):
						# ~ lista.insert(j,z)

						ab3.insert(j3,z3)
					# ~ print(a)
					c=ab3
					s1=list(set([a[0],b[0],c[0]]))
					s2=list(set([a[1],b[1],c[1]]))

					s3=list(set([a[2],b[2],c[2]]))
					
					s4=list(set([a[3],b[3],c[3]]))
					
					s5=list(set([a[4],b[4],c[4]]))
					s6=list(set([a[5],b[5],c[5]]))
					# ~ if tipo_sud==9:
					s7=list(set([a[6],b[6],c[6]]))
					
					s8=list(set([a[7],b[7],c[7]]))
					s9=list(set([a[8],b[8],c[8]]))
					if len(s1)==conta and len (s2)==conta and len (s3)==conta and len (s4)==conta and len (s5)==conta and len (s6)==conta and len (s7)==conta and len (s8)==conta and len (s9)==conta:
						print(len(s1),len(s2),len(s3),len(s4),len(s5),len(s6),len(s7),len(s8),len(s9))
						
						print(conta)
						print(a)
						print(b)
						print(c)
						print()
						# ~ print(d)
						conta=4
						for  d in itertools.permutations(lista4):
						
							ab4=list(d)
							for j4,z4 in zip(diz4.keys(),diz4.values()):
								# ~ lista.insert(j,z)

								ab4.insert(j4,z4)
							# ~ print(a)
							d=ab4
							s1=list(set([a[0],b[0],c[0],d[0]]))
							s2=list(set([a[1],b[1],c[1],d[1]]))

							s3=list(set([a[2],b[2],c[2],d[2]]))
							
							s4=list(set([a[3],b[3],c[3],d[3]]))
							
							s5=list(set([a[4],b[4],c[4],d[4]]))
							s6=list(set([a[5],b[5],c[5],d[5]]))
							# ~ if tipo_sud==9:
							s7=list(set([a[6],b[6],c[6],d[6]]))
							
							s8=list(set([a[7],b[7],c[7],d[7]]))
							s9=list(set([a[8],b[8],c[8],d[8]]))
							if len(s1)==conta and len (s2)==conta and len (s3)==conta and len (s4)==conta and len (s5)==conta and len (s6)==conta and len (s7)==conta and len (s8)==conta and len (s9)==conta:
								print(len(s1),len(s2),len(s3),len(s4),len(s5),len(s6),len(s7),len(s8),len(s9))
								print(conta)
								print(a)
								print(b)
								print(c)
								print(d)
								print()
			# ~ print(lista)
# ~ while True:
# ~ if a[2]==5 and a [7]==3:
# ~ if a[2]==5 and a [7]==3:
def ciao():
	# ~ for  a in itertools.permutations([1,2,3,4,5,6,7,8,9]):
		
			# ~ print(a)
	# ~ def ciao():
		for b in itertools.permutations([1,2,3,4,5,6,7,8,9]):
				
					s1=list(set([a[0],b[0]]))
					s2=list(set([a[1],b[1]]))
