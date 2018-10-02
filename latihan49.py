class static_dan_classmethod:
	def __init__(ini, masukan):
		ini.masukan=masukan
	
	@staticmethod
	def proses(input):
		try:
			m = int(masukan)
			return True
		except ValueError:
			print("ERROR : Masukkan angka, bukan huruf")
		
	@classmethod
	def cetak_Ayam(cls,loop):
		for i in range(int(loop)):
			print("ayam")
	
masukan = input("Masukkan angka: ")
if static_dan_classmethod.proses(masukan) == True:
	static_dan_classmethod.cetak_Ayam(masukan)