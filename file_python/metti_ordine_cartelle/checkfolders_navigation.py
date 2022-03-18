def path():
	path.var=r'C:/Users/Attilio/'
path()
# ~ indi='"'+"explorer /select",+str(path.var)+'"'
# ~ file=open(path.var, "r")
# ~ indi=path.var
# ~ print(indi)
import subprocess
import os
# ~ path="C:\\Users\\Attilio\\Desktop\\file_python\\"
# ~ import time
# ~ time.sleep(3)
# ~ os.closefile(path)
# ~ subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
# ~ subprocess.Popen(indi)
# ~ st=r'explorer /select'+path.var	+"'"
# ~ import subprocess
# ~ subprocess.Popen(st)
import os
def naviga_tra_i_file():
	def x22():
		x22.var=""
	x22()
	def comando_cd():
		x1=""	
		c=0	
		x22.var=""#per tornare indietro
		for x in path.var[::-1]:
			if x=="/":
				c=c+1
				if c>=2:
					break
			x22.var=x22.var+x
		c=0
		# ~ print(x2[::-1])		
		if path.var!="C:/":
			s3 =path.var.replace(x22.var[::-1]		,"")#per cancellare l ultimo pezzo di path in modo da tornare indietro

		# ~ print(s3)
			path.var=s3
	
	def open_f():

		# ~ st=r'explorer /select'+path.var	+"'"
		# ~ import subprocess
		# ~ subprocess.Popen(st)
		os.startfile(path.var)


	print(path.var)
	while True:
				# ~ print()
				# ~ print()
				# ~ try:
				
				
				print()
		
				inp =input("scrivi NOME CARTELLA oppure 'break' per scegliere il path e chiudere cmd		")
				# ~ print(path.var)
				if inp!="cd.." and inp!="break" and inp!="" and inp!="open":

					path.var=path.var+inp+"/"
					
				elif inp=="cd..":
						comando_cd()
						print(path.var)	
				elif inp=="break":
						break
				elif inp=="open":
						open_f()	
				# ~ elif inp=="":
						# ~ continue
				try:
				
					os.listdir(path.var)
					# ~ print(path.var)
				except:
					comando_cd()
					print(inp," non esiste")#se inserisco una cartella che non esiste , non avanza nel path,rimane dov era
					# ~ path.var=path.var
					# ~ print("abcdefgh")
					# ~ pass
				print(path.var)
				print(os.listdir(path.var))
naviga_tra_i_file()
