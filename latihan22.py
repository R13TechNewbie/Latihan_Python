with open("readme.txt") as yes:
	print(yes.read(1000))

test = open('readme.txt', 'rb')
print(test.read(30))
print(test.read(31))
#print(test.readlines())
for a in test:
	print(a)
test.close()

lagi=open('readme.txt', 'a')
test=lagi.write('ayam')
print(test)
lagi.close()

try:
	ayy=open("readme.txt", "r")
	print(ayy.read(1000))
finally:
	ayy.close()

