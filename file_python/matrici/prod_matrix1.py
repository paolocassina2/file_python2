a=[[1,2],
[3,4],
]
b=[[5,6],
[7,8]

]

prodmatr=0
c=[]
conta=0

c=[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1],
	a[1][0]*b[0][0]+a[1][1]*b[1][0]	,	a[1][0]*b[0][1]+a[1][1]*b[1][1]	]			

count=0
# ~ print("[")
for x in c:
	count=count+1
	if count%2>=1:
		# ~ print("]")
		print()
	print (x,end=" ")
		
# ~ print(c)														
