import enchant

 #languages#['de_DE', 'en_AU', 'en_GB', 'en_US', 'fr_FR'].
d = enchant.Dict('en_AU')

from itertools import permutations
import string
string.ascii_lowercase

parola="t***l"#remo parola sconosciuta	qusta variabile serve solo per la lunghezza, non importa il contenuto

#questo programma funziona anche se la parola ha più di 5 lettere ma in questo caso controlla condizione solo sulle prime tre lettere che trova.#quindi la condizione riguarda solo le prime tre lettere diverse da "-" 
print("parola_sconosciuta",parola)
print()
minuscole=list(string.ascii_lowercase)# Print the
# ~ perm = permutations(minuscole,len(parola)) #obtained #permutations
# ~ par1=""
import itertools
# ~ x = [1, 2, 3, 4, 5, 6]
#permutazioni con ripetizioni 
# ~ print('\033[2J')  # Clear screen
# ~ print('\033[31m' + 'Hello' + '\033[0m')  # Red text
listaindice=[]
listalet=[]

a=""
# ~ ciao="ciao"
# ~ ciao.add("2",2)
# ~ ciao[0:2]+*ciao
# ~ print(ciao)
for j in range(3,6):
	perm=[p for p in itertools.product(minuscole, repeat=j)]	
	print(perm)
# ~ def ciao():	
	
	for x in perm:	
		for j in x:
			a=a+str(j)	
	
		if a[0]==parola[0] and x[len(parola)-1]==parola[len(parola)-1]:

		
		# ~ if a[0]=="a" and a[2]=="t":
		#controlla che la ultima e prima lettera siano al posto giusto
				
						# ~ print(a)
					# ~ if a[0]=="b" and a[4]=="k":
						# ~ print(d.check(a))
			if d.check(a)==True:
					print(a)	
			# ~ eak
	a=""
						# ~ par1=""
			# ~ ciao()

		###CARTELLA==parole_crociate
