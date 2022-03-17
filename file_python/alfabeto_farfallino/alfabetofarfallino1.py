def ciao():
	import syllables
	# ~ print(syllables.estimate('cantare'))
	# ~ syllables.estimte('syllables')
	# ~ print(syllables("cantare"))
	word=input("Enter the word:")
	syllable_count=0

shepherd=age=2
stuff_in_string = "Shepherd %s is %d years old." % (shepherd, age)
# ~ print(stuff_in_string)
# ~ Shepherd Martha is 34 years old.	
# ~ print(ciao())
line = 'cavallo'
# ~ line.add("ciao")
# ~ index = line.find('ca')
# ~ output_line = line[:index] + 'Fa ' + line[index:]
# ~ print(output_line)
# ~ output_line

parola ="CANTARE"
sill=["CAN",
 "BA", "BE", "BI"," BO", "BU",
"CA", "CE", "CI", "CO", "CU", "CHE", "CHI",
 "DA", "DE", "DI", "DO", "DU",
 "FA", "FE", "FI", "FO", "FU",
"GA", "GE", "GI", "GO"," GU", "GHE", "GHI",
"LA", "LE", "LI", "LO", "LU",
 "MA", "ME", "MI", "MO", "MU",
"NA", "NE", "NI", "NO", "NU",
"PA" ,"PE", "PI", "PO", "PU",
"QU",
"RA", "RE", "RI", "RO", "RU",
"SA", "SE", "SI", "SO", "SU",
 "TA", "TE", "TI", "TO", "TU",
"VA", "VE", "VI", "VO", "VU",
"ZA", "ZE", "ZI", "ZO", "ZU",]
# ~ conta=0
		# ~ print(x," ciao",type(x))
import random
# ~ if aaa[0]!="0":

# the use of sample() function .
  
from random import sample
LISTA=[]
for x in sill:
	if x in parola:
		if x in "CAN":
			x="CAN"
		# ~ print(x)
		LISTA.append(x)
		# ~ for xu in LISTA:
LISTA1=list(set(LISTA))	
parola1=""

anagramma2=sample(LISTA,len(LISTA1))
# ~ print(anagramma2)

lista=["a","b","c"]
for x in anagramma2:
	parola1=parola1+x
	
print(parola1)
# ~ for x1 in anagramma2:
	# ~ str(x1)
	# ~ print(x1)
	# ~ print(type(x1))
	# ~ print("aaa",parola1)
	# ~ print(x1)
# ~ print("C",parola1)
	# ~ if parola1==parola:
		# ~ print(parola1)
		# ~ break
	# ~ print(anagramma2)
	
# ~ print(str(LISTA1))

		# ~ conta=conta+1
		# ~ print(x)
# ~ print(conta)


	
def syllable_count(str):
		count = 0
		
		syllables = set("AEIOUaeiou")
		
		for letter in str:
			if letter in syllables:
				count = count + 1
		  
		print("Total no. of syllables :", count)

# ~ str = 'beautiful'

# ~ syllable_count(str)

# ~ syllable_count = {}.fromkeys(syllables,0)

# ~ for w in word:
   # ~ if w in syllable_count:
       # ~ syllable_count[w] += 1

# ~ print(syllable_count)
