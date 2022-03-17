from PyDictionary import PyDictionary

dictionary=PyDictionary("hotel","ambush","nonchalant","perceptive")
# ~ 'There can be any number of words in the Instance'

# ~ print(dictionary.printMeanings())
# ~ ciao=list(dictionary.printMeanings())
print(type(dictionary))
ciao=list(dictionary)
print(type(ciao))
for x in ciao:
	print(x)
