from itertools import permutations
###CARTELLA==prova
# Get all permutations of length 2
# and length 2
import itertools
tipo_sud=9
# ~ for v in itertools.permutations([1,2,3,4,5,6,7,8,9]):
	# ~ print(v)
# ~ perm1=list(itertools.permutations([1,2,3,4,5,6,7,8,9])

# ~ perm2=list(itertools.permutations([1,2,3,4,5,6,7,8,9])
# ~ perm3=list(itertools.permutations([1,2,3,4,5,6,7,8,9])
# ~ perm4=list(itertools.permutations([1,2,3,4,5,6,7,8,9])
# ~ perm5=list(itertools.permutations([1,2,3,4,5,6,7,8,9])
# ~ perm6=list(itertools.permutations([1,2,3,4,5,6,7,8,9])
# ~ perm7=list(itertools.permutations([1,2,3,4,5,6,7,8,9])
# ~ perm8=list(itertools.permutations([1,2,3,4,5,6,7,8,9])
# ~ perm9=list(itertools.permutations([1,2,3,4,5,6,7,8,9])

def ciao():
	perm1 = permutations([x for x in range(1,tipo_sud+1)], tipo_sud)
	perm2 = permutations([x for x in range(1,tipo_sud+1)], tipo_sud) 
	# ~ # Print the obtained permutations
	perm3 = permutations([x for x in range(1,tipo_sud+1)], tipo_sud) 
	perm4 = permutations([x for x in range(1,tipo_sud+1)], tipo_sud) 
	perm5 = permutations([x for x in range(1,tipo_sud+1)], tipo_sud) 
	perm6 = permutations([x for x in range(1,tipo_sud+1)], tipo_sud) 
	# ~ if tipo_sud==9:
	perm7 = permutations([x for x in range(1,10)], tipo_sud) 
	perm8 = permutations([x for x in range(1,10)], tipo_sud) 
	perm9 = permutations([x for x in range(1,10)], tipo_sud) 
# ~ while True:
# ~ if a[2]==5 and a [7]==3:
# ~ if a[2]==5 and a [7]==3:
for  a in itertools.permutations([1,2,3,4,5,6,7,8,9]):
	if a[0]==5 and a [3]==7:
		print(a)
# ~ def ciao():
		for b in itertools.permutations([1,2,3,4,5,6,7,8,9]):
			if b[2]==1 and b [3]==5 and b[6]==6:
				s1=list(set([a[0],b[0]]))
				s2=list(set([a[1],b[1]]))

				s3=list(set([a[2],b[2]]))
				
				s4=list(set([a[3],b[3]]))
				
				s5=list(set([a[4],b[4]]))
				s6=list(set([a[5],b[5]]))
				# ~ if tipo_sud==9:
				s7=list(set([a[6],b[6]]))
				
				s8=list(set([a[7],b[7]]))
				s9=list(set([a[8],b[8]]))
			
				if len(s1)==2 and len (s2)==2 and len (s3)==2 and len (s4)==2 and len (s5)==2 and len (s6)==2 and len (s7)==2 and len (s8)==2 and len (s9)==2:
			# ~ elif tipo_sud==6:
				# ~ if len(s1)==2 and len (s2)==2 and len (s3)==2 and len (s4)==2 and len (s5)==2 and len (s6)==2:
					# ~ print(a)
					# ~ print(b)
			# ~ print(i)
