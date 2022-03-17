##CARTELLA==operazioni_stringhe
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))
def word_count1(str):
	counts =0
	words = str.split()
	words1= set(words)
	for w1 in words1:
		counts=0
		c1=0
		for y in w1:
			c1=c1+1
		for w in words:
			
				# ~ print(y)
			if w1==w:
				counts=counts+1
				# ~ c1=str(counts)
        # ~ if word in counts:
            # ~ counts[word] += 1
        # ~ else:
		print(w1," ",counts,"lengthWord ",c1)    # ~ counts[wored] = 1
		# ~ print(counts)
		# ~ return w + c1
print( word_count1('brown brown the quick brown fox jumps over the lazy dog.'))
