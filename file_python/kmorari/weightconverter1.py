
inp=float(input("grammi"))

decigrammi=inp*10
centigrammi=inp*100
milligrammi=inp*1000
decagrammi=inp*1/10
etti=inp*1/100
chili=inp*1/1000
print(decigrammi)
print(centigrammi)
print(milligrammi)
print(decagrammi)
print(etti)
print(chili)
# ~ pip install tk
import tkinter as tk
import tkinter as tk
root = tk.Tk()
root.geometry("400x240")

def getTextInput():
    result=textExample.get(1.0, tk.END+"-1c")
    print(result)
from Tkinter import *

textExample=tk.Text(root, height=10)
textExample.pack()
btnRead=tk.Button(root, height=1, width=10, text="Read", 
                    command=getTextInput)

btnRead.pack()
label = label( root, textvariable=result, relief=RAISED )

var.set(result)
label.pack()
# ~ root.mainloop()
# ~ inp = tk.Entry(m)
# ~ inp.bind('<Return>', show) # binding the Return event with an handler
# ~ inp.pack(fill='x', side='left')
# ~ inp = tk.Entry(m)
# ~ inp.bind('<Return>', show) # binding the Return event with an handler
# ~ inp.pack(fill='x', side='left')
# ~ ok = tk.Button(m, text='GO', command=show)
# ~ ok.pack(fill='x', side='left')

root.mainloop()

###CARTELLA==kmorari