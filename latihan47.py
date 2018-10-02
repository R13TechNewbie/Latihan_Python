class ayam:
	def __init__(self,telur):
		print("Menghitung telur..")
		self.telur=telur
	def __del__(self):
		print("Selesai menghitung telur, hapus data..")
		del self

ayam=ayam(19)
print(ayam.telur)