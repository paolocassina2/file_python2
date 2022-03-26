from tones import SINE_WAVE, SAWTOOTH_WAVE
from tones.mixer import Mixer
import os
# Create mixer, set sample rate and amplitude
mixer = Mixer(44100, 0.5)
######CARTELLA==timer
# ~ import datetime
import time
#lunghezza allarme qualhe minuto
# ~ datem = datetime. datetime. strptime(adesso, "%Y-%m-%d %H:%M:%S")

# ~ print(datem)
# ~ print(adesso)

# Create two monophonic tracks that will play simultaneously, and set
# initial values for note attack, decay and vibrato frequency (these can
# be changed again at any time, see documentation for tones.Mixer
def crea():
	mixer.create_track(0, SAWTOOTH_WAVE, vibrato_frequency=7.0, vibrato_variance=30.0, attack=0.01, decay=0.1)
	mixer.create_track(1, SINE_WAVE, attack=0.01, decay=0.1)

	# Add a 1-second tone on track 0, slide pitch from c# to f#)
	mixer.add_note(0, note='c', octave=3, duration=8.0, endnote='c#')

	# Add a 1-second tone on track 1, slide pitch from f# to g#)
	mixer.add_note(1, note='e', octave=3, duration=8.0, endnote='f')
	mixer.add_note(1, note='g', octave=3, duration=8.0, endnote='g#')
	# Mix all tracks into a single list of samples and write to .wav file
	mixer.write_wav('tones.wav')

# Mix all tracks into a single list of samples scaled from 0.0 to 1.0, and
# return the sample list
	samples = mixer.mix()
# ~ os.open("tones.wav")
# ~ s = Sound() 
# ~ s.read('tones.wav') 
# ~ s.play()
# ~ crea()
# ~ os.open("tones.wav", 5)
def tk_i():
	import tkinter as tk
	root = tk.Tk()
	root.geometry("400x240")
	w = tk.Label(root, text="sveglia, sono le " ) 
	w.pack()
	root.mainloop()
def timer():
	def alarm():
		import pyglet

		music = pyglet.resource.media('tones.wav')
		music.play()

		pyglet.app.run()
	# ~ import tkinter as tk
	# ~ root = tk.Tk()
	# ~ root.geometry("400x240")

	# ~ def ora_min():
		# ~ ora_min.var=""
	# ~ ora_min()
	# ~ def getTextInput():
		# ~ ora=textExample.get("1.0","end")
		# ~ result1=textExample.get("1.0","end")
		# ~ print(ora)
		# ~ ora_min.var=ora.split()
		# ~ print(ora_min.var)
		# ~ print(result1)

	# 2015 5 6 8 53 40
	# ~ textExample=tk.Text(root, height=10)
	# ~ textExample.pack()
	# ~ btnRead=tk.Button(root, height=1, width=10, text="Read", 
						# ~ command=getTextInput)

	# ~ minute="9"
	# ~ if len(minute)<2:
		# ~ for x in minute:
			# ~ minute="0"+x
	# ~ print("m",minute)

	# ~ def ciao():
	# ~ print("ciaoo",now.minute)
	# ~ btnRead.pack()
	# ~ import
	# ~ import
	# ~ root.mainloop()
	# ~ a="ciao"
	# ~ print("sveglia impostata per  "+str(ora_min.var[0])+":"+str(ora_min.var[1]))
	# ~ print(type(now.hour))

	# ~ while True:
	import datetime
	
		
	set_timer1=int(input("inserisci minuti) 		"))
	
	set_timer2=int(input("inserisci secondi) 		"))
	secondi=int(set_timer1*60)+int(set_timer2)
	# ~ pri
	
	if set_timer1!="" and set_timer2!="":		#prendo il tempo iniziale quando sceglo l intervallo di tempo del timer , non dall avvio del programma
		adesso=time.time()	
		print("adesso",adesso)	# ~ s=0
		while True:
			dopo=time.time()
			
			# ~ if dopo-set_timer>=1:
				# ~ adesso=adesso+1
				# ~ s=s+1
			# ~ print(dopo)
			# ~ time = dopo.strftime("%H:%M:%S")
			# ~ print(dopo-adesso)
			# ~ if dopo-adesso>set_timer:
			
			#if dopo-adesso>=set_timer:
				#alarm()
			if dopo>=adesso+secondi:
		# ~ if adesso==adesso+1:
				print("SONO TRASCORSI "+str(secondi)+" secondi")
		# ~ time.sleep()
		# ~ print("o",ora)
		# ~ print("m",minuti)
		# ~ if int(ora_min.var[0])==int(now.hour) and int(ora_min.var[1])==int(minute):	
		# ~ if int(ora_min.var[0])==int(ora) and  int(ora_min.var[1])==int(minuti):
				# ~ print("sveglia sono le "+str(ora)+":"+str(minuti)+"!!!!")
				break
				# ~ tk_i()
				# ~ a="abc"
		while True:
			alarm()
					# ~ import tkinter as tk
					# ~ root = tk.Tk()
					# ~ root.geometry("400x240")
					# ~ w = tk.Label(root, text="sveglia, sono le " +str(ore)+":"+str(minuti)) 
					# ~ w.pack()
					# ~ root.mainloop()
				# ~ break
timer()
