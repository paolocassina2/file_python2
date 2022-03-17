
# ~ 3/km*60
n=1

print(n, "min/km")
minkim=str(1/n*60)+" km/h"
print(minkim)
def ciao():
	import tkinter as tk

	master = tk.Tk()
	tk.Label(master, text="First Name").grid(row=0)
	tk.Label(master, text="Last Name").grid(row=1)

	e1 = tk.Entry(master)
	e2 = tk.Entry(master)

	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)

	master.mainloop()
