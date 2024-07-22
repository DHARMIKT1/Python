a = 10 #global variable

def func():
	a = 5 #local variable

	print(a) 
func() #print local variable

print(a) #print global variable
