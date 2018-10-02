from random import randint

def DiceRoll(): 
	#Dice rolls simulator program
	judul="Dice Roll Simulator"
	iterate=len(judul)
	print(iterate * "=")
	print(judul)
	print(iterate * "=")
	jmlDadu = input("Masukkan Jumlah Dadu: ")
	try:
		jmlDadu = int(jmlDadu)
		dadu = []
		for i in range(jmlDadu):
			dadu.append(randint(1,6))
		print(dadu)
	except:
		print(" Masukkan angka, bukan huruf")