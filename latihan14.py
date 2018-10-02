try:	
	var=15
	print(var+"yee")
	print(var/3)
except ZeroDivisionError:
	print("error, can't divided by 0")
except TypeError:
	print("error, wrong type")

try:
	var=20
	print(var/0)
except:
	print("error happen")
