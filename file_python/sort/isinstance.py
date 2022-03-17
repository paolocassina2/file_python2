#ORDINA LISTE MISTE
def ordina():
	X=[3,4,1,5,0,"ciao","bene"]
# ~ for x in a:
	# ~ b=isinstance(x,int)
	# ~ if b==True:
			# ~ print(x)
	f=[]
	d=[]
	# ~ f.append(3)
	# ~ print(f)
	# ~ X_str_changed = [ "ciao" if isinstance(el, int)  else el for el in X ]   #
	stri1 = [ x for x in X if isinstance(x, int)==True]
	stri2 = [ x for x in X if isinstance(x, str)==True]
	str_ord=sorted(stri1)+sorted(stri2)
	# ~ c=[x for x in a if isinstance(x,int)==True else "b"]
	# ~ print(c)
	return str_ord
# ~ print(ordina())
def ordina1():
	X=[3,4,1,5,0,"ciao","bene"]
# ~ for x in a:
	# ~ b=isinstance(x,int)
	# ~ if b==True:
			# ~ print(x)
	f=[]
	d=[]
	# ~ print(sorted(X))
	# ~ f.append(3)
	# ~ print(f)
	# ~ X_str_changed = [ "ciao" if isinstance(el, int)  else el for el in X ]   #9
	lista =  sorted([x for x in X if isinstance(x, int)==True])+sorted([x for x in X if isinstance(x, str)==True])
	# ~ print(lista)
		# ~ stri2 = [ x for x in X if isinstance(x, str)==True]
	# ~ str_ord=sorted(stri1)+sorted(stri2)
	# ~ c=[x for x in a if isinstance(x,int)==True else "b"]
	# ~ print(c)
	return lista
print(ordina1())
# ~ X = [1.5, 2.3, 4.4, 5.4, 'n', 1.5, 5.1, 'a']     # Original list

# Extract non-strings from X to new list
# ~ X_non_str = [el for el in X if not isinstance(el, str)]  # When using only 'if', put 'for' in the beginning

# Change all strings in X to 'b', preserve everything else as is
# ~ X_str_changed = ['b' if isinstance(el, str)  else el for el in X]   #
# ~ print(X_str_changed)
