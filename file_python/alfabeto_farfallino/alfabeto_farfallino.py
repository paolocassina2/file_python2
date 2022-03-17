import italian_dictionary

# Use this to get only the meaning 
# ~ definition = italian_dictionary.get_definition('cane', limit=3, all_data=False) 
# ~ print(definition[0])
#Use this to get all datas of a word (all_data default is True)
# ~ datas = italian_dictionary.lemma('albero')
datas = italian_dictionary.get_definition('marionetta')

	# ~ print(x)
sillabe=datas["sillabe"]
print(sillabe)

parola_alf_farf=""
for x in sillabe:
	if len(x)==1:
		if x=="a":
			fa="FA"
		elif x =="e":
			fa="FE"
		elif x =="i":
			fa="FI"
		elif x =="o":
			fa="FO"
		elif x =="u":
			fa="FU"
	elif len(x)==2:
		if "a" in x:
			fa="FA"
		elif "e" in x:
			fa="FE"
		elif "i" in x:
			fa="FI"
		elif "o" in x:
			fa="FO"
		elif "u" in x:
			fa="FU"

	elif len(x)==3:	
			
			
		last_char = x[-1]		#se e lungo tre e fininsce per vocale la variabile dipende dall ultima vocale
		# Get last character of string i.e. char at index position -1
		if	last_char=="a" or last_char =="e" or last_char =="i" or last_char=="o" or last_char=="u":
			
			if last_char=="a":
				fa="FA"
			if last_char=="e":
				fa="FE"
			if last_char=="i":
				fa="FI"
			if last_char=="o":
				fa="FO"
			if last_char=="u":
				fa="FU"
		else:#se lungo 3 ma non finisce per vocale 
					
			if "a" in x:
				fa="FA"
			elif "e" in x:
				fa="FE"
			elif "i" in x:
				fa="FI"
			elif "o" in x:
				fa="FO"
			elif "u" in x:
				fa="FU"
				
			# ~ print("l",last_char)
	parola_alf_farf=parola_alf_farf+x+fa
print(parola_alf_farf)
