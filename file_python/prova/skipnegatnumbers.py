#Python Program to Find Sum of 10 Numbers and Skip Negative Numbers
import random
s=0
def sol1():
	for x in range(11):
		x=random.randint(-5,8)
		print(x)

		if x<0:
			continue
		s=s+x
	print(s)

# ~ def sol2():
for x in range(11):
		x=random.randint(-5,8)
		print(x)

		if x>=0:
			# ~ continue
			s=s+x
print(s)
from string import ascii_lowercase as asc_lower
#pangram :a sentence containing every letter of the alphabet.
# ~ ù/ˈpanɡram/
# ~ noun 
# ~ s="The quick brown fox jumps over the lazy dog"


def is_panagram():
	
	s="sixty zippers were quickly picked from the woven jute bag"
	s="waltz, nymph, for quick jigs vex Bud"
	s="two driven jocks help fax my big quiz."
	# ~ s="aaaaaaaaaaaaaaddwwwwwwwwwwwwwwwwwwwfgdfgdfgfgdfgdferttttyyyynxtrtrtnnnbnbndffffffffffffffffffffffffm"
	# ~ s="dkfjfl"
	s1=s.lower()
	def remove(string):
		return "".join(string.split())
	s2=remove(s1)  
	# ~ print(s2) 

	lista=[]
	# ~ print(asc_lower)
	# ~ print("Sdf",s1)
	# ~ print(s2)
	for x in s2:
		
		if x=="," or x==";" or x==".":
			continue
		print(x)
		lista.append(x)
	# ~ print(j)
	j1=set(lista)
	# ~ print(s2)
	#print(j1)
	# ~ print(lista)
	# ~ print(len(j1))
	# ~ print(len(asc_lower))
	#lista.sort()
	# ~ xx=""
	# ~ for i in j1:
		# ~ xx=xx+i
	# ~ print(xx)
	# ~ print(lista)
	# ~ print(asc_lower)
	if len(j1)==len(asc_lower):
		return "{}. is a pangram".format(s)
		# ~ print()
	else:
		return "{}. is NOT a pangram".format(s)

print(is_panagram())
		
	

###CARTELLA==prova