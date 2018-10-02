#cuma bisa di run ama python3
#caranya "python3 [NamaFile.py]"

filename = "latihan31.py"

def hitung_karakter_tertentu(teks, huruf):
	jumlah=0
	for x in teks:
		if x==str(huruf):
			jumlah+=1
	return jumlah

with open(filename) as o:
	ayam=o.read()

huruf=str(input("masukkan huruf yang ingin dihitung: "))
print(hitung_karakter_tertentu(ayam, huruf))

for huruf in "abcdefghijklmnopklqrstuvwxyz":
	persen = hitung_karakter_tertentu(ayam, huruf)/len(ayam)
	print("{0} - {1}%".format(huruf, round(persen, 2)))

