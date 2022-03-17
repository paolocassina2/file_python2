from PIL import Image


nomi=["cybr.jpg","cybr1.jpg","seraph.jpg"]
# ~ for x in nomi:	
filename = r'C:\Users\Attilio\Desktop\\ico_files\cybr3.png'
img = Image.open(filename)
	# ~ Convert png to ico file with pillow
	# ~ img.save('logo16.ico',format = 'ICO', sizes=[(32,32)])
	# ~ img.save('logo16.ico',format = 'ICO', sizes=[(32,32)])
img.save('C:\\Users\\Attilio\Desktop\ico_files\\cybr3.ico',format = 'ICO', sizes=[(255,255)])

###CARTELLA==animated_pic