lettere="certosa"
# ~ print(
lettere1=list(lettere)
import itertools
# ~ x = [1, 2, 3, 4, 5, 6]
# ~ for i in range(1,len(lettere)+1):
# ~ print(

with open('C:\\Users\Attilio\\Desktop\\60000_parole_italiane.txt') as f:
    lines = f.readlines()
dizionario_parole=[]	
for j in lines:
	# ~ if j=="canto":
		
	parola_dizionario=j.strip()
		# ~ printlen(j.strip()))
		# ~ print()
	dizionario_parole.append(parola_dizionario)
	# ~ print("1234",parola_dizionario)
# ~ print(dizionario_parole)	
		# ~ if parola=="caghh":
		# ~ print(parola_dizionario)
		# ~ break
  
# ~ def ciao():

# ~ def ciao():
lista_comb=[]
# A Python program to print all

# A Python program to print all
# permutations using library function

# A Python program to print all
# permutations of given length
from itertools import permutations
 
# Get all permutations of length 2
# and length 2
for xx in range(1,len(lettere1)+1):
	perm = permutations(lettere1, xx)
	parola=""
	# Print the obtained permutations
	for i in list(perm):
		# ~ print (i)
		for j in i:
			parola=parola+j
		# ~ print(parola)
		# ~ print(len(parola))
		lista_comb.append(parola)
		parola=""
		
		# ~ parola=parola+i
	# ~ print(parola)
	# ~ parola=""
    # ~ print (i)
    
# ~ def ciao():
parole_trovate=[]
for x in lista_comb:
	# ~ print(x)
	# ~ print(len(x))		
		if x in dizionario_parole:
			# ~ print(x)
			parole_trovate.append(x)
print(parole_trovate)
print(len(parole_trovate))					
# ~ def ciao():		
# ~ print(lista_comb)
	# ~ for parola_diz in dizionario_parole:    
		# ~ for x in lista_comb:
		# ~ print(parola_diz)
			# ~ if parola_diz==x:
				# ~ print(parola_diz)
	# ~ print(len(parola_diz))
			# ~ print(
	# ~ print([p for p in itertools.product(str(lettere1), repeat=i)])
