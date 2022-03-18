import os
###CARTELLA==programmi_os
library=['"pip install opencv-python"','"pip install pyenchant"','"pip install random2"']

for x in library:
	print(x)
	os.system('cmd /c {}'.format(x))
	print()

	
print("controlla che tutte le librerie installate siano in questo elenco")	
os.system('cmd /c {}'.format("pip list"))	
# ~ print("abc",abc)
	# ~ time.sleep(10)
# ~ import sys
# ~ for arg in sys.argv:
    # ~ print(arg)
# ~ os.system(j1)
# ~ os.system('cmd /k "Your Command Prompt Command"')

# ~ os.system('cmd /k "Your Command Prompt Command"')

# ~ j="'cmd /k  {}".format(library[1])
# ~ j1=j+"'"
# ~ print(j1)
# ~ print(j)	
# ~ os.system(j1)
# ~ for x in library:
	# ~ print(x)
	
# ~ txt3 = "My name is {}".format("John")
# ~ print(txt3)
# ~ import subprocess
# ~ os.system('cmd /c "dir"')
# ~ command = ['ls', '-l']
# ~ p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.IGNORE)
# ~ text = p.stdout.read()
# ~ retcode = p.wait()
