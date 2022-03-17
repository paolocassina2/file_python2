

###CARTELLA==operazionistringhe


#remove punctuation from string
ciao="ciao, come va!!!?"
ciao1=""
import string 
    
# Storing the sets of punctuation in variable result 
result = string.punctuation 
    
# Printing the punctuation values 
print(result) 
for x in ciao:
	if x in result:
		# ~ if x==y:
		continue
	
	ciao1=ciao1+x
			
print(ciao1)
