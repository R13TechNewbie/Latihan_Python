#!/usr/bin/python

x=5
y=2
if x==5:
	print("benar")
	if y!=1:
		print("yang benar saja")

if (1+1==5) and (3-2==1):
	print("a")
else:
	print(not 3)

while True:
	if x>3:
		print(x)
		x-=1
		if y>0:
			continue
			print("howdy")
	else:
		break
