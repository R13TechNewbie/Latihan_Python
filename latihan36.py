def rekursif(x):
	if x == 1:
		return 1
	else:
		return x*rekursif(x-1)

print(rekursif(9))

def genap(aw):
	if aw == 0:
		return True
	else:
		return genap(aw-1)

def ganjil(aw):
	return not genap(aw)

print(genap(80))
print(ganjil(80))
