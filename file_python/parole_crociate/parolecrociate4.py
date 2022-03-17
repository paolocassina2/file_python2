import italian_dictionary
#	print(definition)
#parola="buonasera"
#while True:


def k():
	k.var=2
k()
#k.var=""
def l_a():
	l_a.var=[]
l_a()
def definition():
	definition.var="3"
definition()
def definizione():
	import colorama
	from colorama import Fore, Style
	definition.var = italian_dictionary.get_definition(k.var, limit=3, all_data=False)
#	print(k.var)
	# ~ print('\033[31m' + k.var + '\033[0m')
	print(k.var)
	print(definition.var)
	print()
from itertools import permutations
import string
string.ascii_lowercase
#
print("risolutore parole crociate")
parola="alb--o"#remo parola sconosciuta#	qusta variabile serve solo per la lunghezza, non importa il contenuto

#questo programma funziona anche se la parola ha più di 5 lettere ma in questo caso controlla condizione solo sulle prime tre lettere che trova.#quindi la condizione riguarda solo le prime tre lettere diverse da "-" 
print("parola_sconosciuta",parola)
print()
minuscole=list(string.ascii_lowercase)# Print the
perm = permutations(minuscole,len(parola)) #obtained #permutations
par1=""
# ~ print('\033[2J')  # Clear screen
# ~ print('\033[31m' + 'Hello' + '\033[0m')  # Red text
listaindice=[]
listalet=[]

for xj in parola:
	# ~ print(xj)
	if xj!="-":
		# ~ print(parola.index(xj))
		# ~ print("xj",xj)
		# ~ print()
		# ~ print(parola.index(xj)
		indice=parola.index(xj)
		listaindice.append(indice)
		listalet.append(xj)
#problema: la stessa lettera restituisce lo stesso indice
print(listaindice)
print(listalet)
print("lenparola",len(parola))	# ~ print(i)

#def ciao():		
print("1",listaindice[0])
print(listalet[0])
print("2",listaindice[1])
print(listalet[1])
print(listaindice[2])
print(listalet[2])
print()
# ~ perm=["larice","larino","vetro","laqua"]

# ~ for i in list(perm):
		# ~ print(i)


# ~ if len(listaindice)==3:#nel caso conosci tre lettere su cinque
	# ~ if i[listaindice[0]]==listalet[0] and  i[listaindice[1]]==listalet[1]  and i[listaindice[2]]==listalet[2]:
		 # ~ #cerca tutte le permutazioni delle lettere dell'alfabeto a gruppi di grandezza corrispondente alla lunghezza della stringa PAROLA che soddisfano questa condizione qui sopra 
		# ~ #per esempio se la variabile parola è lunga 5 cercherà le permutazioni di tutte le lettere dell'alfabeto a gruppi di 5
			# ~ print (i)
listaposssoluz=[]
for i in list(perm):
	# ~ print(i)


	# ~ if len(listaindice)==3:#nel caso conosci tre lettere su cinque
	if i[listaindice[0]]==listalet[0] and  i[listaindice[1]]==listalet[1]  and i[listaindice[2]]==listalet[2] and i[listaindice[3]]==listalet[3]:
		 #cerca tutte le permutazioni delle lettere dell'alfabeto a gruppi di grandezza corrispondente alla lunghezza della stringa PAROLA che soddisfano questa condizione qui sopra 
		#per esempio se la variabile parola è lunga 5 cercherà le permutazioni di tutte le lettere dell'alfabeto a gruppi di 5
			# ~ print (i)
			#print()
			for x in i:
				# ~ print(x)
				par1=par1+str(x)
			# ~ print(par1)
			listaposssoluz.append(par1)

			par1=""
print(listaposssoluz)
for xzj in listaposssoluz:	
			try:
		
				k.var=xzj
				#print(k.var)
				definizione()
		
			except:
			
				#pass
				# ~ par1=""
			#oppure
			#except:
				pass
			# ~ par1=""
# ~ ciao()

###CARTELLA==parole_crociate