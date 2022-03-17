def ciao():
	import syllables
	print(syllables.estimate('cantare'))
	# ~ syllables.estimte('syllables')
	print(syllables("cantare"))
	word=input("Enter the word:")
	syllable_count=0

parola ="SASASA"
sill=["CAN","TA","RE",
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
"ZA", "ZE", "ZI", "ZO", "ZU",
]
conta=0
for x in sill:
	if x in parola:
		conta=conta+1
print(conta)
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
