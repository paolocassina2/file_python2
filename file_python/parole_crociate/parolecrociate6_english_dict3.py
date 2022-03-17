import enchant
import string
def abc():
	abc.var=""
abc()
import pyodbc 
###CARTELLA==parole_crociate
		#sql server
# ~ def conn():
	# ~ conn.var = pyodbc.connect('Driver={SQL Server};'
										  # ~ 'Server=DESKTOP-DOQB38B;'
# ~ d = enchant.Dict('en_AU')										  # ~ 'Database=ciao;'
import itertools										  # ~ 'Trusted_Connection=yes;')
# ~ conn()
parola="alt*****e"#r
print(parola,"len ",len(parola))
d = enchant.Dict('en_AU')
# ~ for  x in d:
print(set(d))
# ~ print(d.items())
# ~ for x in list(d.values()):
	# ~ print(x)
# ~ print(len(d))
parola1=""
minuscole=list(string.ascii_lowercase)# Print the
c2=0
for x in parola:
	if x=="*":
		# ~ parola1=parola1+x
		c2+=1

for p in itertools.product(minuscole, repeat=c2):		
	# ~ c2=c2+1
	# ~ if c2>3:
		
	# ~ print(p)
		# ~ break
		# ~ print(a.var)

		# ~ print(perm2)
	# ~ from itertools import permutations
	# ~ import string
	# ~ string.ascii_lowercase
	s=""
	c=-1
	p1=str(p)
	for x in parola:
		
		if x=="*":
			c=c+1
			s=s+p[c]
		else:
			s=s+x
			
	# ~ print(s)
	if d.check(s)==True:
		print(s)
		break
	# ~ print()
