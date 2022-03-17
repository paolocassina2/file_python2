t=10
def timer(t):

	import time
	while t>0:
		time.sleep(1)
		t=t-1
		print(t)
		if t==0:
			# ~ import pygame
			# ~ pygame.mixer.init()
			# ~ pygame.mixer.music.load('C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input\\CentoDiQuestiGiorni.mp3')
			# ~ pygame.mixer.music.play()
			import os

			os.system("C:\\Users\\Attilio\\Desktop\\file_python\\tk_inter_input\\CentoDiQuestiGiorni.mp3")
timer(3)
#CARTELLA==alarm_clock
