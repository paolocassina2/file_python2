import italian_dictionary
print("alfabeto farfallino corretto, le sillabe non servono")
# Use this to get only the meaning 
# ~ definition = italian_dictionary.get_definition('cane', limit=3, all_data=False) 
# ~ print(definition[0])
#Use this to get all datas of a word (all_data default is True)
# ~ datas = italian_dictionary.lemma('albero')
#forse se la sillaba ü di tre lettere e l ultima finisfe per consonatne bisogna troncare la consonatne
while True:
		
	parola=input("parola		")
	#in realtä non c entrano niente le sillabe--> quando incontra una vocale aggiunge una F+vocale
	parola1=""
	for x in parola:
		parola1=parola1+x
		if x=="a":
			parola1=parola1+"FA"
		if x=="e":
			parola1=parola1+"FE"
			
		if x=="i":
			parola1=parola1+"FI"
		if x=="o":
			parola1=parola1+"FO"
		# ~ if x=="a":
			# ~ parola1=parola1+"FA"
		if x=="u":
			parola1=parola1+"FU"
	print("alfabeto farfallino  ",parola1)
	print()
			
		
def ciao():
	while True:
		try:
			parola=input("parola	")
			datas = italian_dictionary.get_definition(parola)

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
				elif len(x)==4:			
					
					
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
								
						if x[-2]=="a":
							fa="FA"
						elif x[-2]=="e":
							fa="FE"
						elif x[-2]=="i":
							fa="FI"
						elif x[-2]=="o":
							fa="FO"
						elif x[-2]=="u":
							fa="FU"	
						# ~ print("l",last_char)
				parola_alf_farf=parola_alf_farf+x+fa
			print("parola alfabeto farfallino	",parola_alf_farf)
			print()
		except:
			continue
