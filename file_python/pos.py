a=[1,2,3]
posiz=[1,2,3]
c=["a","x","x","x","b","c"]
j=-1
for x in c:
	j+=1
	for jg in posiz:
		if jg==j:
			c[j]=a[j]
print(c)
