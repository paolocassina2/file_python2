# ~ a=[1,2,3]
# ~ conta=0
# ~ condizione=""
# ~ for x in a:
	# ~ conta=conta+1
	# ~ if conta==1:
		# ~ condizione=condizione+"if "+str(x)+ " and "
	# ~ else:
		# ~ condizione=condizione+str(x)+ " and "

# ~ print(condizione)
D = [{'apple': 2, 'meizu': 12, 'samsung': 9, 'oppo': 12, 'foo': 42, 'bar': 42}, 
     {'apple': 91, 'meizu': 22, 'samsung': 72, 'foo': 'test', 'bar': "blub"}]
import re
def to_code(string):
    code = "(" + string + ")"
    code = re.sub("[a-z]+", lambda m: "d['%s']" % m.group(0), code)
    code = code.replace(",", ") and (")
    code = code.replace(";", " or ")
    code = code.replace("=", "==")
    return code

s = 'apple<3,meizu>5;samsung=9,foo=bar'
code = to_code(s)
for d in D:
    print(eval(code)) # prints True, False
