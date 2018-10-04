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

koleksiHewan = ["ayam","kambing","sapi","kucing","buaya","harimau"]

daftarHewan = open("daftarHewan", "w")

for hewan in koleksiHewan:
	daftarHewan.write(hewan + "\n")
	
daftarHewan.close()

bacaDaftarHewan = open("daftarHewan", "r")

bacaFile = bacaDaftarHewan.read()
barisPertama = bacaDaftarHewan.readline()

print(barisPertama)
for hewan in bacaFile:
	print(hewan, end = '')

bacaDaftarHewan.close()