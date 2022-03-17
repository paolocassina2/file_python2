##CARTELLA==stringhe
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
		for w in words:
			if w1==w:
				counts=counts+1
				# ~ c1=str(counts)
        # ~ if word in counts:
            # ~ counts[word] += 1
        # ~ else:
		print(w1," ",counts)    # ~ counts[wored] = 1
		# ~ print(counts)
		# ~ return w + c1
print( word_count1('brown brown the quick brown fox jumps over the lazy dog.'))
