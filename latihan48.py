class kambing:
	def __init__(ini,jumlah):
		print("menghitung..")
		ini._jumlah=jumlah
	def panggil(ini):
		print(_jumlah)
		
kambing = kambing("ayam")
print(kambing._jumlah)

class sapi:
	__ayam = 6
	def cetak_ayam(self):
		print(self.__ayam)
		
sapi().cetak_ayam()
print(sapi()._sapi__ayam)
print(sapi().__ayam)