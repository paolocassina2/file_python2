# ~ def func1(a):
	# ~ return 2**func2(a-3)
# ~ def func2(b):
	# ~ return b+1
# ~ print(func1(5))


def recursive(n):
	if n==1:
		return 2
	return 3*recursive(n-1)
# ~ print(recursive(3))e

minu=(27*60+5)//7.5
# ~ sec=27.5*60%7.5

print(minu//60)
print(minu%180)
# ~ print(minu%180)
# ~ print(sec)
# ~ print(minu-180)
