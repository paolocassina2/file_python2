import enchant
import string
def abc():
	abc.var=""
abc()
import pyodbc 
		#sql server
# ~ def conn():
	# ~ conn.var = pyodbc.connect('Driver={SQL Server};'
										  # ~ 'Server=DESKTOP-DOQB38B;'
										  # ~ 'Database=ciao;'
										  # ~ 'Trusted_Connection=yes;')
# ~ conn()
parola="d****e"#r
d = enchant.Dict('en_AU')
parola1=""
for x in parola:
	if x=="*":
		parola1=parola1+x
		
def ciaoo():
#se x es let iniziale fosse d,se la parola ha 6 lettere e inutile che cerco combinazioni di 6 lettere. cerco combinazioni delle lettere mancanti
	def findCombinations(A, k, i=0, out=[]):

	 
		# base case: if the combination size is `k`, print it
		# ~ if out[0]=="d":
		if len(out) == k:
			# ~ abc.var.append(out)
			# ~ if out[0]=="d":
			# ~ print(len(abc.var))
			# ~ print(out)
			
			# ~ return
		 # ~ conn.var.cursor()
				# ~ cursor.execute("insert into dbo.parole1(parole) values (?)", str(out))
				# ~ conn.var.commit()
				# ~ print(out)
				
			return
		
		
				
		
		# ~ if len(abc.var)>1:
			# ~ if out[0]=="d" and out[5]=="e":
				# ~ print(out)
		#	 start from the previous element in the current combination
		# till the last element
		j = i
		# ~ while len(abc.var)<24:
		while j < len(A):
	 
			# add current element `A[j]` to the solution and recur with the
			# same index `j` (as repeated elements are allowed in combinations)
				out.append(A[j])
				findCombinations(A, k, j, out)
		 
				# backtrack: remove the current element from the solution
				out.pop()
		 
				# code to handle duplicates – skip adjacent duplicates
				while j < len(A) - 1 and A[j] == A[j + 1]:
					j = j + 1
					# ~ if len(abc.var)==80:
						# ~ break
				
				j = j + 1
				# ~ abc.var=""
				# ~ abc2=""	
		for x in out:
			abc.var=abc.var+x
		abc2=parola[0]+abc.var+parola[len(parola)-1]	
			# ~ if len(abc2)==len(parola):
		if d.check(abc2)==True:
			
				print(abc2)	
		
				# ~ cursor =
				# ~ if len(A)==10:
					
					# ~ break
				# ~ if len(out)==k:
		# ~ if out[0]=="d" and out[5]=="e":
		# ~ try:
			# ~ print(out)
		# ~ except:
				# ~ continue
			# ~ pass
				
				# ~ if len(abc.var)==19:
					# ~ break
		 
		# ~ for i in abc.var:
			# ~ print(i)
	

# ~ cursor = conn.cursor()
# ~ cursor.execute('SELECT * FROM parole1')





	# ~ for i in cursor:
		# ~ print(i)

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	# ~ con.close()


	# ~ for i in cursor:
		# ~ print(i)
	import string
	string.ascii_lowercase



	###CARTELLA==database
	 #languages#['de_DE', 'en_AU', 'en_GB', 'en_US', 'fr_FR'].

	minuscole=list(string.ascii_lowercase)# Print the
	# ~ if __name__ == '__main__':
	while True:
		A = minuscole
		k = len(parola1)
	 
		# if the list contains repeated elements, sort the list to
		# handle duplicates combinations
		A.sort()
	 
		findCombinations(A, k)
		# ~ print(abc.var)
		

		# ~ print(a.var)

		# ~ print(perm2)
	# ~ from itertools import permutations
	# ~ import string
	# ~ string.ascii_lowercase
def ciao():
	# ~ parola="d****e"#remo parola sconosciuta	qusta variabile serve solo per la lunghezza, non importa il contenuto

	#questo programma funziona anche se la parola ha più di 5 lettere ma in questo caso controlla condizione solo sulle prime tre lettere che trova.#quindi la condizione riguarda solo le prime tre lettere diverse da "-" 
	print("parola_sconosciuta",parola)
	# ~ print()
	# ~ minuscole=list(string.ascii_lowercase)# Print the
	# ~ perm = permutations(minuscole,len(parola)) #obtained #permutations
	# ~ par1=""
	# ~ import itertools
	# ~ x = [1, 2, +3, 4, 5, 6]
	# ~ perm=[]
	# ~ if len(perm)<200:
		# ~ perm=[p for p in itertools.product(minuscole, repeat=len(parola))]
		# ~ print(len(perm))	#permutazioni con ripetizioni 
	# ~ print('\033[2J')  # Clear screen
	# ~ print('\033[31m' + 'Hello' + '\033[0m')  # Red text
	listaindice=[]
	listalet=[]

	a=""

	c=0
	
	# ~ for x in perm:
		
		
		# ~ if a[0]=="a" and a[2]=="t":
	if perm2[0]==parola[0] and perm2[len(parola)-1]==parola[len(parola)-1]:#controlla che la ultima e prima lettera siano al posto giusto
			for j in perm2:
				a=a+str(j)		
						# ~ print(a)
					# ~ if a[0]=="b" and a[4]=="k":
						# ~ print(d.check(a))
			
				c=c+1
				if c<10:
					
					cursor = conn.cursor()
					number = 1234
					name = "GeeksforGeeks"
					x="abcdef"
					cursor.execute("insert into dbo.parole1(parole) values (?)", a)
					conn.commit()
				# ~ else:
					# ~ break

	# ~ conn.commit()
				
					# ~ print(a)	
				# ~ eak
	a=""
						# ~ par1=""
			# ~ ciao()

		###CARTELLA==parole_crociate
	# ~ cursor = conn.cursor()
	# ~ cursor.execute('SELECT * FROM parole1')


	# ~ for i in cursor:
		# ~ print(i)