def ciao():
				# ~ print(j)
					for c in itertools.permutations([1,2,3,4,5,6,7,8,9]):
						if c[4]==2 and c[5]==6 and c[6]==8:
				# ~ print (i)
							s1=list(set([a[0],b[0],c[0]]))
							s2=list(set([a[1],b[1],c[1]]))

							s3=list(set([a[2],b[2],c[2]]))
							
							s4=list(set([a[3],b[3],c[3]]))
							
							s5=list(set([a[4],b[4],c[4]]))
							s6=list(set([a[5],b[5],c[5]]))
							# ~ if tipo_sud==9:
							s7=list(set([a[6],b[6],c[6]]))
							s8=list(set([a[7],b[7],c[7]]))
							s9=list(set([a[8],b[8],c[8]]))
							# ~ break
							# ~ if tipo_sud==9:
							# ~ print()
							if len(s1)==3 and len (s2)==3 and len (s3)==3 and len (s4)==3 and len (s5)==3 and len (s6)==3 and len (s7)==3 and len (s8)==3 and len (s9)==3:
							# ~ elif tipo_sud==6:
								# ~ if len(s1)==3 and len (s2)==3 and len (s3)==3 and len (s4)==3 and len (s5)==3 and len (s6)==3:
									# ~ print(a)
									# ~ print(b)
									# ~ print(c)
									# ~ print()
			# ~ def ciao():
									# ~ break
									for d in itertools.permutations([1,2,3,4,5,6,7,8,9]):
										s1=list(set([a[0],b[0],c[0],d[0]]))
										s2=list(set([a[1],b[1],c[1],d[1]]))

										s3=list(set([a[2],b[2],c[2],d[2]]))
										
										s4=list(set([a[3],b[3],c[3],d[3]]))
										
										s5=list(set([a[4],b[4],c[4],d[4]]))
										s6=list(set([a[5],b[5],c[5],d[5]]))
										# ~ if tipo_sud==9:
										s7=list(set([a[6],b[6],c[6],d[6]]))
										s8=list(set([a[7],b[7],c[7],d[7]]))
										s9=list(set([a[8],b[8],c[8],d[8]]))
										if len(s1)==4 and len (s2)==4 and len (s3)==4 and len (s4)==4 and len (s5)==4 and len (s6)==4 and len (s7)==4 and len (s8)==4 and len (s9)==4:
								# ~ print()
											for e in itertools.permutations([1,2,3,4,5,6,7,8,9]):
												s1=list(set([a[0],b[0],c[0],d[0],e[0]]))
												s2=list(set([a[1],b[1],c[1],d[1],e[1]]))

												s3=list(set([a[2],b[2],c[2],d[2],e[2]]))
												
												s4=list(set([a[3],b[3],c[3],d[3],e[3]]))
												
												s5=list(set([a[4],b[4],c[4],d[4],e[4]]))
												s6=list(set([a[5],b[5],c[5],d[5],e[5]]))
												# ~ if tipo_sud==9:
												s7=list(set([a[6],b[6],c[6],d[6],e[6]]))
												s8=list(set([a[7],b[7],c[7],d[7],e[7]]))
												s9=list(set([a[8],b[8],c[8],d[8],e[8]]))
												if len(s1)==5 and len (s2)==5 and len (s3)==5 and len (s4)==5 and len (s5)==5 and len (s6)==5 and len (s7)==5 and len (s8)==5 and len (s9)==5:
													for f in itertools.permutations([1,2,3,4,5,6,7,8,9]):
														s1=list(set([a[0],b[0],c[0],d[0],e[0],f[0]]))
														s2=list(set([a[1],b[1],c[1],d[1],e[1],f[1]]))

														s3=list(set([a[2],b[2],c[2],d[2],e[2],f[2]]))
														
														s4=list(set([a[3],b[3],c[3],d[3],e[3],f[3]]))
														
														s5=list(set([a[4],b[4],c[4],d[4],e[4],f[4]]))
														s6=list(set([a[5],b[5],c[5],d[5],e[5],f[5]]))
														# ~ if tipo_sud==9:
														s7=list(set([a[6],b[6],c[6],d[6],e[6],f[6]]))
														s8=list(set([a[7],b[7],c[7],d[7],e[7],f[7]]))
														s9=list(set([a[8],b[8],c[8],d[8],e[8],f[8]]))
														
														if len(s1)==6 and len (s2)==6 and len (s3)==6 and len (s4)==6 and len (s5)==6 and len (s6)==6 and len (s7)==6 and len (s8)==6 and len (s9)==6:
															# ~ if tipo_sud==6:
																# ~ print(a)
																# ~ print(b)
																# ~ print(c)
																# ~ print(d)
																# ~ print(e)
																# ~ print(f)
													
																
																# ~ break	
															# ~ if tipo_sud==9:	
																for g in itertools.permutations([1,2,3,4,5,6,7,8,9]):
																	s1=list(set([a[0],b[0],c[0],d[0],e[0],f[0],g[0]]))
																	s2=list(set([a[1],b[1],c[1],d[1],e[1],f[1],g[1]]))

																	s3=list(set([a[2],b[2],c[2],d[2],e[2],f[2],g[2]]))
																
																	s4=list(set([a[3],b[3],c[3],d[3],e[3],f[3],g[3]]))
																	
																	s5=list(set([a[4],b[4],c[4],d[4],e[4],f[4],g[4]]))
																	s6=list(set([a[5],b[5],c[5],d[5],e[5],f[5],g[5]]))
																	s7=list(set([a[6],b[6],c[6],d[6],e[6],f[6],g[6]]))
																	s8=list(set([a[7],b[7],c[7],d[7],e[7],f[7],g[7]]))
																	s9=list(set([a[8],b[8],c[8],d[8],e[8],f[8],g[8]]))
																	
																	if len(s1)==7 and len (s2)==7 and len (s3)==7 and len (s4)==7 and len (s5)==7 and len (s6)==7 and len (s7)==7 and len (s8)==7 and len (s9)==7:
													# ~ print(i)		p
																		for h in itertools.permutations([1,2,3,4,5,6,7,8,9]):
																			s1=list(set([a[0],b[0],c[0],d[0],e[0],f[0],g[0],h[0]]))
																			s2=list(set([a[1],b[1],c[1],d[1],e[1],f[1],g[1],h[1]]))

																			s3=list(set([a[2],b[2],c[2],d[2],e[2],f[2],g[2],h[2]]))
																			
																			s4=list(set([a[3],b[3],c[3],d[3],e[3],f[3],g[3],h[3]]))
																			
																			s5=list(set([a[4],b[4],c[4],d[4],e[4],f[4],g[4],h[4]]))
																			s6=list(set([a[5],b[5],c[5],d[5],e[5],f[5],g[5],h[5]]))
																			s7=list(set([a[6],b[6],c[6],d[6],e[6],f[6],g[6],h[6]]))
																			s8=list(set([a[7],b[7],c[7],d[7],e[7],f[7],g[7],h[7]]))
																			s9=list(set([a[8],b[8],c[8],d[8],e[8],f[8],g[8],h[8]]))
																			if len(s1)==8 and len (s2)==8 and len (s3)==8 and len (s4)==8 and len (s5)==8 and len (s6)==8 and len (s7)==8 and len (s8)==8 and len (s9)==8:
																				for i in itertools.permutations([1,2,3,4,5,6,7,8,9]):
																					s1=list(set([a[0],b[0],c[0],d[0],e[0],f[0],g[0],h[0],i[0]]))
																					s2=list(set([a[1],b[1],c[1],d[1],e[1],f[1],g[1],h[1],i[1]]))

																					s3=list(set([a[2],b[2],c[2],d[2],e[2],f[2],g[2],h[2],i[2]]))
																					
																					s4=list(set([a[3],b[3],c[3],d[3],e[3],f[3],g[3],h[3],i[3]]))
																					
																					s5=list(set([a[4],b[4],c[4],d[4],e[4],f[4],g[4],h[4],i[4]]))
																					s6=list(set([a[5],b[5],c[5],d[5],e[5],f[5],g[5],h[5],i[5]]))
																					s7=list(set([a[6],b[6],c[6],d[6],e[6],f[6],g[6],h[6],i[6]]))
																					s8=list(set([a[7],b[7],c[7],d[7],e[7],f[7],g[7],h[7],i[7]]))
																					s9=list(set([a[8],b[8],c[8],d[8],e[8],f[8],g[8],h[8],i[8]]))
																					if len(s1)==9 and len (s2)==9 and len (s3)==9 and len (s4)==9 and len (s5)==9 and len (s6)==9 and len (s7)==9 and len (s8)==9 and len (s9)==9:
																						print(a)
																						print(b)
																						print(c)
																						print(d)
																						print(e)
																						print(f)
																						print(g)
																						print(h)
																						print(i)
																						print()
																						break
													# ~ print(x)
											# ~ print(y)
										# ~ print()
